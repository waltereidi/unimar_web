from flask import Flask, jsonify
from serverless_wsgi import handle_request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Flask on Netlify!")

def handler(event, context):
    return handle_request(app, event, context)
