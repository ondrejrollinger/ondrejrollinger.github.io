---
layout: post
title: "Retrospective: What Held Up, What I'd Change, and What's Next"
date: 2026-08-25
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, retrospective, roadmap]
summary: >
  Four months and eight completed phases in — what structural decisions held
  up (Reviewer rejection authority, repo-based institutional memory, physical
  proof over log lines), what would be done differently (checking
  manufacturer schematics first, an earlier phase-exit gate), and the
  roadmap ahead through Phase 13: auth and identity, cert management, OTA
  updates, resilience, and standalone deployment.
---

Four months, eight completed phases, forty-plus merged pull requests, two ESP32 boards that have been flashed well over a hundred times combined. Phase 8 — full message integrity and TLS encryption — just merged. This is the point to actually step back and ask what worked, what I'd build differently, and whether any of this generalizes past a personal IoT lab.

## What held up

**The Reviewer's authority to reject.** This is the single structural decision I'd keep without hesitation. A checklist that can only suggest is a checklist that gets ignored under time pressure — by a human team or an AI one. A checklist with hard-fail conditions that actually blocks a merge changed the character of every subsequent phase: the pipeline wasn't optimizing for "looks done," it was optimizing for "passes the gate," and those turned out to be different things more often than I expected.

**Institutional memory living in the repo, not the conversation.** `decisions.md` and `PROJECT_KB.md`, read at the start of every session regardless of what the chat history claims to remember, turned session amnesia from a real risk into a minor inconvenience. Every project that expects to run across model updates, session resets, or even just long gaps between working sessions should treat this as non-negotiable infrastructure, not documentation overhead.

**Requiring physical proof, not just log lines.** The pattern that showed up again and again — in the OLED display debugging, in proving TLS encryption with a packet capture instead of trusting a `mqtt_connected` log event — is that a system reporting success and a system actually succeeding are two different claims, and only one of them is verifiable by reading logs. Building in a habit of independent physical verification, even when it felt redundant, caught real gaps every single time it was used.

**Instrumenting the physical device, even briefly, to answer a real question.** For a few weeks around Phase 8.6, an hourly battery-status readout piped to Telegram tracked exactly how both boards discharged under the new TLS and sleep-optimized firmware — genuinely useful data, not busywork, and it answered the actual question (how long does this realistically run on a 500mAh cell) faster than estimating from datasheet numbers would have. Once that question was answered, the monitor came off. Small thing, but it's a good example of the pipeline being used for a quick, targeted measurement rather than only big phase-sized features.

## What I'd do differently

**Check the manufacturer's schematic and example code before writing a line of firmware for new hardware, every time, no exceptions.** All three hardware-debugging incidents — wrong I2C pins, wrong sensor address assumption, wrong display controller — would have cost minutes instead of hours if this had been a hard first step rather than something reached for after debugging had already started. This is now a written rule for the rest of the roadmap; I wish it had been one from Phase 3.1.

**Build the phase-exit gate earlier.** The Phase 6 process violation — real, working firmware committed straight to `main` with no PR trail — only got caught because the pattern of "verify the paperwork, not just the outcome" existed by then as a general instinct, not yet as an enforced gate. It became one immediately afterward. It should have been one from the start; a five-step mandatory exit sequence (environment snapshot, human-confirmed Telegram log, generated summary, commit, tag — in that order) is cheap to write and expensive to skip after the fact.

**Take board-to-board hardware variance seriously sooner.** The Phase 5.4 soak test anomaly — one board sending 1,849 messages, its twin sending two — got documented and treated with appropriate caution, but never fully resolved to a single root cause. With only two boards, it's genuinely hard to know if that's a board defect, a cable issue, or environmental interference. If I were scaling this to more devices, I'd want a much more deliberate hardware-variance testing step earlier in the roadmap, rather than discovering it mid-soak-test.

## Where this generalizes and where it probably doesn't

The core pattern — TDD enforced structurally, review with real rejection authority, an audit trail that survives context loss, physical verification over self-reported success — isn't specific to firmware or to this particular set of agents. It's a reasonable shape for any project where you want to delegate real autonomy to an AI system without delegating away your ability to trust the output.

What's specific to this project, and probably shouldn't be assumed to transfer, is the amount of human judgment still sitting in the loop at every phase boundary. Nothing merged without my explicit go-ahead. Nothing advanced to the next phase without a manual review of the phase-exit summary. The pipeline is autonomous *within* a phase and deliberately not autonomous *across* phase boundaries — that's a design choice, not a limitation I ran into, and it's the reason I'm comfortable with how much of the actual engineering happened without me writing code.

## The roadmap ahead

Phase 8's completion — CRC, sequence numbers, cross-board replay detection, LWT-based recovery, TLS, and battery-optimized operation — closes out the message-integrity arc. ([transcript link](/iot/evidence/#msg-1206)) What's still ahead:

- **Phase 9 — Auth & identity.** PSK setup, HMAC-SHA256 message signing, device identity tokens, key rotation. Mosquitto is still running with `allow_anonymous true`, flagged as temporary back in Phase 3 specifically pending this phase. ([transcript link](/iot/evidence/#msg-228))
- **Phase 10 — Cert management.** Expiry monitoring, automated rotation, revocation — building on the TLS foundation from 8.5.
- **Phase 11 — OTA updates.** Signed binaries, rollback on boot failure, multi-device rollout.
- **Phase 12 — Resilience.** Watchdog hardening, crash dumps, brownout detection, autonomous recovery.
- **Phase 13 — Standalone deployment.** A factory-flashable image with WiFi and certificate provisioning and OLED-based status reporting — the point where this stops being a lab project tethered to my specific network and becomes something that could actually be deployed somewhere.

That's still a lot of ground. But four months in, with a security posture I trust and a process that's caught its own mistakes more than once, it feels like the pipeline has earned the rest of the roadmap rather than just survived it.

That's the series, at least for now. If Phase 9 onward produces anything worth writing about — and given how Phase 3 and Phase 8 went, I'd bet on it — there'll be more.
