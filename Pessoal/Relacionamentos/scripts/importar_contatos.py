#!/usr/bin/env python3
"""
Script para importar contatos do Instagram e Facebook
e criar arquivos Markdown para cada pessoa.

Requisitos:
- instaloader (para Instagram)
- facebook-sdk (para Facebook)

Instalação:
pip install instaloader facebook-sdk python-dotenv
"""

import os
import json
import ssl
import urllib3
from datetime import datetime
from pathlib import Path

# Desabilitar avisos de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Desabilitar verificação SSL (use com cuidado!)
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Configurações
RELACIONAMENTOS_DIR = Path(__file__).parent.parent
TEMPLATE_FILE = RELACIONAMENTOS_DIR / "_Template Pessoa.md"


def criar_arquivo_pessoa(nome, data_nascimento="", tipo_relacionamento="", 
                         como_conheceu="", instagram="", facebook="", 
                         interesses=None):
    """
    Cria um arquivo MD para uma pessoa baseado no template.
    """
    if interesses is None:
        interesses = []
    
    # Sanitizar nome para nome de arquivo
    nome_arquivo = nome.replace(" ", "_").replace("/", "-")
    arquivo_path = RELACIONAMENTOS_DIR / f"{nome_arquivo}.md"
    
    # Verificar se já existe
    if arquivo_path.exists():
        print(f"⚠️  Arquivo já existe: {nome_arquivo}.md")
        return False
    
    # Calcular idade se tiver data de nascimento
    idade = ""
    aniversario = ""
    if data_nascimento:
        try:
            dt = datetime.strptime(data_nascimento, "%d/%m/%Y")
            hoje = datetime.now()
            idade = hoje.year - dt.year - ((hoje.month, hoje.day) < (dt.month, dt.day))
            aniversario = f"{dt.day} de {dt.strftime('%B')}"
        except:
            pass
    
    # Criar conteúdo
    conteudo = f"""# {nome}

## Informações Básicas
- **Data de Nascimento:** {data_nascimento}
- **Idade:** {idade} anos
- **Aniversário:** {aniversario}

## Relacionamento
- **Tipo:** {tipo_relacionamento}
- **Parentesco/Vínculo:** 
- **Como nos conhecemos:** {como_conheceu}
- **Tempo de conhecimento:** 

## Contato
- **Telefone:** 
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
[Qualquer informação adicional relevante]

---
**Tags:** #relacionamento #{tipo_relacionamento.lower()}
**Criado em:** {datetime.now().strftime("%d/%m/%Y")}
**Última atualização:** {datetime.now().strftime("%d/%m/%Y")}
"""
    
    # Salvar arquivo
    with open(arquivo_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"✅ Criado: {nome_arquivo}.md")
    return True


def importar_instagram_seguidores(username):
    """
    Importa lista de seguidores do Instagram.
    
    NOTA: O Instagram tem restrições de API. Este método usa instaloader
    que pode requerer login e tem limitações de rate.
    """
    try:
        import instaloader
        
        L = instaloader.Instaloader()
        
        print(f"\n📱 Importando seguidores do Instagram de @{username}...")
        print("⚠️  Você pode precisar fazer login. O Instagram pode bloquear após muitas requisições.")
        
        # Descomentar para fazer login
        # L.login(username, input("Senha: "))
        
        profile = instaloader.Profile.from_username(L.context, username)
        
        seguidores = []
        for follower in profile.get_followers():
            seguidores.append({
                'nome': follower.full_name or follower.username,
                'instagram': f"@{follower.username}",
                'tipo': 'Conhecido'
            })
            
            # Limitar para evitar bloqueio
            if len(seguidores) >= 50:
                print("⚠️  Limitado a 50 seguidores para evitar bloqueio do Instagram")
                break
        
        return seguidores
        
    except ImportError:
        print("❌ Erro: instale o instaloader com: pip install instaloader")
        return []
    except Exception as e:
        print(f"❌ Erro ao importar do Instagram: {e}")
        return []


