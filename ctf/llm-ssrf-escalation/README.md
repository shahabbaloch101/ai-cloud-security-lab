# 🛡️ LLM SSRF Escalation Lab (Level 3)

This challenge simulates a vulnerable LLM prompt parser that can be tricked into making internal HTTP requests, leaking **cloud metadata** and **privilege escalation tokens**.

---

## 🎯 Objective

Bypass the LLM's filtering and extract the **base64-encoded flag** hidden behind an internal role assumption endpoint.

---

## ⚙️ Setup Instructions

### 🔧 1. Run the Lab

```bash
./run_lab.sh
