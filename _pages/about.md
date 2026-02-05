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
  <div class="services-grid">
    <div class="service-card">
      <div class="card-header">
        <i class="fas fa-edit"></i>
        <h3>Academic Review</h3>
      </div>
      <div class="card-content">
        <div class="service-item">
          <span class="label">Conferences</span>
          <span class="venues">CVPR, ICCV, ECCV, NeurIPS, ICML, AAAI, MM</span>
        </div>
        <div class="service-item">
          <span class="label">Journals</span>
          <span class="venues">TPAMI, TIP, TCSVT, TCI</span>
        </div>
      </div>
    </div>
    <div class="service-card">
      <div class="card-header">
        <i class="fas fa-chalkboard-teacher"></i>
        <h3>Teaching & Mentoring</h3>
      </div>
      <div class="card-content">
        <div class="service-item">
          <span class="label">Mentor</span>
          <span class="venues">Turing Class, EECS, PKU (2021-2025)</span>
        </div>
        <div class="service-item">
          <span class="label">TA</span>
          <span class="venues">Computational Photography (Spring 2022)</span>
        </div>
        <div class="service-item">
          <span class="label">TA</span>
          <span class="venues">Ideological & Moral Cultivation (Autumn 2022)</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .services .divider {
    border: none;
    border-top: 1px solid rgba(128, 128, 128, 0.2);
    margin-bottom: 20px;
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
  }

  .service-card {
    background: var(--global-bg-color, #fff);
    border: 1px solid rgba(128, 128, 128, 0.1);
    border-radius: 12px;
    padding: 20px 24px;
    transition: all 0.3s ease;
  }

  .service-card:hover {
    border-color: var(--global-theme-color, #007bff);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transform: translateY(-2px);
  }

  .card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(128, 128, 128, 0.1);
  }

  .card-header i {
    color: var(--global-theme-color, #007bff);
    font-size: 20px;
  }

  .card-header h3 {
    margin: 0;
    font-size: 16px;
    font-weight: 600;
    color: var(--global-text-color, #333);
  }

  .card-content {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .service-item {
    display: flex;
    align-items: baseline;
    gap: 10px;
  }

  .service-item .label {
    font-size: 12px;
    font-weight: 600;
    color: var(--global-theme-color, #007bff);
    background: rgba(0, 123, 255, 0.08);
    padding: 2px 8px;
    border-radius: 4px;
    flex-shrink: 0;
    min-width: 75px;
    text-align: center;
  }

  .service-item .venues {
    font-size: 14px;
    color: var(--global-text-color, #555);
    line-height: 1.5;
  }

  @media screen and (max-width: 600px) {
    .services-grid {
      grid-template-columns: 1fr;
    }
    .service-card {
      padding: 16px 18px;
    }
    .service-item {
      flex-direction: column;
      gap: 4px;
    }
    .service-item .label {
      min-width: auto;
    }
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
