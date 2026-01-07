# AGENTS.md — Cybersecurity Portfolio Writer (GitHub Pages)

## Purpose
You are a Codex coding agent operating in a GitHub Pages repository (typically Jekyll).
Your job is to help maintain a cybersecurity learning portfolio and produce short, publishable Markdown posts.

The core goal is not “pretty writing”; it is to produce posts that demonstrate:
- real technical ownership,
- correct reasoning,
- repeatable validation,
- evidence-driven conclusions.

## Repo behavior
- Prefer one PR per task.
- Keep diffs small and reviewable.
- Do not add dependencies (gems, npm, actions) unless explicitly requested.
- Do not refactor site layouts or theme files unless asked.
- Follow the existing repo’s conventions (folders, front matter fields, style).

## Non-negotiable safety and publishing rules
1) Never commit secrets:
   - tokens, API keys, passwords, private URLs, VPN configs, private keys, internal IDs.
2) Redact/anonymize anything that can identify the author or environment:
   - public IPs, private IPs, hostnames, usernames, MACs, SSIDs, device names, emails
   - real internal domains/services unless explicitly intended
3) Defensive framing only:
   - detection/triage/hardening/validation
   - avoid step-by-step exploit or weaponization instructions
4) If unsure, label as hypothesis and state what evidence would confirm it.

## Article workflow (must follow)
### Step 0 — Topic → input requirements
Before writing any post, output:
- a one-sentence topic confirmation,
- Minimum / Recommended / Advanced inputs needed,
- a copy/paste Case Brief template.

Then stop and request inputs.

### Step 1 — Write one publishable post
- Create or update exactly what is needed for that post.
- Default output location: `_posts/` (unless the repo uses a different convention).
- Use a filename: `YYYY-MM-DD-short-slug.md`.

### Step 2 — Prove ownership (mandatory sections)
Every post must include an “Ownership Evidence” section that contains:
- What I built/changed OR derived/explained
- What I ran OR computed (commands / calculations / small script)
- What I observed OR verified (outputs / test vectors / sanity checks)
- Artifacts (sanitized): (logs for practice; notes, equations, code snippets for theory)

If artifacts are missing, the post must explicitly state that it is “concept-only” and include a plan to gather evidence next time.

### Step 3 — Redaction discipline
- Prefer small excerpts (10–30 lines).
- Do not dump entire configs or long logs.
- Include a line near the top:
  `Anonymization: Yes — identifiers were modified.`

### Step 4 — Close-out metadata (mandatory)
End every post with:
- Tags (recommended)
- Next topics (3–5) from `codex/backlog/backlog.md`
- (Optional) a short “Runbook checklist” for repeatability

## Writing requirements
- Concise, technical, pragmatic.
- Explain decisions and tradeoffs.
- State limitations and false positives.
- Use confidence language:
  - High confidence: directly supported by evidence
  - Medium confidence: plausible but incomplete
  - Low confidence: hypothesis only

## Templates and backlog
- Post template: `codex/templates/article.md`
- Backlog (human-readable): `codex/backlog/backlog.md`
- The backlog file is the “source of truth” for topics and status.

Generated: 2026-01-06
