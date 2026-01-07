# Write one publishable GitHub Pages post (evidence-driven)

Task:
- Use the user's case brief and artifacts to produce ONE publishable Markdown post.
- Apply strict redaction/anonymization (IPs, hostnames, usernames, domains, emails, tokens).
- Prefer measurable evidence and repeatable validation.

Output requirements:
- Create a file under `_posts/` unless repo conventions differ.
- File name: `YYYY-MM-DD-short-slug.md`
- Include Jekyll front matter: title, date, tags, track, level, status
- Must include:
  - `Anonymization: Yes — identifiers were modified.`
  - “Ownership Evidence” section (mandatory):
    * What I built/changed
    * What I ran (commands/queries/tests)
    * What I observed (results)
    * What I verified (expected vs actual)
    * Artifacts (sanitized)
- Include limitations + false positives.
- End with:
  - recommended tags
  - 3–5 follow-up topics from codex/backlog/backlog.md

Safety:
- Defensive content only; no exploit walkthroughs.
- If a claim is not supported by artifacts, mark it as hypothesis and list the missing evidence.
