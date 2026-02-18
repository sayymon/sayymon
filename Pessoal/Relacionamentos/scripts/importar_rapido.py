#!/usr/bin/env python3
"""
Script simplificado para importação rápida do Google Contacts.
Organiza contatos em pastas: Família, Amigos, Profissional, Conhecidos.
"""

import csv
import re
from pathlib import Path
from datetime import datetime

RELACIONAMENTOS_DIR = Path(__file__).parent.parent

# Pastas por tipo de relacionamento
PASTAS = {
    'Família': RELACIONAMENTOS_DIR / 'Família',
    'Amigo': RELACIONAMENTOS_DIR / 'Amigos',
    'Profissional': RELACIONAMENTOS_DIR / 'Profissional',
    'Conhecido': RELACIONAMENTOS_DIR / 'Conhecidos'
}


def criar_arquivo_pessoa(nome, data_nascimento="", tipo_relacionamento="", 
                         telefone="", email="", notas=""):
    """Cria um arquivo MD para uma pessoa na pasta apropriada."""
    
    # Determinar pasta baseada no tipo
    pasta = PASTAS.get(tipo_relacionamento, RELACIONAMENTOS_DIR / 'Conhecidos')
    
    # Sanitizar nome para nome de arquivo
    nome_arquivo = nome.replace(" ", "_").replace("/", "-").replace(":", "")
    # Remover caracteres especiais adicionais
    nome_arquivo = re.sub(r'[<>:"|?*]', '', nome_arquivo)
    arquivo_path = pasta / f"{nome_arquivo}.md"
    
    if arquivo_path.exists():
        return False
    
    # Calcular idade se tiver data de nascimento
    idade = ""
    aniversario = ""
    if data_nascimento:
        try:
            # Tentar vários formatos de data
            for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"]:
                try:
                    dt = datetime.strptime(data_nascimento, fmt)
                    hoje = datetime.now()
                    idade = hoje.year - dt.year - ((hoje.month, hoje.day) < (dt.month, dt.day))
                    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
                    aniversario = f"{dt.day} de {meses[dt.month-1]}"
                    data_nascimento = dt.strftime("%d/%m/%Y")
                    break
                except:
                    continue
        except:
            pass
    
    conteudo = f"""# {nome}

## Informações Básicas
- **Data de Nascimento:** {data_nascimento}
- **Idade:** {idade} anos
- **Aniversário:** {aniversario}

## Relacionamento
- **Tipo:** {tipo_relacionamento or "Conhecido"}
- **Parentesco/Vínculo:** 
- **Como nos conhecemos:** 
- **Tempo de conhecimento:** 

## Contato
- **Telefone:** {telefone}
- **Email:** {email}
- **Instagram:** 
- **Facebook:** 
- **Outros:** 

## Interesses e Características
### Coisas em Comum
- 

### Hobbies e Interesses
- 

### Características Marcantes
- 

## Histórico de Interações
### Últimos Encontros
- **[Data]:** [Descrição do encontro]

### Conversas Importantes
- **[Data]:** [Assunto/Nota]

### Presentes Dados/Recebidos
- **[Data]:** [Descrição]

## Lembretes
- [ ] Enviar mensagem de aniversário
- [ ] Marcar encontro

## Notas Adicionais
{notas}

---
**Tags:** #relacionamento #{(tipo_relacionamento or "conhecido").lower()}
**Criado em:** {datetime.now().strftime("%d/%m/%Y")}
**Última atualização:** {datetime.now().strftime("%d/%m/%Y")}
"""
    
    with open(arquivo_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    return True


def importar_google_csv(arquivo_csv):
    """Importa contatos do Google CSV."""
    print("\n" + "="*60)
    print("📇 IMPORTANDO DO GOOGLE CONTACTS")
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
                emoji_pattern = r'^[\U0001F300-\U0001F9FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U00002600-\U000027BF\U0001F1E0-\U0001F1FF]+'
                first = re.sub(emoji_pattern, '', first).strip()
                
                nome_parts = [p for p in [first, middle, last] if p]
                nome = ' '.join(nome_parts)
                
                if not nome:
                    continue
                
                telefone = row.get('Phone 1 - Value', '').strip()
                if not telefone:
                    telefone = row.get('Phone 2 - Value', '').strip()
                
                email = row.get('E-mail 1 - Value', '').strip()
                if not email:
                    email = row.get('E-mail 2 - Value', '').strip()
                
                aniversario = row.get('Birthday', '').strip()
                notas = row.get('Notes', '').strip()
                organizacao = row.get('Organization Name', '').strip()
                
                # Determinar tipo
                tipo = "Conhecido"
                if organizacao:
                    tipo = "Profissional"
                
                contatos.append({
                    'nome': nome,
                    'telefone': telefone,
                    'email': email,
                    'data_nascimento': aniversario,
                    'notas': notas,
                    'tipo': tipo
                })
        
        print(f"✅ {len(contatos)} contatos encontrados!\n")
        return contatos
        
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_csv}")
        return []
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {e}")
        import traceback
        traceback.print_exc()
        return []


