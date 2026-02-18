#!/usr/bin/env python3
"""
Script interativo para organizar arquivos de relacionamentos em pastas.
Move arquivos da raiz para: Família, Amigos, Profissional ou Conhecidos.
"""

import os
import shutil
from pathlib import Path

RELACIONAMENTOS_DIR = Path(__file__).parent.parent

# Pastas de destino
PASTAS = {
    '1': ('Família', RELACIONAMENTOS_DIR / 'Família'),
    '2': ('Amigos', RELACIONAMENTOS_DIR / 'Amigos'),
    '3': ('Profissional', RELACIONAMENTOS_DIR / 'Profissional'),
    '4': ('Conhecidos', RELACIONAMENTOS_DIR / 'Conhecidos')
}

# Arquivos que não devem ser movidos
ARQUIVOS_SISTEMA = [
    '_Template Pessoa.md',
    'Relacionamentos.md',
    'Calendário de Aniversários.md',
    'GUIA_RÁPIDO.md',
    'ESTRUTURA.md',
    'Exemplo - Maria Silva.md',
    'Lista Amigos.md',
    'Lista Conhecidos.md',
    'Lista Família.md',
    'Lista Profissional.md',
    'README.md'
]


def listar_arquivos_para_organizar():
    """Lista todos os arquivos .md na raiz que precisam ser organizados."""
    arquivos = []
    
    for arquivo in RELACIONAMENTOS_DIR.glob('*.md'):
        if arquivo.name not in ARQUIVOS_SISTEMA:
            arquivos.append(arquivo)
    
    return sorted(arquivos, key=lambda x: x.name)


def identificar_categoria_automatica(nome_arquivo):
    """Tenta identificar automaticamente a categoria baseada no nome."""
    nome_lower = nome_arquivo.lower()
    
    # Família
    familia_keywords = ['tio', 'tia', 'primo', 'prima', 'pai', 'mãe', 'mamãe', 
                       'avô', 'avó', 'irmã', 'irmão', 'filho', 'filha', 
                       'sobrinho', 'sobrinha', 'cunhado', 'cunhada']
    
    # Profissional
    prof_keywords = ['hotmart', 'porto', 'eqi', 'advogado', 'dr', 'drª', 
                    'prof', 'gerente', 'aws', 'meta', 'mongo', 'tcs',
                    'fornax', 'intera', 'praticci', 'roboteens', 'sesc']
    
    for keyword in familia_keywords:
        if keyword in nome_lower:
            return '1'  # Família
    
    for keyword in prof_keywords:
        if keyword in nome_lower:
            return '3'  # Profissional
    
    return None  # Não identificado


def mover_arquivo(arquivo, pasta_destino):
    """Move arquivo para a pasta de destino."""
    try:
        destino = pasta_destino / arquivo.name
        
        if destino.exists():
            print(f"   ⚠️  Arquivo já existe no destino: {destino.name}")
            return False
        
        shutil.move(str(arquivo), str(destino))
        return True
    except Exception as e:
        print(f"   ❌ Erro ao mover arquivo: {e}")
        return False


def organizar_interativo():
    """Modo interativo - pergunta para cada arquivo."""
    arquivos = listar_arquivos_para_organizar()
    
    if not arquivos:
        print("\n✅ Nenhum arquivo para organizar!")
        return
    
    print("\n" + "="*60)
    print("📁 ORGANIZAÇÃO INTERATIVA DE RELACIONAMENTOS")
    print("="*60)
    print(f"\n📊 {len(arquivos)} arquivos para organizar\n")
    print("Opções:")
    print("  1 - Família")
    print("  2 - Amigos")
    print("  3 - Profissional")
    print("  4 - Conhecidos")
    print("  S - Pular este arquivo")
    print("  T - Classificar todos restantes como mesmo tipo")
    print("  Q - Sair")
    print()
    
    movidos = {'Família': 0, 'Amigos': 0, 'Profissional': 0, 'Conhecidos': 0}
    pulados = 0
    classificacao_massa = None
    
    for i, arquivo in enumerate(arquivos, 1):
        if classificacao_massa:
            escolha = classificacao_massa
        else:
            # Tentar identificar automaticamente
            sugestao = identificar_categoria_automatica(arquivo.name)
            sugestao_texto = f" (Sugestão: {PASTAS[sugestao][0]})" if sugestao else ""
            
            print(f"\n[{i}/{len(arquivos)}] {arquivo.name}{sugestao_texto}")
            escolha = input("Mover para (1/2/3/4/S/T/Q): ").strip().upper()
        
        if escolha == 'Q':
            print("\n🛑 Organização interrompida pelo usuário")
            break
        
        elif escolha == 'S':
            pulados += 1
            continue
        
        elif escolha == 'T':
            print("\nClassificar todos restantes como:")
            print("  1 - Família")
            print("  2 - Amigos")
            print("  3 - Profissional")
            print("  4 - Conhecidos")
            tipo_massa = input("Escolha: ").strip()
            
            if tipo_massa in PASTAS:
                classificacao_massa = tipo_massa
                escolha = tipo_massa
                print(f"✅ Todos restantes serão movidos para: {PASTAS[tipo_massa][0]}")
            else:
                print("❌ Opção inválida, pulando arquivo")
                pulados += 1
                continue
        
        if escolha in PASTAS:
            nome_pasta, pasta_destino = PASTAS[escolha]
            if mover_arquivo(arquivo, pasta_destino):
                movidos[nome_pasta] += 1
                print(f"   ✅ Movido para {nome_pasta}/")
        else:
            print("   ⚠️  Opção inválida, pulando")
            pulados += 1
    
    # Resumo
    print("\n" + "="*60)
    print("✅ ORGANIZAÇÃO CONCLUÍDA!")
    print("="*60)
    print("\n📊 Resumo:")
    for pasta, count in movidos.items():
        if count > 0:
            print(f"  📂 {pasta}: {count} arquivos")
    print(f"  ⏭️  Pulados: {pulados} arquivos")
    print()


