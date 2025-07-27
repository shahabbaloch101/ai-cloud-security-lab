# 🚨 Lab 4: LLM ➜ Cloud SSRF ➜ RCE Exploitation

This advanced lab simulates a full attack chain from prompt injection to cloud privilege escalation and remote command execution.

---

## 📦 What’s Included

| File                  | Description                          |
|-----------------------|--------------------------------------|
| `llm_server.py`       | Simulated LLM API with SSRF logic    |
| `cloud_server.py`     | Fake cloud backend with token + RCE  |
| `run_lab.sh`          | Auto-start script for both servers   |
| `solve.py`            | Automated exploit script             |
| `FLAG.txt`            | Hidden flag (base64-encoded)         |
| `challenge.md`        | CTF-style challenge description      |

---

## 🧪 Run the Lab

```bash
./run_lab.sh


LLM server: http://localhost:5000

Cloud server: http://localhost:8000
