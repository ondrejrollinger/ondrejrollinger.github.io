---
layout: default
title: Tags
permalink: /tags/
---

<div class="page-header">
  <h1 class="page-title">Tags</h1>
</div>
<p class="page-description">Browse topics across investigations, projects, and theory notes.</p>

{% assign tags_sorted = site.tags | sort %}
<ul class="tag-list">
  {% for t in tags_sorted %}
    {% assign tag_name = t[0] %}
    {% assign tag_slug = tag_name | slugify %}
    {% assign posts = t[1] %}
    <li class="tag-list-item">
      <a href="/tag-{{ tag_slug }}/">
        <span class="tag-name">#{{ tag_name }}</span>
        <span class="tag-count">{{ posts | size }} post{% if posts.size != 1 %}s{% endif %}</span>
      </a>
    </li>
  {% endfor %}
</ul>
