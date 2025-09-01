from flask import Blueprint, jsonify, request

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    """Retorna lista de todos os usuários"""
    return jsonify('error'), 200
