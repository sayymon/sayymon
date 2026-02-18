#!/usr/bin/env python3
"""
Script alternativo para importar do Facebook usando requests diretamente.
Desabilita verificação SSL para ambientes de desenvolvimento.
"""

import json
import ssl
import urllib3
import requests
from pathlib import Path
from datetime import datetime

# Desabilitar avisos de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RELACIONAMENTOS_DIR = Path(__file__).parent.parent


def criar_arquivo_pessoa(nome, data_nascimento="", tipo_relacionamento="", 
                         como_conheceu="", instagram="", facebook="", 
                         interesses=None):
    """Cria um arquivo MD para uma pessoa."""
    if interesses is None:
        interesses = []
    
    nome_arquivo = nome.replace(" ", "_").replace("/", "-")
    arquivo_path = RELACIONAMENTOS_DIR / f"{nome_arquivo}.md"
    
    if arquivo_path.exists():
        print(f"⚠️  Arquivo já existe: {nome_arquivo}.md")
        return False
    
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
    
    with open(arquivo_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"✅ Criado: {nome_arquivo}.md")
    return True


def importar_facebook_api(access_token):
    """
    Importa amigos do Facebook usando requests diretamente.
    SSL verification desabilitada.
    """
    print("\n" + "="*60)
    print("👥 IMPORTANDO DO FACEBOOK")
    print("="*60)
    print("⚠️  Verificação SSL desabilitada")
    print("⚠️  Use apenas em ambiente de desenvolvimento\n")
    
    base_url = "https://graph.facebook.com/v18.0"
    
    try:
        # Testar conexão - obter informações do usuário
        print("🔍 Testando conexão...")
        me_url = f"{base_url}/me"
        params = {
            'access_token': access_token,
            'fields': 'id,name,email'
        }
        
        response = requests.get(me_url, params=params, verify=False, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Erro na autenticação: {response.status_code}")
            print(f"Resposta: {response.text}")
            return []
        
        user_data = response.json()
        print(f"✅ Conectado como: {user_data.get('name', 'Desconhecido')}")
        print(f"   ID: {user_data.get('id', 'N/A')}\n")
        
        # Tentar obter amigos
        print("🔍 Buscando lista de amigos...")
        friends_url = f"{base_url}/me/friends"
        params = {
            'access_token': access_token,
            'fields': 'id,name',
            'limit': 5000
        }
        
        response = requests.get(friends_url, params=params, verify=False, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Erro ao buscar amigos: {response.status_code}")
            print(f"Resposta: {response.text}")
            return []
        
        friends_data = response.json()
        
        if not friends_data.get('data'):
            print("\n⚠️  IMPORTANTE:")
            print("A API do Facebook não retornou amigos.")
            print("\nMotivos possíveis:")
            print("1. A API do Facebook mudou e não permite mais listar todos os amigos")
            print("2. Apenas amigos que também usam o mesmo app são retornados")
            print("3. Você precisa de permissões especiais (user_friends)")
            print("\n💡 SOLUÇÃO:")
            print("Use a exportação manual do Facebook:")
            print("1. Acesse: facebook.com/dyi")
            print("2. Baixe 'Amigos'")
            print("3. Converta para JSON")
            print("4. Use a opção 1 do menu principal\n")
            return []
        
        amigos = []
        for friend in friends_data['data']:
            amigos.append({
                'nome': friend.get('name', 'Sem nome'),
                'facebook_id': friend.get('id', ''),
                'facebook': friend.get('name', ''),
                'tipo': 'Amigo'
            })
        
        print(f"✅ {len(amigos)} amigos encontrados!\n")
        return amigos
        
    except requests.exceptions.SSLError as e:
        print(f"❌ Erro SSL: {e}")
        print("\n💡 Mesmo com SSL desabilitado, houve erro.")
        print("Tente instalar certificados:")
        print("  macOS: /Applications/Python*/Install\\ Certificates.command")
        return []
    
    except requests.exceptions.Timeout:
        print("❌ Timeout na conexão com Facebook")
        return []
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return []
    
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return []


def obter_novo_token():
    """Instruções para obter um novo access token."""
    print("\n" + "="*60)
    print("🔑 COMO OBTER UM ACCESS TOKEN DO FACEBOOK")
    print("="*60)
    print("\n1. Acesse: https://developers.facebook.com/tools/explorer/")
    print("2. Clique em 'Get User Access Token'")
    print("3. Marque as permissões:")
    print("   - user_friends")
    print("   - public_profile")
    print("4. Clique em 'Generate Access Token'")
    print("5. Copie o token gerado")
    print("\n⚠️  IMPORTANTE:")
    print("- O token expira em algumas horas")
    print("- NUNCA compartilhe seu token publicamente")
    print("- Revogue tokens antigos em: facebook.com/settings?tab=security")
    print("\n" + "="*60 + "\n")


def menu_principal():
    """Menu interativo."""
    print("=" * 60)
    print("📱 IMPORTADOR DO FACEBOOK (SSL Desabilitado)")
    print("=" * 60)
    print("\nEscolha uma opção:")
    print("1. Importar amigos do Facebook")
    print("2. Como obter um novo Access Token")
    print("3. Testar conexão com Facebook")
    print("4. Sair")
    print()
    
    opcao = input("Opção: ").strip()
    
    if opcao == "1":
        print("\n⚠️  ATENÇÃO: Seu token anterior pode estar comprometido!")
        print("Recomendo gerar um novo token antes de continuar.\n")
        
        token = input("Access Token do Facebook: ").strip()
        
        if not token:
            print("❌ Token vazio!")
            return
        
        amigos = importar_facebook_api(token)
        
        if amigos:
            print(f"\n📋 {len(amigos)} amigos encontrados")
            criar = input("\nCriar arquivos para todos? (s/n): ").strip().lower()
            
            if criar == 's':
                criados = 0
                for amigo in amigos:
                    if criar_arquivo_pessoa(
                        nome=amigo['nome'],
                        tipo_relacionamento=amigo['tipo'],
                        facebook=amigo['facebook'],
                        como_conheceu="Facebook"
                    ):
                        criados += 1
                
                print(f"\n✅ {criados} arquivos criados com sucesso!")
    
    elif opcao == "2":
        obter_novo_token()
    
    elif opcao == "3":
        token = input("Access Token do Facebook: ").strip()
        
        if not token:
            print("❌ Token vazio!")
            return
        
        print("\n🔍 Testando conexão...")
        
        try:
            response = requests.get(
                "https://graph.facebook.com/v18.0/me",
                params={'access_token': token, 'fields': 'id,name,email'},
                verify=False,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"\n✅ Conexão OK!")
                print(f"Nome: {data.get('name', 'N/A')}")
                print(f"ID: {data.get('id', 'N/A')}")
                print(f"Email: {data.get('email', 'N/A')}")
            else:
                print(f"\n❌ Erro: {response.status_code}")
                print(f"Resposta: {response.text}")
        
        except Exception as e:
            print(f"\n❌ Erro: {e}")
    
    elif opcao == "4":
        print("\n👋 Até logo!")
        return
    
    else:
        print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
