import re
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from backEnd.infrastructure.database.models import User
from sqlalchemy import text , create_engine
from injector import inject


class LoginService:
    def __init__(self , db: SQLAlchemy):
        self.db = db

    def authenticate(self, email: str, password: str, remember: bool):
        # Lógica de autenticação (exemplo fictício)
        user = self.db.session.query(User).filter_by(email=email, password=password).first()
        if user:
            return {"message": "Autenticação bem-sucedida", "user": user.email}
        else:
            return {"message": "Falha na autenticação"}, 401
        
