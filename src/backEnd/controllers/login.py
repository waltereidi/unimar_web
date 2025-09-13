from flask import Blueprint, jsonify, request
from backEnd.infrastructure.database.models import User 
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from injector import inject


login_bp = Blueprint('login', __name__)

@login_bp.route('/authentication', methods=['POST'])
def authenticationd(db: SQLAlchemy):

    # exemplo fictício: apenas listando livros
    books = db.session.query(User).all()
    print('retorno db:', books)
    
    # exemplo: ler o corpo JSON enviado pelo Vue
    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")
    remember = data.get("remember", False)


    return jsonify(books)

@login_bp.route('/logout', methods=['GET'])
def logout():
    print('retorno db:')
    return jsonify({"message": "Logout bem-sucedido"})  