def importar_facebook_amigos(access_token):
    """
    Importa lista de amigos do Facebook.
    
    NOTA: A API do Facebook mudou e não permite mais listar todos os amigos.
    Você precisará de um access token e permissões específicas.
    """
    try:
        import facebook
        import requests
        
        print(f"\n👥 Importando amigos do Facebook...")
        print("⚠️  A API do Facebook tem restrições. Você precisa de um access token válido.")
        print("⚠️  Verificação SSL desabilitada - use apenas em ambiente de desenvolvimento!")
        
        # Criar sessão com SSL desabilitado
        session = requests.Session()
        session.verify = False
        
        # Criar GraphAPI com sessão customizada
        graph = facebook.GraphAPI(access_token, session=session)
        
        # Tentar obter informações do usuário primeiro
        try:
            me = graph.get_object('me', fields='id,name')
            print(f"✅ Conectado como: {me.get('name', 'Desconhecido')}")
        except Exception as e:
            print(f"⚠️  Erro ao obter informações do usuário: {e}")
        
        # Tentar obter amigos (pode não funcionar devido a restrições da API)
        try:
            amigos = graph.get_connections('me', 'friends')
            
            if not amigos.get('data'):
                print("⚠️  Nenhum amigo retornado. A API do Facebook não permite mais listar todos os amigos.")
                print("💡 Apenas amigos que também usam o mesmo app são retornados.")
                return []
            
            lista_amigos = []
            for amigo in amigos['data']:
                lista_amigos.append({
                    'nome': amigo['name'],
                    'facebook': amigo['name'],
                    'tipo': 'Amigo'
                })
            
            print(f"✅ {len(lista_amigos)} amigos encontrados")
            return lista_amigos
            
        except Exception as e:
            print(f"❌ Erro ao buscar amigos: {e}")
            print("💡 Dica: A API do Facebook mudou e não permite mais listar todos os amigos.")
            print("💡 Considere usar a opção de importação via JSON manual.")
            return []
        
    except ImportError:
        print("❌ Erro: instale as dependências com:")
        print("   pip install facebook-sdk requests urllib3")
        return []
    except Exception as e:
        print(f"❌ Erro ao importar do Facebook: {e}")
        return []


def importar_de_json(arquivo_json):
    """
    Importa contatos de um arquivo JSON.
    
    Formato esperado:
    [
        {
            "nome": "João Silva",
            "data_nascimento": "15/03/1990",
            "tipo": "Amigo",
            "como_conheceu": "Faculdade",
            "instagram": "@joaosilva",
            "facebook": "João Silva",
            "interesses": ["Tecnologia", "Música"]
        }
    ]
    """
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            contatos = json.load(f)
        
        print(f"\n📄 Importando {len(contatos)} contatos do arquivo JSON...")
        
        criados = 0
        for contato in contatos:
            if criar_arquivo_pessoa(
                nome=contato.get('nome', ''),
                data_nascimento=contato.get('data_nascimento', ''),
                tipo_relacionamento=contato.get('tipo', 'Conhecido'),
                como_conheceu=contato.get('como_conheceu', ''),
                instagram=contato.get('instagram', ''),
                facebook=contato.get('facebook', ''),
                interesses=contato.get('interesses', [])
            ):
                criados += 1
        
        print(f"\n✅ {criados} arquivos criados com sucesso!")
        return criados
        
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_json}")
        return 0
    except json.JSONDecodeError:
        print(f"❌ Erro ao ler JSON: arquivo inválido")
        return 0
    except Exception as e:
        print(f"❌ Erro: {e}")
        return 0


def menu_principal():
    """Menu interativo para escolher método de importação."""
    print("=" * 60)
    print("🤝 IMPORTADOR DE CONTATOS PARA OBSIDIAN")
    print("=" * 60)
    print("\nEscolha uma opção:")
    print("1. Importar de arquivo JSON")
    print("2. Importar seguidores do Instagram (experimental)")
    print("3. Importar amigos do Facebook (experimental)")
    print("4. Criar pessoa manualmente")
    print("5. Sair")
    print()
    
    opcao = input("Opção: ").strip()
    
    if opcao == "1":
        arquivo = input("Caminho do arquivo JSON: ").strip()
        importar_de_json(arquivo)
    
    elif opcao == "2":
        username = input("Seu username do Instagram: ").strip()
        seguidores = importar_instagram_seguidores(username)
        if seguidores:
            for seg in seguidores:
                criar_arquivo_pessoa(
                    nome=seg['nome'],
                    tipo_relacionamento=seg['tipo'],
                    instagram=seg['instagram']
                )
    
    elif opcao == "3":
        token = input("Access token do Facebook: ").strip()
        amigos = importar_facebook_amigos(token)
        if amigos:
            for amigo in amigos:
                criar_arquivo_pessoa(
                    nome=amigo['nome'],
                    tipo_relacionamento=amigo['tipo'],
                    facebook=amigo['facebook']
                )
    
    elif opcao == "4":
        print("\n📝 Criar pessoa manualmente")
        nome = input("Nome: ").strip()
        data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
        tipo = input("Tipo (Família/Amigo/Colega/Conhecido): ").strip()
        como = input("Como se conheceram: ").strip()
        insta = input("Instagram (@usuario): ").strip()
        face = input("Facebook: ").strip()
        
        criar_arquivo_pessoa(
            nome=nome,
            data_nascimento=data_nasc,
            tipo_relacionamento=tipo,
            como_conheceu=como,
            instagram=insta,
            facebook=face
        )
    
    elif opcao == "5":
        print("\n👋 Até logo!")
        return
    
    else:
        print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
