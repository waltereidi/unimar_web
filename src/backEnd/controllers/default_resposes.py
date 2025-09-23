import re
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text , create_engine

default_responses_bp = Blueprint('default_responses', __name__)

@default_responses_bp.route('/unauthorized', methods=['POST'])
def unauthorized():
    return jsonify("Unauthorized") , 401