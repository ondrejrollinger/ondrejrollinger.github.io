---
layout: default
title: Blog
permalink: /blog/
---

<h1>Blog</h1>

<ul>
{% for post in site.posts %}
  <li>
    <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <small>({{ post.date | date: "%-d %b %Y" }})</small>

    {% if post.tags %}
      <div>
        <small>Tags:
          {% for tag in post.tags %}
            <a href="{{ '/tag/' | append: (tag | slugify) | append: '/' | relative_url }}">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </small>
      </div>
    {% endif %}
  </li>
{% endfor %}
</ul>
