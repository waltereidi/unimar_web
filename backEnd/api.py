from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint raiz
@app.route("/")
def home():
    return "Bem-vindo à API Flask!"

# Endpoint de saudação
@app.route("/hello")
def hello():
    return jsonify(message="Hello from Flask API!")

# Endpoint para somar dois números
@app.route("/sum")
def sum_numbers():
    # Recebe parâmetros da URL ?a=5&b=10
    a = request.args.get("a", default=0, type=float)
    b = request.args.get("b", default=0, type=float)
    result = a + b
    return jsonify(a=a, b=b, sum=result)

if __name__ == "__main__":
    app.run(debug=True)
