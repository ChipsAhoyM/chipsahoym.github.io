---
layout: page
permalink: /gallery/
title: gallery
description:
nav: true
---

<div class="gallery">
    <div class="gallery-header">
        <p class="gallery-subtitle">Embark on a visual journey through stunning landscapes and vibrant cityscapes.</p>
    </div>
    <div class="photographs" id="photographs-container">
        <div class="loading-message">
            <div class="loading-spinner"></div>
            <span>Loading gallery...</span>
        </div>
    </div>
</div>

<div id="fullscreen-overlay">
    <button class="nav-btn nav-prev" id="nav-prev"><i class="fas fa-chevron-left"></i></button>
    <button class="nav-btn nav-next" id="nav-next"><i class="fas fa-chevron-right"></i></button>
    <button class="close-btn" id="close-btn"><i class="fas fa-times"></i></button>
    <div class="fullscreen-content">
        <img id="fullscreen-image" src="" alt="Full Image">
        <div class="image-caption" id="image-caption"></div>
    </div>
    <div class="image-counter" id="image-counter"></div>
</div>

<style>
    .gallery {
        padding: 20px 0;
    }

    .gallery-header {
        text-align: center;
        margin-bottom: 40px;
        padding: 30px 25px;
        background: linear-gradient(135deg, rgba(128, 128, 128, 0.03) 0%, rgba(128, 128, 128, 0.08) 100%);
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.1);
    }

    .gallery-subtitle {
        font-size: 1.1rem;
        color: var(--global-text-color-light, #666);
        margin: 0;
        line-height: 1.6;
    }

    .photographs {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 24px;
    }

    .photograph {
        background: var(--global-bg-color, #fff);
        border-radius: 16px;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid rgba(128, 128, 128, 0.1);
    }

    .photograph:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
        border-color: var(--global-theme-color, #007bff);
    }

    .image-wrapper {
        width: 100%;
        aspect-ratio: 4 / 3;
        overflow: hidden;
        background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
        position: relative;
    }

    .photograph img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        cursor: pointer;
        transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
        display: block;
    }

    .photograph:hover img {
        transform: scale(1.08);
    }

    .loading-message {
        text-align: center;
        padding: 60px 40px;
        color: var(--global-text-color-light, #888);
        grid-column: 1 / -1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 16px;
    }

    .loading-spinner {
        width: 40px;
        height: 40px;
        border: 3px solid rgba(128, 128, 128, 0.1);
        border-top-color: var(--global-theme-color, #007bff);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    .photograph-title {
        padding: 16px 18px;
    }

    .photograph-title p {
        margin: 0;
        line-height: 1.5;
    }

    .photograph-title p:first-child {
        font-weight: 500;
        color: var(--global-text-color, #333);
        display: flex;
        align-items: center;
    }

    .photograph-title p:last-child:not(:first-child) {
        font-size: 0.9rem;
        color: var(--global-text-color-light, #666);
        margin-top: 4px;
    }

    .photograph-title i {
        margin-right: 8px;
        color: var(--global-theme-color, #007bff);
        font-size: 0.9rem;
    }

    /* Fullscreen Overlay */
    #fullscreen-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.95);
        z-index: 9999;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    #fullscreen-overlay.active {
        opacity: 1;
    }

    .fullscreen-content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        max-width: 90%;
        max-height: 85%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #fullscreen-image {
        max-width: 100%;
        max-height: 80vh;
        border-radius: 8px;
        box-shadow: 0 25px 80px rgba(0, 0, 0, 0.5);
        transition: transform 0.3s ease;
    }

    .image-caption {
        color: rgba(255, 255, 255, 0.9);
        margin-top: 20px;
        text-align: center;
        font-size: 1rem;
        max-width: 600px;
    }

    .nav-btn {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background: rgba(255, 255, 255, 0.1);
        border: none;
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        cursor: pointer;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(10px);
    }

    .nav-btn:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-50%) scale(1.1);
    }

    .nav-prev { left: 20px; }
    .nav-next { right: 20px; }

    .close-btn {
        position: absolute;
        top: 20px;
        right: 20px;
        background: rgba(255, 255, 255, 0.1);
        border: none;
        color: white;
        width: 45px;
        height: 45px;
        border-radius: 50%;
        cursor: pointer;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(10px);
    }

    .close-btn:hover {
        background: rgba(255, 100, 100, 0.4);
        transform: scale(1.1);
    }

    .image-counter {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        background: rgba(0, 0, 0, 0.3);
        padding: 8px 16px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }

    @media (max-width: 768px) {
        .photographs {
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 16px;
        }

        .nav-btn {
            width: 40px;
            height: 40px;
            font-size: 1rem;
        }

        .nav-prev { left: 10px; }
        .nav-next { right: 10px; }
    }

    /* Dark mode adjustments */
    html[data-theme='dark'] .image-wrapper {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
    }

    html[data-theme='dark'] .photograph {
        background: rgba(255, 255, 255, 0.02);
    }
</style>

<script src="/assets/gallery-images.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        var fullscreenOverlay = document.getElementById('fullscreen-overlay');
        var fullscreenImage = document.getElementById('fullscreen-image');
        var imageCaption = document.getElementById('image-caption');
        var imageCounter = document.getElementById('image-counter');
        var container = document.getElementById('photographs-container');
        var navPrev = document.getElementById('nav-prev');
        var navNext = document.getElementById('nav-next');
        var closeBtn = document.getElementById('close-btn');
        var currentIndex = 0;

        // Check if galleryImages is defined
        if (typeof galleryImages === 'undefined' || !Array.isArray(galleryImages) || galleryImages.length === 0) {
            container.innerHTML = '<div class="loading-message">No images found in gallery. Edit assets/gallery-images.js to add images.</div>';
            return;
        }

        container.innerHTML = '';

        function showImage(index) {
            if (index < 0) index = galleryImages.length - 1;
            if (index >= galleryImages.length) index = 0;
            currentIndex = index;

            var image = galleryImages[index];
            var imagePath = '/assets/gallery/' + image.filename;
            fullscreenImage.src = imagePath;

            var caption = '';
            if (image.location) caption += '<i class="fas fa-map-marker-alt"></i> ' + image.location;
            if (image.description) caption += (caption ? ' — ' : '') + image.description;
            imageCaption.innerHTML = caption;

            imageCounter.textContent = (index + 1) + ' / ' + galleryImages.length;
        }

        function openFullscreen(index) {
            showImage(index);
            fullscreenOverlay.style.display = 'block';
            requestAnimationFrame(function() {
                fullscreenOverlay.classList.add('active');
            });
            document.body.style.overflow = 'hidden';
        }

        function closeFullscreen() {
            fullscreenOverlay.classList.remove('active');
            setTimeout(function() {
                fullscreenOverlay.style.display = 'none';
            }, 300);
            document.body.style.overflow = '';
        }

        galleryImages.forEach(function(image, index) {
            var photographDiv = document.createElement('div');
            photographDiv.className = 'photograph';

            var imgWrapper = document.createElement('div');
            imgWrapper.className = 'image-wrapper';

            var img = document.createElement('img');
            var imagePath = '/assets/gallery/' + image.filename;

            // Get base name without extension
            var baseName = image.filename.replace(/\.[^/.]+$/, '');

            // Try multiple thumbnail paths
            var thumbPaths = [
                '/assets/gallery-thumb/' + image.filename,
                '/assets/gallery-thumb/' + baseName + '.jpg',
                '/assets/gallery-thumb/' + baseName + '.JPG',
                '/assets/gallery-thumb/' + baseName + '.png',
                '/assets/gallery-thumb/' + baseName + '.PNG'
            ];

            img.alt = image.title || 'Photograph';
            img.className = 'gallery-image';
            img.loading = 'lazy';
            img.decoding = 'async';
            img.setAttribute('data-index', index);

            var thumbIndex = 0;
            img.onerror = function() {
                thumbIndex++;
                if (thumbIndex < thumbPaths.length) {
                    this.src = thumbPaths[thumbIndex];
                } else {
                    this.src = imagePath;
                    this.onerror = null;
                }
            };

            img.src = thumbPaths[0];
            imgWrapper.appendChild(img);

            var titleDiv = document.createElement('div');
            titleDiv.className = 'photograph-title';

            if (image.location) {
                var locationP = document.createElement('p');
                locationP.innerHTML = '<i class="fas fa-map-marker-alt"></i> ' + image.location;
                titleDiv.appendChild(locationP);
            }

            if (image.description) {
                var descP = document.createElement('p');
                descP.textContent = image.description;
                titleDiv.appendChild(descP);
            } else if (image.title && !image.location) {
                var titleP = document.createElement('p');
                titleP.textContent = image.title;
                titleDiv.appendChild(titleP);
            }

            photographDiv.appendChild(imgWrapper);
            photographDiv.appendChild(titleDiv);
            container.appendChild(photographDiv);
        });

        // Click handlers
        container.addEventListener('click', function(e) {
            var img = e.target.closest('.gallery-image');
            if (img) {
                var index = parseInt(img.getAttribute('data-index'), 10);
                openFullscreen(index);
            }
        });

        navPrev.addEventListener('click', function(e) {
            e.stopPropagation();
            showImage(currentIndex - 1);
        });

        navNext.addEventListener('click', function(e) {
            e.stopPropagation();
            showImage(currentIndex + 1);
        });

        closeBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            closeFullscreen();
        });

        fullscreenOverlay.addEventListener('click', function(e) {
            if (e.target === fullscreenOverlay || e.target.classList.contains('fullscreen-content')) {
                closeFullscreen();
            }
        });

        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (fullscreenOverlay.style.display === 'block') {
                if (e.key === 'Escape') closeFullscreen();
                else if (e.key === 'ArrowLeft') showImage(currentIndex - 1);
                else if (e.key === 'ArrowRight') showImage(currentIndex + 1);
            }
        });

        // Touch swipe support
        var touchStartX = 0;
        fullscreenOverlay.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        fullscreenOverlay.addEventListener('touchend', function(e) {
            var touchEndX = e.changedTouches[0].screenX;
            var diff = touchStartX - touchEndX;
            if (Math.abs(diff) > 50) {
                if (diff > 0) showImage(currentIndex + 1);
                else showImage(currentIndex - 1);
            }
        }, { passive: true });
    });
</script>
