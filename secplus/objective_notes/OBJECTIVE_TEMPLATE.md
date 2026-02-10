# Objective Page Template for Claude Code

## Description

This template defines the standard structure for Security+ SY0-701 objective
pages published at `secplus/objectives/X-Y/index.md`. Use it when creating or
completing any pending objective.

### How to use this template

1. **Look up the objective** in `_data/secplus701.yml` to get the `id`, `slug`,
   `title`, `domain name`, and `domain id`.
2. **Copy the template below** (everything under "--- START TEMPLATE ---") into
   the target `secplus/objectives/X-Y/index.md` file, replacing the existing
   pending content.
3. **Replace every `{{PLACEHOLDER}}`** with the real value for that objective.
4. **Write the content sections** following the guidelines after the template.
5. **Update status** in `_data/secplus701.yml` from `"pending"` to `"done"` once
   the page is complete.
6. **Update the README** in `secplus/objective_notes/README.md` to mark the
   objective as complete (`[x]`).

### Placeholder reference

| Placeholder | Source | Example |
|---|---|---|
| `{{OBJECTIVE_ID}}` | `_data/secplus701.yml` `id` field | `2.1` |
| `{{OBJECTIVE_SLUG}}` | `_data/secplus701.yml` `slug` field | `2-1` |
| `{{OBJECTIVE_TITLE}}` | `_data/secplus701.yml` `title` field | `Compare and contrast common threat actors and motivations.` |
| `{{DOMAIN_ID}}` | `_data/secplus701.yml` domain `id` field | `2.0` |
| `{{DOMAIN_NAME}}` | `_data/secplus701.yml` domain `name` field | `Threats, Vulnerabilities, and Mitigations` |
| `{{PREV_SLUG}}` | Previous objective slug (or omit if first in domain) | `1-4` |
| `{{PREV_TITLE}}` | Previous objective title | `Explain the importance of...` |
| `{{NEXT_SLUG}}` | Next objective slug (or omit if last in domain) | `2-2` |
| `{{NEXT_TITLE}}` | Next objective title | `Explain common threat vectors...` |
| `{{DOMAIN_NAV_TABLE_ROWS}}` | All objectives in the same domain | see existing pages |
| `{{RELATED_OBJECTIVES}}` | 2-4 related objectives from other domains | see existing pages |

---

## --- START TEMPLATE ---

