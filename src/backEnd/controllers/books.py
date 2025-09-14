from flask import Blueprint, jsonify, request
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker
from backEnd.infrastructure.database.models import Books 
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from injector import inject

book_bp = Blueprint('book', __name__)



@book_bp.route('/books', methods=['GET'])
def get_books(db: SQLAlchemy):
    print(db)

    return jsonify('1')


def getBookDescription(book_id):
    
    return jsonify('s')
