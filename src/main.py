import os
import sys
from flask import Flask, send_from_directory, jsonify, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from backEnd.infrastructure.models import db
from backEnd.infrastructure.database.models import User, Books
from sqlalchemy import text
from injector import Binder
from flask_injector import FlaskInjector
from flask_caching import Cache
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
import threading



app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'backEnd/defaultPages'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
app.config['DEBUG'] = True
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/biblioteca4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Debug remoto
if os.environ.get("DEBUGPY") == "1":
    import debugpy
    if not getattr(sys, "_debugpy_started", False):
        debugpy.listen(("0.0.0.0", 5678))
        sys._debugpy_started = True
        print("🔹 debugpy listening on port 5678")
        app.config['TEMPLATES_AUTO_RELOAD'] = True

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

jwt = JWTManager(app)

# Importar e registrar blueprints das rotas
def register_blueprints():
    """Registra todos os blueprints da pasta routes"""
    routes_path = os.path.join(os.path.dirname(__file__), 'backEnd', 'controllers')
   
    # Função para registrar automaticamente novos blueprints
    def auto_register_blueprints():
        """Registra automaticamente todos os blueprints encontrados na pasta routes"""
        import importlib
        import pkgutil
        
        try:
            # Importar o módulo routes
            routes_module = importlib.import_module('backEnd.controllers')
            
            # Procurar por blueprints em todos os módulos da pasta routes
            for _, module_name, _ in pkgutil.iter_modules([routes_path]):
                if module_name != '__init__':
                    try:
                        module = importlib.import_module(f'backEnd.controllers.{module_name}')
                        
                        # Procurar por atributos que terminam com '_bp' (blueprint)
                        for attr_name in dir(module):
                            if attr_name.endswith('_bp'):
                                blueprint = getattr(module, attr_name)
                                if hasattr(blueprint, 'name'):
                                    app.register_blueprint(blueprint, url_prefix='/api')
                                    print(f"✅ Blueprint '{blueprint.name}' registrado automaticamente")
                    except Exception as e:
                        print(f"⚠️ Erro ao registrar blueprint do módulo '{module_name}': {e}")
        except Exception as e:
            print(f"⚠️ Erro ao registrar blueprints automaticamente: {e}")
    
    # Executar registro automático
    auto_register_blueprints()

# Registrar blueprints
register_blueprints()
# Configurar injeção de dependência

def configure(binder: Binder) -> None:
    binder.bind(SQLAlchemy, to=db, scope=request)

def run_watcher():
    from backEnd.watcher import start_watcher 
    start_watcher(".")
     
FlaskInjector(app=app, modules=[configure])
    
if __name__ == 'main':
    watcher_thread = threading.Thread(target=run_watcher, daemon=True)
    watcher_thread.start()
    # Criar tabelas do banco de dados
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    print(app.static_folder)
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'notFound404.html')
        print(index_path)
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'notFound404.html')
        else:
            return "index.html not found", 404
    
@app.before_request
def before_request_middleware():
    print(f"Middleware BEFORE: {request.method} {request.path}")

# Middleware para modificar a resposta
@app.after_request
def after_request_middleware(response):
    response.headers['X-Custom-Header'] = 'MeuMiddleware'
    print(f"Middleware AFTER: status {response.status_code}")
    return response