```markdown
---
layout: default
title: "Security+ {{OBJECTIVE_ID}} — {{OBJECTIVE_TITLE}}"
objective_id: "{{OBJECTIVE_ID}}"
domain: "{{DOMAIN_ID}} {{DOMAIN_NAME}}"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/{{OBJECTIVE_SLUG}}/
---

# Security+ {{OBJECTIVE_ID}} — {{OBJECTIVE_TITLE}}

Status: <span class="status-badge done">done</span>

## Exam objective
{{OBJECTIVE_TITLE}}

{% assign objective_slug = page.slug %}
{% if objective_slug == nil or objective_slug == '' or objective_slug == 'index' %}
  {% assign url_parts = page.url | split: '/' %}
  {% assign objective_slug = url_parts | last %}
  {% if objective_slug == '' %}
    {% assign objective_slug = url_parts | slice: -2, 1 | first %}
  {% endif %}
{% endif %}
{% assign objective_id = objective_slug | replace: '-', '.' %}
{% include official_scope_pdf.html objective_id=objective_id %}

---

## My notes

### Overview

<!-- 2-4 sentences introducing the topic and why it matters for the exam. -->

---

### <Section heading>

<!-- Organize the core content into logical subsections (### level).
     Use as many subsections as the topic demands.
     Each subsection should cover a distinct concept area.

     GUIDELINES:
     - Use comparison tables (markdown) whenever contrasting categories,
       types, or methods. Tables should have 3-6 columns.
     - Include "Memory aid" call-outs where helpful:
       > **Mnemonic** — explanation
     - Include "Exam tip" notes inline where relevant.
     - Keep language concise and exam-focused.
-->

---

### Key distinctions to know for the exam

<!-- Markdown table comparing easily confused concepts.
     Format:
     | Comparison | Distinction |
     |---|---|
     | **A vs. B** | A does X; B does Y. |
-->

---

### Common exam traps

<!-- 3-5 traps in bold/reality format:
     **Trap: <misconception>.**
     Reality: <correct understanding>.
-->

---

### Exam tips

<!-- Numbered list of 4-6 actionable tips for answering exam questions
     on this objective. -->

---

## Key terms

<!-- Bulleted glossary of 8-15 essential terms:
     - **Term** — Definition focused on exam relevance.
-->

---

## Examples / scenarios

<!-- 3-5 short scenarios with answers. Format:
     **Scenario N:** Description.
     - **Answer:** Explanation.
-->

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> <!-- Question text --></summary>

**Answer:** <!-- Explanation -->
</details>

<details>
<summary><strong>Question 2:</strong> <!-- Question text --></summary>

**Answer:** <!-- Explanation -->
</details>

<details>
<summary><strong>Question 3:</strong> <!-- Question text --></summary>

**Answer:** <!-- Explanation -->
</details>

<details>
<summary><strong>Question 4:</strong> <!-- Question text --></summary>

**Answer:** <!-- Explanation -->
</details>

<details>
<summary><strong>Question 5:</strong> <!-- Question text --></summary>

**Answer:** <!-- Explanation -->
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> <!-- Question text with 4 answer choices on separate lines using <br> --></summary>

**Correct Answer: <!-- Letter. Choice text -->**

<!-- Explanation of correct answer and why each distractor is wrong. -->
</details>

<details>
<summary><strong>Question 7:</strong> <!-- Question text with 4 answer choices --></summary>

**Correct Answer: <!-- Letter. Choice text -->**

<!-- Explanation -->
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> <!-- Question text with 5 answer choices, ask to select TWO --></summary>

**Correct Answers: <!-- Letters. Choice texts -->**

<!-- Explanation -->
</details>

---

## Related objectives

<!-- 2-4 links to related objectives from other domains:
- [**X.Y**]({{ '/secplus/objectives/X-Y/' | relative_url }}) — Brief reason for the relationship
-->

---

## Navigation

**Domain {{DOMAIN_ID}}: {{DOMAIN_NAME}}**

| Objective | Title | Status |
|---|---|---|
{{DOMAIN_NAV_TABLE_ROWS}}

[← Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective {{NEXT_SLUG}} →]({{ '/secplus/objectives/{{NEXT_SLUG}}/' | relative_url }})
```

## --- END TEMPLATE ---

---

## Content guidelines

### Tone and depth
- Write for someone who has watched the video lectures and needs a concise,
  exam-focused review — not a textbook chapter.
- Prefer short sentences and bullet points over paragraphs.
- Bold key terms on first use.

### Tables
- Use markdown tables for any comparison of 3+ items.
- Keep column count between 3 and 6 for readability.
- Include an "Exam tip" or "Key phrase" column where it helps recognition.

### Memory aids
- Add at least one mnemonic or memory aid per major concept group.
- Format as a blockquote: `> **Mnemonic** — explanation`

### Quiz questions
- Questions 1-5: open-ended with collapsible answers (concept recall).
- Questions 6-7: four-choice single-answer (CompTIA PBQ style).
- Question 8: five-choice multi-select (select TWO) — CompTIA frequently
  uses this format.
- Every answer must explain WHY the correct choice is right and WHY each
  distractor is wrong.

### Navigation section
- List ALL objectives in the same domain in the navigation table.
- Mark the current objective row with `(current)` and no link.
- The "Next" link at the bottom should point to the next objective; for the
  last objective in a domain, link to the first objective of the next domain.

### Cross-references
- The "Related objectives" section should link to 2-4 objectives from OTHER
  domains that share conceptual overlap.
- Include a brief reason for each relationship.

### Checklist before marking done
- [ ] Front matter is complete (layout, title, objective_id, domain, status,
      tags, permalink).
- [ ] Liquid PDF include block is present and unmodified.
- [ ] All content sections are filled (no "Pending." placeholders remain).
- [ ] At least 8 quiz questions (5 open + 3 CompTIA-style).
- [ ] Navigation table lists every objective in the domain.
- [ ] Status updated to `"done"` in `_data/secplus701.yml`.
- [ ] README.md checkbox updated to `[x]`.
