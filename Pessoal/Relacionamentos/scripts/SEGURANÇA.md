# 🔒 Guia de Segurança - Access Tokens

## ⚠️ ALERTA IMPORTANTE

**Você expôs seu access token do Facebook publicamente!**

Access token exposto: `27543983edd828480ba7313cd07077a0`

## 🚨 O QUE FAZER AGORA

### 1. Revogar o Token Imediatamente

1. Acesse: https://www.facebook.com/settings?tab=security
2. Vá em "Apps e sites"
3. Encontre o app que gerou o token
4. Clique em "Remover" ou "Revogar acesso"

OU

1. Acesse: https://developers.facebook.com/tools/debug/accesstoken/
2. Cole o token
3. Clique em "Debug"
4. Clique em "Invalidate Access Token"

### 2. Verificar Atividades Suspeitas

1. Acesse: https://www.facebook.com/settings?tab=security
2. Revise "Onde você está conectado"
3. Encerre sessões desconhecidas

### 3. Gerar um Novo Token

Quando precisar de um novo token:
1. Acesse: https://developers.facebook.com/tools/explorer/
2. Gere um novo token
3. **NUNCA compartilhe em chats, emails ou código público**

## 🛡️ Boas Práticas de Segurança

### ❌ NUNCA Faça Isso

- Compartilhar tokens em chats ou emails
- Commitar tokens em repositórios Git
- Postar tokens em fóruns ou redes sociais
- Deixar tokens em código-fonte
- Usar tokens em ambientes públicos

### ✅ SEMPRE Faça Isso

- Use variáveis de ambiente para tokens
- Adicione `.env` ao `.gitignore`
- Revogue tokens após uso
- Use tokens com permissões mínimas necessárias
- Monitore uso de tokens regularmente

## 🔐 Como Usar Tokens com Segurança

### Opção 1: Variáveis de Ambiente

```bash
# Criar arquivo .env (NÃO commitar!)
echo "FACEBOOK_TOKEN=seu_token_aqui" > .env
echo ".env" >> .gitignore
```

```python
# No script Python
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('FACEBOOK_TOKEN')
```

### Opção 2: Input Interativo

```python
# Sempre pedir o token quando executar
token = input("Access Token: ").strip()
```

### Opção 3: Arquivo de Configuração Local

```bash
# Criar arquivo config.json (NÃO commitar!)
echo '{"facebook_token": "seu_token"}' > config.json
echo "config.json" >> .gitignore
```

```python
# No script Python
import json

with open('config.json') as f:
    config = json.load(f)
    token = config['facebook_token']
```

## 🔍 Verificar se Token Está Válido

```bash
# Testar token
curl -i -X GET "https://graph.facebook.com/v18.0/me?access_token=SEU_TOKEN"
```

## 📋 Checklist de Segurança

- [ ] Revogou o token exposto
- [ ] Verificou atividades suspeitas na conta
- [ ] Criou arquivo `.gitignore` com `.env` e `config.json`
- [ ] Configurou variáveis de ambiente
- [ ] Removeu tokens de código-fonte
- [ ] Ativou autenticação de dois fatores no Facebook

## 🚫 Sobre Desabilitar SSL

**Por que desabilitamos SSL no script?**
- Problema com certificados locais no macOS
- Apenas para desenvolvimento local
- **NUNCA use em produção**

**Como resolver o problema de certificados:**

```bash
# macOS - Instalar certificados Python
/Applications/Python\ 3.*/Install\ Certificates.command

# Ou reinstalar certifi
pip install --upgrade certifi

# Ou usar certificados do sistema
export SSL_CERT_FILE=/etc/ssl/cert.pem
```

## 📚 Recursos Adicionais

- [Facebook Security Settings](https://www.facebook.com/settings?tab=security)
- [Facebook App Dashboard](https://developers.facebook.com/apps/)
- [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)

## 💡 Alternativas Mais Seguras

### 1. Exportação Manual do Facebook

Mais seguro que usar API:
1. Acesse: https://www.facebook.com/dyi
2. Baixe "Informações sobre amigos"
3. Converta para JSON
4. Importe usando script local

### 2. Adicionar Manualmente

Para poucos contatos:
- Use o template `_Template Pessoa.md`
- Copie e preencha manualmente
- Mais trabalhoso, mas mais seguro

### 3. Google Contacts

Se seus contatos estão no Google:
1. Exporte do Google Contacts
2. Converta CSV para JSON
3. Importe usando script

---

**Lembre-se:** Segurança é responsabilidade de todos. Proteja seus dados e tokens!

**Data:** 30/01/2026
