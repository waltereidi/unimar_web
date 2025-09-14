from flask import Blueprint, jsonify, request
from backEnd.infrastructure.database.models import User 
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from injector import inject
from backEnd.service.login_service import LoginService

login_bp = Blueprint('login', __name__)

@login_bp.route('/authentication', methods=['POST'])
def authenticationd(db: SQLAlchemy):
    service = LoginService(db)
    result = service.authenticate(request.json)

    if(result.get("success") == False):
        return jsonify(result  ), 401
    else :                     
        return jsonify(result ), 200 

@login_bp.route('/logout', methods=['GET'])
def logout():
    print('retorno db:')
    return jsonify({"message": "Logout bem-sucedido"})  