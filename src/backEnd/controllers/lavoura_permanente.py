from flask import Blueprint, jsonify, request
from backEnd.infrastructure.database.models import LavouraPermanente 
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from injector import inject
from backEnd.service.login_service import LoginService
from backEnd.controllers.functool.jwt_authentication import jwtAuthentication

lavoura_permanente_bp = Blueprint('lavoura_permanente', __name__)

@lavoura_permanente_bp.route('/authentication', methods=['POST'])
def authenticationd(db: SQLAlchemy):
    service = LoginService(db)
    result = service.authenticate(request.json)

    if(result.get("success") == False):
        return jsonify(result  ), 401
    else :                     
        return jsonify(result ), 200 
