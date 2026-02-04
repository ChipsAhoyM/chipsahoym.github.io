---
layout: page
permalink: /publications/
title: publications
description:
years: [2025, 2024, 2023, 2022, 2021]
nav: true
---

<div class="publications">
<div class="pub-legend">
  <span class="legend-item"><sup>*</sup> Equal Contribution</span>
  <span class="legend-item"><i class="fas fa-envelope mail-small"></i> Corresponding Author</span>
</div>
{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
</div>

<style>
  .pub-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    padding: 1rem 1.2rem;
    background: rgba(128, 128, 128, 0.05);
    border-radius: 8px;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--global-text-color-light);
  }
  .legend-item {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
  }
  .legend-item sup {
    font-size: 1rem;
    color: var(--global-theme-color);
  }
  .legend-item i {
    color: var(--global-theme-color);
    font-size: 0.85rem;
  }
</style>
