import os
import sys
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from backEnd.infrastructure.models import db
from backEnd.infrastructure.database.models import User, Product
from sqlalchemy import text



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

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()



# Importar e registrar blueprints das rotas
def register_blueprints():
    """Registra todos os blueprints da pasta routes"""
    routes_path = os.path.join(os.path.dirname(__file__), 'backEnd', 'routes')
    
    # Importar blueprints existentes
    try:
        from backEnd.routes.user import user_bp
        app.register_blueprint(user_bp, url_prefix='/api')
        print("✅ Blueprint 'user' registrado com sucesso")
    except ImportError as e:
        print(f"⚠️ Erro ao importar blueprint 'user': {e}")
    
    # Função para registrar automaticamente novos blueprints
    def auto_register_blueprints():
        """Registra automaticamente todos os blueprints encontrados na pasta routes"""
        import importlib
        import pkgutil
        
        try:
            # Importar o módulo routes
            routes_module = importlib.import_module('backEnd.routes')
            
            # Procurar por blueprints em todos os módulos da pasta routes
            for _, module_name, _ in pkgutil.iter_modules([routes_path]):
                if module_name != '__init__':
                    try:
                        module = importlib.import_module(f'backEnd.routes.{module_name}')
                        
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

if __name__ == '__main__':
    # Criar tabelas do banco de dados
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
