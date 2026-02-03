---
layout: default
title: "Security+ 1.2 — Summarize fundamental security concepts."
objective_id: "1.2"
domain: "1.0 General Security Concepts"
status: "pending"
tags:
  - secplus701
permalink: /secplus/objectives/1-2/
---

# Security+ 1.2 — Summarize fundamental security concepts.

Status: <span class="status-badge pending">Pending</span>

## Exam objective
Summarize fundamental security concepts.

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
