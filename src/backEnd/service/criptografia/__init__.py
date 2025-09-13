# Arquivo __init__.py para a pasta routes
# Este arquivo facilita a importação dos blueprints

from .criptografia_simetrica import CriptografiaSimetrica

# Lista de todos os blueprints disponíveis
__all__ = ['CriptografiaSimetrica']
