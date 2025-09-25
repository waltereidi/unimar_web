from flask import Blueprint, jsonify, request
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from backEnd.service.open_ai_service import OpenAiService
from backEnd.controllers.functool.jwt_authentication import jwtAuthentication

open_ai_bp = Blueprint('open_ai', __name__)

@open_ai_bp.route('/GPT5nano_GetResponse', methods=['POST'])
def authenticationd():
    
    service = OpenAiService()
    result = service.GPT5nano_GetResponse(request.json)

    return jsonify({"message" :result} ), 200     