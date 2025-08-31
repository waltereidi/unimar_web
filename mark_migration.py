#!/usr/bin/env python3
"""
Script para marcar migração como aplicada no Alembic
"""

import sqlite3
import os

def mark_migration_applied():
    """Marca a migração como aplicada no Alembic"""
    db_path = 'src/backEnd/database/app.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Banco de dados não encontrado: {db_path}")
        return False
    
    try:
        # Conectar ao banco
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Verificar se a tabela alembic_version já existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='alembic_version'")
        if not cursor.fetchone():
            # Criar tabela alembic_version
            cursor.execute("""
                CREATE TABLE alembic_version (
                    version_num VARCHAR(32) PRIMARY KEY
                )
            """)
            print("✅ Tabela 'alembic_version' criada")
        
        # Inserir versão atual
        cursor.execute("DELETE FROM alembic_version")  # Limpar versões anteriores
        cursor.execute("INSERT INTO alembic_version (version_num) VALUES (?)", ('0002',))
        conn.commit()
        
        print("✅ Migração '0002' marcada como aplicada!")
        
        # Verificar versão atual
        cursor.execute("SELECT version_num FROM alembic_version")
        version = cursor.fetchone()
        if version:
            print(f"📊 Versão atual: {version[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro ao marcar migração: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Marcando migração como aplicada no Alembic")
    print("=" * 50)
    
    if mark_migration_applied():
        print("\n✅ Migração marcada com sucesso!")
    else:
        print("\n❌ Falha ao marcar migração!")

