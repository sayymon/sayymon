# Campos Obrigatórios - Salesforce Lead API

## 📋 Campos Obrigatórios Padrão

### Para CREATE (POST)
```json
{
  "LastName": "string (max 80 chars) - OBRIGATÓRIO",
  "Company": "string (max 255 chars) - OBRIGATÓRIO"
}
```

### Para UPDATE (PATCH)
- Nenhum campo é obrigatório no PATCH, mas você precisa do ID do Lead na URL

---

## ⚠️ Campos Booleanos Customizados (Obrigatórios mas com Default)

Estes campos são tecnicamente obrigatórios (nillable=false), mas geralmente têm valores default. Se você não enviá-los, o Salesforce pode aplicar o valor padrão (false):

```json
{
  "whatslly__Created_by_Whatslly__c": false,
  "UpdatedBySession__c": false,
  "NPSContact__c": false,
  "UnqualifiedForCadence__c": false,
  "Advertising_Investment__c": false,
  "Hotmart_Express__c": false,
  "Low_Revenue_Potential__c": false,
  "Sparkle__c": false,
  "Is_Lead__c": false,
  "et4ae5__HasOptedOutOfMobile__c": false,
  "WishList__c": false,
  "Share_of_Wallet__c": false,
  "AutomaticWhatsappMessageSent__c": false,
  "Send_first_WhatsApp_contact__c": false,
  "InboundLeadCreatedAfterHours__c": false,
  "Automated_Lead__c": false,
  "AutomaticUnqualified__c": false,
  "WhatsAppSentToLeadCreatedAfterHour__c": false,
  "ActiveCheckout__c": false
}
```

---

## 🎯 Campos Altamente Recomendados

Embora não sejam tecnicamente obrigatórios, estes campos são essenciais para o processo de negócio:

```json
{
  "FirstName": "string (max 40 chars)",
  "Email": "email (max 80 chars)",
  "Phone": "phone (max 40 chars)",
  "RecordTypeId": "reference (18 chars) - Ex: 0123u000000nQdYAAU",
  "LeadSource": "picklist - Ex: Website",
  "Status": "picklist - Ex: Open, Contacted, Qualified, Unqualified"
}
```

---

## 📝 Análise do Seu Exemplo

### Campos no seu PATCH que são importantes:

```json
{
  // OBRIGATÓRIOS
  "LastName": "NA",  // ✅ Presente
  // Company não está no PATCH - pode causar erro se não existir no Lead
  
  // RECOMENDADOS
  "FirstName": "José",  // ✅ Bom
  "Email": "junior19278@gmail.com",  // ✅ Essencial
  "Phone": "+5599988192590",  // ✅ Bom
  "RecordTypeId": "0123u000000nQdYAAU",  // ✅ Importante
  "LeadSource": "Website",  // ✅ Bom
  
  // CUSTOMIZADOS HOTMART
  "CurrencyIsoCode": "BRL",
  "PrimaryLanguage__c": "Portuguese",
  "Currency__c": "BRL",
  "ConfidenceLevel__c": "High",
  "Niche__c": "General",
  "LeadOrigin_Specification__c": "Campanha_9_Banner_Home_Controle",
  "Profile__c": "Producer",
  "Hotmart_Office__c": "Brazil",
  "Lead_Flow__c": "Inbound",
  "LeadMacroOrigin__c": "Growth Marketing",
  "Send_first_WhatsApp_contact__c": "true",  // ⚠️ Deveria ser boolean, não string
  "Whatsapp__c": "+5599988192590",
  "Lead_Origin_Custom__c": "Organic Growth",
  "Instagram_Link__c": "https://www.instagram.com/@dinoaplicativo",
  "Instagram_audience__c": "50.000 - 75.000",
  "Instagram__c": "@dinoaplicativo",
  "InstagramAudience__c": "50.000 - 75.000",
  "Input_List_CD__c": "k2qopp7ti0",
  "Input_Lead_CD__c": "PNxXd3CNTL",
  "Score_CD__c": "32",
  "LeadFlowDetail__c": "New Business Approach"
}
```

---

## 🔧 Checklist para Mitigar Erros

### 1. **Validação Pré-Envio**

```javascript
// Campos obrigatórios mínimos para CREATE
const requiredFieldsCreate = {
  LastName: payload.LastName || 'NA',
  Company: payload.Company || 'NA'
};

// Campos obrigatórios mínimos para UPDATE
const requiredFieldsUpdate = {
  // Nenhum campo obrigatório, mas valide o ID
};
```

