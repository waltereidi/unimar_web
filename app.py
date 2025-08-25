from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
    app.run()