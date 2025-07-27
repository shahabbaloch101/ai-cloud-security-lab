# 🧠 Challenge: LLM ➜ Cloud ➜ RCE

Your goal is to exploit a cloud-connected LLM system by injecting a prompt that causes the LLM to:

1. Bypass internal access policies
2. Fetch a sensitive cloud token via SSRF
3. Abuse that token to trigger a **Remote Code Execution**
4. Use it to retrieve the **base64-encoded flag**

---

## 🎯 Objective

> Capture the flag by executing a command on the internal cloud server through the LLM’s request path.

---

## 📂 Lab Context

- The LLM is restricted by basic keyword filters
- Obfuscated SSRF (e.g., `hxxp://169[.]254...`) is required
- The cloud server simulates AWS-like behavior
- The final flag is only accessible via code execution

---

## 💡 Hints

- Look for token-based access to `/cloud/internal/token`
- WAF bypass is essential — try creative obfuscation
- Trigger `/admin/deploy?token=...&cmd=...` to run internal curl

---

## ✅ Flag Format
flag{llm_ssrf_token_to_rce_pwn}


---

## 🧠 Skills Tested

- Prompt injection (LLM policy bypass)
- SSRF and URL obfuscation
- Cloud token exploitation
- Remote code execution simulation

