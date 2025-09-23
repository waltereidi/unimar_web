from flask import Blueprint, jsonify, request
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from backEnd.service.open_ai_service import OpenAiService
from backEnd.controllers.functool.jwt_authentication import jwtAuthentication

open_ai_bp = Blueprint('open_ai', __name__)

@open_ai_bp.route('/openai', methods=['POST'])
@jwtAuthentication
def authenticationd():
        
    return jsonify("result" ), 200     
    
        