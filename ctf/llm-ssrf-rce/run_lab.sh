#!/bin/bash

echo "[+] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "[+] Installing Python dependencies..."
pip install flask requests

echo "[+] Starting LLM prompt server on port 5000..."
python3 llm_server.py &

echo "[+] Starting cloud backend server on port 8000..."
python3 cloud_server.py &

