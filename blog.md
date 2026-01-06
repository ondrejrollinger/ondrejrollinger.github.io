---
layout: default
title: Blog
permalink: /blog/
---

# Blog

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url | relative_url }})**
  <small>({{ post.date | date: "%-d %b %Y" }})</small>
  {% if post.tags %}
  — Tags:
    {% for tag in post.tags %}
      [{{ tag }}]({{ '/tag/' | append: (tag | slugify) | append: '/' | relative_url }}){% unless forloop.last %}, {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}
