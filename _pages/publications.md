---
layout: page
permalink: /publications/
title: publications
description: 
years: [2025, 2024, 2023, 2022, 2021]
nav: true
---

<div class="publications">
<p><sup>*</sup>   Equal Contribution   <sup><i class="fas fa-envelope mail-small"></i></sup>  Corresponding Author</p>
{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
