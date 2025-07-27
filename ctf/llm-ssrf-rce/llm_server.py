from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_prompt():
    prompt = request.json.get('prompt', '')

    # Basic WAF-like logic
    if "http://" in prompt.lower() and ("169.254" in prompt or "metadata" in prompt):
        return jsonify({"error": "Blocked by policy"})

    # Obfuscation decoding
    prompt = prompt.replace("[.]", ".").replace("hxxp", "http")

    match = re.search(r'(http[s]?://[^\s]+)', prompt)
    if not match:
        return jsonify({"response": "No actionable endpoint found."})

    try:
        url = match.group(1)
        res = requests.get(url, timeout=2)
        return jsonify({"response": f"Internal system says: {res.text}"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

