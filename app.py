from flask import Flask, jsonify

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

# Esta parte é apenas para desenvolvimento local
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)