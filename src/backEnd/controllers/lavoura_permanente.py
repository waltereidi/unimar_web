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
def rendimento_ponderado_por_uf(db: SQLAlchemy):
    service = LavouraService(db)
    resultados = service.rendimento_ponderado_por_uf('2020')
    
    result = [{"uf": uf, "rendimento_ponderado": float(rend)} for uf, rend in resultados]
    # converte para JSON
    return json.dumps(result, ensure_ascii=False, indent=2) , 200

@lavoura_permanente_bp.route('/indicadores_agricolas' , methods=['POST'])
def indicadores_agricolas(db:SQLAlchemy ):
    service = LavouraService(db)
    resultados = service.indicadores_agricolas('2023')
    
    
    return jsonify(resultados) , 200 
     
     