---
layout: about
title: about
permalink: /

profile:
  align: right
  image: profile/DDK.JPG

publication: true  # includes a list of papers
publication_years: [2025, 2024, 2023, 2022]  # to show the papers in these years
social: true  # includes social icons at the bottom of the page
---

I am a final-year Ph.D. student in the School of Computer Science at Peking University, advised by Prof. Boxin Shi at the <a href="https://camera.pku.edu.cn" target="_blank">Camera Intelligence Lab</a>. My current research interests lie in Computational Photography and Generative AI, with a primary focus on neuromorphic cameras and video generation.

I obtained my B.S. in Computer Science from the School of EECS and my B.H. in History from the Department of History at Peking University in 2021, with the History degree earned as a double degree.

Outside of research, I am a railway and aviation enthusiast, and I enjoy photography — some of my shots can be found in the <a href="/gallery">gallery</a>. I also share photos and stories on <a href="{{ site.rednote_url }}" target="_blank">Xiaohongshu (RedNote)</a>; feel free to follow and say hi!

## Selected Publications
<div class="publications">
<p><sup>*</sup> Equal Contribution</p>
{% for y in page.publication_years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}, selected=true]* %}
{% endfor %}
<div class="center-button">
  <a href="/publications" class="btn btn-transparent">all publications</a>
</div>
</div>

<br>

## Experiences

{% include experiences.html %}

<br>

## Services

{% include services.html %}
