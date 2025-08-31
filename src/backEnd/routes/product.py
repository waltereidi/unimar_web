from flask import Blueprint, jsonify, request
from backEnd.models import Product
from backEnd.database.models import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    """Retorna lista de produtos"""
    try:
        # Verificar se quer apenas produtos ativos
        active_only = request.args.get('active', 'true').lower() == 'true'
        
        if active_only:
            products = Product.get_active_products()
        else:
            products = Product.get_all()
        
        return jsonify([product.to_dict() for product in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products', methods=['POST'])
def create_product():
    """Cria um novo produto"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Validar campos obrigatórios
        if not data.get('name') or not data.get('price'):
            return jsonify({'error': 'Nome e preço são obrigatórios'}), 400
        
        # Criar novo produto
        product = Product.create(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            stock_quantity=data.get('stock_quantity', 0),
            category=data.get('category'),
            image_url=data.get('image_url'),
            is_active=data.get('is_active', True)
        )
        
        return jsonify(product.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retorna um produto específico"""
    try:
        product = Product.get_by_id(product_id)
        if not product:
            return jsonify({'error': 'Produto não encontrado'}), 404
        return jsonify(product.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualiza um produto"""
    try:
        product = Product.get_by_id(product_id)
        if not product:
            return jsonify({'error': 'Produto não encontrado'}), 404
        
        data = request.json
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Atualizar campos
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'price' in data:
            product.price = data['price']
        if 'stock_quantity' in data:
            product.stock_quantity = data['stock_quantity']
        if 'category' in data:
            product.category = data['category']
        if 'image_url' in data:
            product.image_url = data['image_url']
        if 'is_active' in data:
            product.is_active = data['is_active']
        
        product.save()
        return jsonify(product.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Deleta um produto"""
    try:
        product = Product.get_by_id(product_id)
        if not product:
            return jsonify({'error': 'Produto não encontrado'}), 404
        
        product.delete()
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/category/<category>', methods=['GET'])
def get_products_by_category(category):
    """Retorna produtos por categoria"""
    try:
        products = Product.get_by_category(category)
        return jsonify([product.to_dict() for product in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<int:product_id>/stock', methods=['PUT'])
def update_stock(product_id):
    """Atualiza o estoque de um produto"""
    try:
        product = Product.get_by_id(product_id)
        if not product:
            return jsonify({'error': 'Produto não encontrado'}), 404
        
        data = request.json
        if not data or 'quantity' not in data:
            return jsonify({'error': 'Quantidade é obrigatória'}), 400
        
        quantity = data['quantity']
        product.update_stock(quantity)
        
        return jsonify(product.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

