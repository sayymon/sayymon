# 📱 Guia Completo - Google Contacts

## 🎯 Por que usar Google Contacts?

✅ **Vantagens:**
- Sem necessidade de tokens ou APIs complicadas
- Seus contatos já estão organizados
- Inclui telefones, emails, aniversários automaticamente
- Funciona 100% offline após exportar
- Mais seguro (sem exposição de credenciais)
- Suporta centenas de contatos de uma vez

❌ **Desvantagens de outras opções:**
- Instagram: API limitada, requer login, pode bloquear
- Facebook: API não retorna amigos, requer tokens complexos
- Manual: Trabalhoso para muitos contatos

## 📥 Passo a Passo Completo

### 1️⃣ Exportar do Google Contacts

1. Abra seu navegador e acesse:
   ```
   https://contacts.google.com/
   ```

2. Faça login com sua conta Google

3. No menu lateral esquerdo, clique em **"Exportar"**

4. Escolha o que exportar:
   - **"Contatos"** - Todos os contatos
   - Ou selecione um grupo específico (Família, Amigos, etc.)

5. Escolha o formato:
   - **"Google CSV"** ⭐ RECOMENDADO
     - Contém mais informações
     - Inclui aniversários, notas, organizações
   - **"vCard (para contatos iOS)"**
     - Mais universal
     - Funciona com iPhone/Android

6. Clique em **"Exportar"**

7. Salve o arquivo (geralmente vai para Downloads)
   - CSV: `contacts.csv`
   - vCard: `contacts.vcf`

### 2️⃣ Executar o Script

1. Abra o Terminal

2. Navegue até a pasta dos scripts:
   ```bash
   cd ~/caminho/para/Pessoal/Relacionamentos/scripts
   ```

3. Execute o script:
   ```bash
   python3 importar_google_contacts.py
   ```

4. Escolha a opção:
   - **1** para Google CSV
   - **2** para vCard

5. Informe o caminho do arquivo:
   ```
   Caminho do arquivo CSV: ~/Downloads/contacts.csv
   ```
   
   Ou arraste o arquivo para o Terminal!

### 3️⃣ Classificar Contatos

O script vai perguntar para cada contato:

```
[1/50] João Silva
    Tel: (11) 98765-4321
    Email: joao@email.com
Tipo (1/2/3/4/S/T): 
```

**Opções:**
- **1** - Família
- **2** - Amigo
- **3** - Profissional
- **4** - Conhecido
- **S** - Pular (manter como está)
- **T** - Classificar todos restantes como mesmo tipo

**Dica:** Use "T" quando chegar em um grupo homogêneo (ex: todos colegas de trabalho)

### 4️⃣ Revisar e Criar

1. O script pergunta se quer exportar para JSON primeiro:
   ```
   Exportar para JSON para revisão? (s/n): s
   ```
   
   **Recomendado:** Diga "s" para revisar antes de criar

2. Revise o arquivo `contatos_google.json` gerado

3. Edite se necessário (adicionar informações, corrigir tipos)

4. Execute novamente e escolha criar arquivos:
   ```
   Criar arquivos MD para todos? (s/n): s
   ```

### 5️⃣ Resultado

Arquivos criados em `Pessoal/Relacionamentos/`:
```
João_Silva.md
Maria_Santos.md
Pedro_Oliveira.md
...
```

Cada arquivo contém:
- ✅ Nome completo
- ✅ Telefone
- ✅ Email
- ✅ Data de nascimento (se cadastrada)
- ✅ Tipo de relacionamento
- ✅ Notas do Google Contacts
- ✅ Template pronto para preencher mais informações

## 🎨 Exemplo de Arquivo Gerado

```markdown
# João Silva

## Informações Básicas
- **Data de Nascimento:** 15/03/1990
- **Idade:** 35 anos
- **Aniversário:** 15 de Março

## Relacionamento
- **Tipo:** Amigo
- **Parentesco/Vínculo:** 
- **Como nos conhecemos:** 
- **Tempo de conhecimento:** 

## Contato
- **Telefone:** (11) 98765-4321
- **Email:** joao.silva@email.com
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
Amigo da faculdade, trabalha com tecnologia

---
**Tags:** #relacionamento #amigo
**Criado em:** 30/01/2026
**Última atualização:** 30/01/2026
```

## 💡 Dicas e Truques

### Organizar Contatos no Google Antes de Exportar

1. Crie grupos no Google Contacts:
   - Família
   - Amigos Próximos
   - Trabalho
   - Conhecidos

2. Exporte cada grupo separadamente

3. Ao importar, todos do grupo já terão o tipo correto!

### Adicionar Aniversários no Google

1. Abra o contato no Google Contacts
2. Clique em "Adicionar campo"
3. Escolha "Aniversário"
4. Preencha a data
5. Exporte novamente

### Limpar Contatos Duplicados

Antes de exportar:
1. No Google Contacts, vá em "Sugestões"
2. Clique em "Mesclar e corrigir"
3. Revise e mescle duplicatas
4. Depois exporte

### Adicionar Notas Úteis

No Google Contacts, adicione notas como:
- "Conheci na faculdade em 2015"
- "Gosta de café e tecnologia"
- "Instagram: @usuario"

Essas notas serão importadas automaticamente!

## 🔧 Troubleshooting

### Erro: Arquivo não encontrado

```bash
# Use caminho completo
python3 importar_google_contacts.py
# Quando pedir: /Users/seu_usuario/Downloads/contacts.csv

# Ou arraste o arquivo para o Terminal
```

### Caracteres estranhos no nome

O script já trata automaticamente:
- Remove caracteres inválidos
- Substitui espaços por underscore
- Mantém acentos corretamente

### Datas de aniversário não aparecem

Verifique no Google Contacts:
1. Abra o contato
2. Veja se tem campo "Aniversário" preenchido
3. Formato deve ser DD/MM/AAAA ou AAAA-MM-DD

### Muitos contatos para classificar

Use a opção "T" (classificar todos):
1. Classifique os primeiros manualmente
2. Quando chegar em um grupo homogêneo, use "T"
3. Escolha o tipo para todos restantes

## 📊 Comparação de Formatos

### Google CSV
✅ Mais completo
✅ Inclui aniversários
✅ Inclui notas
✅ Inclui organização
✅ Melhor para importação

### vCard (VCF)
✅ Mais universal
✅ Funciona com qualquer sistema
✅ Pode importar de iPhone/Android
⚠️ Menos campos disponíveis

**Recomendação:** Use Google CSV sempre que possível!

## 🎯 Próximos Passos

Após importar:

1. ✅ Revise os arquivos criados
2. ✅ Complete informações faltantes
3. ✅ Adicione "Coisas em Comum"
4. ✅ Preencha "Como nos conhecemos"
5. ✅ Execute `gerar_relatorios.py` para ver aniversários
6. ✅ Configure lembretes semanais

## 🔄 Atualizar Contatos

Para adicionar novos contatos depois:

1. Adicione no Google Contacts
2. Exporte novamente
3. Execute o script
4. Apenas novos contatos serão criados (existentes são pulados)

## 📱 Sincronizar com Celular

Seus contatos do Google já sincronizam com:
- ✅ Android (automático)
- ✅ iPhone (adicione conta Google)
- ✅ Outlook
- ✅ Outros apps

Mantenha tudo atualizado em um só lugar!

---

**Criado em:** 30/01/2026

💡 **Dica Final:** Mantenha seus contatos organizados no Google Contacts e exporte periodicamente para manter seu sistema atualizado!
