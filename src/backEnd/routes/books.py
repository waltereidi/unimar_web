from flask import Blueprint, jsonify, request
from sqlalchemy import text

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['GET'])
def get_books():
    """Retorna lista de produtos"""
        
    return jsonify('s')

def getBookDescription(book_id):
    
    return jsonify('s')