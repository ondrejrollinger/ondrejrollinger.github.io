---
layout: default
title: Search
permalink: /search/
---

# Search

Search across posts and notes to quickly find tools, playbooks, investigations, and key concepts.

<input id="q" type="search" placeholder="Search..." autofocus />
<div id="results"></div>

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script>
(async function () {
  const res = await fetch("{{ '/search.json' | relative_url }}");
  const docs = await res.json();

  const idx = lunr(function () {
    this.ref('url');
    this.field('title');
    this.field('content');
    this.field('tags');
    docs.forEach(d => this.add(d));
  });

  const q = document.getElementById('q');
  const out = document.getElementById('results');

  function render(query) {
    out.innerHTML = "";
    if (!query || query.length < 2) return;
    const hits = idx.search(query).slice(0, 20);
    hits.forEach(h => {
      const doc = docs.find(d => d.url === h.ref);
      const a = document.createElement('a');
      a.href = doc.url;
      a.textContent = doc.title;
      const div = document.createElement('div');
      div.appendChild(a);
      out.appendChild(div);
    });
  }

  q.addEventListener('input', () => render(q.value));
})();
</script>

<p><a href="{{ '/' | relative_url }}">← Home</a></p>
