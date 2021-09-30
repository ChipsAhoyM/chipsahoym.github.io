---
layout: about
title: about
permalink: /
description: PhD Candidate | Member of <a href="http://ci.idm.pku.edu.cn/">Camera Intelligence Lab</a> | Computational Photography

profile:
  align: right
  image: prof_pic.jpg
  address:

publication: true  # includes a list of papers
publication_years: [2021, 2020]  # to show the papers in these years
social: true  # includes social icons at the bottom of the page
---

## Education
* PhD candidate at [Peking University](https://english.pku.edu.cn/){:target="\_blank"}, Beijing, China
  
  Advisors: Prof. Chao Xu and Prof. Boxin Shi
  
  Sept. 2019 ~ Present, in Key Laboratory of Machine Perception (MOE), [Dept. of Machine Intelligence](http://www.cis.pku.edu.cn/English/Home.htm){:target="\_blank"}
  
* Bachelor of Engineering at [Huazhong University of Science and Technology](http://english.hust.edu.cn/){:target="\_blank"}, Wuhan, China

  Sept. 2015 ~ Jul. 2019, in School of Electronic Information and Communications

<br>
<br>

## Publications
<div class="publications">
{% for y in page.publication_years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
</div>
