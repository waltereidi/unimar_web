from flask_sqlalchemy import SQLAlchemy

# Cria a instância do SQLAlchemy
db = SQLAlchemy()

# Importa os modelos depois de criar o db
from .models import User, Books  # substitua pelo nome real do arquivo onde estão os models

__all__ = ["db", "User", "Books"]
