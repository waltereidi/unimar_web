from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Instância do SQLAlchemy
db = SQLAlchemy()

class BaseModel(db.Model):
    """Classe base para todos os modelos"""
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Converte o modelo para dicionário"""
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, datetime):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value
        return result
    
    def save(self):
        """Salva o modelo no banco de dados"""
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        """Deleta o modelo do banco de dados"""
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def get_by_id(cls, id):
        """Busca um modelo pelo ID"""
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls):
        """Retorna todos os registros do modelo"""
        return cls.query.all()
    
    @classmethod
    def create(cls, **kwargs):
        """Cria um novo registro"""
        instance = cls(**kwargs)
        return instance.save()
