#!/usr/bin/env python3
"""
Script para gerar relatórios e lembretes de aniversários
a partir dos arquivos Markdown de relacionamentos.
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

RELACIONAMENTOS_DIR = Path(__file__).parent.parent


def extrair_info_pessoa(arquivo_md):
    """Extrai informações de um arquivo MD de pessoa."""
    try:
        with open(arquivo_md, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Extrair nome (primeira linha com #)
        nome_match = re.search(r'^#\s+(.+)$', conteudo, re.MULTILINE)
        nome = nome_match.group(1) if nome_match else arquivo_md.stem
        
        # Extrair data de nascimento
        data_nasc_match = re.search(r'\*\*Data de Nascimento:\*\*\s*(\d{2}/\d{2}/\d{4})', conteudo)
        data_nascimento = data_nasc_match.group(1) if data_nasc_match else None
        
        # Extrair tipo de relacionamento
        tipo_match = re.search(r'\*\*Tipo:\*\*\s*(.+)$', conteudo, re.MULTILINE)
        tipo = tipo_match.group(1).strip() if tipo_match else "Desconhecido"
        
        # Extrair Instagram
        insta_match = re.search(r'\*\*Instagram:\*\*\s*(@\w+)', conteudo)
        instagram = insta_match.group(1) if insta_match else ""
        
        return {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'tipo': tipo,
            'instagram': instagram,
            'arquivo': arquivo_md.name
        }
    except Exception as e:
        print(f"Erro ao processar {arquivo_md}: {e}")
        return None


def listar_todas_pessoas():
    """Lista todas as pessoas cadastradas."""
    pessoas = []
    
    for arquivo in RELACIONAMENTOS_DIR.glob("*.md"):
        # Ignorar arquivos especiais
        if arquivo.name.startswith('_') or arquivo.name.startswith('Lista') or \
           arquivo.name in ['Relacionamentos.md', 'Calendário de Aniversários.md']:
            continue
        
        info = extrair_info_pessoa(arquivo)
        if info:
            pessoas.append(info)
    
    return pessoas


def aniversarios_proximos(dias=30):
    """Retorna aniversários nos próximos X dias."""
    pessoas = listar_todas_pessoas()
    hoje = datetime.now()
    aniversariantes = []
    
    for pessoa in pessoas:
        if not pessoa['data_nascimento']:
            continue
        
        try:
            # Parsear data
            dia, mes, ano = map(int, pessoa['data_nascimento'].split('/'))
            
            # Criar data do aniversário neste ano
            aniversario_este_ano = datetime(hoje.year, mes, dia)
            
            # Se já passou, considerar ano que vem
            if aniversario_este_ano < hoje:
                aniversario_este_ano = datetime(hoje.year + 1, mes, dia)
            
            # Calcular dias até o aniversário
            dias_ate = (aniversario_este_ano - hoje).days
            
            if 0 <= dias_ate <= dias:
                idade = hoje.year - ano
                if aniversario_este_ano.year > hoje.year:
                    idade += 1
                
                aniversariantes.append({
                    **pessoa,
                    'dias_ate': dias_ate,
                    'idade': idade,
                    'data_aniversario': aniversario_este_ano
                })
        
        except Exception as e:
            print(f"Erro ao processar data de {pessoa['nome']}: {e}")
    
    # Ordenar por proximidade
    aniversariantes.sort(key=lambda x: x['dias_ate'])
    
    return aniversariantes


def gerar_relatorio_aniversarios(dias=30):
    """Gera relatório de aniversários próximos."""
    aniversariantes = aniversarios_proximos(dias)
    
    if not aniversariantes:
        return "Nenhum aniversário nos próximos {} dias.".format(dias)
    
    relatorio = f"# 🎂 Aniversários nos Próximos {dias} Dias\n\n"
    relatorio += f"**Gerado em:** {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n\n"
    
    for pessoa in aniversariantes:
        emoji = "🎉" if pessoa['dias_ate'] == 0 else "📅"
        dias_texto = "HOJE!" if pessoa['dias_ate'] == 0 else f"em {pessoa['dias_ate']} dias"
        
        relatorio += f"{emoji} **[[{pessoa['nome']}]]** - {dias_texto}\n"
        relatorio += f"   - Data: {pessoa['data_aniversario'].strftime('%d/%m/%Y')}\n"
        relatorio += f"   - Idade: {pessoa['idade']} anos\n"
        relatorio += f"   - Tipo: {pessoa['tipo']}\n"
        if pessoa['instagram']:
            relatorio += f"   - Instagram: {pessoa['instagram']}\n"
        relatorio += "\n"
    
    return relatorio


def estatisticas_relacionamentos():
    """Gera estatísticas sobre relacionamentos."""
    pessoas = listar_todas_pessoas()
    
    # Contar por tipo
    por_tipo = defaultdict(int)
    com_aniversario = 0
    com_instagram = 0
    
    for pessoa in pessoas:
        por_tipo[pessoa['tipo']] += 1
        if pessoa['data_nascimento']:
            com_aniversario += 1
        if pessoa['instagram']:
            com_instagram += 1
    
    relatorio = "# 📊 Estatísticas de Relacionamentos\n\n"
    relatorio += f"**Gerado em:** {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n\n"
    relatorio += f"## Total de Pessoas: {len(pessoas)}\n\n"
    
    relatorio += "## Por Tipo de Relacionamento\n"
    for tipo, count in sorted(por_tipo.items(), key=lambda x: x[1], reverse=True):
        relatorio += f"- **{tipo}:** {count} pessoas\n"
    
    relatorio += f"\n## Informações Cadastradas\n"
    relatorio += f"- Com data de nascimento: {com_aniversario} ({com_aniversario/len(pessoas)*100:.1f}%)\n"
    relatorio += f"- Com Instagram: {com_instagram} ({com_instagram/len(pessoas)*100:.1f}%)\n"
    
    return relatorio


def gerar_calendario_anual():
    """Gera calendário de aniversários para o ano todo."""
    pessoas = listar_todas_pessoas()
    hoje = datetime.now()
    
    # Organizar por mês
    por_mes = defaultdict(list)
    
    for pessoa in pessoas:
        if not pessoa['data_nascimento']:
            continue
        
        try:
            dia, mes, ano = map(int, pessoa['data_nascimento'].split('/'))
            por_mes[mes].append({
                'dia': dia,
                'nome': pessoa['nome'],
                'tipo': pessoa['tipo']
            })
        except:
            continue
    
    # Gerar calendário
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    calendario = f"# 📅 Calendário de Aniversários {hoje.year}\n\n"
    calendario += f"**Gerado em:** {hoje.strftime('%d/%m/%Y às %H:%M')}\n\n"
    
    for mes_num, mes_nome in enumerate(meses, 1):
        calendario += f"## {mes_nome}\n"
        
        if mes_num in por_mes:
            # Ordenar por dia
            aniversariantes = sorted(por_mes[mes_num], key=lambda x: x['dia'])
            for pessoa in aniversariantes:
                calendario += f"- [ ] {pessoa['dia']:02d} - [[{pessoa['nome']}]] - {pessoa['tipo']}\n"
        else:
            calendario += "- Nenhum aniversário\n"
        
        calendario += "\n"
    
    return calendario


def menu_principal():
    """Menu interativo."""
    print("=" * 60)
    print("📊 RELATÓRIOS DE RELACIONAMENTOS")
    print("=" * 60)
    print("\nEscolha uma opção:")
    print("1. Aniversários próximos (30 dias)")
    print("2. Aniversários próximos (7 dias)")
    print("3. Estatísticas gerais")
    print("4. Calendário anual completo")
    print("5. Listar todas as pessoas")
    print("6. Gerar todos os relatórios")
    print("7. Sair")
    print()
    
    opcao = input("Opção: ").strip()
    
    if opcao == "1":
        print("\n" + gerar_relatorio_aniversarios(30))
        
        salvar = input("\nSalvar relatório? (s/n): ").strip().lower()
        if salvar == 's':
            arquivo = RELACIONAMENTOS_DIR / "Relatório_Aniversários_30dias.md"
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(gerar_relatorio_aniversarios(30))
            print(f"✅ Salvo em: {arquivo.name}")
    
    elif opcao == "2":
        print("\n" + gerar_relatorio_aniversarios(7))
        
        salvar = input("\nSalvar relatório? (s/n): ").strip().lower()
        if salvar == 's':
            arquivo = RELACIONAMENTOS_DIR / "Relatório_Aniversários_7dias.md"
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(gerar_relatorio_aniversarios(7))
            print(f"✅ Salvo em: {arquivo.name}")
    
    elif opcao == "3":
        print("\n" + estatisticas_relacionamentos())
        
        salvar = input("\nSalvar relatório? (s/n): ").strip().lower()
        if salvar == 's':
            arquivo = RELACIONAMENTOS_DIR / "Estatísticas_Relacionamentos.md"
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(estatisticas_relacionamentos())
            print(f"✅ Salvo em: {arquivo.name}")
    
    elif opcao == "4":
        print("\n" + gerar_calendario_anual())
        
        salvar = input("\nSalvar calendário? (s/n): ").strip().lower()
        if salvar == 's':
            arquivo = RELACIONAMENTOS_DIR / "Calendário de Aniversários.md"
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(gerar_calendario_anual())
            print(f"✅ Salvo em: {arquivo.name}")
    
    elif opcao == "5":
        pessoas = listar_todas_pessoas()
        print(f"\n📋 Total: {len(pessoas)} pessoas\n")
        for pessoa in sorted(pessoas, key=lambda x: x['nome']):
            print(f"- {pessoa['nome']} ({pessoa['tipo']})")
    
    elif opcao == "6":
        print("\n🔄 Gerando todos os relatórios...")
        
        # Aniversários 7 dias
        with open(RELACIONAMENTOS_DIR / "Relatório_Aniversários_7dias.md", 'w', encoding='utf-8') as f:
            f.write(gerar_relatorio_aniversarios(7))
        print("✅ Relatório_Aniversários_7dias.md")
        
        # Aniversários 30 dias
        with open(RELACIONAMENTOS_DIR / "Relatório_Aniversários_30dias.md", 'w', encoding='utf-8') as f:
            f.write(gerar_relatorio_aniversarios(30))
        print("✅ Relatório_Aniversários_30dias.md")
        
        # Estatísticas
        with open(RELACIONAMENTOS_DIR / "Estatísticas_Relacionamentos.md", 'w', encoding='utf-8') as f:
            f.write(estatisticas_relacionamentos())
        print("✅ Estatísticas_Relacionamentos.md")
        
        # Calendário
        with open(RELACIONAMENTOS_DIR / "Calendário de Aniversários.md", 'w', encoding='utf-8') as f:
            f.write(gerar_calendario_anual())
        print("✅ Calendário de Aniversários.md")
        
        print("\n✅ Todos os relatórios foram gerados!")
    
    elif opcao == "7":
        print("\n👋 Até logo!")
        return
    
    else:
        print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
