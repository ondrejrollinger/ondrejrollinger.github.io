---
layout: default
title: IoT Tags
permalink: /iot/tags/
---

<div class="page-header">
  <h1 class="page-title">Tags</h1>
</div>
<p class="page-description">Browse IoT posts by topic. Links go to the site-wide tag pages.</p>

{% assign tags_sorted = site.tags | sort %}
<ul class="tag-list">
  {% for t in tags_sorted %}
    {% assign tag_name = t[0] %}
    {% assign tag_slug = tag_name | slugify %}
    {% assign tag_posts = t[1] %}
    {% assign iot_match = tag_posts | where_exp: "post", "post.tags contains 'iot'" %}
    {% if iot_match.size > 0 %}
    <li class="tag-list-item">
      <a href="/tag-{{ tag_slug }}/">
        <span class="tag-name">#{{ tag_name }}</span>
        <span class="tag-count">{{ tag_posts | size }} post{% if tag_posts.size != 1 %}s{% endif %}</span>
      </a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
