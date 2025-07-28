from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/cloud/upload-data')
def upload_data():
    data = {
        "data": "FAKE-SSRF-TOKEN-KEY",
        "flag": open("FLAG.txt").read().strip()
    }
    try:
        requests.post("http://127.0.0.1:9002/callback", json=data, timeout=2)
        return "Uploaded to external storage."
    except Exception as e:
        return f"Upload failed: {str(e)}"

if __name__ == "__main__":
    app.run(port=8000)

