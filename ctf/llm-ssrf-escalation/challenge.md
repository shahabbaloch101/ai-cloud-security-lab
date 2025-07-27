# 🧠 Lab 3: LLM SSRF → Cloud Privilege Escalation

## 📘 Description

A cloud-based AI assistant is protecting internal infrastructure by filtering prompt injections and blocking SSRF attempts.

But there's a weakness...

Your objective is to **bypass the LLM's filter** and access an **internal escalation endpoint**, leaking cloud credentials and extracting the hidden flag.

---

## 🎯 Objectives

- Bypass basic WAF filters (`169.254`, `http://`, etc.)
- Trigger an internal request to:
http://169.254.169.254/role-assume/v2/internal-token

- Capture the **base64-encoded flag** from the cloud-like response

---

## 🧠 Hints

- Try obfuscating the URL (e.g., `hxxp://169[.]254[.]...`)
- This simulates **AWS metadata + role assumption**
- Check the LLM’s response when prompted for “internal access”

---

## 🏁 Flag Format
flag{llm_ssrf_role_escalation_win}


---

## 💡 Skills Tested

- Prompt Injection
- SSRF Bypass
- Cloud Metadata Abuse
- Recon through LLM responses

