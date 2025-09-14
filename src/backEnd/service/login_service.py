import re
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from backEnd.infrastructure.database.models import User
from sqlalchemy import text , create_engine
from backEnd.service.criptografia import CriptografiaSimetrica , JWTManager

class LoginService:
    def __init__(self , db: SQLAlchemy):
        self.db = db

    def authenticate(self, json:str ) : 
        
        email = json.get("email")
        password = json.get("password")
        
        user = (
        self.db.session.query(User)
            .filter(
                User.email == email
                )
            .first()
        )
        senhaDescripto = CriptografiaSimetrica().descriptografar(user.encrypted_password)
        
        if(user == None or senhaDescripto != password):
            return {"message": "Usuário ou senha inválidos" , "success": False}        
        else:
            jwt = JWTManager()
            return {
                        "message": "Sucesso ao realizar Login" , 
                        "success": True , 
                        "token" : jwt.generate_token({"email": user.email}) ,
                        "data": None 
                    }
        
