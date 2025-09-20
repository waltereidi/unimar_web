import re
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from backEnd.infrastructure.database.models import User
from sqlalchemy import text , create_engine
from backEnd.service.criptografia import CriptografiaSimetrica , JWTManager
from backEnd.value_objects.emailVO import EmailVO
from backEnd.value_objects.passwordVO import PasswordVO

class LoginService:
    def __init__(self , db: SQLAlchemy):
        self.db = db

    def authenticate(self, json:str ) : 
        
        email = EmailVO(json.get("email"))
        password = PasswordVO(json.get("password"))
        
        if(password.validate()):
            raise Exception(password)
        
        user = (
        self.db.session.query(User)
            .filter(
                User.email == email.value
                )
            .first()
        )
        if(user == None ):
            raise Exception("Não foi possível encontrar o e-mail")
        
        senhaDescripto = CriptografiaSimetrica().descriptografar(user.encrypted_password)
        
        if(senhaDescripto != password.raw ):
            raise Exception("Senha incorreta")
        
        jwt = JWTManager()
        return {
                    "message": "Sucesso ao realizar Login" , 
                    "success": True , 
                    "token" : jwt.generate_token({"email": user.email}) ,
                    "email" : user.email ,
                    "data": None 
                }
            
    def validate_token(self , json:str )    :
        
        jwt = JWTManager()
        token = json.get("token")
        
        try:
            decoded = jwt.validate_token(token)
            return {"message": "Token válido", "success": True}
        
        except ValueError as e:
            return {"message": str(e), "success": False}

        
