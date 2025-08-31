#!/usr/bin/env python3
"""
Script para aplicar migração manual da tabela products
"""

import sqlite3
import os

def create_products_table():
    """Cria a tabela products no banco de dados"""
    db_path = 'src/backEnd/database/app.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Banco de dados não encontrado: {db_path}")
        return False
    
    try:
        # Conectar ao banco
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Verificar se a tabela já existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        if cursor.fetchone():
            print("✅ Tabela 'products' já existe")
            return True
        
        # Criar tabela products
        create_table_sql = """
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME,
            updated_at DATETIME,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            price NUMERIC(10,2) NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            is_active BOOLEAN DEFAULT 1,
            category VARCHAR(50),
            image_url VARCHAR(255)
        )
        """
        
        cursor.execute(create_table_sql)
        conn.commit()
        
        print("✅ Tabela 'products' criada com sucesso!")
        
        # Verificar tabelas existentes
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"📊 Tabelas no banco: {tables}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar tabela: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Aplicando migração manual - Tabela Products")
    print("=" * 50)
    
    if create_products_table():
        print("\n✅ Migração aplicada com sucesso!")
    else:
        print("\n❌ Falha na migração!")
