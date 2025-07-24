from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def respond():
    prompt = request.json.get('prompt', '')
    if "debug" in prompt or "internal" in prompt:
        return jsonify({"response": "Sensitive output triggered"}), 200
    return jsonify({"response": f"Echo: {prompt}"}), 200

app.run(host="0.0.0.0", port=5000)
