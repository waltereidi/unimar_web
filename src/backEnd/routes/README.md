# Sistema de Rotas

Este diretório contém todos os blueprints (rotas) da aplicação Flask.

## Estrutura

Cada arquivo Python nesta pasta deve conter um blueprint Flask que será automaticamente registrado na aplicação principal.

## Convenções

1. **Nome do arquivo**: Use nomes descritivos em minúsculas (ex: `user.py`, `product.py`)
2. **Nome do blueprint**: Use o padrão `{nome}_bp` (ex: `user_bp`, `product_bp`)
3. **URL prefix**: Todos os blueprints são registrados com o prefixo `/api`

## Exemplo de Criação de Rotas

```python
from flask import Blueprint, jsonify, request

# Criar o blueprint
user_bp = Blueprint('user', __name__)

# Definir rotas
@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({"message": "Lista de usuários"})

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({"message": "Usuário criado"}), 201
```

## Registro Automático

Os blueprints são registrados automaticamente pelo sistema. Para que um blueprint seja detectado:

1. O arquivo deve estar na pasta `src/backEnd/routes/`
2. O blueprint deve ter um nome que termine com `_bp`
3. O blueprint deve ter um atributo `name`

## URLs Disponíveis

Após o registro, as URLs ficam disponíveis em:
- `/api/users` (do blueprint user)
- `/api/products` (do blueprint product)

## Adicionando Novas Rotas

1. Crie um novo arquivo Python na pasta `routes/`
2. Defina seu blueprint seguindo as convenções
3. Reinicie a aplicação - o blueprint será registrado automaticamente
4. Atualize este README se necessário

