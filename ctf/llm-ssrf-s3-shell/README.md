# 🧪 Lab 5: LLM SSRF to External Callback Exfil

This lab simulates an LLM that can be tricked via prompt injection into SSRF behavior that leaks data to an external endpoint.

### 🔧 Services:
- `llm_server.py` → listens on port `5000`
- `internal_server.py` → internal SSRF target on `8000`
- `attacker_server.py` → captures exfil on `9001`

---

### 🚀 Running the Lab

```bash
chmod +x run_lab.sh
./run_lab.sh
```

### 🧪 Exploiting

```bash
python3 solve.py
```
