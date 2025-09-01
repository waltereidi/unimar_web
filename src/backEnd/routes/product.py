from flask import Blueprint, jsonify, request

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    """Retorna lista de produtos"""

        
    return jsonify('s')
