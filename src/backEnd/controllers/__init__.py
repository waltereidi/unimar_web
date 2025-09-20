# Arquivo __init__.py para a pasta routes
# Este arquivo facilita a importação dos blueprints

from .user import user_bp
from .lavoura_permanente import lavoura_permanente_bp
from .login import login_bp

# Lista de todos os blueprints disponíveis
__all__ = ['user_bp', 'lavoura_permanente_bp' , 'login_bp']
