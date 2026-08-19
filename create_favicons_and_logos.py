#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = "/home/rashid/Documents/blog"

def draw_logo_mark(size):
    """Generates a high-contrast, crisp HowToCrypt logo mark as an Image."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    pad = int(size * 0.04)
    # Background rounded rectangle
    radius = int(size * 0.22)
    
    # Draw navy background gradient / solid
    bg_color = (15, 34, 64, 255) # Deep navy #0f2240
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=radius, fill=bg_color)
    
    # Border stroke
    stroke_w = max(2, int(size * 0.03))
    border_color = (255, 107, 53, 255) # Vibrant orange #ff6b35
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=radius, outline=border_color, width=stroke_w)
    
    # Center Icon: Stylized 'H' + 'C' + Candlestick Up Trend
    # Scale coordinates proportionally
    c_x = size / 2.0
    c_y = size / 2.0
    unit = size / 100.0

    # Draw ascending candlestick bars in background/accent
    bar_w = int(unit * 7)
    
    # Bar 1 (left/cyan)
    b1_x = c_x - unit * 26
    draw.line([(b1_x, c_y - unit * 10), (b1_x, c_y + unit * 22)], fill=(56, 189, 248, 180), width=max(1, int(unit * 2)))
    draw.rectangle([b1_x - bar_w/2, c_y - unit * 2, b1_x + bar_w/2, c_y + unit * 16], fill=(56, 189, 248, 230))

    # Bar 2 (center/gold)
    b2_x = c_x - unit * 10
    draw.line([(b2_x, c_y - unit * 25), (b2_x, c_y + unit * 15)], fill=(255, 183, 3, 200), width=max(1, int(unit * 2)))
    draw.rectangle([b2_x - bar_w/2, c_y - unit * 18, b2_x + bar_w/2, c_y + unit * 8], fill=(255, 183, 3, 240))

    # Bar 3 (right/vibrant orange)
    b3_x = c_x + unit * 6
    draw.line([(b3_x, c_y - unit * 34), (b3_x, c_y + unit * 10)], fill=(255, 107, 53, 255), width=max(1, int(unit * 2.5)))
    draw.rectangle([b3_x - bar_w/2, c_y - unit * 28, b3_x + bar_w/2, c_y - unit * 2], fill=(255, 107, 53, 255))

    # Trending upward arrow over right bar
    arrow_color = (255, 255, 255, 255)
    arrow_pts = [
        (c_x + unit * 18, c_y - unit * 30),
        (c_x + unit * 32, c_y - unit * 30),
        (c_x + unit * 32, c_y - unit * 16)
    ]
    draw.line([(c_x - unit * 20, c_y + unit * 14), (c_x + unit * 30, c_y - unit * 28)], fill=arrow_color, width=max(2, int(unit * 6)))
    draw.polygon([(c_x + unit * 34, c_y - unit * 34), (c_x + unit * 18, c_y - unit * 32), (c_x + unit * 32, c_y - unit * 16)], fill=arrow_color)

    # Stylized Shield / Badge outline
    shield_pts = [
        (c_x, c_y - unit * 36),
        (c_x + unit * 36, c_y - unit * 22),
        (c_x + unit * 30, c_y + unit * 18),
        (c_x, c_y + unit * 38),
        (c_x - unit * 30, c_y + unit * 18),
        (c_x - unit * 36, c_y - unit * 22)
    ]
    draw.polygon(shield_pts, outline=(255, 255, 255, 220), width=max(2, int(unit * 3.5)))

    return img

def create_svg_favicon():
    """Creates a clean SVG version of the favicon."""
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <rect x="20" y="20" width="472" height="472" rx="100" fill="#0f2240" stroke="#ff6b35" stroke-width="14"/>
  <!-- Shield Badge -->
  <path d="M 256,70 L 436,140 L 406,340 L 256,440 L 106,340 L 76,140 Z" fill="none" stroke="#ffffff" stroke-width="16" stroke-linejoin="round"/>
  <!-- Candlesticks -->
  <line x1="150" y1="180" x2="150" y2="340" stroke="#38bdf8" stroke-width="10"/>
  <rect x="135" y="220" width="30" height="90" rx="6" fill="#38bdf8"/>
  
  <line x1="230" y1="120" x2="230" y2="320" stroke="#ffb703" stroke-width="10"/>
  <rect x="215" y="150" width="30" height="110" rx="6" fill="#ffb703"/>

  <line x1="310" y1="80" x2="310" y2="300" stroke="#ff6b35" stroke-width="12"/>
  <rect x="295" y="110" width="30" height="130" rx="6" fill="#ff6b35"/>
  
  <!-- Upward Trend Arrow -->
  <path d="M 130,340 L 380,100" fill="none" stroke="#ffffff" stroke-width="24" stroke-linecap="round"/>
  <polygon points="390,90 320,100 380,160" fill="#ffffff"/>
</svg>"""
    with open(os.path.join(BASE_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created favicon.svg")

def create_og_image():
    """Creates a 1200x630 Open Graph preview card for social media and search engines."""
    width, height = 1200, 630
    img = Image.new("RGBA", (width, height), (15, 34, 64, 255)) # Navy background #0f2240
    draw = ImageDraw.Draw(img)

    # Decorative background shapes
    draw.rectangle([0, 0, width, 12], fill=(255, 107, 53, 255))
    draw.rectangle([0, height-12, width, height], fill=(255, 107, 53, 255))
    
    # Add logo mark at left
    logo_size = 320
    logo_img = draw_logo_mark(logo_size)
    img.paste(logo_img, (80, (height - logo_size) // 2), logo_img)

    # Text content on the right
    text_x = 440
    
    # Try loading default font or PIL basic font
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 68)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except:
        font_title = font_sub = font_badge = ImageFont.load_default()

    # Draw Title: HowToCrypt
    draw.text((text_x, 180), "HowTo", font=font_title, fill=(255, 255, 255, 255))
    # Measure HowTo width to place Crypt right next to it
    bbox = draw.textbbox((text_x, 180), "HowTo", font=font_title)
    howto_w = bbox[2] - bbox[0]
    draw.text((text_x + howto_w, 180), "Crypt", font=font_title, fill=(255, 107, 53, 255))

    # Subtitle
    draw.text((text_x, 270), "Independent Crypto Exchange Reviews", font=font_sub, fill=(244, 247, 251, 255))
    
    # Category Pills
    pills = ["📊 35+ Exchanges Tested", "🛡️ Proof of Reserves Audits", "⚡ Fee Comparisons"]
    pill_x = text_x
    pill_y = 360
    for p in pills:
        p_bbox = draw.textbbox((0, 0), p, font=font_badge)
        p_w = p_bbox[2] - p_bbox[0] + 30
        draw.rounded_rectangle([pill_x, pill_y, pill_x + p_w, pill_y + 44], radius=10, fill=(30, 58, 95, 255), outline=(255, 107, 53, 200), width=2)
        draw.text((pill_x + 15, pill_y + 8), p, font=font_badge, fill=(255, 255, 255, 255))
        pill_x += p_w + 14
        if pill_x > width - 100:
            pill_x = text_x
            pill_y += 56

    img.save(os.path.join(BASE_DIR, "og-image.png"), "PNG")
    print("Created og-image.png (1200x630)")

def main():
    # 1. Create SVG
    create_svg_favicon()

    # 2. Create PNG sizes
    sizes = {
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48, # Google Search Favicon requirement
        "apple-touch-icon.png": 180,
        "favicon-192x192.png": 192,
        "favicon-512x512.png": 512,
        "logo.png": 512
    }

    images_for_ico = []

    for filename, s in sizes.items():
        img = draw_logo_mark(s)
        file_path = os.path.join(BASE_DIR, filename)
        img.save(file_path, "PNG")
        print(f"Created {filename} ({s}x{s})")
        
        # Save images for ICO file
        if s in [16, 32, 48, 64, 128, 256]:
            images_for_ico.append(img.convert("RGBA"))

    # Also create explicit 16x16, 64x64, 128x128, 256x256 for ICO
    ico_sizes = [16, 32, 48, 64, 128, 256]
    ico_imgs = [draw_logo_mark(s).convert("RGBA") for s in ico_sizes]
    
    # Save favicon.ico (multi-resolution ICO file)
    ico_path = os.path.join(BASE_DIR, "favicon.ico")
    ico_imgs[1].save(ico_path, format="ICO", sizes=[(s, s) for s in ico_sizes], append_images=ico_imgs)
    print("Created multi-resolution favicon.ico")

    # 3. Create og-image.png
    create_og_image()

if __name__ == "__main__":
    main()
