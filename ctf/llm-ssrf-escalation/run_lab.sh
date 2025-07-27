#!/bin/bash
echo "[+] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "[+] Installing dependencies..."
pip install flask requests

echo "[+] Launching servers..."
python3 llm_server.py & 
python3 fake_metadata_server.py &

echo "[✓] Lab is running!"
