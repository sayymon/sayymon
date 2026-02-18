# Scripts de Importação de Contatos

## 📋 Visão Geral
Scripts para automatizar a criação de arquivos Markdown para cada pessoa do seu círculo social.

## 🚀 Como Usar

### Opção 1: Google Contacts (MAIS RECOMENDADO) ⭐

Esta é a forma mais simples, segura e completa!

**Vantagens:**
- ✅ Sem problemas de API ou tokens
- ✅ Importa telefones, emails, aniversários
- ✅ Funciona offline
- ✅ Dados já organizados

**Como usar:**

1. Exporte seus contatos do Google:
   - Acesse: https://contacts.google.com/
   - Clique em "Exportar" no menu lateral
   - Escolha "Google CSV" (recomendado) ou "vCard"
   - Baixe o arquivo

2. Execute o script:
```bash
cd "Pessoal/Relacionamentos/scripts"
python3 importar_google_contacts.py
```

3. Escolha opção 1 (CSV) ou 2 (vCard)
4. Informe o caminho do arquivo baixado
5. Classifique os contatos (Família/Amigo/Profissional/Conhecido)
6. Pronto! Arquivos criados automaticamente

### Opção 2: Importar de JSON
Boa para adicionar contatos manualmente ou importar de outras fontes.

1. Edite o arquivo `exemplo_contatos.json` com seus contatos
2. Execute o script:
```bash
cd "Pessoal/Relacionamentos/scripts"
python3 importar_contatos.py
```
3. Escolha a opção 1 e informe o caminho: `exemplo_contatos.json`

### Opção 3: Instagram (Experimental)
⚠️ **Limitações:**
- Instagram restringe acesso à API
- Pode requerer login
- Limitado a 50 seguidores para evitar bloqueio
- Pode não funcionar devido a mudanças na API

**Instalação:**
```bash
pip install instaloader
```

**Uso:**
```bash
python3 importar_contatos.py
# Escolha opção 2
```

### Opção 4: Facebook (Experimental)
⚠️ **Limitações:**
- Facebook não permite mais listar todos os amigos via API
- Requer access token com permissões específicas
- Muito restritivo para uso pessoal

**Instalação:**
```bash
pip install facebook-sdk
```

**Como obter Access Token:**
1. Acesse: https://developers.facebook.com/tools/explorer/
2. Selecione "Get User Access Token"
3. Marque permissões: `user_friends`
4. Copie o token gerado

### Opção 5: Manual
Crie pessoas uma por uma através do menu interativo.

## 📝 Formato do JSON

```json
[
  {
    "nome": "Nome Completo",
    "data_nascimento": "DD/MM/AAAA",
    "tipo": "Família|Amigo|Colega|Conhecido",
    "como_conheceu": "Descrição de como se conheceram",
    "instagram": "@usuario",
    "facebook": "Nome no Facebook",
    "interesses": ["Interesse 1", "Interesse 2"]
  }
]
```

## 📊 Comparação de Métodos

| Método | Facilidade | Segurança | Dados Completos | Recomendado |
|--------|-----------|-----------|-----------------|-------------|
| Google Contacts | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ SIM |
| JSON Manual | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ SIM |
| Instagram | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ❌ NÃO |
| Facebook | ⭐ | ⭐⭐ | ⭐ | ❌ NÃO |

## 🎯 Outras Fontes de Contatos

### Exportar Contatos do Celular
- **iPhone:** Configurações > Contatos > Exportar vCard
- **Android:** App Contatos > Configurações > Exportar

Depois converta vCard para JSON usando ferramentas online.

## 🔧 Troubleshooting

### Erro: Module not found
```bash
pip install instaloader facebook-sdk python-dotenv
```

### Instagram bloqueou
- Aguarde algumas horas
- Use a opção JSON manual
- Exporte seus seguidores manualmente

### Facebook não retorna amigos
- A API do Facebook mudou e não permite mais isso
- Use a opção JSON manual
- Exporte seus amigos manualmente do Facebook

## 💡 Dicas

1. **Comece pequeno:** Adicione primeiro família e amigos próximos
2. **Use o template:** Copie `_Template Pessoa.md` para criar manualmente
3. **Atualize regularmente:** Revise e atualize as informações periodicamente
4. **Backup:** Faça backup dos arquivos criados

## 🔐 Privacidade

- Nunca compartilhe seus access tokens
- Não commite arquivos com dados pessoais em repositórios públicos
- Mantenha seus scripts e dados locais

---
**Última atualização:** 30/01/2026
