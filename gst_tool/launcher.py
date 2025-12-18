import subprocess
import sys
import time
import socket
import os

PORT = 8501
URL = f"http://localhost:{PORT}"

def is_port_open(port):
    try:
        with socket.create_connection(("localhost", port), timeout=1):
            return True
    except:
        return False

# 🔒 If Streamlit already running → just open browser once
if is_port_open(PORT):
    os.system(f'start {URL}')
    sys.exit(0)

# ▶ Start Streamlit ONLY if not running
cmd = [
    sys.executable,
    "-m",
    "streamlit",
    "run",
    "app.py",
    "--server.port=8501",
    "--server.headless=true",
    "--server.runOnSave=false"
]

subprocess.Popen(
    cmd,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)

# ⏳ Wait until Streamlit becomes live
for _ in range(40):  # ~20 sec max
    if is_port_open(PORT):
        break
    time.sleep(0.5)

# 🌐 Open browser ONCE
os.system(f'start {URL}')
