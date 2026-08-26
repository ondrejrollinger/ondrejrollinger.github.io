---
layout: post
title: "Building Up Security One Layer at a Time: CRC, Sequence Numbers, Replay Detection, and TLS"
date: 2026-08-23
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, security, mqtt, tls, encryption]
summary: >
  Phase 8's six sub-phases, each built strictly on the last: CRC-32 message
  integrity, sequence numbers with gap detection, cross-board replay
  detection with LWT-based window reset, deep-sleep persistence, MQTT over
  TLS with an embedded CA cert, and battery-optimized operation. Includes
  the tcpdump packet capture used to prove the encryption was real, not
  just a log line.
---

By Phase 8, both ESP32 boards had been talking to each other over plain, unauthenticated MQTT for months — fine for a lab network sitting behind VLAN isolation, not fine as a foundation to build anything more serious on. Phase 8 is where the project stopped trusting the network and started verifying everything on it, one incremental, independently-tested layer at a time.

## 8.1–8.2: proving a message wasn't corrupted or duplicated

The first two sub-phases are the unglamorous foundation everything else sits on:

- **CRC-32** on every published message, verified on receipt.
- **Sequence numbers** with gap detection, so a receiver can tell not just "is this message intact" but "did I miss one."

Neither is exciting on its own. Both are prerequisites for the interesting part.

## 8.3: replay detection, and the fix that had to happen twice

The design: each board keeps a sliding window of the last 10 sequence numbers it's seen from its peer. A duplicate seq number inside that window gets flagged as a replay attempt.

The first implementation shipped with each board tracking its *own* replay window against its *own* messages — which tests fine in isolation but proves nothing, because a board can't attack itself. The actual threat model is cross-board: node1's messages need to be checked by node2, and vice versa. That meant reworking the MQTT topic subscriptions so each board listens to its *peer's* replay topic, not its own — a design correction caught before merge, not after, specifically because the PR was held for review rather than auto-merged on green tests.

The trickier problem showed up once cross-board checking was real: what happens when a board reconnects after a reset? Its sequence numbers restart from zero, and the peer's replay window — full of high numbers from before the reset — correctly flags every subsequent message as a duplicate. Technically accurate, practically useless; a legitimate reconnect now looks identical to an attack.

The fix uses MQTT's Last Will and Testament mechanism, which already exists to announce when a client disconnects unexpectedly. Each board publishes a retained `online` status on connect and configures an `offline` LWT to fire automatically if it disappears. The peer, on seeing a fresh `online` from the other board, clears its replay window and resets its counter — a `peer_reset` event, logged and testable. Verified on real hardware: reset node1 while monitoring node2's serial output, confirm `peer_reset` fires, confirm the next few sequence numbers (`seq:1`, `seq:2`) get accepted instead of flagged. ([transcript link](/iot/evidence/#msg-1005))

## 8.4: making all of that survive deep sleep

Phase 7 had already gotten deep sleep working on its own. Phase 8.4's job was making the integrity and replay-detection machinery from 8.3 survive it — sequence numbers need to persist across a sleep cycle (stored in both fast RTC memory and NVS flash, so they survive both a wake-from-sleep and a full power cycle), and the whole connect → verify → publish → disconnect cycle needs to fit inside a short comms window before the board goes back to sleep.

This sub-phase took the most iteration of the whole security arc — multiple rounds of the same two peer-side tests (`test_peer_crc_verify_present`, `test_peer_replay_check_present`) failing because capture windows weren't long enough to reliably overlap both boards' wake cycles, plus a genuinely fiddly bug where the OLED display simply stopped updating on wake and it took explicitly re-checking Phase 8.3's known-working display code path to find the gap. Eventually landing on staggered wake timing (one board offset from the other) rather than trying to force perfect synchronization solved most of the flakiness — a good reminder that "make two independent, sleeping devices talk to each other reliably" is a harder problem than it sounds, agents or not.

## 8.5: TLS, and proving it with a packet capture instead of a log line

Everything up to this point ran on plain MQTT, port 1883. Phase 8.5's job: move to port 8883 with `WiFiClientSecure`, an embedded CA certificate baked into the firmware binary via PlatformIO's `board_build.embed_files`, and full certificate verification before any MQTT traffic flows.

The interesting part isn't the implementation — it's the proof. A firmware log line that says `"event":"mqtt_connected","port":8883` tells you the *code* thinks it's on the TLS port. It doesn't tell you the traffic is actually encrypted. So the verification step was a side-by-side `tcpdump` capture on both ports ([transcript link](/iot/evidence/#msg-1156)): plain 1883 traffic showing MQTT topic names and payloads in cleartext, directly readable — `sensor/esp-node2/status`, `online`, `esp-node2` — right there in the packet dump. The 8883 capture showing a TLS ClientHello/ServerHello handshake, certificate exchange, and then nothing but encrypted bytes; no topic name, no payload, no board identity anywhere in the raw capture.

That contrast — one readable, one not, from the exact same firmware family with one flag changed — is a better piece of evidence than any test assertion could be, and it's the same lesson from the hardware-debugging post applied to a network instead of a display: don't trust the log line that says something worked. Go look at the actual bytes.

## 8.6: making all of that cheap enough to run on a battery

The final piece folded battery efficiency into the TLS baseline: CPU underclocked to 80MHz, WiFi modem sleep enabled, comms window cut from ten seconds to three (connect, publish, disconnect — no idle waiting), and a minimal publish payload stripped down to just board name, sequence number, CRC, and battery voltage. An RGB LED gives a physical green/red readout of battery state without needing to check a display or a log at all — green above 3.5V, red below, off before the board sleeps.

## What this arc actually proves

Six sub-phases, each shipped as its own tested, reviewed, merged PR, built in strict dependency order — integrity before replay detection, replay detection before it needed to survive sleep, sleep before it needed to survive encryption, encryption before it needed to survive a battery budget. None of it skipped ahead. Every layer was validated on real hardware before the next one was allowed to depend on it.

That's the case, I think, for building this way at all: not that an AI pipeline gets security right by default, but that a pipeline forced through TDD and independent review, one small verified layer at a time, ends up somewhere a "just write the secure version" prompt never would.

Next: the parts of running this pipeline for months that had nothing to do with firmware at all.
