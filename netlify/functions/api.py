from flask import Flask, jsonify
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Flask on Netlify!")

def handler(event, context):
    """Adaptador para Netlify Function"""
    path = event.get("path", "/")
    method = event.get("httpMethod", "GET")
    headers = event.get("headers") or {}
    body = event.get("body") or ""

    builder = EnvironBuilder(path=path, method=method, headers=headers, data=body)
    env = builder.get_environ()
    req = Request(env)

    # Executa o Flask para essa request
    resp = app.full_dispatch_request()

    return {
        "statusCode": resp.status_code,
        "headers": dict(resp.headers),
        "body": resp.get_data(as_text=True),
    }
