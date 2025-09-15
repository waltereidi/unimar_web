from functools import wraps
from flask import Flask, request, jsonify
import os 
import jwt
from backEnd.service.criptografia.jwt_manager import JWTManager

def jwtAuthentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # O token pode vir no header Authorization
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"erro": "Token ausente!"}), 401

        try:
           jwt_manager = JWTManager()
           decode = jwt_manager.validate_token(token)
           
        except jwt.ExpiredSignatureError:
            return jsonify({"erro": "Token expirado!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token inválido!"}), 401

        return f(*args, **kwargs)
    return decorated