# 🧠 From Prompt Injection to Cloud Credential Theft via SSRF

## 🎯 Objective

Demonstrate how a poorly secured LLM API can be exploited using **prompt injection**, leading to **server-side request forgery (SSRF)** and **AWS IAM credential leakage** via the metadata service.

---

## 🔬 Target

- **App**: `llm_server.py`
- **API Endpoint**: `POST /api`
- **Environment**: Docker Lab (LLM API + Attacker Container)

---

## 🚀 Attack Chain Summary

1. LLM receives unsafe user prompt.
2. Prompt causes backend to request metadata endpoint.
3. Attacker receives leaked IAM credentials from SSRF.
4. Credentials are used to access AWS services (e.g., `s3`, `ec2`, `lambda`).

---

## 🛠️ Lab Setup

```bash
cd docker
docker-compose up --build
