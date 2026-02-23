---
layout: default
title: Tags
permalink: /tags/
---

# Tags

Browse topics across investigations, projects, and theory notes using consistent tags and tracks.

{% assign tags_sorted = site.tags | sort %}
<ul>
{% for t in tags_sorted %}
  {% assign tag_name = t[0] %}
  {% assign tag_slug = tag_name | slugify %}
  {% assign posts = t[1] %}
  <li>
    <a href="{{ '/tag/' | append: tag_slug | append: '/' | relative_url }}">
      {{ tag_name }}
    </a>
    ({{ posts | size }})
  </li>
{% endfor %}
</ul>

<p><a href="{{ '/' | relative_url }}">← Home</a></p>
