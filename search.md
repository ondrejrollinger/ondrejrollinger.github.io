---
layout: default
title: Search
permalink: /search/
---

<div class="page-header">
  <h1 class="page-title">Search</h1>
</div>
<p class="page-description">Search across posts and notes to quickly find tools, playbooks, investigations, and key concepts.</p>

<input id="q" type="search" placeholder="Search..." autofocus />
<p id="results-count"></p>
<div id="search-results"></div>

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
  const out = document.getElementById('search-results');
  const count = document.getElementById('results-count');

  function render(query) {
    out.innerHTML = '';
    count.textContent = '';
    if (!query || query.length < 2) return;
    const hits = idx.search(query).slice(0, 20);
    count.textContent = hits.length + ' result' + (hits.length === 1 ? '' : 's');
    hits.forEach(h => {
      const doc = docs.find(d => d.url === h.ref);
      const item = document.createElement('div');
      item.className = 'search-result-item';
      item.innerHTML = '<a class="search-result-title" href="' + doc.url + '">' + doc.title + '</a>'
        + (doc.date ? '<span class="search-result-date">' + doc.date + '</span>' : '');
      out.appendChild(item);
    });
  }

  q.addEventListener('input', () => render(q.value));
})();
</script>
