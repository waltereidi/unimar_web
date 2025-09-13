import pytest
from flask import Flask
from backEnd.infrastructure.models import db

@pytest.fixture
def app():
    app = Flask(__name__)
    # app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # banco em memória
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)
    
    # with app.app_context():
    #     db.create_all()  # cria tabelas no SQLite in-memory
    #     app.register_blueprint(login_bp, url_prefix='/api/login')
    #     yield app
    #     db.drop_all()
    assert False

@pytest.fixture
def client(app):
    return app.test_client()

# def test_authentication_success(client):
#     payload = {
#         "email": "teste@exemplo.com",
#         "password": "123456",
#         "remember": True
#     }

#     response = client.post('/api/login/authentication', json=payload)
#     json_data = response.get_json()

#     assert response.status_code == 200
#     assert json_data['email'] == payload['email']
#     assert json_data['remember'] is True
#     assert 'books_count' in json_data
#     assert json_data['message'] == "Requisição recebida"

# def test_authentication_no_payload(client):
#     # Requisição sem JSON
#     response = client.post('/api/login/authentication')
#     json_data = response.get_json()

#     assert response.status_code == 200  # sua rota atual retorna 200 mesmo sem payload
#     assert json_data['email'] is None
#     assert json_data['remember'] is False
