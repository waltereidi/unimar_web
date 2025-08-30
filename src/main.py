
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# DON'T CHANGE THIS !!!
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

        

        
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'frontEnd'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
app.config['DEBUG'] = True
# Configurar CORS para permitir requisições de qualquer origem
CORS(app)

# Registrar blueprints
# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'src/database', 'app.db')}"
print(os.environ)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.environ.get("DEBUGPY") == "1":
    import debugpy
    if not getattr(sys, "_debugpy_started", False):
        debugpy.listen(("0.0.0.0", 5678))
        sys._debugpy_started = True
        print("🔹 debugpy listening on port 5678")
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found"+app.static_folder, 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)