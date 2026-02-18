# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal cybersecurity portfolio and learning site built with Jekyll, hosted on GitHub Pages. It serves as a public notebook for hands-on security work and CompTIA Security+ SY0-701 exam preparation.

## Build and development

```bash
# Serve locally with live reload
bundle exec jekyll serve

# Production build (mirrors GitHub Actions)
JEKYLL_ENV=production bundle exec jekyll build
```

The site deploys automatically on push to `main` via `.github/workflows/pages.yml`.

## Architecture

The site combines a standard Jekyll blog with two purpose-built subsystems:

### Blog (`_posts/`)
Standard Jekyll posts with filename `YYYY-MM-DD-short-slug.md`. The article workflow is defined in `AGENTS.md` and uses the template at `codex/templates/article.md`. Topic backlog lives in `codex/backlog/backlog.md` (source of truth for article status).

### Security+ dashboard (`secplus/`)
A study tracker for all 28 SY0-701 objectives across 5 domains.

- **`_data/secplus701.yml`** — Single source of truth for objective metadata (id, slug, title, domain, status). The dashboard at `secplus/index.md` reads this file to render the status overview.
- **`secplus/objectives/X-Y/index.md`** — Published objective pages (one per objective). Completed objectives follow the template in `secplus/objective_notes/OBJECTIVE_TEMPLATE.md`.
- **`secplus/objective_notes/`** — Draft/working notes before a page is published. `README.md` in this folder tracks completion with checkboxes.
- **`secplus/_data/sy0_701_pdf_pages.yml`** — Maps objective IDs to page numbers in the official CompTIA PDF so `_includes/official_scope_pdf.html` can deep-link.
- **`assets/comptia/CompTIA-Security-Plus-SY0-701-Exam-Objectives-v5.0.pdf`** — Must stay at this path; do not rename without updating the mapping.

### Tag system
`_plugins/tag_generator.rb` dynamically generates tag pages at build time — there is no `_tags/` directory to maintain manually.

### Theme and layout
Uses `jekyll-theme-hacker`. Custom CSS is in `assets/css/site.css`. The sidebar nav is `_includes/sidebar.html`. Do not refactor layout or theme files unless explicitly asked.

## Completing a Security+ objective

1. Look up the objective in `_data/secplus701.yml` to get `id`, `slug`, `title`, domain `id` and `name`.
2. Copy the template from `secplus/objective_notes/OBJECTIVE_TEMPLATE.md` into `secplus/objectives/X-Y/index.md`, replacing all `{{PLACEHOLDER}}` values.
3. Write content following the template's guidelines (comparison tables, mnemonics, exam tips, 8 quiz questions: 5 open + 2 four-choice + 1 five-choice multi-select).
4. Update `status` in `_data/secplus701.yml` from `"pending"` to `"done"`.
5. Check the objective off (`[x]`) in `secplus/objective_notes/README.md`.

## Writing blog posts

Follow the workflow in `AGENTS.md`:
- Every post requires an **Ownership Evidence** section (what was built, run, observed, and any sanitized artifacts).
- All identifiers must be anonymized (IPs, hostnames, usernames, MACs, SSIDs).
- Defensive framing only — no step-by-step exploit instructions.
- State confidence level: High (evidence-backed) / Medium (plausible) / Low (hypothesis).
- End each post with tags, 3–5 next topics from the backlog, and optionally a runbook checklist.

## Key conventions

- Front matter fields used across the site: `layout`, `title`, `objective_id`, `domain`, `status`, `tags`, `permalink`.
- Permalink pattern for blog posts: `/blog/:year/:month/:day/:title/`.
- Status badge values: `pending`, `in-progress`, `review`, `done` — rendered as colored spans via `site.css`.
- Collapsible quiz answers use native HTML `<details>`/`<summary>` elements (no JS framework).
- Do not add gems, npm packages, or GitHub Actions steps without an explicit request.
