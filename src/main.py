import os
import sys
import threading
from flask import Flask, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
from backEnd.kernel.routes import RouteRegister
from backEnd.infrastructure.models import db
from injector import Binder
from flask_injector import FlaskInjector
from flask_caching import Cache
from flask_jwt_extended import ( JWTManager )

#sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'backEnd/defaultPages'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
app.config['DEBUG'] = True
CORS(app)

connectionString = (
    f"postgresql://{os.environ.get('DATABASE_USERNAME')}:"
    f"{os.environ.get('DATABASE_PASSWORD')}@db:"
    f"{os.environ.get('DATABASE_PORT')}/"
    f"{os.environ.get('DATABASE_NAME')}"
)
app.config["SQLALCHEMY_DATABASE_URI"] = connectionString
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
cache = Cache(app)

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

RouteRegister.register_blueprints(app)
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


#Middlewares ------
@app.before_request
def before_request_middleware():
    print(f"Middleware BEFORE: {request.method} {request.path}")

# Middleware para modificar a resposta
@app.after_request
def after_request_middleware(response):
    response.headers['X-Custom-Header'] = 'MeuMiddleware'
    print(f"Middleware AFTER: status {response.status_code}")
    return response



