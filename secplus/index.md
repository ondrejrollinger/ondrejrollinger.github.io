---
layout: page
title: CompTIA Security+ (SY0-701) Dashboard
permalink: /secplus/
---

This dashboard tracks my progress across the SY0-701 exam objectives. Each objective links to a dedicated notes page and carries a simple status badge.

{% assign total = 0 %}
{% assign pending = 0 %}
{% assign in_progress = 0 %}
{% assign review = 0 %}
{% assign done = 0 %}
{% assign pdf_path = site.data.sy0_701_pdf_pages.pdf.local_path %}

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

<div class="secplus-stats">
  <div class="secplus-stat secplus-stat--done">
    <span class="secplus-stat-value">{{ done }}</span>
    <span class="secplus-stat-label">Done</span>
  </div>
  <div class="secplus-stat">
    <span class="secplus-stat-value">{{ in_progress }}</span>
    <span class="secplus-stat-label">In progress</span>
  </div>
  <div class="secplus-stat">
    <span class="secplus-stat-value">{{ review }}</span>
    <span class="secplus-stat-label">Review</span>
  </div>
  <div class="secplus-stat">
    <span class="secplus-stat-value">{{ pending }}</span>
    <span class="secplus-stat-label">Pending</span>
  </div>
  <div class="secplus-stat secplus-stat--total">
    <span class="secplus-stat-value">{{ total }}</span>
    <span class="secplus-stat-label">Total</span>
  </div>
</div>
<div class="secplus-progress">
  <div class="secplus-progress-bar" style="width: {{ completion }}%"></div>
</div>
<p class="secplus-progress-label">{{ completion }}% complete — {{ done }} of {{ total }} objectives</p>

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
                  Official PDF
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

<p><strong>Attribution:</strong> Exam objectives content © CompTIA. Source: SY0-701 Exam Objectives (v5.0).</p>
