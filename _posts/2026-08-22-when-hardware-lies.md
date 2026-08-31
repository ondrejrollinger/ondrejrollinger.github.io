---
layout: post
title: "When the Hardware Lies to You"
date: 2026-08-22
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, esp32, i2c, hardware, debugging, networking]
summary: >
  Four hardware-debugging incidents, four different root causes, one shared
  lesson: firmware that reports "init OK" doesn't mean the physical device
  is doing anything — and sometimes the culprit isn't the firmware at all.
  Covers the I2C bus wired to non-default GPIO pins, a BMP280 answering at
  0x77 instead of 0x76, an OLED that needed the SH1106 driver library
  instead of SSD1306, and a week-long access-point mystery that turned out
  to be a known bug in the Raspberry Pi's own WiFi chip.
---

Phase 3 was supposed to be the easy part. Wire up a light sensor, read some lux values, move on. Instead it became the phase that taught me the most important lesson of the whole project: an AI agent can write flawless code against a wrong assumption, and every layer of the pipeline — compiler, boot log, even the test suite — will confirm it's fine, right up until you look at the actual physical device and it's doing nothing at all.

Four separate incidents, four separate root causes, all with the same shape — three in Phase 3, one from Phase 4 that's really the same lesson wearing a different hat.

## Incident one: the I2C bus that wasn't there

Task: read lux from a BH1750 light sensor over the board's I2C connector. Should be routine — call `Wire.begin()`, scan the bus, find the sensor at address `0x23`.

Except the bus was completely empty. Not "wrong sensor," not "bad address" — the I2C scanner reported `"found":[]`. Nothing at all.

The instinct here is to suspect the sensor, the cable, or the power rail — and that's exactly what got checked first. The sensor got moved to the other board. Same result, empty bus. 3.3V was confirmed present at the connector with a meter. Everything *should* have worked. ([transcript link](/iot/evidence/#msg-200))

The actual answer was sitting in the manufacturer's own example code, which used `Wire.begin(8, 10)` — explicit pin numbers. The board's I2C connector isn't wired to the ESP32's default I2C pins (GPIO21/22, what `Wire.begin()` assumes with no arguments). It's wired to GPIO42 (SDA) and GPIO2 (SCL). Calling `Wire.begin()` with no arguments doesn't fail loudly — it just quietly initializes a bus that has nothing connected to it, and every downstream operation reports back accurately that there's nothing there. The firmware wasn't broken. It was talking to the wrong two pins with total confidence.

