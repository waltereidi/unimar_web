import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class CriptografiaSimetrica:
    def __init__(self):
        if os.environ.get("CRIPTOGRAPHY") is None:
            raise ValueError("Não foi possível encontrar a chave de criptografia no ambiente.")
        else: 
            self.salt = b'salt_fixo'  # precisa ser bytes
    
    def gerar_chave(self) -> str:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Fernet precisa de 32 bytes
            salt=self.salt,
            iterations=390000,
            backend=default_backend()
        )
    
        key = base64.urlsafe_b64encode(
            kdf.derive(os.environ.get("CRIPTOGRAPHY").encode())
        )
        return key.decode('utf-8')  # retorna como string

    def criptografar(self, texto: str) -> str:
        chave = self.gerar_chave()
        fernet = Fernet(chave.encode())
        token = fernet.encrypt(texto.encode("utf-8"))
        return token.decode("utf-8")  # retorna como string

    def descriptografar(self, texto_criptografado: str) -> str:
        chave = self.gerar_chave()
        fernet = Fernet(chave.encode())
        return fernet.decrypt(texto_criptografado.encode("utf-8")).decode("utf-8")
