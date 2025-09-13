import pytest
from flask import Flask
# from src.backEnd.infrastructure.models import db
from backEnd.controllers.login import login_bp  

@pytest.fixture
def app():
    """Cria app Flask para rodar os testes"""
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def client(app):
    """Cria cliente de teste Flask"""
    return app.test_client()


class TestLoginBlueprint:
        
    def test_logout(self, client):
        response = client.get("/logout")

        assert response.status_code == 200
        data = response.get_json()
        assert data["message"] == "Logout bem-sucedido"
        
        
