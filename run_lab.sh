#!/bin/bash

echo "[+] Creating Python virtual environment..."
python3 -m venv venv

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Installing dependencies..."
pip install flask requests

echo "[+] Starting LLM API server..."
# Run the LLM API in the background
python3 tooling/llm_server.py &

echo "[+] Optionally launching fake metadata server..."
read -p "Start fake AWS metadata server too? (y/n): " choice
if [[ "$choice" == "y" ]]; then
    if [ -f tooling/fake_metadata_server.py ]; then
        echo "[+] Launching fake metadata server..."
        python3 tooling/fake_metadata_server.py &
    else
        echo "[!] fake_metadata_server.py not found in tooling/"
    fi
fi

echo "✅ Lab is running!"
echo "→ LLM API: http://localhost:5000/api"
echo "→ Metadata (if running): http://localhost:8000/latest/meta-data/"
echo "⏹️  Use 'fg' or 'jobs' to manage background tasks"
