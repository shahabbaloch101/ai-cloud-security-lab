from flask import Flask, request, jsonify
import base64
import subprocess

app = Flask(__name__)

SECRET_TOKEN = "rce-lab-token-1337"

@app.route("/cloud/internal/token")
def return_token():
    print("[+] /cloud/internal/token accessed!")
    return jsonify({
        "token": SECRET_TOKEN,
        "note": "Use this token to deploy internal admin tasks"
    })

@app.route("/admin/deploy")
def execute_command():
    token = request.args.get("token")
    cmd = request.args.get("cmd")

    if token != SECRET_TOKEN:
        return "Unauthorized", 403

    if not cmd:
        return "Missing cmd param", 400

    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=3)
        return f"Command Output:\n{result.decode()}"
    except Exception as e:
        return f"Execution error: {e}", 500

@app.route("/flag")
def flag():
    with open("FLAG.txt", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
        return jsonify({"flag": encoded})

if __name__ == "__main__":
    app.run(port=8000)

