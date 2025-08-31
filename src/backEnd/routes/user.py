from flask import Blueprint, jsonify, request
from backEnd.models import User
from backEnd.database.models import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    """Retorna lista de todos os usuários"""
    try:
        users = User.get_all()
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users', methods=['POST'])
def create_user():
    """Cria um novo usuário"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Validar campos obrigatórios
        if not data.get('username') or not data.get('email'):
            return jsonify({'error': 'Username e email são obrigatórios'}), 400
        
        # Verificar se usuário já existe
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return jsonify({'error': 'Username já existe'}), 409
        
        existing_email = User.query.filter_by(email=data['email']).first()
        if existing_email:
            return jsonify({'error': 'Email já existe'}), 409
        
        # Criar novo usuário
        user = User.create(
            username=data['username'],
            email=data['email'],
            password_hash=data.get('password_hash')  # Em produção, deve ser hash da senha
        )
        
        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retorna um usuário específico"""
    try:
        user = User.get_by_id(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Atualiza um usuário"""
    try:
        user = User.get_by_id(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        data = request.json
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Atualizar campos
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'password_hash' in data:
            user.password_hash = data['password_hash']
        if 'is_active' in data:
            user.is_active = data['is_active']
        
        user.save()
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deleta um usuário"""
    try:
        user = User.get_by_id(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        user.delete()
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500
