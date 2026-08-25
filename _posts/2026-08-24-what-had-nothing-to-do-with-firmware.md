---
layout: post
title: "The Parts of Running an AI Pipeline That Have Nothing to Do With AI"
date: 2026-08-24
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, ai-agents, process, lessons-learned]
summary: >
  Three operational failure modes that had nothing to do with the Coder
  agent writing bad code: an entire phase committed straight to main with
  no PR trail, a new agent session starting completely cold with no memory
  of project state, and a soak-test anomaly between two identical boards
  that never got a fully satisfying explanation. The common thread — these
  are the standard costs of running any long-lived, semi-autonomous system.
---

Most of what made this project hard wasn't the firmware. The Coder agent writing incorrect C++ was rare and usually caught fast. What actually cost time and attention were the same things that cost any engineering team time and attention: process discipline slipping under momentum, continuity that can't be assumed across a reset, and the ordinary chaos of a long-running project accumulating state nobody's tracking closely enough.

## When "it works" quietly bypassed the process

Phase 6 — getting sensor data flowing over MQTT — landed with both boards confirmed working on real hardware. Good news. The problem: it had all been committed directly to `main`, in two commits, with no individual branches, no separate pull requests per sub-project, and no Reviewer checklist posted on any of it.

Nothing about the *firmware* was wrong. The bidirectional MQTT, the cross-board display integration, all of it worked. But the entire audit trail the rest of the pipeline depends on — a PR per sub-project, a checklist comment, a documented review — simply didn't exist for this phase. It had to be corrected retroactively: real hardware verification re-confirmed live (a 30-second `mosquitto_sub` capture, pasted in full), then four separate branches and PRs created after the fact, each carrying the existing commits, each getting its proper checklist and merge, before Phase 6 was allowed to count as done.

The lesson isn't "the agent cut corners." It's that momentum is its own failure mode — a pipeline that's been running smoothly for a while will happily keep running smoothly past a process step nobody explicitly checked for, and the fix isn't a smarter agent, it's a phase-exit gate that verifies the *paperwork*, not just the outcome. That gate — snapshot the environment, generate a phase summary, confirm the PR trail, tag the release, in that specific order — got written into the agents' shared skill file directly after this happened, and held for the rest of the project.

## Session amnesia is a real constraint, not a metaphor

More than once, a new agent session started completely cold — no memory of what phase the project was in, what the last commit was, or what was still in flight. One session, asked to generate a diagram of "the current Phase 8.3 firmware," searched the repository, found nothing resembling Phase 8.3, and reported back — correctly — that it appeared to be looking at the wrong repository entirely. It was right. A prior session had drifted into a different working directory, and starting fresh actually surfaced the mistake rather than compounding it.

This is why `docs/decisions.md` and `docs/PROJECT_KB.md` exist as mandatory first reads for every session, independent of chat history: the rule became "load these before doing anything," specifically because relying on conversational continuity across sessions turned out to be exactly as fragile as it sounds. A file committed to the repo survives a context reset. A remembered conversation doesn't.

## The soak test that never got a satisfying answer

During Phase 5.4 — a one-hour continuous TCP stability test — node1 sent 1,849 messages. Node2 sent two, with three disconnects in the same window. That's not a subtle anomaly; that's one board working and the other one barely functioning, running the identical firmware, on identical hardware, on the same network.

It got investigated, logged in both `decisions.md` and the board's own health file, and treated as a real signal before Phase 6 was allowed to start — the project's rule was explicit: don't move on to MQTT with an unexplained instability sitting underneath it. But it's also honestly the kind of thing that's hard to fully close the loop on with two boards and a lab setup — was it the specific board, the specific USB cable, RF interference in that exact spot on that exact day? Documented, watched for recurrence, never with a single smoking-gun root cause. That's a true-to-life outcome for anyone who's debugged flaky hardware, and worth including precisely because it doesn't wrap up neatly.

## The pattern underneath all three

None of these three things are about an AI agent making a reasoning error. They're the standard operating costs of running any long-lived, semi-autonomous system: process discipline eroding under the pressure of "it already works," continuity that can't be assumed across a reset, and hardware behaving inconsistently for reasons that resist a clean explanation.

If there's a single takeaway from four months of this, it's that the interesting failure modes of an AI engineering pipeline look a lot less like "the model got confused" and a lot more like "the humans running any team need process gates that don't erode when things are going well." That turned out to be the most transferable lesson of the whole project — and arguably the one least specific to AI at all.

Next, and last in this series: what I'd do differently, what actually held up over four months, and where the roadmap goes from here.
