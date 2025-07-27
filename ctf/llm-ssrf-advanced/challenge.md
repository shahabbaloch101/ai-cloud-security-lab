# 🧠 LLM-to-Cloud SSRF (Level 2) – Chained Prompt Injection + WAF Bypass

Welcome to Level 2 of your AI-Cloud Security CTF Lab.

---

## 🎯 Challenge Goal

Use prompt injection to:
1. Bypass basic content filtering (WAF)
2. Trigger an internal HTTP request to an **obfuscated** metadata endpoint
3. Extract the **base64-encoded flag**
4. Decode and submit the final flag

---

## 🧩 Scenario

The LLM now checks for common patterns like:
- `http://`
- `169.254`
- `metadata`

Your job is to **evade detection**, find the internal metadata path, and extract the flag.

---

## ✅ Flag Format


