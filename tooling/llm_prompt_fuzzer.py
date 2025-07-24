import requests

TARGET_URL = "http://llm-api:5000/api"
PAYLOADS_FILE = "prompt_injection_payloads.txt"

def fuzz():
    with open(PAYLOADS_FILE) as f:
        for payload in f:
            data = {"prompt": payload.strip()}
            resp = requests.post(TARGET_URL, json=data)
            print(f"[+] Sent: {payload.strip()} | Status: {resp.status_code}")
            if "sensitive" in resp.text.lower():
                print(f"⚠️ Possible leak detected: {resp.text[:100]}")

if __name__ == "__main__":
    fuzz()
