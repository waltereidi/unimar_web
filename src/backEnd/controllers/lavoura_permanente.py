from flask import Blueprint, jsonify, request
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from injector import inject
from backEnd.service.lavoura_service import LavouraService
from backEnd.controllers.functool.jwt_authentication import jwtAuthentication
import json

lavoura_permanente_bp = Blueprint('lavoura_permanente', __name__)

@lavoura_permanente_bp.route('/rendimento_ponderado_por_uf', methods=['POST'])
@jwtAuthentication
def rendimento_ponderado_por_uf(db: SQLAlchemy):
    service = LavouraService(db)
    resultados = service.rendimento_ponderado_por_uf(request.json)
    
    result = [{"uf": uf, "rendimento_ponderado": float(rend)} for uf, rend in resultados]
    # converte para JSON
    return json.dumps(result, ensure_ascii=False, indent=2) , 200

@lavoura_permanente_bp.route('/indicadores_agricolas' , methods=['POST'])
@jwtAuthentication
def indicadores_agricolas(db:SQLAlchemy ):
    service = LavouraService(db)
    resultados = service.rendimento_ponderado_por_uf(request.json)
    resultados = service.indicadores_agricolas(request.json)
    
    
    return jsonify(resultados) , 200 
     
     
     
@lavoura_permanente_bp.route('/get_anos_disponiveis' , methods=['POST'])
@jwtAuthentication
def get_anos_disponiveis(db:SQLAlchemy ):
    service = LavouraService(db)
    resultados = service.get_anos_disponiveis()
    
    
    return jsonify(resultados) , 200 