---
layout: default
title: "Security+ 3.2 — Given a scenario, apply security principles to secure enterprise infrastructure."
objective_id: "3.2"
domain: "3.0 Security Architecture"
status: "pending"
tags:
  - secplus701
permalink: /secplus/objectives/3-2/
---

# Security+ 3.2 — Given a scenario, apply security principles to secure enterprise infrastructure.

Status: <span class="status-badge pending">Pending</span>

## Exam objective
Given a scenario, apply security principles to secure enterprise infrastructure.

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
