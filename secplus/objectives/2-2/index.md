---
layout: default
title: "Security+ 2.2 — Explain common threat vectors and attack surfaces."
objective_id: "2.2"
domain: "2.0 Threats, Vulnerabilities, and Mitigations"
status: "pending"
tags:
  - secplus701
permalink: /secplus/objectives/2-2/
---

# Security+ 2.2 — Explain common threat vectors and attack surfaces.

Status: <span class="status-badge pending">Pending</span>

## Exam objective
Explain common threat vectors and attack surfaces.

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

## My notes
- Pending.

## Key terms
- Pending.

## Examples / scenarios
- Pending.

## Mini quiz
- Pending.
