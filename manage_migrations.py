#!/usr/bin/env python3
"""
Script para gerenciar migrações do banco de dados
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔄 {description}")
    print(f"Comando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Sucesso!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro!")
        print(f"Erro: {e.stderr}")
        return False

def main():
    """Função principal"""
    print("🚀 Gerenciador de Migrações do Banco de Dados")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("alembic.ini"):
        print("❌ Erro: Execute este script no diretório raiz do projeto")
        sys.exit(1)
    
    # Verificar se o Alembic está instalado
    try:
        import alembic
        print("✅ Alembic encontrado")
    except ImportError:
        print("❌ Alembic não encontrado. Instalando...")
        if not run_command("pip install alembic", "Instalando Alembic"):
            sys.exit(1)
    
    # Menu de opções
    while True:
        print("\n📋 Opções disponíveis:")
        print("1. Inicializar migrações (primeira vez)")
        print("2. Criar nova migração")
        print("3. Aplicar migrações pendentes")
        print("4. Verificar status das migrações")
        print("5. Fazer downgrade da última migração")
        print("6. Ver histórico de migrações")
        print("0. Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            print("\n🔧 Inicializando migrações...")
            if run_command("alembic init src/backEnd/database/migrations", "Inicializando Alembic"):
                print("✅ Migrações inicializadas com sucesso!")
                print("📝 Agora você pode criar migrações com a opção 2")
        
        elif choice == "2":
            message = input("Digite uma descrição para a migração: ").strip()
            if message:
                if run_command(f'alembic revision --autogenerate -m "{message}"', "Criando nova migração"):
                    print("✅ Migração criada com sucesso!")
                    print("📝 Aplique a migração com a opção 3")
            else:
                print("❌ Descrição é obrigatória")
        
        elif choice == "3":
            if run_command("alembic upgrade head", "Aplicando migrações"):
                print("✅ Migrações aplicadas com sucesso!")
        
        elif choice == "4":
            if run_command("alembic current", "Verificando migração atual"):
                print("\n📊 Status das migrações:")
                run_command("alembic history", "Histórico de migrações")
        
        elif choice == "5":
            if run_command("alembic downgrade -1", "Fazendo downgrade"):
                print("✅ Downgrade realizado com sucesso!")
        
        elif choice == "6":
            run_command("alembic history --verbose", "Histórico detalhado")
        
        elif choice == "0":
            print("\n👋 Saindo...")
            break
        
        else:
            print("❌ Opção inválida")

if __name__ == "__main__":
    main()
