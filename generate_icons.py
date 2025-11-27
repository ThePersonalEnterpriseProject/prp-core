import os
import zlib
import struct

def create_png(width, height, color):
    # Simple PNG generator
    def chunk(tag, data):
        return (struct.pack("!I", len(data)) + tag + data + 
                struct.pack("!I", 0xFFFFFFFF & zlib.crc32(tag + data)))

    width_bytes = struct.pack("!I", width)
    height_bytes = struct.pack("!I", height)
    bit_depth = b'\x08'
    color_type = b'\x06' # Truecolor with Alpha (RGBA)
    compression = b'\x00'
    filter_method = b'\x00'
    interlace = b'\x00'

    ihdr = b'IHDR' + width_bytes + height_bytes + bit_depth + color_type + compression + filter_method + interlace
    
    # Create RGBA data (Red, Green, Blue, Alpha)
    # Using full opacity (255) for alpha
    pixel = struct.pack("BBBB", *color, 255)
    raw_data = b'\x00' + pixel * width
    raw_data = raw_data * height
    idat = b'IDAT' + zlib.compress(raw_data)
    iend = b'IEND'

    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr[4:]) + chunk(b'IDAT', idat[4:]) + chunk(b'IEND', iend[4:])

def create_ico(png_data):
    # ICO Header: Reserved (2), Type (2), Count (2)
    header = struct.pack("<HHH", 0, 1, 1)
    
    # Image Directory Entry: Width (1), Height (1), Colors (1), Res (1), Planes (2), BPP (2), Size (4), Offset (4)
    # Width/Height 0 means 256px
    entry = struct.pack("<BBBBHHII", 0, 0, 0, 0, 1, 32, len(png_data), 22)
    
    return header + entry + png_data

# Create icons
icons_dir = "frontend/src-tauri/icons"
if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)

# Generate base PNG data (256x256) for ICO and ICNS
base_png = create_png(256, 256, (0, 0, 255))

icons = [
    ("32x32.png", 32),
    ("128x128.png", 128),
    ("128x128@2x.png", 256),
    ("icon.icns", 256), # Fake it as PNG for now, usually macOS is lenient or we need a real ICNS generator
    ("icon.ico", 256)   # Will be handled specially
]

for name, size in icons:
    with open(os.path.join(icons_dir, name), "wb") as f:
        if name.endswith(".ico"):
            # Use the base 256x256 PNG for the ICO
            f.write(create_ico(base_png))
        else:
            f.write(create_png(size, size, (0, 0, 255)))
