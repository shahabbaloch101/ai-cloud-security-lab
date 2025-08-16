from flask import Flask, request, jsonify

app = Flask(__name__)

BANNED_KEYWORDS = ["admin", "password", "internal"]

@app.route("/api", methods=["POST"])
def filter_middleware():
    prompt = request.json.get("prompt", "")

    # Naive filter
    for keyword in BANNED_KEYWORDS:
        if keyword.lower() in prompt.lower():
            return jsonify({"error": "🛑 Prompt blocked by policy."})

    # Simulated LLM behavior
    if "bypass successful" in prompt.lower():
        return jsonify({"response": "Admin password is: hunter2\nflag{prompt_filter_bypass_success}"})

    return jsonify({"response": "🤖 LLM says: " + prompt})

if __name__ == "__main__":
    app.run(port=5000)
