---
layout: post
title: "The Boring Part First: Isolating the Network Before Writing Firmware"
date: 2026-08-20
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, lab, networking, vlan, esp32]
summary: >
  Before any AI agent touched a keyboard, a day was spent isolating two
  internet-connected microcontrollers on their own VLAN, verifying the
  isolation with a four-check exit gate, and locking board identity to MAC
  address via static DHCP. Covers the network topology, the esptool
  read-mac gotcha, and why this unglamorous Phase 0 work underpins nearly
  every rule added later in the pipeline.
---

Before any AI agent touched a keyboard, I spent a day doing something deliberately unglamorous: making sure two internet-connected microcontrollers physically could not reach my home network, my laptop, or anything beyond a small isolated segment I controlled. No agent involvement. No automation. Just me, a router, and a checklist.

It's not the part of the project anyone asks about. It's also the part I'd redo first if I were starting over, because almost everything downstream — every Reviewer rule, every "no hardcoded IP" check, every hostname-only firmware convention — exists because of decisions made in this first afternoon.

## Why isolate first

The plan from day one was to let AI agents write and flash firmware onto real hardware with real network access, autonomously, over weeks. That's a reasonable thing to want and a genuinely bad idea to allow unsupervised on a home network. So Phase 0 had one job: build a blast radius small enough that nothing built later could do damage outside it.

The topology ended up looking like this:

```
Internet → Mikrotik router
         → VLAN50 → RPi eth0 — internet access, SSH via Tailscale
         → VLAN99 (192.168.99.0/24) → EAP225 access point (iot-lab SSID)
                                     → ESP32 boards (192.168.99.101–102)
                                     → RPi wlan0 (192.168.99.1, static)
```

Two VLANs, one Raspberry Pi bridging them deliberately (as the MQTT broker and mDNS host), and the ESP32 boards living entirely inside the isolated segment with no path outward except through services I control.

## The exit gate

Before Phase 1 could start, four checks had to pass, and pass in the *expected* direction — including two that were supposed to fail:

- From an ESP board: `ping 192.168.99.1` → should succeed (broker reachable)
- From an ESP board: `curl github.com` → should **fail** (no internet access)
- From the Pi: `curl github.com` → should succeed (Pi has its own uplink)
- From the Pi: `ping <home-laptop-IP>` → should **fail** (no path back to the home LAN)

Two of the four checks are explicitly testing that things *don't* work. That's an easy thing to skip when you're eager to get to the interesting part, and it's exactly the check that matters most before you hand autonomy to a pipeline that will run unsupervised for months.

## Static identity, decided early

The other decision made in Phase 0 that paid off constantly later: static DHCP leases keyed to MAC address, for both ESP boards, configured before either board had any firmware at all.

```
dhcp-host=10:20:ba:17:e4:34,esp-node1,192.168.99.101
dhcp-host=10:20:ba:17:e3:e4,esp-node2,192.168.99.102
```

The MAC addresses were pulled with `esptool` before either board had a single byte of firmware flashed — which is its own small, useful discovery: `esptool --port /dev/ttyACM0 read-mac` works on a completely blank chip. (Note the hyphen — `read_mac` with an underscore silently doesn't exist and will send you down a confused rabbit hole for longer than it should.)

Why bother with static leases for two boards on a lab network nobody else uses? Because "board identity" turned out to be a recurring headache later — boards get unplugged, replugged, swapped, and without a fixed IP tied to a fixed MAC, the Tester agent has no reliable way to know which physical board it's actually talking to. This is the kind of problem that's trivial to solve *before* you have firmware depending on it, and genuinely annoying to retrofit after. (It got retrofitted anyway, a few weeks later, when a board briefly started announcing itself under the wrong name — more on that in the TDD post.)

## The one serial-port surprise

Kernel 6.12 on Raspberry Pi OS Bookworm uses the `cdc_acm` driver for the ESP32-S3's CH9102F USB-serial chip, not the older `ch341` driver most tutorials assume. That means the board shows up as `/dev/ttyACM0`, not `/dev/ttyUSB0`. With both boards plugged in simultaneously, plug order decides which one gets `ttyACM0` and which gets `ttyACM1` — port assignment isn't fixed, only the MAC-to-IP mapping is. Small thing, but it's exactly the kind of undocumented environment quirk that costs an hour if you don't know it going in.

## What this bought later

None of this shows up in a demo. Nobody screenshots a working VLAN. But every rule that mattered later traces back to a decision made here:

- **"No IP addresses in firmware after Phase 4.3"** — only possible because hostnames (`esp-node1.local`, `mqtt-broker.local`) were designed in from the start via Avahi mDNS, not bolted on.
- **The Reviewer's hardcoded-IP hard-reject** — meaningless without a network topology that actually punishes IP-based coupling.
- **Board identity assertions in the Tester** — built on MAC-to-hostname mappings decided in an afternoon before any code existed.

The unglamorous work is unglamorous precisely because it doesn't produce anything to look at. But it's also the reason a pipeline of AI agents could be trusted to run unsupervised on physical hardware for months without me needing to watch every step.

Next: what it actually looked like to enforce test-driven development on an AI Coder agent — and the adversarial test that proved the Reviewer wasn't just rubber-stamping.
