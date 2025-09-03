from flask import Blueprint, jsonify, request
from sqlalchemy import text

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    """Retorna lista de produtos"""

        
    return jsonify('s')