### 2. **Validação de Tipos**

```javascript
// Booleanos devem ser boolean, não string
if (payload.Send_first_WhatsApp_contact__c === "true") {
  payload.Send_first_WhatsApp_contact__c = true;
}
if (payload.Send_first_WhatsApp_contact__c === "false") {
  payload.Send_first_WhatsApp_contact__c = false;
}
```

### 3. **Validação de Tamanhos**

```javascript
const fieldLengths = {
  LastName: 80,
  FirstName: 40,
  Company: 255,
  Email: 80,
  Phone: 40,
  RecordTypeId: 18
};

// Validar antes de enviar
if (payload.LastName && payload.LastName.length > 80) {
  throw new Error('LastName excede 80 caracteres');
}
```

### 4. **Validação de Email e Telefone**

```javascript
// Email válido
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (payload.Email && !emailRegex.test(payload.Email)) {
  throw new Error('Email inválido');
}

// Telefone com formato internacional
const phoneRegex = /^\+?[1-9]\d{1,14}$/;
if (payload.Phone && !phoneRegex.test(payload.Phone.replace(/[\s-]/g, ''))) {
  console.warn('Telefone pode estar em formato inválido');
}
```

### 5. **Tratamento de Erros da API**

```javascript
try {
  const response = await fetch(url, {
    method: 'PATCH',
    headers: headers,
    body: JSON.stringify(payload)
  });
  
  if (!response.ok) {
    const error = await response.json();
    console.error('Erro Salesforce:', error);
    
    // Erros comuns:
    // - REQUIRED_FIELD_MISSING: Campo obrigatório faltando
    // - INVALID_EMAIL_ADDRESS: Email inválido
    // - STRING_TOO_LONG: Campo excede tamanho máximo
    // - INVALID_TYPE_FOR_OPERATION: Tipo de dado incorreto
  }
} catch (error) {
  console.error('Erro na integração:', error);
}
```

---

## 🚨 Problemas Comuns Identificados

### 1. **Boolean como String**
```json
// ❌ ERRADO
"Send_first_WhatsApp_contact__c": "true"

// ✅ CORRETO
"Send_first_WhatsApp_contact__c": true
```

### 2. **Company Faltando no CREATE**
Se você está criando um Lead novo, sempre inclua:
```json
{
  "LastName": "Silva",
  "Company": "NA"  // Ou o nome real da empresa
}
```

### 3. **RecordTypeId Inválido**
Valide se o RecordTypeId existe e está ativo:
```bash
curl 'https://hotmart.my.salesforce.com/services/data/v62.0/sobjects/RecordType/0123u000000nQdYAAU'
```

---

## 📊 Resumo Executivo

| Campo | Operação | Obrigatório | Tipo | Tamanho Max |
|-------|----------|-------------|------|-------------|
| LastName | CREATE | ✅ Sim | string | 80 |
| Company | CREATE | ✅ Sim | string | 255 |
| FirstName | Ambos | ⚠️ Recomendado | string | 40 |
| Email | Ambos | ⚠️ Recomendado | email | 80 |
| Phone | Ambos | ⚠️ Recomendado | phone | 40 |
| RecordTypeId | Ambos | ⚠️ Recomendado | reference | 18 |
| Send_first_WhatsApp_contact__c | Ambos | ⚠️ Boolean obrigatório | boolean | - |

---

## 🔍 Como Descobrir Mais Campos Obrigatórios

Execute este comando para ver TODOS os campos obrigatórios:

```bash
curl 'https://hotmart.my.salesforce.com/services/data/v62.0/sobjects/Lead/describe' \
  --header 'Authorization: Bearer SEU_TOKEN' | \
  jq '.fields[] | select(.nillable == false and .createable == true) | {name, label, type, length}'
```

---

## 💡 Recomendações Finais

1. **Sempre valide tipos de dados** antes de enviar (especialmente booleanos)
2. **Implemente retry logic** para erros temporários (500, 503)
3. **Logue todos os erros** com o payload completo para debug
4. **Valide RecordTypeId** antes de usar
5. **Use valores default** para campos booleanos obrigatórios
6. **Teste em Sandbox** antes de produção
7. **Monitore rate limits** da API Salesforce (15.000 calls/24h por default)

