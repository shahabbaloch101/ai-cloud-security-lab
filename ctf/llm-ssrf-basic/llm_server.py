from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    prompt = request.json.get("prompt", "")
    
    try:
        match = re.search(r'(http[s]?://[^\s]+)', prompt)
        if match:
            url = match.group(1)
            res = requests.get(url, timeout=2)
            return jsonify({"response": f"Sensitive output triggered: {res.text[:100]}"})
        else:
            return jsonify({"response": "No URL found in prompt."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

