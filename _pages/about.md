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
    border: 1.5px solid var(--global-theme-color, #007bff);
    color: var(--global-theme-color, #007bff);
    padding: 8px 20px;
    font-size: 14px;
    border-radius: 25px;
    text-decoration: none;
    transition: all 0.3s ease;
    font-weight: 500;
    letter-spacing: 0.5px;
  }

  .btn-transparent:hover {
    background-color: var(--global-theme-color, #007bff);
    color: #fff;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.25);
    text-decoration: none;
  }

  .center-button {
    text-align: center;
    margin-top: 30px;
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
    margin-top: 15px;
  }

  .services li {
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    padding: 12px 16px;
    background: var(--global-bg-color, #fff);
    border-radius: 8px;
    border: 1px solid rgba(128, 128, 128, 0.1);
    transition: all 0.2s ease;
  }

  .services li:hover {
    border-color: var(--global-theme-color, #007bff);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .services i {
    margin-right: 14px;
    color: var(--global-theme-color, #6c757d);
    font-size: 18px;
    flex-shrink: 0;
    width: 25px;
    text-align: center;
    margin-top: 2px;
  }

  .services .text {
    line-height: 1.5;
    font-size: 15px;
  }

  .services strong {
    font-weight: 600;
  }

  .services .divider {
    border: none;
    border-top: 1px solid rgba(128, 128, 128, 0.2);
    margin-bottom: 20px;
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

<style>
  .experience ul {
    list-style: none;
    padding-left: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 24px;
    margin-top: 15px;
  }

  .experience li {
    background-color: var(--global-bg-color, #f8f9fa);
    padding: 24px 20px;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    border: 1px solid rgba(128, 128, 128, 0.1);
    transition: all 0.3s ease;
  }

  .experience li:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    border-color: var(--global-theme-color, #007bff);
  }

  .experience li a {
    text-decoration: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .experience .logo {
    width: auto;
    height: 45px;
    object-fit: contain;
    margin-bottom: 18px;
    transition: transform 0.3s ease;
  }

  .experience li:hover .logo {
    transform: scale(1.05);
  }

  .experience .text {
    line-height: 1.5;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .experience .role {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 4px;
    color: var(--global-text-color, #333);
  }

  .experience .time {
    font-size: 13px;
    color: var(--global-text-color-light, #6c757d);
  }

  .experience .divider {
    border: none;
    border-top: 1px solid rgba(128, 128, 128, 0.2);
    margin-bottom: 20px;
  }

  @media (prefers-color-scheme: light) {
    .divider {
      border-color: #ddd;
    }
  }

  @media (prefers-color-scheme: dark) {
    .divider {
      border-color: #333;
    }
    .experience li {
      background-color: rgba(255, 255, 255, 0.03);
    }
  }

  @media screen and (max-width: 480px) {
    .experience ul {
      grid-template-columns: 1fr;
      gap: 16px;
    }
    .experience li {
      padding: 18px 15px;
    }
    .experience .logo {
      height: 35px;
      margin-bottom: 12px;
    }
    .experience .role {
      font-size: 14px;
    }
    .experience .time {
      font-size: 12px;
    }
  }
</style>
