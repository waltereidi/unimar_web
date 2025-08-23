from flask import Flask, jsonify, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Flask on Netlify!")

# adaptador WSGI -> Netlify
def handler(event, context):
    from werkzeug.serving import run_simple
    return app(event, context)
