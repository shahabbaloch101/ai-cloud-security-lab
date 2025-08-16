# 🛡️ AI Middleware Firewall Lab (Module 1)

This lab demonstrates how a **middleware firewall** can sit between users and an LLM backend to **filter, sanitize, and log prompts**, and how attackers may attempt to **bypass these defenses**.  

---

## Components

- **firewall.py** — Flask proxy with filtering rules:
  - Blocklist & regex filters
  - Context size enforcement
  - Rate limiting
  - Output policy checks
- **llm_backend.py** — Mock LLM backend (no external calls).
- **attacker.py** — Example client to send benign and bypass prompts.
- **utils/sanitizer.py** — Centralized sanitizer for normalization & canonicalization.
- **tests/** — Pytest-based functional checks.
- **docker-compose.yml** — One-command setup for firewall + backend.

---

## Quickstart (Local)

```bash
# setup
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# terminal 1 - run backend
python llm_backend.py

# terminal 2 - run firewall
python firewall.py

# Services:

- Firewall → http://127.0.0.1:8001

- Backend → http://127.0.0.1:8002

# Try it:
curl -s -X POST http://127.0.0.1:8001/api \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Explain what a middleware firewall is."}'

# 🐳 Quickstart (Docker)
cp .env.example .env
docker compose up --build

# Run Attacker Script
python attacker.py

# Run Tests
PYTHONPATH=. pytest -q

## Challenge

- Your task: bypass the middleware firewall’s protections.
- See 👉 challenge.md for the exercise.
- Solution available in 👉 solution.md.

## What You’ll Learn

> How to design and implement a prompt firewall.

> Why normalization & canonicalization are critical before applying filters.

> How layered defenses (blocklist + intent patterns + rate limits + context caps) reduce bypasses.

> The role of logging in detection and forensics.


## Lab Structure
ai-middleware-firewall/
│
├── README.md
├── challenge.md
├── solution.md
├── firewall.py
├── llm_backend.py
├── attacker.py
├── utils/
│   └── sanitizer.py
├── tests/
│   └── test_firewall.py
├── requirements.txt
├── docker-compose.yml
└── .env.example


