from flask import Flask, jsonify
import base64
import os

app = Flask(__name__)

@app.route("/role-assume/v2/internal-token")
def get_escalated_creds():
    flag_path = os.path.join(os.path.dirname(__file__), "FLAG.txt")
    return jsonify({
        "AccessKeyId": "ESCALATEDKEY-ABCD",
        "SecretAccessKey": "ESCALATEDSECRET-1234",
        "SessionToken": "FakeSessionToken==",
        "Flag": base64.b64encode(open(flag_path, "rb").read()).decode()
    })

if __name__ == "__main__":
    app.run(port=8000)
