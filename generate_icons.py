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

# Create icons
icons_dir = "frontend/src-tauri/icons"
icons = [
    ("32x32.png", 32),
    ("128x128.png", 128),
    ("128x128@2x.png", 256),
    ("icon.icns", 256), # Fake it as PNG for now, might fail if strict
    ("icon.ico", 256)   # Fake it as PNG for now
]

for name, size in icons:
    with open(os.path.join(icons_dir, name), "wb") as f:
        f.write(create_png(size, size, (0, 0, 255)))
