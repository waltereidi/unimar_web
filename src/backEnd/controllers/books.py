from flask import Blueprint, jsonify, request
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from backEnd.infrastructure.database.models import Books 
from backEnd.infrastructure.database import db

book_bp = Blueprint('book', __name__)



@book_bp.route('/books', methods=['GET'])
def get_books():
    print(db)
    books = db.session.query(Books).all()  # use db.session
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "author": b.author
    } for b in books])

def getBookDescription(book_id):
    
    return jsonify('s')