Once `Wire.begin(42, 2)` was in place, the sensor was found at `0x23` immediately, and lux readings tracked exactly as expected — 41 lux in a dim room, 566 lux well-lit. ([transcript link](/iot/evidence/#msg-207))

## Incident two: the sensor that moved its own address

The BMP280 pressure/temperature sensor is documented at I2C address `0x76`. Ours answered at `0x77`. ([transcript link](/iot/evidence/#msg-234)) The datasheet explanation is mundane once you know it — the SDO pin on this particular module is pulled high, which flips the address by one bit — but it meant the first attempt to read the sensor got a clean "device not found" from an address that, on paper, should have been correct. The fix was adding a fallback: try `0x76`, then `0x77`. Not a firmware bug, just an assumption about a part number that turned out to have a jumper-configurable detail nobody had checked.

## Incident three: init reported success, and the screen stayed black

This is the one that actually changed how I think about testing AI-written firmware. Both OLED displays were nominally the same part — 128x64, 1.3 inch — and the firmware used the `SSD1306` driver library, initialized it, called `display_init`, got a clean success response, and moved on. Every serial log said "init OK." On one board, the display worked. On the second board, nothing. Black screen, no error, no exception, no failed assertion anywhere in the test suite.

It took physically looking at the second screen — not reading a log — to even know there was a problem, because nothing in the firmware's own reporting suggested anything was wrong.

The actual issue: the 1.3-inch OLED module uses an **SH1106** controller, not SSD1306. ([transcript link](/iot/evidence/#msg-281)) They're similar enough — same resolution, similar command set — that an SSD1306 driver will often *partially* work, or work on one instance of a part and not another, depending on manufacturing tolerances and exactly how forgiving that particular chip's silicon is about being talked to with the wrong protocol. Switching to the `Adafruit_SH110X` library fixed it — mostly. A second, related issue turned up right behind it: `Wire`'s default 100kHz I2C clock speed was unreliable for the SH1106G controller specifically when the OLED was the *only* device on the bus. An explicit `TwoWire` instance running at 400kHz resolved that too.

## Incident four: the access point that blamed the firmware

This one predates the other three chronologically and cost far more time — the better part of a week, spanning Phase 4.1 — because it wasn't a sensor giving a wrong reading, it was the network itself intermittently refusing to let a board connect at all.

The original plan didn't involve a dedicated access point. The Raspberry Pi's own onboard WiFi chip would run `hostapd` and serve the `iot-lab` SSID directly — one less piece of hardware, one less thing to configure. Both ESP boards would connect to it like any other WiFi client.

It mostly worked. Then it started not working, in a way that looked exactly like a firmware bug: boards would cold-boot, attempt to connect, and sometimes just... not. No consistent pattern at first. The initial suspects were the usual ones — wrong password (ruled out, verified directly), then a `dnsmasq` DHCP issue (found and fixed — the AP interface didn't have a persistent static IP, so DHCP leases were failing intermittently). That fix helped, but didn't fully resolve it. Then the boards started behaving *differently from each other*: `esp-node1` connected reliably, `esp-node2` sat in a disconnect loop. Same firmware, different behavior — which is exactly the kind of asymmetry that makes you start doubting the board, the antenna, the solder joints, anything except the actual cause. ([transcript link](/iot/evidence/#msg-579))

The actual root cause, once found: the Raspberry Pi's onboard WiFi chip (a BCM4345/6, using the `brcmfmac` driver) has a documented bug in AP mode — after a client disconnects, it stops responding to new authentication requests until `hostapd` is manually restarted. Every cold boot that "randomly" failed to connect was hitting exactly this. It had nothing to do with firmware, nothing to do with which board, nothing to do with DHCP once that first fix was in. It was a known limitation of the exact chip sitting inside the Pi being used as the access point — [documented on the Raspberry Pi Foundation's own kernel issue tracker](https://github.com/raspberrypi/linux/issues/6876), under a report titled, almost too on the nose, "AP mode re-connection issue with IoT devices using ESP32."

The fix was hardware, not software: retire the Pi-as-AP setup entirely and put a dedicated TP-Link EAP225 in its place, with the Mikrotik router handling DHCP instead of `dnsmasq`. After the switch, cold-boot connection succeeded on the first attempt, every time, confirmed on hardware. `hostapd` and `dnsmasq` were disabled on the Pi and never turned back on.

## The actual lesson

None of these four problems were "the AI got the code wrong." In three of the four cases, the firmware that was written was a completely correct implementation of an incorrect assumption about the physical hardware — pin mapping, I2C address, controller chip. The code compiled. The code ran. In one case, the code reported success while the physical outcome was silently wrong (a lit display that wasn't lit). In the fourth case — the access point — nothing in the codebase was wrong at all; the bug was in a chip most of the project never had reason to think about, three layers removed from any board being flashed. That's the wider version of the trap: a test suite built entirely on serial log assertions can pass 100% while the actual physical outcome — a working sensor reading, a lit display, a WiFi connection that doesn't randomly refuse a client — simply isn't happening, for reasons that can live anywhere in the stack, not just in the code under test.

The fix, in the end, wasn't a smarter agent. It was a cheaper and more reliable discipline: **check the manufacturer's own example code and schematic before writing firmware, every time, even for parts that look standard.** All three incidents would have been caught in minutes by that one habit instead of hours of debugging after the fact. And for anything with a physical, visible output — a display, an LED, a motor — "init OK" in the logs is not evidence. Looking at the actual device is.

That distinction — between what the logs say and what's physically true — turned out to matter again later, in a very different context: proving that encrypted MQTT traffic was actually encrypted, not just labeled as such in a log line. More on that next.
