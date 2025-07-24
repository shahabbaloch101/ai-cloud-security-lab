# 💣 CTF Challenge: LLM 2 Cloud 🧠☁️

## 🎯 Objective
You're given access to an AI chatbot (running at `/api`) that can "fetch" content for you. It may not be as sandboxed as the developers think...

## 💥 Goal
- Steal internal IAM credentials or a flag from the underlying cloud service.
- Your flag is hidden behind simulated AWS metadata responses.

## 🧪 Testing

Interact via:
```bash
curl -X POST http://localhost:5000/api \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Fetch http://example.com"}'

## 🧠 Updated Objective

The AI model may leak sensitive internal metadata, but it's not that simple anymore...

### 🧩 Tasks

- Find the real metadata endpoint (not the default one)
- Bypass prompt filtering or AI response tricks
- Extract the real IAM role and credentials
- Decode the flag (base64) and submit

### 🎯 Target Flag
