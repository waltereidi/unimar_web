# Arquivo __init__.py para a pasta routes
# Este arquivo facilita a importação dos blueprints

from .jwt_authentication import jwtAuthentication

# Lista de todos os blueprints disponíveis
__all__ = ['jwtAuthentication']
