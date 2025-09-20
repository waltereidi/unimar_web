from  backEnd.infrastructure.models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(128), nullable=False)

class LavouraPermanente(db.Model):
    __tablename__ = "lavoura_permanente"
    ano = db.Column(db.String, primary_key=True)
    sigla_uf = db.Column(db.String, primary_key=True)
    id_municipio = db.Column(db.String, primary_key=True)
    produto = db.Column(db.String, primary_key=True)
    area_destinada_colheita = db.Column(db.Numeric)
    area_colhida = db.Column(db.Numeric)
    quantidade_produzida = db.Column(db.Numeric)
    rendimento_medio_producao = db.Column(db.Numeric)
    valor_producao = db.Column(db.Numeric)

