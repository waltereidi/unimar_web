import pytest
import time
import jwt
from backEnd.service.criptografia.jwt_manager import JWTManager

SECRET_KEY = "chave_teste"


def test_generate_and_validate_token():
    jwt_manager = JWTManager()

    token = jwt_manager.generate_token({"user": "admin"})
    assert isinstance(token, str)

    decoded = jwt_manager.validate_token(token)
    assert decoded["user"] == "admin"


def test_expired_token():
    jwt_manager = JWTManager(expiration_minutes=0)

    token = jwt_manager.generate_token({"user": "admin"})

    # esperar 1 segundo para expirar
    time.sleep(1)

    with pytest.raises(ValueError, match="Token expirado"):
        jwt_manager.validate_token(token)


def test_invalid_token():
    jwt_manager = JWTManager()

    # Criar um token inválido (assinatura errada)
    invalid_token = jwt.encode({"user": "admin"}, "outra_chave", algorithm="HS256")

    with pytest.raises(ValueError, match="Token inválido"):
        jwt_manager.validate_token(invalid_token)
