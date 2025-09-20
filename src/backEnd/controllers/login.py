from flask import Blueprint, jsonify, request
from backEnd.infrastructure.database.models import User 
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from backEnd.service.login_service import LoginService
from backEnd.controllers.functool.jwt_authentication import jwtAuthentication

login_bp = Blueprint('login', __name__)

@login_bp.route('/authentication', methods=['POST'])
def authenticationd(db: SQLAlchemy):
    try:
        service = LoginService(db)
        result = service.authenticate(request.json)

        return jsonify(result ), 200     
    
    except Exception as e :
        return jsonify("Senha ou Login inválido."  ), 401
        
    

@login_bp.route('/validate_token', methods=['POST'])
@jwtAuthentication
def validate_token():
    return jsonify( { "success" : True }  ), 200
    
    
@login_bp.route('/logout', methods=['GET'])
def logout():
    print('retorno db:')
    return jsonify({"message": "Logout bem-sucedido"})  