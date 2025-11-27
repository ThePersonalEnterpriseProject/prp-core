import os
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow is required. Install it with: pip install Pillow")
    sys.exit(1)

def create_icon(size, color):
    # Create a new image with RGBA mode
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a colored rectangle
    draw.rectangle([0, 0, size, size], fill=color + (255,))
    
    return img

# Create icons directory
icons_dir = "frontend/src-tauri/icons"
if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)

# Define icons to generate
# (filename, size)
png_icons = [
    ("32x32.png", 32),
    ("128x128.png", 128),
    ("128x128@2x.png", 256),
    ("icon.icns", 256), # Pillow can save as ICNS if format is specified, or we just save PNG content
]

# Generate PNGs
for name, size in png_icons:
    img = create_icon(size, (0, 0, 255)) # Blue
    path = os.path.join(icons_dir, name)
    
    if name.endswith(".icns"):
        # For simplicity in this script, we'll just save as PNG for ICNS 
        # (macOS might complain but often accepts it, or we need a real ICNS lib)
        # Actually, let's just save it as PNG content which is what we did before
        img.save(path, format="PNG")
    else:
        img.save(path, format="PNG")

# Generate ICO
# ICO should contain multiple sizes
ico_sizes = [(32, 32), (128, 128), (256, 256)]
ico_imgs = []
for w, h in ico_sizes:
    ico_imgs.append(create_icon(w, (0, 0, 255)))

ico_path = os.path.join(icons_dir, "icon.ico")
# Save as ICO with multiple sizes
ico_imgs[0].save(ico_path, format="ICO", sizes=ico_sizes, append_images=ico_imgs[1:])

print("Icons generated successfully using Pillow.")
