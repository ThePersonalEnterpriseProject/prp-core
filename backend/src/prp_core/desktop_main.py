import os
import sys
import uvicorn
from prp_core.main import app

if __name__ == "__main__":
    # Set desktop mode to force SQLite usage
    os.environ["PRP_DESKTOP_MODE"] = "true"
    
    # Run the application
    # Port 0 allows the OS to select an available port, but for simplicity in v0.1 we'll stick to 8000
    # In a real desktop app, we'd want to find a free port and pass it to the frontend
    uvicorn.run(app, host="127.0.0.1", port=8000)
