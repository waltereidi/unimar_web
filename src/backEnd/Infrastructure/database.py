from sqlalchemy import create_engine

# Sintaxe: postgresql+driver://usuario:senha@host:porta/banco
engine = create_engine("postgresql+psycopg2://meu_usuario:minha_senha@localhost:5432/meu_banco")
