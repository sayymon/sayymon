#!/usr/bin/env python3
"""
Script para importar contatos do Google Contacts.
Suporta CSV e vCard (VCF) exportados do Google.
"""

import csv
import json
import re
from pathlib import Path
from datetime import datetime

RELACIONAMENTOS_DIR = Path(__file__).parent.parent


def criar_arquivo_pessoa(nome, data_nascimento="", tipo_relacionamento="", 
                         como_conheceu="", instagram="", facebook="", 
                         telefone="", email="", notas="", interesses=None):
    """Cria um arquivo MD para uma pessoa."""
    if interesses is None:
        interesses = []
    
    # Sanitizar nome para nome de arquivo
    nome_arquivo = nome.replace(" ", "_").replace("/", "-").replace(":", "")
    arquivo_path = RELACIONAMENTOS_DIR / f"{nome_arquivo}.md"
    
    if arquivo_path.exists():
        print(f"⚠️  Arquivo já existe: {nome_arquivo}.md")
        return False
    
    # Calcular idade se tiver data de nascimento
    idade = ""
    aniversario = ""
    if data_nascimento:
        try:
            # Tentar vários formatos de data
            for fmt in ["%d/%m/%Y", "%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]:
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
    
    # Extrair Instagram e Facebook de notas se existir
    if notas:
        insta_match = re.search(r'@(\w+)', notas)
        if insta_match and not instagram:
            instagram = f"@{insta_match.group(1)}"
    
    conteudo = f"""# {nome}

## Informações Básicas
- **Data de Nascimento:** {data_nascimento}
- **Idade:** {idade} anos
- **Aniversário:** {aniversario}

## Relacionamento
- **Tipo:** {tipo_relacionamento or "Conhecido"}
- **Parentesco/Vínculo:** 
- **Como nos conhecemos:** {como_conheceu}
- **Tempo de conhecimento:** 

## Contato
- **Telefone:** {telefone}
- **Email:** {email}
- **Instagram:** {instagram}
- **Facebook:** {facebook}
- **Outros:** 

## Interesses e Características
### Coisas em Comum
{chr(10).join([f"- {i}" for i in interesses]) if interesses else "- "}

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
    
    print(f"✅ Criado: {nome_arquivo}.md")
    return True


def importar_google_csv(arquivo_csv):
    """
    Importa contatos de um CSV exportado do Google Contacts.
    
    Como exportar do Google Contacts:
    1. Acesse: https://contacts.google.com/
    2. Clique em "Exportar" no menu lateral
    3. Escolha "Google CSV"
    4. Baixe o arquivo
    """
    print("\n" + "="*60)
    print("📇 IMPORTANDO DO GOOGLE CONTACTS (CSV)")
    print("="*60 + "\n")
    
    try:
        contatos = []
        
        # Tentar diferentes encodings
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'iso-8859-1']
        
        arquivo_aberto = None
        for enc in encodings:
            try:
                arquivo_aberto = open(arquivo_csv, 'r', encoding=enc)
                arquivo_aberto.read()
                arquivo_aberto.seek(0)
                break
            except UnicodeDecodeError:
                if arquivo_aberto:
                    arquivo_aberto.close()
                continue
        
        if not arquivo_aberto:
            print("❌ Erro ao ler arquivo com encoding UTF-8")
            return []
        
        reader = csv.DictReader(arquivo_aberto)
        
        for row in reader:
            # Extrair nome - tentar vários formatos
            nome = row.get('Name', '').strip()
            
            # Formato Google CSV novo (First Name, Last Name)
            if not nome:
                first = row.get('First Name', '').strip()
                middle = row.get('Middle Name', '').strip()
                last = row.get('Last Name', '').strip()
                
                # Remover emojis do início do nome (padrão comum no Google Contacts)
                import re
                emoji_pattern = r'^[\U0001F300-\U0001F9FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U00002600-\U000027BF\U0001F1E0-\U0001F1FF]+'
                first = re.sub(emoji_pattern, '', first).strip()
                
                nome_parts = [p for p in [first, middle, last] if p]
                nome = ' '.join(nome_parts)
            
            # Formato Google CSV antigo (Given Name, Family Name)
            if not nome:
                given = row.get('Given Name', '').strip()
                family = row.get('Family Name', '').strip()
                nome = f"{given} {family}".strip()
            
            if not nome:
                continue
            
            # Extrair outros campos
            telefone = row.get('Phone 1 - Value', '').strip()
            if not telefone:
                telefone = row.get('Phone 2 - Value', '').strip()
            
            email = row.get('E-mail 1 - Value', '').strip()
            if not email:
                email = row.get('E-mail 2 - Value', '').strip()
            
            aniversario = row.get('Birthday', '').strip()
            notas = row.get('Notes', '').strip()
            
            organizacao = row.get('Organization Name', '').strip()
            if not organizacao:
                organizacao = row.get('Organization 1 - Name', '').strip()
            
            # Determinar tipo baseado em organização
            tipo = "Conhecido"
            if organizacao:
                tipo = "Profissional"
            
            contatos.append({
                'nome': nome,
                'telefone': telefone,
                'email': email,
                'data_nascimento': aniversario,
                'notas': notas,
                'tipo': tipo,
                'como_conheceu': f"Organização: {organizacao}" if organizacao else ""
            })
        
        arquivo_aberto.close()
        
        print(f"✅ {len(contatos)} contatos encontrados no CSV\n")
        return contatos
        
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_csv}")
        return []
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {e}")
        return []


def importar_vcf(arquivo_vcf):
    """
    Importa contatos de um arquivo vCard (VCF).
    
    Como exportar vCard:
    1. Google Contacts: Exportar > vCard
    2. iPhone: Contatos > Exportar vCard
    3. Android: Contatos > Exportar
    """
    print("\n" + "="*60)
    print("📇 IMPORTANDO VCARD (VCF)")
    print("="*60 + "\n")
    
    try:
        contatos = []
        
        with open(arquivo_vcf, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Dividir por vCards individuais
        vcards = conteudo.split('BEGIN:VCARD')
        
        for vcard in vcards:
            if not vcard.strip():
                continue
            
            # Extrair campos
            nome = ""
            telefone = ""
            email = ""
            aniversario = ""
            notas = ""
            
            # Nome
            fn_match = re.search(r'FN:(.+)', vcard)
            if fn_match:
                nome = fn_match.group(1).strip()
            
            # Telefone
            tel_match = re.search(r'TEL[^:]*:(.+)', vcard)
            if tel_match:
                telefone = tel_match.group(1).strip()
            
            # Email
            email_match = re.search(r'EMAIL[^:]*:(.+)', vcard)
            if email_match:
                email = email_match.group(1).strip()
            
            # Aniversário
            bday_match = re.search(r'BDAY:(.+)', vcard)
            if bday_match:
                aniversario = bday_match.group(1).strip()
            
            # Notas
            note_match = re.search(r'NOTE:(.+)', vcard)
            if note_match:
                notas = note_match.group(1).strip()
            
            if nome:
                contatos.append({
                    'nome': nome,
                    'telefone': telefone,
                    'email': email,
                    'data_nascimento': aniversario,
                    'notas': notas,
                    'tipo': 'Conhecido'
                })
        
        print(f"✅ {len(contatos)} contatos encontrados no VCF\n")
        return contatos
        
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_vcf}")
        return []
    except Exception as e:
        print(f"❌ Erro ao ler VCF: {e}")
        return []


def classificar_contatos_interativo(contatos):
    """
    Permite classificar contatos interativamente.
    """
    print("\n" + "="*60)
    print("🏷️  CLASSIFICAÇÃO DE CONTATOS")
    print("="*60)
    print("\nVocê pode classificar cada contato como:")
    print("1. Família")
    print("2. Amigo")
    print("3. Profissional")
    print("4. Conhecido")
    print("S. Pular (manter como está)")
    print("T. Classificar todos restantes como mesmo tipo")
    print("\n")
    
    classificacao_em_massa = None
    
    for i, contato in enumerate(contatos, 1):
        if classificacao_em_massa:
            contato['tipo'] = classificacao_em_massa
            continue
        
        print(f"\n[{i}/{len(contatos)}] {contato['nome']}")
        if contato.get('telefone'):
            print(f"    Tel: {contato['telefone']}")
        if contato.get('email'):
            print(f"    Email: {contato['email']}")
        
        escolha = input("Tipo (1/2/3/4/S/T): ").strip().upper()
        
        if escolha == '1':
            contato['tipo'] = 'Família'
        elif escolha == '2':
            contato['tipo'] = 'Amigo'
        elif escolha == '3':
            contato['tipo'] = 'Profissional'
        elif escolha == '4':
            contato['tipo'] = 'Conhecido'
        elif escolha == 'T':
            print("\nClassificar todos restantes como:")
            print("1. Família")
            print("2. Amigo")
            print("3. Profissional")
            print("4. Conhecido")
            tipo_massa = input("Escolha: ").strip()
            
            tipos = {'1': 'Família', '2': 'Amigo', '3': 'Profissional', '4': 'Conhecido'}
            classificacao_em_massa = tipos.get(tipo_massa, 'Conhecido')
            contato['tipo'] = classificacao_em_massa
            print(f"✅ Todos restantes serão: {classificacao_em_massa}")
        elif escolha == 'S':
            pass  # Manter como está
        else:
            print("⚠️  Opção inválida, mantendo como Conhecido")
    
    return contatos


def exportar_para_json(contatos, arquivo_saida):
    """Exporta contatos para JSON para revisão."""
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(contatos, f, ensure_ascii=False, indent=2)
        print(f"✅ Contatos exportados para: {arquivo_saida}")
        return True
    except Exception as e:
        print(f"❌ Erro ao exportar JSON: {e}")
        return False


def menu_principal():
    """Menu interativo."""
    print("=" * 60)
    print("📱 IMPORTADOR DO GOOGLE CONTACTS")
    print("=" * 60)
    print("\nEscolha uma opção:")
    print("1. Importar de Google CSV")
    print("2. Importar de vCard (VCF)")
    print("3. Como exportar do Google Contacts")
    print("4. Sair")
    print()
    
    opcao = input("Opção: ").strip()
    
    if opcao == "1":
        arquivo = input("\nCaminho do arquivo CSV: ").strip()
        contatos = importar_google_csv(arquivo)
        
        if contatos:
            print(f"\n📋 {len(contatos)} contatos importados")
            
            classificar = input("\nDeseja classificar os contatos? (s/n): ").strip().lower()
            if classificar == 's':
                contatos = classificar_contatos_interativo(contatos)
            
            # Opção de exportar para JSON primeiro
            exportar = input("\nExportar para JSON para revisão? (s/n): ").strip().lower()
            if exportar == 's':
                arquivo_json = RELACIONAMENTOS_DIR / "scripts" / "contatos_google.json"
                if exportar_para_json(contatos, arquivo_json):
                    print(f"\n💡 Revise o arquivo {arquivo_json.name} e depois importe usando a opção 1 do menu principal")
                    return
            
            # Criar arquivos
            criar = input("\nCriar arquivos MD para todos? (s/n): ").strip().lower()
            if criar == 's':
                criados = 0
                for contato in contatos:
                    if criar_arquivo_pessoa(
                        nome=contato['nome'],
                        telefone=contato.get('telefone', ''),
                        email=contato.get('email', ''),
                        data_nascimento=contato.get('data_nascimento', ''),
                        tipo_relacionamento=contato.get('tipo', 'Conhecido'),
                        notas=contato.get('notas', ''),
                        como_conheceu=contato.get('como_conheceu', '')
                    ):
                        criados += 1
                
                print(f"\n✅ {criados} arquivos criados com sucesso!")
    
    elif opcao == "2":
        arquivo = input("\nCaminho do arquivo VCF: ").strip()
        contatos = importar_vcf(arquivo)
        
        if contatos:
            print(f"\n📋 {len(contatos)} contatos importados")
            
            classificar = input("\nDeseja classificar os contatos? (s/n): ").strip().lower()
            if classificar == 's':
                contatos = classificar_contatos_interativo(contatos)
            
            criar = input("\nCriar arquivos MD para todos? (s/n): ").strip().lower()
            if criar == 's':
                criados = 0
                for contato in contatos:
                    if criar_arquivo_pessoa(
                        nome=contato['nome'],
                        telefone=contato.get('telefone', ''),
                        email=contato.get('email', ''),
                        data_nascimento=contato.get('data_nascimento', ''),
                        tipo_relacionamento=contato.get('tipo', 'Conhecido'),
                        notas=contato.get('notas', '')
                    ):
                        criados += 1
                
                print(f"\n✅ {criados} arquivos criados com sucesso!")
    
    elif opcao == "3":
        print("\n" + "="*60)
        print("📚 COMO EXPORTAR DO GOOGLE CONTACTS")
        print("="*60)
        print("\n### Método 1: Google CSV (Recomendado)")
        print("1. Acesse: https://contacts.google.com/")
        print("2. No menu lateral esquerdo, clique em 'Exportar'")
        print("3. Selecione 'Contatos' ou grupo específico")
        print("4. Escolha formato: 'Google CSV'")
        print("5. Clique em 'Exportar'")
        print("6. Salve o arquivo e use neste script")
        print("\n### Método 2: vCard")
        print("1. Acesse: https://contacts.google.com/")
        print("2. No menu lateral esquerdo, clique em 'Exportar'")
        print("3. Selecione 'Contatos' ou grupo específico")
        print("4. Escolha formato: 'vCard (para contatos iOS)'")
        print("5. Clique em 'Exportar'")
        print("6. Salve o arquivo .vcf e use neste script")
        print("\n### Dica:")
        print("- Google CSV contém mais informações (aniversários, notas, etc.)")
        print("- vCard é mais universal e funciona com iPhone/Android")
        print("\n" + "="*60 + "\n")
    
    elif opcao == "4":
        print("\n👋 Até logo!")
        return
    
    else:
        print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
