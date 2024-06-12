---
layout: page
permalink: /gallery/
title: gallery
description: 
nav: true
---


<div class="gallery">
    <div class="gallery-description">
        <p>Embark on a visual journey through stunning landscapes, vibrant cityscapes, and captivating moments captured between 2023-2024.</p>
    </div>
    <div class="photographs">
        <div class="photograph">
            <img src="/assets/gallery-thumb/Boya.JPG" alt="Photograph 1" data-full="/assets/gallery/Boya.JPG" class="gallery-image">
            <div class="photograph-title">
                <p><i class="fas fa-map-marker-alt"></i> Boya Tower</p>
                <p>The moon illuminates an iconic tower against the night sky</p>
            </div>
        </div>
        <div class="photograph">
            <img src="/assets/gallery-thumb/HRB.PNG" alt="Photograph 2" data-full="/assets/gallery/HRB.PNG" class="gallery-image">
            <div class="photograph-title">
                <p><i class="fas fa-map-marker-alt"></i> Harbin</p>
                <p>A building showcases the artistic potential of ice through its sleek, gleaming design</p>
            </div>
        </div>
        <div class="photograph">
            <img src="/assets/gallery-thumb/Kobe.JPG" alt="Photograph 3" data-full="/assets/gallery/Kobe.JPG" class="gallery-image">
            <div class="photograph-title">
                <p><i class="fas fa-map-marker-alt"></i> Kobe</p>
                <p>A tranquil harbor at dusk with boats silhouetted against the setting sun</p>
            </div>
        </div>
        <div class="photograph">
            <img src="/assets/gallery-thumb/Nara.jpg" alt="Photograph 4" data-full="/assets/gallery/Nara.jpg" class="gallery-image">
            <div class="photograph-title">
                <p><i class="fas fa-map-marker-alt"></i> Nara</p>
                <p>My friend photographed me sitting and admiring the scenic view</p>
            </div>
        </div>
        <div class="photograph">
            <img src="/assets/gallery-thumb/XinSu.JPG" alt="Photograph 5" data-full="/assets/gallery/XinSu.JPG" class="gallery-image">
            <div class="photograph-title">
                <p><i class="fas fa-map-marker-alt"></i> Shinjuku</p>
                <p>Busy street scene at night in Shinjuku with illuminated signs and crowds</p>
            </div>
        </div>
        <div class="photograph">
            <img src="/assets/gallery-thumb/Wuhan.JPG" alt="Photograph 6" data-full="/assets/gallery/Wuhan.JPG" class="gallery-image">
            <div class="photograph-title">
                <p><i class="fas fa-map-marker-alt"></i> Wuhan</p>
                <p>People admire a stunning Yangtze River sunset sharing a moment together.</p>
            </div>
        </div>
    </div>
</div>

<div id="fullscreen-overlay">
    <img id="fullscreen-image" src="" alt="Full Image">
</div>

<style>
    .gallery {
        padding: 30px;
    }

    .gallery-description {
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        border: 2px solid #ccc;
        border-radius: 5px;
    }

    .photographs {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
    }

    .photograph {
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        transition: transform 0.3s ease;
    }

    .photograph:hover {
        transform: scale(1.05);
    }

    .photograph img {
        width: 100%;
        height: auto;
        border-radius: 5px;
        object-fit: cover;
        aspect-ratio: 1/1;
        cursor: pointer;
    }

    .photograph-title {
        margin-top: 10px;
    }

    .photograph-title p {
        margin: 5px 0;
    }

    .photograph-title i {
        margin-right: 5px;
        color: #888;
    }

    #fullscreen-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 9999;
        text-align: center;
    }

    #fullscreen-image {
        max-width: 90%;
        max-height: 90%;
        margin-top: 5%;
        border-radius: 5px;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
    }
</style>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        var photographs = document.querySelectorAll('.photograph img');
        var fullscreenOverlay = document.getElementById('fullscreen-overlay');
        var fullscreenImage = document.getElementById('fullscreen-image');

        photographs.forEach(function(photograph) {
            photograph.addEventListener('click', function() {
                var imageSrc = this.getAttribute('data-full');
                fullscreenImage.src = imageSrc;
                fullscreenOverlay.style.display = 'block';
            });
        });

        fullscreenOverlay.addEventListener('click', function() {
            fullscreenOverlay.style.display = 'none';
        });
    });
</script>
