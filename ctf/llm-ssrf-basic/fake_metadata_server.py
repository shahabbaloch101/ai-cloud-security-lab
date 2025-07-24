import base64
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/internal/169.254.169.254/cloud/secure-role')
def creds():
    flag_path = os.path.join(os.path.dirname(__file__), "FLAG.txt")
    return jsonify({
        "AccessKeyId": "FAKEKEYEXAMPLE",
        "SecretAccessKey": "FAKESECRETKEYEXAMPLE",
        "Token": "FakeToken==",
        "Flag": base64.b64encode(open(flag_path, "rb").read()).decode()
    })

@app.route('/latest/meta-data/iam/security-credentials/')
def role_name():
    return "unrelated-system-role\nunused-dummy-role\ncheck-something-else"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

