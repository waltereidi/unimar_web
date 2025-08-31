# ORM com SQLAlchemy - Documentação

Este projeto utiliza SQLAlchemy como ORM (Object-Relational Mapping) para gerenciar o banco de dados.

## Estrutura

### 1. **BaseModel** (`src/backEnd/database/models.py`)
Classe base que fornece funcionalidades comuns para todos os modelos:
- `id`: Chave primária automática
- `created_at`: Data de criação
- `updated_at`: Data de última atualização
- Métodos úteis: `to_dict()`, `save()`, `delete()`, `get_by_id()`, `get_all()`, `create()`

### 2. **Modelos**
- **User** (`src/backEnd/models/user.py`): Gerenciamento de usuários
- **Product** (`src/backEnd/models/product.py`): Gerenciamento de produtos

## Como Usar

### Criando um Novo Modelo

```python
from backEnd.database.models import BaseModel, db

class Category(BaseModel):
    __tablename__ = 'categories'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'
```

### Operações Básicas

```python
# Criar
category = Category.create(name="Eletrônicos", description="Produtos eletrônicos")

# Buscar por ID
category = Category.get_by_id(1)

# Buscar todos
categories = Category.get_all()

# Atualizar
category.name = "Novo Nome"
category.save()

# Deletar
category.delete()

# Converter para dicionário
data = category.to_dict()
```

### Queries Avançadas

```python
# Filtrar por condição
active_categories = Category.query.filter_by(is_active=True).all()

# Ordenar
categories = Category.query.order_by(Category.name).all()

# Limitar resultados
categories = Category.query.limit(10).all()

# Buscar primeiro
category = Category.query.filter_by(name="Eletrônicos").first()
```

## Rotas Disponíveis

### Usuários (`/api/users`)
- `GET /api/users` - Listar todos os usuários
- `POST /api/users` - Criar usuário
- `GET /api/users/{id}` - Buscar usuário específico
- `PUT /api/users/{id}` - Atualizar usuário
- `DELETE /api/users/{id}` - Deletar usuário

### Produtos (`/api/products`)
- `GET /api/products` - Listar produtos (aceita parâmetro `active=true/false`)
- `POST /api/products` - Criar produto
- `GET /api/products/{id}` - Buscar produto específico
- `PUT /api/products/{id}` - Atualizar produto
- `DELETE /api/products/{id}` - Deletar produto
- `GET /api/products/category/{category}` - Produtos por categoria
- `PUT /api/products/{id}/stock` - Atualizar estoque

## Exemplos de Uso

### Criar um Produto
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Smartphone",
    "description": "Smartphone de última geração",
    "price": 999.99,
    "stock_quantity": 50,
    "category": "Eletrônicos"
  }'
```

### Criar um Usuário
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "joao_silva",
    "email": "joao@email.com"
  }'
```

## Configuração do Banco

O banco de dados SQLite é criado automaticamente em `src/backEnd/database/app.db` quando a aplicação é iniciada pela primeira vez.

## Migrações

Para adicionar novos campos ou tabelas:
1. Modifique o modelo
2. Delete o arquivo `app.db` (se existir)
3. Reinicie a aplicação - as tabelas serão recriadas automaticamente

**Nota:** Em produção, use Alembic para migrações mais seguras.
