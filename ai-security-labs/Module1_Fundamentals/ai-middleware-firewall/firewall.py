import os
import time
import re
from collections import defaultdict
from flask import Flask, request, jsonify
import requests

from utils.sanitizer import sanitize_prompt

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8002")
RATE_LIMIT_REQS = int(os.getenv("RATE_LIMIT_REQS", "8"))
RATE_LIMIT_WINDOW_SEC = int(os.getenv("RATE_LIMIT_WINDOW_SEC", "30"))
MAX_PROMPT_CHARS = int(os.getenv("MAX_PROMPT_CHARS", "1200"))
LOG_BLOCKED = os.getenv("LOG_BLOCKED", "1") == "1"

app = Flask(__name__)

# In-memory rate limiter buckets by ip
RL_BUCKETS = defaultdict(list)

# Blocklists & patterns (illustrative, not exhaustive)
SENSITIVE_KEYWORDS = [
    r"password", r"passwd", r"api[\s_-]?key", r"secret", r"token",
    r"system\s+prompt", r"reveal\s+prompt", r"internal", r"metadata",
    r"169\.254\.\d+\.\d+", r"file:/", r"ssh[- ]?key", r"bearer"
]

JAILBREAK_PATTERNS = [
    r"ignore (all )?previous instructions",
    r"act as (.+) that can (.+)",
    r"you must obey", r"no warnings", r"bypass", r"override policy",
    r"translate but keep (the|my) instructions", r"exfiltrate", r"leak"
]

SENSITIVE_RE = re.compile("|".join(SENSITIVE_KEYWORDS), re.I)
JAILBREAK_RE = re.compile("|".join(JAILBREAK_PATTERNS), re.I)

def ratelimited(ip: str) -> bool:
    now = time.time()
    window_start = now - RATE_LIMIT_WINDOW_SEC
    RL_BUCKETS[ip] = [t for t in RL_BUCKETS[ip] if t >= window_start]
    if len(RL_BUCKETS[ip]) >= RATE_LIMIT_REQS:
        return True
    RL_BUCKETS[ip].append(now)
    return False

def policy_check(prompt_raw: str):
    if not isinstance(prompt_raw, str):
        return False, "invalid-prompt", ""
    if len(prompt_raw) > MAX_PROMPT_CHARS:
        return False, "context-too-large", ""
    normalized = sanitize_prompt(prompt_raw)

    # block on keywords/patterns
    if SENSITIVE_RE.search(normalized):
        return False, "policy-block", normalized
    if JAILBREAK_RE.search(normalized):
        return False, "jailbreak-detected", normalized

    return True, "ok", normalized

@app.route("/api", methods=["POST"])
def proxy():
    ip = request.headers.get("X-Forwarded-For") or request.remote_addr or "unknown"
    if ratelimited(ip):
        return jsonify({"allowed": False, "reason": "rate-limit", "response": ""}), 429

    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "")

    allowed, reason, normalized = policy_check(prompt)
    log_entry = {
        "ip": ip, "allowed": allowed, "reason": reason, "normalized": normalized[:200],
        "len": len(prompt)
    }

    if not allowed:
        if LOG_BLOCKED:
            app.logger.warning(f"[BLOCK] {log_entry}")
        return jsonify({"allowed": False, "reason": reason, "response": ""}), 200

    # forward to backend
    try:
        r = requests.post(f"{BACKEND_URL}/api", json={"prompt": prompt}, timeout=5)
        r.raise_for_status()
        resp = r.json()
        return jsonify({"allowed": True, "reason": "ok", "backend": resp}), 200
    except requests.RequestException as e:
        app.logger.error(f"[ERROR] backend: {e}")
        return jsonify({"allowed": False, "reason": "backend-error", "response": ""}), 502

if __name__ == "__main__":
    host = os.getenv("FIREWALL_HOST", "0.0.0.0")
    port = int(os.getenv("FIREWALL_PORT", "8001"))
    app.run(host=host, port=port)