def organizar_automatico():
    """Modo automático - usa identificação automática."""
    arquivos = listar_arquivos_para_organizar()
    
    if not arquivos:
        print("\n✅ Nenhum arquivo para organizar!")
        return
    
    print("\n" + "="*60)
    print("🤖 ORGANIZAÇÃO AUTOMÁTICA DE RELACIONAMENTOS")
    print("="*60)
    print(f"\n📊 {len(arquivos)} arquivos para organizar\n")
    print("⚠️  Arquivos não identificados irão para 'Conhecidos'\n")
    
    confirmar = input("Continuar? (s/n): ").strip().lower()
    if confirmar != 's':
        print("❌ Organização cancelada")
        return
    
    movidos = {'Família': 0, 'Amigos': 0, 'Profissional': 0, 'Conhecidos': 0}
    
    for arquivo in arquivos:
        categoria = identificar_categoria_automatica(arquivo.name)
        
        # Se não identificou, vai para Conhecidos
        if not categoria:
            categoria = '4'
        
        nome_pasta, pasta_destino = PASTAS[categoria]
        
        if mover_arquivo(arquivo, pasta_destino):
            movidos[nome_pasta] += 1
            print(f"✅ {arquivo.name} → {nome_pasta}/")
    
    # Resumo
    print("\n" + "="*60)
    print("✅ ORGANIZAÇÃO CONCLUÍDA!")
    print("="*60)
    print("\n📊 Resumo:")
    for pasta, count in movidos.items():
        if count > 0:
            print(f"  📂 {pasta}: {count} arquivos")
    print()


def listar_arquivos_por_categoria():
    """Lista arquivos agrupados por categoria sugerida."""
    arquivos = listar_arquivos_para_organizar()
    
    if not arquivos:
        print("\n✅ Nenhum arquivo para organizar!")
        return
    
    print("\n" + "="*60)
    print("📋 PRÉVIA DE ORGANIZAÇÃO")
    print("="*60)
    
    categorias = {
        'Família': [],
        'Profissional': [],
        'Não Identificado': []
    }
    
    for arquivo in arquivos:
        categoria = identificar_categoria_automatica(arquivo.name)
        
        if categoria == '1':
            categorias['Família'].append(arquivo.name)
        elif categoria == '3':
            categorias['Profissional'].append(arquivo.name)
        else:
            categorias['Não Identificado'].append(arquivo.name)
    
    for categoria, lista in categorias.items():
        if lista:
            print(f"\n📂 {categoria} ({len(lista)} arquivos):")
            for nome in sorted(lista):
                print(f"  - {nome}")
    
    print("\n" + "="*60)
    print(f"Total: {len(arquivos)} arquivos")
    print("="*60 + "\n")


def menu_principal():
    """Menu principal."""
    while True:
        print("\n" + "="*60)
        print("📁 ORGANIZADOR DE RELACIONAMENTOS")
        print("="*60)
        print("\nEscolha uma opção:")
        print("1. Organizar interativamente (recomendado)")
        print("2. Organizar automaticamente")
        print("3. Ver prévia de organização")
        print("4. Contar arquivos por pasta")
        print("5. Sair")
        print()
        
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            organizar_interativo()
        
        elif opcao == '2':
            organizar_automatico()
        
        elif opcao == '3':
            listar_arquivos_por_categoria()
        
        elif opcao == '4':
            print("\n📊 Arquivos por pasta:")
            for nome, (_, pasta) in PASTAS.items():
                count = len(list(pasta.glob('*.md')))
                # Excluir arquivos especiais
                if nome == '1':  # Família
                    especiais = ['README.md', 'Árvore Genealógica.md']
                    count -= sum(1 for e in especiais if (pasta / e).exists())
                print(f"  📂 {PASTAS[nome][0]}: {count} arquivos")
            
            raiz = len(listar_arquivos_para_organizar())
            print(f"  📄 Raiz (para organizar): {raiz} arquivos")
        
        elif opcao == '5':
            print("\n👋 Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
