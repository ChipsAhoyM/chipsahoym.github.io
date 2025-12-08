---
layout: about
title: about
permalink: /

profile:
  align: right
  image: DDK.JPG

publication: true  # includes a list of papers
publication_years: [2025, 2024, 2023, 2022]  # to show the papers in these years
social: true  # includes social icons at the bottom of the page
---

I am a final-year Ph.D. student in the School of Computer Science at Peking University, advised by Prof. Boxin Shi at the <a href="https://camera.pku.edu.cn" target="_blank">Camera Intelligence Lab</a>. My current research interests lie in Computational Photography and Generative AI, with a primary focus on neuromorphic cameras and video generation.

My goal is to reimagine the future of camera systems by integrating neuromorphic cameras or advanced generative models, unlocking new possibilities in how we capture and create visual experiences. As an amateur photographer, I enjoy capturing the world through my lens. Explore <a href="/gallery/">gallery</a> to see images in the recent time.

I obtained my B.S. in Computer Science from the School of EECS and my B.H. in History from the Department of History at Peking University in 2021. During my undergraduate studies, I concentrated on low-quality image enhancement guided by event cameras. In addition, I maintain a strong interest in contemporary world history, particularly the history of science and technology.
<br>
<br>
<br>
<br>

## Selected Publications
<div class="publications">
<p><sup>*</sup>   Equal Contribution   <sup><i class="fas fa-envelope mail-small"></i></sup>  Corresponding Author</p>
{% for y in page.publication_years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}, selected=true]* %}
{% endfor %}
<div class="center-button">
      <a href="/publications" class="btn btn-transparent">all publications</a>
</div>
</div>

<style>
  .btn-transparent {
    background-color: transparent;
    border: 1px solid #007bff;
    color: #007bff;
    padding: 5px 10px;
    font-size: 14px;
    border-radius: 5px;
    text-decoration: none;
  }

  .btn-transparent:hover {
    background-color: #007bff;
    color: #fff;
  }

  .center-button {
    text-align: center;
    margin-top: 20px;
  }
</style>


<br>

## Services
<div class="services">
  <hr class="divider">
  <ul>
    <li>
      <i class="fas fa-book-open"></i>
      <div class="text">
        Reviewer of Conferences: CVPR 2023/2024, ICCV 2023/2025, ECCV 2022/2024, NeurIPS 2025, ICML 2025, AAAI 2025/2026, MM 2025
      </div>
    </li>
    <li>
      <i class="fas fa-book-reader"></i>
      <div class="text">
        Reviewer of Journal: TPAMI, TIP, TCSVT, TCI
      </div>
    </li>
    <li>
      <i class="fas fa-user-graduate"></i>
      <div class="text">
        Undergraduate Student Mentor: Turing Class, EECS, Peking University, 2021/9-2025/7
      </div>
    </li>
    <li>
      <i class="fas fa-chalkboard-teacher"></i>
      <div class="text">
        Teaching Assistant: Computational Photography, Spring 2021-2022
      </div>
    </li>
    <li>
      <i class="fas fa-chalkboard-teacher"></i>
      <div class="text">
        Teaching Assistant: Ideological & Moral Cultivation and Fundamentals of Law, Autumn 2021-2022
      </div>
    </li>
  </ul>
</div>

<style>
  .services ul {
    list-style: none;
    padding-left: 0;
  }

  .services li {
    margin-bottom: 10px;
    display: flex;
  }

  .services i {
    margin-right: 10px;
    color: #6c757d;
    font-size: 18px;
    flex-shrink: 0;
    width: 25px;
    text-align: center;
  }

  .services .text {
    line-height: 1.4;
    font-size: 16px;
  }

  .services strong {
    font-weight: 600;
  }
</style>

<br>

## Experiences
<div class="experience">
  <hr class="divider">
  <ul>
    <li>
      <a href="https://camera.pku.edu.cn" target="_blank">
        <img src="/assets/img/cameralab.png" alt="Camera Team Logo" class="logo">
        <div class="text">
          <span class="time">Research Assistant</span>
          <span class="time">February 2019 - Present</span>
        </div>
      </a>
    </li>
    <li>
      <a href="https://www.nii.ac.jp/en/" target="_blank">
        <img src="/assets/img/NII.png" alt="NII Logo" class="logo">
        <div class="text">
          <span class="time">Visiting Student</span>
          <span class="time"> September 2025 - March 2026</span>
        </div>
      </a>
    </li>
    <li>
      <a href="https://apple.com" target="_blank">
        <img src="/assets/img/apple.png" alt="Apple Logo" class="logo">
        <div class="text">
          <span class="time">ML Engineer Intern</span>
          <span class="time">February 2025 - August 2025</span>
        </div>
      </a>
    </li>
  </ul>
</div>

<style> .experience ul { list-style: none; padding-left: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; } .experience li { background-color: #f8f9fa; padding: 20px; border-radius: 5px; display: flex; flex-direction: column; align-items: center; text-align: center; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); } .experience .logo { width: auto; height: 40px; object-fit: contain; margin-bottom: 15px; } .experience .text { line-height: 1.4; display: flex; flex-direction: column; } .experience .role { font-size: 16px; font-weight: bold; margin-bottom: 5px; } .experience .time { font-size: 14px; color: #6c757d; } @media (prefers-color-scheme: light) { .divider { border-color: #ddd; } } @media (prefers-color-scheme: dark) { .divider { border-color: #333; } } @media screen and (max-width: 480px) { .experience ul { grid-template-columns: 1fr; } .experience li { padding: 15px; } .experience .logo { height: 30px; margin-bottom: 10px; } .experience .role { font-size: 14px; } .experience .time { font-size: 12px; } } </style>
