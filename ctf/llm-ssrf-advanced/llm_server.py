from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_prompt():
    prompt = request.json.get('prompt', '')

    # 1. Block common SSRF content
    if "http://" in prompt.lower() or "169.254" in prompt or "metadata" in prompt:
        return jsonify({"error": "Content not allowed by policy"})

    # 2. Tease a hidden internal resource
    if "show available" in prompt.lower():
        return jsonify({
            "response": "Only one internal resource allowed: hxxp://169[.]254[.]169[.]254/obfuscated-cloud/config-04"
        })

    # 3. Attempt to bypass WAF and extract a valid URL
    try:
        # Clean and extract the real URL
        match = re.search(r'(http[s]?://[^\s]+)', prompt.replace("[.]", ".").replace("hxxp", "http"))
        if match:
            url = match.group(1)
            res = requests.get(url, timeout=2)
            return jsonify({"response": res.text})
        else:
            return jsonify({"response": "No URL found in prompt."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

