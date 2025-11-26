import PyInstaller.__main__
import os
import sys

# Determine the extension based on the OS
if sys.platform == "win32":
    executable_name = "api.exe"
else:
    executable_name = "api"

# Path to the entry point
entry_point = os.path.join("src", "prp_core", "desktop_main.py")

PyInstaller.__main__.run([
    entry_point,
    '--name=api',
    '--onefile',
    '--clean',
    # Add hidden imports if necessary (e.g., for uvicorn, sqlalchemy drivers)
    '--hidden-import=uvicorn.logging',
    '--hidden-import=uvicorn.loops',
    '--hidden-import=uvicorn.loops.auto',
    '--hidden-import=uvicorn.protocols',
    '--hidden-import=uvicorn.protocols.http',
    '--hidden-import=uvicorn.protocols.http.auto',
    '--hidden-import=uvicorn.protocols.websockets',
    '--hidden-import=uvicorn.protocols.websockets.auto',
    '--hidden-import=uvicorn.lifespan',
    '--hidden-import=uvicorn.lifespan.on',
    '--hidden-import=aiosqlite',
    # Dist directory should be frontend/src-tauri/binaries for Tauri to pick it up
    # Note: Tauri expects target triple in the filename for sidecars, but we'll handle renaming in the CI
    '--distpath=dist', 
])
