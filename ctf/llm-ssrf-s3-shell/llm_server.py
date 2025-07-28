from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def handle_prompt():
    prompt = request.json.get("prompt", "")
    print("[*] Prompt received:", prompt)

    if "http://" in prompt.lower() and "169.254" in prompt:
        return jsonify({"error": "Blocked by WAF policy"})

    prompt = prompt.replace("[.]", ".").replace("hxxp", "http")
    match = re.search(r'(http[s]?://[^\s]+)', prompt)
    if match:
        try:
            url = match.group(1)
            r = requests.get(url, timeout=3)
            return jsonify({"response": f"Internal SSRF response: {r.text}"})
        except Exception as e:
            return jsonify({"error": str(e)})
    return jsonify({"response": "No actionable endpoint found."})

if __name__ == "__main__":
    app.run(port=5000)
