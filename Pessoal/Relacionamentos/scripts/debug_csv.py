#!/usr/bin/env python3
"""
Script de debug para verificar o formato do CSV do Google Contacts.
"""

import csv
import sys

def analisar_csv(arquivo_csv):
    """Analisa e mostra informações sobre o CSV."""
    print("\n" + "="*60)
    print("🔍 ANÁLISE DO ARQUIVO CSV")
    print("="*60 + "\n")
    
    try:
        # Tentar diferentes encodings
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'iso-8859-1', 'cp1252']
        
        conteudo = None
        encoding_usado = None
        
        for enc in encodings:
            try:
                with open(arquivo_csv, 'r', encoding=enc) as f:
                    conteudo = f.read()
                    encoding_usado = enc
                    print(f"✅ Arquivo lido com encoding: {enc}\n")
                    break
            except UnicodeDecodeError:
                continue
        
        if not conteudo:
            print("❌ Não foi possível ler o arquivo com nenhum encoding")
            return
        
        # Mostrar primeiras linhas
        linhas = conteudo.split('\n')
        print(f"📊 Total de linhas: {len(linhas)}\n")
        print("📄 Primeiras 5 linhas do arquivo:")
        print("-" * 60)
        for i, linha in enumerate(linhas[:5], 1):
            print(f"{i}: {linha[:100]}{'...' if len(linha) > 100 else ''}")
        print("-" * 60 + "\n")
        
        # Analisar cabeçalho
        with open(arquivo_csv, 'r', encoding=encoding_usado) as f:
            reader = csv.DictReader(f)
            
            print("📋 Colunas encontradas no CSV:")
            print("-" * 60)
            colunas = reader.fieldnames
            if colunas:
                for i, col in enumerate(colunas, 1):
                    print(f"{i:3d}. {col}")
            else:
                print("❌ Nenhuma coluna encontrada!")
            print("-" * 60 + "\n")
            
            # Ler primeira linha de dados
            print("📝 Primeira linha de dados:")
            print("-" * 60)
            try:
                primeira_linha = next(reader)
                for key, value in primeira_linha.items():
                    if value:  # Mostrar apenas campos preenchidos
                        print(f"{key}: {value[:50]}{'...' if len(value) > 50 else ''}")
            except StopIteration:
                print("❌ Nenhuma linha de dados encontrada!")
            print("-" * 60 + "\n")
            
            # Contar linhas com dados
            f.seek(0)
            reader = csv.DictReader(f)
            linhas_com_nome = 0
            
            for row in reader:
                # Verificar diferentes campos de nome
                nome = (row.get('Name', '') or 
                       row.get('Given Name', '') or 
                       row.get('Family Name', '') or
                       row.get('First Name', '') or
                       row.get('Last Name', '')).strip()
                
                if nome:
                    linhas_com_nome += 1
            
            print(f"✅ Linhas com nome: {linhas_com_nome}\n")
            
            # Sugestões
            print("💡 SUGESTÕES:")
            print("-" * 60)
            if linhas_com_nome == 0:
                print("❌ Nenhum contato encontrado!")
                print("\nPossíveis causas:")
                print("1. Arquivo CSV vazio ou sem dados")
                print("2. Formato do CSV diferente do esperado")
                print("3. Colunas com nomes diferentes")
                print("\nSoluções:")
                print("1. Verifique se exportou 'Contatos' e não 'Outros contatos'")
                print("2. Tente exportar novamente do Google Contacts")
                print("3. Use formato 'Google CSV' (não Outlook CSV)")
            else:
                print(f"✅ {linhas_com_nome} contatos encontrados!")
                print("\nO arquivo parece estar correto.")
                print("Vou atualizar o script de importação para usar as colunas corretas.")
            print("-" * 60 + "\n")
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_csv}")
        print("\nVerifique:")
        print("1. O caminho está correto?")
        print("2. O arquivo existe?")
        print("3. Você tem permissão para ler o arquivo?")
    except Exception as e:
        print(f"❌ Erro ao analisar arquivo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        arquivo = input("Caminho do arquivo CSV: ").strip()
    
    analisar_csv(arquivo)
