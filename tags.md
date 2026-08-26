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
    {% assign iot_match = posts | where_exp: "post", "post.tags contains 'iot'" %}
    {% if iot_match.size == 0 %}
    <li class="tag-list-item">
      <a href="/tag-{{ tag_slug }}/">
        <span class="tag-name">#{{ tag_name }}</span>
        <span class="tag-count">{{ posts | size }} post{% if posts.size != 1 %}s{% endif %}</span>
      </a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