def main():
    print("=" * 60)
    print("📱 IMPORTAÇÃO RÁPIDA - GOOGLE CONTACTS")
    print("=" * 60)
    print("\n⚡ Este script importa contatos organizados em pastas:")
    print("   📂 Família/ - Familiares")
    print("   📂 Amigos/ - Amigos")
    print("   📂 Profissional/ - Colegas de trabalho")
    print("   📂 Conhecidos/ - Outros contatos")
    print("\n💡 Contatos com organização = Profissional")
    print("   Outros = Conhecidos (você pode editar depois)\n")
    
    arquivo = input("Caminho do arquivo CSV: ").strip()
    
    if not arquivo:
        print("❌ Caminho vazio!")
        return
    
    contatos = importar_google_csv(arquivo)
    
    if not contatos:
        print("\n❌ Nenhum contato para importar!")
        return
    
    print(f"\n📋 {len(contatos)} contatos prontos para importar")
    print("\nEstatísticas:")
    com_telefone = sum(1 for c in contatos if c['telefone'])
    com_email = sum(1 for c in contatos if c['email'])
    com_aniversario = sum(1 for c in contatos if c['data_nascimento'])
    
    print(f"  - Com telefone: {com_telefone}")
    print(f"  - Com email: {com_email}")
    print(f"  - Com aniversário: {com_aniversario}")
    
    confirmar = input("\n🚀 Criar arquivos para todos? (s/n): ").strip().lower()
    
    if confirmar != 's':
        print("\n❌ Importação cancelada!")
        return
    
    print("\n🔄 Criando arquivos...")
    criados = 0
    pulados = 0
    
    for i, contato in enumerate(contatos, 1):
        if i % 50 == 0:
            print(f"   Processando {i}/{len(contatos)}...")
        
        if criar_arquivo_pessoa(
            nome=contato['nome'],
            telefone=contato['telefone'],
            email=contato['email'],
            data_nascimento=contato['data_nascimento'],
            tipo_relacionamento=contato['tipo'],
            notas=contato['notas']
        ):
            criados += 1
        else:
            pulados += 1
    
    print("\n" + "="*60)
    print("✅ IMPORTAÇÃO CONCLUÍDA!")
    print("="*60)
    print(f"\n📊 Resultados:")
    print(f"  - Criados: {criados} arquivos")
    print(f"  - Pulados: {pulados} (já existiam)")
    print(f"  - Total: {len(contatos)} contatos processados")
    print("\n💡 Próximos passos:")
    print("  1. Revise os arquivos criados")
    print("  2. Edite os tipos de relacionamento")
    print("  3. Complete informações faltantes")
    print("  4. Execute gerar_relatorios.py para ver aniversários")
    print()


if __name__ == "__main__":
    main()
