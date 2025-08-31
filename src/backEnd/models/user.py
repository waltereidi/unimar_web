from backEnd.database.models import BaseModel, db

class User(BaseModel):
    __tablename__ = 'users'
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        """Retorna dicionário com dados do usuário (sem senha)"""
        data = super().to_dict()
        data.pop('password_hash', None)  # Remove a senha do dicionário
        return data
