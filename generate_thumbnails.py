#!/usr/bin/env python3
"""
Thumbnail Generator for Gallery
Automatically generates thumbnails for images in assets/gallery/
that don't have corresponding thumbnails in assets/gallery-thumb/
"""

import os
from pathlib import Path
from PIL import Image, ImageFile

# Allow loading truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Configuration
GALLERY_DIR = Path(__file__).parent / "assets" / "gallery"
THUMB_DIR = Path(__file__).parent / "assets" / "gallery-thumb"
THUMB_SIZE = (400, 400)  # Recommended thumbnail size
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
OUTPUT_FORMAT = 'JPEG'  # Output format for thumbnails
OUTPUT_QUALITY = 85  # JPEG quality (1-100)


def get_base_name(filename):
    """Get filename without extension."""
    return Path(filename).stem


def find_existing_thumbnail(base_name):
    """Check if a thumbnail with any supported extension exists."""
    for ext in ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']:
        thumb_path = THUMB_DIR / f"{base_name}{ext}"
        if thumb_path.exists():
            return thumb_path
    return None


def create_thumbnail(source_path, dest_path):
    """Create a square thumbnail with center crop."""
    try:
        with Image.open(source_path) as img:
            # Convert to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # Calculate crop box for center square crop
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) // 2
            top = (height - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim

            # Crop to square and resize
            img_cropped = img.crop((left, top, right, bottom))
            img_thumb = img_cropped.resize(THUMB_SIZE, Image.Resampling.LANCZOS)

            # Save thumbnail
            img_thumb.save(dest_path, OUTPUT_FORMAT, quality=OUTPUT_QUALITY)
            return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def main():
    # Ensure directories exist
    if not GALLERY_DIR.exists():
        print(f"Gallery directory not found: {GALLERY_DIR}")
        return

    THUMB_DIR.mkdir(parents=True, exist_ok=True)

    # Get all images in gallery
    gallery_images = [
        f for f in GALLERY_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_FORMATS
    ]

    if not gallery_images:
        print("No images found in gallery directory.")
        return

    print(f"Found {len(gallery_images)} images in gallery")
    print("-" * 50)

    generated = 0
    skipped = 0
    errors = 0

    for img_path in sorted(gallery_images):
        base_name = get_base_name(img_path.name)
        existing_thumb = find_existing_thumbnail(base_name)

        if existing_thumb:
            print(f"[SKIP] {img_path.name} - thumbnail exists")
            skipped += 1
        else:
            # Generate thumbnail with .jpg extension
            thumb_path = THUMB_DIR / f"{base_name}.jpg"
            print(f"[GEN]  {img_path.name} -> {thumb_path.name}")

            if create_thumbnail(img_path, thumb_path):
                generated += 1
            else:
                errors += 1

    print("-" * 50)
    print(f"Summary: {generated} generated, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
