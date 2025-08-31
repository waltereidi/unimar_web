# Sistema de Migrações com Alembic

Este projeto utiliza Alembic para gerenciar migrações do banco de dados de forma segura e controlada.

## Estrutura de Migrações

```
src/backEnd/database/migrations/
├── env.py                    # Configuração do ambiente Alembic
├── script.py.mako           # Template para arquivos de migração
└── versions/                # Diretório com as migrações
    └── 0001_initial_migration.py  # Primeira migração
```

## Comandos Principais

### 1. **Usando o Script de Gerenciamento**
```bash
python manage_migrations.py
```

### 2. **Comandos Alembic Diretos**

#### Inicializar (primeira vez)
```bash
alembic init src/backEnd/database/migrations
```

#### Criar nova migração
```bash
alembic revision --autogenerate -m "Descrição da migração"
```

#### Aplicar migrações
```bash
alembic upgrade head
```

#### Verificar status
```bash
alembic current
alembic history
```

#### Fazer downgrade
```bash
alembic downgrade -1
```

## Fluxo de Trabalho

### 1. **Desenvolvimento**
1. Faça alterações nos modelos
2. Execute: `alembic revision --autogenerate -m "Descrição"`
3. Revise o arquivo de migração gerado
4. Execute: `alembic upgrade head`

### 2. **Produção**
1. Copie os arquivos de migração para o servidor
2. Execute: `alembic upgrade head`
3. Verifique: `alembic current`

## Migrações Existentes

### **0001 - Initial Migration**
- Cria tabela `users` com campos: id, created_at, updated_at, username, email, password_hash, is_active
- Cria tabela `products` com campos: id, created_at, updated_at, name, description, price, stock_quantity, is_active, category, image_url

## Boas Práticas

### ✅ **Faça**
- Sempre revise as migrações geradas automaticamente
- Use descrições claras para as migrações
- Teste as migrações em ambiente de desenvolvimento
- Faça backup antes de aplicar migrações em produção

### ❌ **Não Faça**
- Não edite migrações já aplicadas em produção
- Não force migrações sem revisar
- Não ignore erros de migração

## Resolução de Problemas

### Erro: "Target database is not up to date"
```bash
# Aplique as migrações pendentes
alembic upgrade head
```

### Erro: "Can't locate revision identified by"
```bash
# Verifique o histórico
alembic history

# Se necessário, marque como aplicada
alembic stamp head
```

### Erro: "Table already exists"
```bash
# Verifique se a migração já foi aplicada
alembic current

# Se necessário, force a aplicação
alembic stamp head
```

## Configuração

O arquivo `alembic.ini` contém as configurações principais:
- `script_location`: Localização dos scripts de migração
- `sqlalchemy.url`: URL do banco de dados
- Configurações de logging

## Integração com a Aplicação

A aplicação automaticamente tenta aplicar migrações na inicialização. Se houver erro, ela cria as tabelas diretamente como fallback.

## Exemplo de Nova Migração

### 1. Adicionar campo ao modelo
```python
# Em src/backEnd/models/user.py
class User(BaseModel):
    # ... campos existentes ...
    phone = db.Column(db.String(20), nullable=True)
```

### 2. Gerar migração
```bash
alembic revision --autogenerate -m "Add phone field to users"
```

### 3. Aplicar migração
```bash
alembic upgrade head
```

## Monitoramento

Para monitorar o estado das migrações:
```bash
# Status atual
alembic current

# Histórico completo
alembic history --verbose

# Migrações pendentes
alembic show head
```
