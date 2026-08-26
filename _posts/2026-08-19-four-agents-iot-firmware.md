---
layout: post
title: "I Let Four Claude Agents Build IoT Firmware for Me"
date: 2026-08-19
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, ai-agents, esp32, overview]
summary: >
  A Raspberry Pi 4 runs four Claude agents — Orchestrator, Coder, Reviewer,
  Tester — that autonomously write, review, flash, and test ESP32-S3 firmware.
  Tasks arrive over Telegram; the full audit trail lives in GitHub as pull
  requests. Series intro: the pipeline architecture, the adversarial test that
  proved the Reviewer actually rejects bad code, and where the project stands
  four months and eight phases in.
---

It's a Wednesday evening in March. I open Telegram, type one line to a bot, and go make dinner. By the time I'm back, there's a pull request open on GitHub with test logs from a real ESP32 board, a code review posted as a PR comment, and a firmware image already flashed. I didn't write a single line of C++.

That's the shape this project took for the better part of four months — and by the time the dust settled on Phase 8, it had produced firmware with TLS-encrypted MQTT, replay-attack detection, deep-sleep power management, and a security posture I'd trust more than most of the things *I've* personally written at 11pm.

## The setup

The hardware is unglamorous: a Raspberry Pi 4 and two ESP32-S3 dev boards. The Pi runs everything — MQTT broker, mDNS, NTP — and hosts four Claude Sonnet 4.6 agents through a framework called OpenClaw, each with a specific job:

- **Orchestrator** — receives my instructions over Telegram, routes work to the other agents, merges pull requests, reports back to me
- **Coder** — writes the firmware, opens PRs, never touches test files
- **Reviewer** — reviews every PR against a mandatory JSON checklist, can hard-reject on things like hardcoded credentials or missing watchdog resets
- **Tester** — flashes real hardware, captures serial output, asserts against test specs, writes the report

Tasks come in over Telegram. Everything else — code, review comments, test evidence, merge history — lives in GitHub as an ordinary, auditable trail of pull requests. If I ever want to know exactly what happened and why, it's not buried in a chat log; it's a commit.

## Why build it this way

It would have been faster, in the short term, to just write the firmware myself. The point wasn't speed. It was seeing whether a small team of AI agents, given the same constraints a human engineering team would have, could actually hold to them — not just produce code that *looks* right, but code that's been tested on physical hardware and reviewed by another party with the authority to say no.

Three things make that possible here, and none of them are exotic:

1. **Test-driven development is structural, not a suggestion.** The Tester writes the test spec *before* any firmware exists, confirms it fails against an empty stub, and only then does the Coder get to write code. The Coder is contractually forbidden from touching test files.
2. **The Reviewer can actually reject.** Not "here are some suggestions" — a JSON checklist with hard-fail conditions: no WiFi error handling, a blocking `delay()`, a hardcoded IP, a missing test file. Fail any of them and it's `CHANGES_REQUESTED`, automatically.
3. **Nothing is faked.** Every PASS comes from a real board — actual serial output, actual sensor readings, actual flash cycles logged in a health file. If the hardware doesn't cooperate, the pipeline doesn't get to pretend it did.

## The moment that convinced me it was actually working

Early on, at the end of Phase 1, I asked the pipeline to test itself: submit three deliberately broken firmware variants and see if the Reviewer would actually catch them. ([transcript link](/iot/evidence/#msg-72))

| Variant | Violation | Caught by |
|---|---|---|
| no-heartbeat | Heartbeat logging silently commented out | Reviewer |
| blocking-delay | `delay(2000)` inside the main loop | Reviewer |
| hardcoded-ip | Broker IP hardcoded as a literal string | **Reviewer only** |

The third one is the interesting one. The hardcoded IP was declared but never actually used anywhere in the firmware — which meant the Tester's serial-output assertions would never have caught it. It compiled clean, it ran clean, it would have passed every hardware test. The *only* thing standing between that firmware and a merge was the Reviewer reading the code and recognizing a policy violation that had no runtime symptom.

That's when the checklist stopped feeling like busywork and started feeling like the actual point.

## Where things stand

The project follows a 14-phase roadmap, starting from pure network isolation and ending at a standalone, field-deployable device:

`Network isolation → Pipeline bootstrap → Sensors → WiFi/mDNS → Reliable WiFi → MQTT → Power & sleep → Message integrity & encryption → Auth & identity → Cert management → OTA updates → Resilience → Standalone deployment`

As of the latest merge, **Phase 8 — message integrity and encrypted transport — is complete.** Both boards do CRC-32 checked, sequence-numbered, replay-protected, TLS-encrypted MQTT publishing, with deep-sleep power management and a battery-aware LED indicator running on top. That's six sub-phases of incremental hardening, each one shipped as its own tested, reviewed pull request. Phases 9 through 14 — authentication, certificate rotation, OTA updates, and final hardening — are still ahead.

## What didn't go smoothly (a preview)

This is not a story about a system that worked flawlessly. A few things are worth their own posts later in this series:

- **The hardware lied more than once.** The I2C bus that "should" have worked on default pins didn't — the board's connector was wired to different GPIOs than the ESP32 defaults, and it took a scanner returning an empty bus before anyone thought to check the schematic.
- **Process discipline slipped at least once.** An entire sub-phase got committed directly to `main` — no branch, no PR, no Reviewer checklist — and had to be caught and retroactively corrected before I'd accept it as "done."
- **A new agent session started completely cold, more than once.** No memory of what phase the project was in or what was still in flight — which is exactly why the repo, not the chat history, had to become the real source of truth. ([transcript link](/iot/evidence/#msg-967))

None of that is a failure of the concept. If anything, it's the most honest part of the story — the parts where a team of AI agents runs into the same mundane friction any engineering team does, and you get to watch how it handles it.

That's the series I want to write: not "AI built my firmware," but what it actually looks like, week to week, when you hand a real, physical, security-sensitive project to a pipeline of agents and hold them to the same standard you'd hold yourself to.

Next up: the unglamorous foundation — VLANs, static DHCP leases, and the moment `esptool read_mac` quietly failed because it should have been `read-mac`.
