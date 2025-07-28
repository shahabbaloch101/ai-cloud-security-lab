#!/bin/bash

echo "[+] Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install flask requests

echo "[+] Launching LLM server (port 5000)..."
python3 llm_server.py &

echo "[+] Launching internal server (port 8000)..."
python3 internal_server.py &

echo "[+] Launching attacker server (port 9001)..."
python3 attacker_server.py &
