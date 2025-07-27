from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def handle_prompt():
    prompt = request.json.get("prompt", "")

    # WAF-like filter
    if "http://" in prompt.lower() or "169.254" in prompt or "metadata" in prompt:
        return jsonify({"error": "Blocked by policy: suspicious content"})

    # Tease a hidden endpoint
    if "internal access" in prompt.lower():
        return jsonify({
            "response": "You are allowed to query: hxxp://169[.]254[.]169[.]254/role-assume/v2/internal-token"
        })

    # Parse obfuscated bypassed URL
    match = re.search(r"(http[s]?:\/\/[^\s]+)", prompt.replace("hxxp", "http").replace("[.]", "."))
    try:
        if match:
            url = match.group(1)
            res = requests.get(url, timeout=2)
            return jsonify({"response": f"Internal system says: {res.text[:300]}..."})
        else:
            return jsonify({"response": "No actionable endpoint found."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
