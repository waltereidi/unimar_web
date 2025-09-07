# Arquivo __init__.py para a pasta routes
# Este arquivo facilita a importação dos blueprints

from .user import user_bp
from .books import product_bp

# Lista de todos os blueprints disponíveis
__all__ = ['user_bp', 'product_bp']
