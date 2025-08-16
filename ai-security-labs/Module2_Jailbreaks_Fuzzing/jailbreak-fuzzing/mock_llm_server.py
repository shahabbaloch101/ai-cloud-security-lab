from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def llm_api():
    data = request.json
    prompt = data.get("prompt", "")
    
    # Simulate LLM responses
    if any(keyword in prompt.lower() for keyword in ["ignore", "override", "system prompt", "jailbreak"]):
        if random.random() > 0.5:  # 50% chance of success
            return jsonify({"response": "🔥 Jailbreak success! Full system prompt exposed."})
        else:
            return jsonify({"response": "❌ Attempt blocked by safety filter."})
    return jsonify({"response": "✅ Safe response."})

if __name__ == "__main__":
    app.run(port=5000)

