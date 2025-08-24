from flask import Flask, jsonify
from netlify_lambda_wsgi import make_handler

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask API!'})

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        'app': 'Unimar Web API',
        'version': '1.0.0',
        'environment': 'production'
    })

# Configuração para o Netlify Functions
handler = make_handler(app)