#!/usr/bin/env python3
"""
Script de teste rápido para verificar se a importação está funcionando.
"""

import csv
import re

arquivo_csv = "/Users/saymon.silva/Downloads/contacts.csv"

print("\n" + "="*60)
print("🧪 TESTE DE IMPORTAÇÃO")
print("="*60 + "\n")

try:
    contatos = []
    
    with open(arquivo_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Extrair nome - formato novo do Google
            first = row.get('First Name', '').strip()
            middle = row.get('Middle Name', '').strip()
            last = row.get('Last Name', '').strip()
            
            # Remover emojis do início
            first = re.sub(r'^[\U0001F300-\U0001F9FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U00002600-\U000027BF]+', '', first).strip()
            
            nome_parts = [p for p in [first, middle, last] if p]
            nome = ' '.join(nome_parts)
            
            if not nome:
                continue
            
            telefone = row.get('Phone 1 - Value', '').strip()
            email = row.get('E-mail 1 - Value', '').strip()
            aniversario = row.get('Birthday', '').strip()
            
            contatos.append({
                'nome': nome,
                'telefone': telefone,
                'email': email,
                'aniversario': aniversario
            })
    
    print(f"✅ {len(contatos)} contatos encontrados!\n")
    
    # Mostrar primeiros 10
    print("📋 Primeiros 10 contatos:")
    print("-" * 60)
    for i, c in enumerate(contatos[:10], 1):
        print(f"{i:2d}. {c['nome']}")
        if c['telefone']:
            print(f"    📱 {c['telefone']}")
        if c['email']:
            print(f"    📧 {c['email']}")
        if c['aniversario']:
            print(f"    🎂 {c['aniversario']}")
        print()
    
    print("-" * 60)
    print(f"\n✅ Importação funcionando! Total: {len(contatos)} contatos")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
