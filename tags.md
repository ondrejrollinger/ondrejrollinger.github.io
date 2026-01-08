---
layout: default
title: Tags
permalink: /tags/
---

# Tags

{% assign tags_sorted = site.tags | sort %}
<ul>
{% for t in tags_sorted %}
  {% assign tag_name = t[0] %}
  {% assign posts = t[1] %}
  <li>
    <a href="{{ '/tag/' | append: (tag_name | slugify) | append: '/' | relative_url }}">
      {{ tag_name }}
    </a>
    ({{ posts | size }})
  </li>
{% endfor %}
</ul>

<p><a href="{{ '/' | relative_url }}">← Home</a></p>
