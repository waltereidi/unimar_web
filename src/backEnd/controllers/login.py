from flask import Blueprint, jsonify, request
from backEnd.infrastructure.database.models import Books 
from backEnd.infrastructure.database import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/authentication', methods=['POST'])
def authentication():
    # exemplo: ler o corpo JSON enviado pelo Vue
    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")
    remember = data.get("remember", False)

    # exemplo fictício: apenas listando livros
    books = db.session.query(Books).all()

    return jsonify({
        "message": "Requisição recebida",
        "email": email,
        "remember": remember,
        "books_count": len(books)
    })

@login_bp.route('/logout', methods=['GET'])
def logout():
    return jsonify({"message": "Logout bem-sucedido"})  