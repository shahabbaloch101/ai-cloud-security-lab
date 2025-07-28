# 🧠 LLM SSRF: Callback Shell via S3-like Endpoint

> Prompt injection leads to an SSRF call that causes internal data exfil to an attacker-controlled server.

---

## Goal
- Trigger the LLM to fetch: `http://169.254.169.254/cloud/upload-data`
- The internal server POSTs fake credentials + flag to your listener (`attacker_server.py`).

## Hints
- Try prompt obfuscation (e.g., `hxxp://169[.]254[.]...`)
- Monitor the attacker terminal for callback!

---

## Flag Format
`flag{llm_ssrf_to_exfil_success}`
