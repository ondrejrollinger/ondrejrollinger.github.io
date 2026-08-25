---
layout: post
title: "Teaching Agents Test-Driven Development — and Watching Them Enforce It on Each Other"
date: 2026-08-26
toc: true
permalink: /iot/blog/:year/:month/:day/:title/
tags: [iot, ai-agents, tdd, testing]
summary: >
  How TDD is enforced structurally across the pipeline — red confirmation
  before any firmware exists, a Coder agent barred from touching test files,
  and a Reviewer checklist with real hard-reject authority. Covers the
  adversarial test that revealed a hardcoded IP was a Reviewer-only catch,
  a Tester agent catching its own broken red-confirmation logic, and the
  board-identity bug that added a third layer of hardware verification.
---

The rule sounds simple written down: tests get written before firmware, and the Coder agent is never, under any circumstances, allowed to modify a test file. In practice, holding four AI agents to that rule for months surfaced some of the most interesting moments in the whole project — including a few where the agents caught problems I hadn't thought to ask about.

## The mechanics

Every sub-project in this pipeline follows the same sequence, and it's enforced structurally, not just requested politely:

1. **Tester writes the test spec first.** Before any firmware exists.
2. **Red confirmation.** The spec is run against a deliberately empty stub — `empty_stub.py` — and every single test must fail. If a test *passes* against nothing, the spec is broken, not the (nonexistent) firmware.
3. **Coder implements firmware to satisfy the spec.**
4. **Coder never touches test files.** This isn't a style guideline — it's a hard rule the Reviewer checks for on every PR.

The Reviewer checklist that gets posted on every pull request has two fields dedicated to exactly this: `test_file_present` and `test_files_unmodified`. Fail either one and it's an automatic `CHANGES_REQUESTED`.

## Proving the Reviewer actually rejects things

At the end of Phase 1, before I'd trust this pipeline with anything real, I asked it to test itself: submit three deliberately broken firmware variants through the full pipeline and see what got caught, and by which agent.

| Variant | What was wrong | Compiles clean? | Caught by |
|---|---|---|---|
| no-heartbeat | Heartbeat logging function commented out at both call sites | Yes | Reviewer (and Tester — two-layer defense) |
| blocking-delay | `delay(2000)` inside the main loop | Yes | Reviewer (and Tester — timing drift, WDT borderline) |
| hardcoded-ip | Broker IP hardcoded as a string literal, never actually used | Yes | **Reviewer only** |

The third one is the one that mattered most. The hardcoded IP was declared but unused anywhere in the actual code path — meaning the Tester's serial-log assertions on real hardware would never trip. It would have flashed clean, run clean, and passed every hardware test in the suite. The Reviewer catching it wasn't a redundant safety net; it was the *only* net. That single result is why `no_hardcoded_ip` became its own dedicated checklist field, separate from the general `no_hardcoded_credentials` check — a distinction added specifically because this test revealed the general check wasn't specific enough.

## The bug that revealed the Tester was actually reasoning, not pattern-matching

Phase 2.3 added automated test reports with a `--suite-results` argument. On the first run, the Tester's own red confirmation came back with 9 tests already passing against the empty stub — which should be impossible; nothing exists yet to satisfy any assertion.

Rather than shrug and move on, the Tester caught its own logic error: the spec had been written loosely enough that several assertions were trivially satisfiable by *absence* of output, not presence of correct output. It corrected the spec so only the two genuinely new `--suite-results` assertions failed against the stub, then re-ran. That's a small moment, but it's the difference between an agent following a checklist item ("run red confirmation") and an agent understanding *why* red confirmation exists in the first place.

## The bug that revealed why board identity needed a third layer

Phase 2.1 shipped structured error/warn logging — 13/13 tests passing on both boards, PR merged. Then, running the same suite against node2, both boards were found to be announcing themselves as `esp-node1` in their boot logs.

The existing test only asserted that *some* board name was present in the boot event — not that it matched the board actually under test. That's a real gap: a firmware image built for the wrong board could pass every test and get flagged green.

The fix (PR #10) added per-board PlatformIO environments with `BOARD_NAME`/`BOARD_MAC` compile-time macros, a `--board` option threaded through the test harness, and a new assertion — `test_board_identity_matches_target` — that fails if the board's self-reported identity doesn't match what the Tester expected to flash. From Phase 2.2 onward, a wrong-board flash is caught automatically instead of silently passing.

Worth noting: this fix involved editing Phase 1's test files retroactively — which sounds like it violates the "Coder never modifies test files" rule. It doesn't, because it wasn't the Coder doing it. It was logged explicitly in `decisions.md` as an Orchestrator-led infrastructure fix, distinct from the prohibition on the *Coder* editing tests to make its own firmware pass. The rule is about who's allowed to move the goalposts, not whether the goalposts can ever move.

## Process rules that came out of this phase

A few conventions got locked in here that held for the rest of the project:

- **No auto-merge.** The pipeline reports PASS and stops. A human merges. Every time.
- **The Reviewer checklist must be posted as a GitHub PR comment, not just reported over Telegram.** This was added directly because a Telegram-only checklist has no permanent, independently auditable record — a PR comment does.
- **Both boards must be tested before PASS is reported**, not just one representative board.

None of these rules exist because I anticipated them in advance. Every one of them exists because something surfaced during Phase 1–2 that made the gap obvious, and got closed before it could cause a real problem later.

Next: the phase where the hardware stopped cooperating, and "compiles clean, boots clean, looks right" turned out to mean almost nothing.
