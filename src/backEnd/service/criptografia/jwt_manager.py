import jwt
import datetime
import os 

class JWTManager:
    def __init__(self , expiration_minutes: int = None):
        if os.environ.get("JWT_KEY") is None or os.environ.get("JWT_EXPIRARTION_MINUTES") is None :
            raise ValueError("Não foi possível encontrar a chave de JWT_KEY e JWT_EXPIRARTION_MINUTES no ambiente.")
        else: 
            self.secret_key = os.environ.get("JWT_KEY")
            self.expiration_minutes = expiration_minutes if expiration_minutes is not None else int(os.environ.get("JWT_EXPIRARTION_MINUTES"))    
            
    def generate_token(self, payload: dict) -> str:
        """
        Gera um novo token JWT com expiração.
        """

        payload_with_exp = {
            **payload,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=self.expiration_minutes)
        }
        token = jwt.encode(payload_with_exp, self.secret_key, algorithm="HS256")
        return token

    def validate_token(self, token: str) -> dict:
        """
        Valida um token JWT e retorna o payload decodificado.
        """
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")
