---
layout: default
title: CompTIA Security+ (SY0-701) Dashboard
permalink: /secplus/
---

# CompTIA Security+ (SY0-701) Dashboard

This dashboard tracks my progress across the SY0-701 exam objectives. Each objective links to a dedicated notes page and carries a simple status badge.

Exam objectives content © CompTIA. Source: SY0-701 Exam Objectives (v5.0).

{% assign total = 0 %}
{% assign pending = 0 %}
{% assign in_progress = 0 %}
{% assign review = 0 %}
{% assign done = 0 %}
{% assign pdf_path = site.data.sy0_701_pdf_pages.pdf.path %}

{% for domain in site.data.secplus701.domains %}
  {% for objective in domain.objectives %}
    {% assign total = total | plus: 1 %}
    {% case objective.status %}
      {% when 'pending' %}
        {% assign pending = pending | plus: 1 %}
      {% when 'in-progress' %}
        {% assign in_progress = in_progress | plus: 1 %}
      {% when 'review' %}
        {% assign review = review | plus: 1 %}
      {% when 'done' %}
        {% assign done = done | plus: 1 %}
    {% endcase %}
  {% endfor %}
{% endfor %}

{% if total > 0 %}
  {% assign completion = done | times: 100 | divided_by: total %}
{% else %}
  {% assign completion = 0 %}
{% endif %}

<div class="secplus-summary">
  <div><strong>Total objectives:</strong> {{ total }}</div>
  <div><strong>Pending:</strong> {{ pending }}</div>
  <div><strong>In progress:</strong> {{ in_progress }}</div>
  <div><strong>Review:</strong> {{ review }}</div>
  <div><strong>Done:</strong> {{ done }}</div>
  <div><strong>Completion:</strong> {{ completion }}%</div>
</div>

{% for domain in site.data.secplus701.domains %}
  <section class="secplus-domain">
    <h2>{{ domain.id }} {{ domain.name }} ({{ domain.weight }}%)</h2>
    <div class="secplus-table-wrapper">
      <table class="secplus-table">
        <thead>
          <tr>
            <th scope="col">Objective</th>
            <th scope="col">Title</th>
            <th scope="col">Status</th>
            <th scope="col">Link</th>
            <th scope="col">Official</th>
          </tr>
        </thead>
        <tbody>
          {% for objective in domain.objectives %}
            {% assign pdf_page = site.data.sy0_701_pdf_pages.pdf.objectives[objective.id] %}
            <tr>
              <td>{{ objective.id }}</td>
              <td>{{ objective.title }}</td>
              <td>
                <span class="status-badge {{ objective.status }}">
                  {{ objective.status | replace: '-', ' ' }}
                </span>
              </td>
              <td>
                <a href="{{ '/secplus/objectives/' | append: objective.slug | append: '/' | relative_url }}">
                  View notes
                </a>
              </td>
              <td>
                <a href="{{ '/secplus/objectives/' | append: objective.slug | append: '/#official-scope' | relative_url }}">
                  Official scope
                </a>
                {% if pdf_page %}
                  <span aria-hidden="true"> · </span>
                  <a href="{{ site.baseurl }}{{ pdf_path }}#page={{ pdf_page }}" target="_blank" rel="noreferrer noopener">
                    PDF p.{{ pdf_page }}
                  </a>
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </section>
{% endfor %}
