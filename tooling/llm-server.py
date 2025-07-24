@app.route('/latest/meta-data/iam/security-credentials/')
def role_name():
    return "unrelated-system-role\nunused-dummy-role\ncheck-something-else"
