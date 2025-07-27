#!/bin/bash

echo "[+] Creating Python virtual environment..."
python3 -m venv venv

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Installing dependencies..."
pip install flask requests

echo "[+] Starting LLM server on port 5000..."
python3 llm_server.py &

echo "[+] Starting fake metadata server on port 8000..."
python3 fake_metadata_server.py &
