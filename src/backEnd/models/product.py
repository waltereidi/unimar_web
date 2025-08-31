from backEnd.database.models import BaseModel, db
from decimal import Decimal

class Product(BaseModel):
    __tablename__ = 'products'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(50), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def to_dict(self):
        """Retorna dicionário com dados do produto"""
        data = super().to_dict()
        # Converte Decimal para float para serialização JSON
        if 'price' in data and isinstance(data['price'], Decimal):
            data['price'] = float(data['price'])
        return data
    
    @classmethod
    def get_active_products(cls):
        """Retorna apenas produtos ativos"""
        return cls.query.filter_by(is_active=True).all()
    
    @classmethod
    def get_by_category(cls, category):
        """Retorna produtos por categoria"""
        return cls.query.filter_by(category=category, is_active=True).all()
    
    def update_stock(self, quantity):
        """Atualiza a quantidade em estoque"""
        self.stock_quantity = max(0, self.stock_quantity + quantity)
        self.save()
        return self
