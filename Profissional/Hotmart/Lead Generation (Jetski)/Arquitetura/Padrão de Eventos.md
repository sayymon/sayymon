# Padrão de Eventos - Lead Generation

## Visão Geral

Todos os fluxos de Lead Generation (Inbound, Signup, Outbound, Meta Ads) seguem um padrão consistente de eventos para garantir rastreabilidade e uniformidade no processamento.

## Estrutura Base de Evento

### Metadados Obrigatórios

```json
{
  "system": "lead_generation",
  "entity": "[tipo_do_fluxo]",
  "action": "[acao_realizada]",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    // Dados específicos do evento
  }
}
```

### Campos dos Metadados

- **system:** Sempre `"lead_generation"` para todos os fluxos
- **entity:** Identifica o fluxo de origem
  - `"inbound"` - Leads de formulários Typeform
  - `"signup"` - Leads de cadastro na plataforma
  - `"outbound"` - Leads de scraping de concorrentes
  - `"meta_ads"` - Leads de Facebook Ads Library
- **action:** Tipo de ação realizada
  - `"script"` - Processamento automatizado
  - `"manual"` - Ação manual
  - `"enrichment"` - Enriquecimento de dados
- **event_version:** Versão do formato do evento (ex: "1.1")
- **data_version:** Versão da estrutura de dados (ex: "1.0")

## Eventos por Fluxo

### Inbound (Typeform)

#### Evento: Lead Capturado
```json
{
  "system": "lead_generation",
  "entity": "inbound",
  "action": "script",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid",
    "name": "Nome do Lead",
    "email": "email@example.com",
    "phone": "+5511999999999",
    "origin": "paid|organic|cold",
    "formId": "typeform_id",
    "submittedAt": "2026-01-30T20:00:00Z",
    "utmSource": "facebook",
    "utmMedium": "cpc",
    "utmCampaign": "campaign_name"
  }
}
```

### Signup (Plataforma Hotmart)

#### Evento: Novo Cadastro
```json
{
  "system": "lead_generation",
  "entity": "signup",
  "action": "script",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "userId": "hotmart_user_id",
    "name": "Nome do Creator",
    "email": "email@example.com",
    "signupDate": "2026-01-30T20:00:00Z",
    "accountType": "creator|affiliate",
    "instagramHandle": "@username",
    "instagramFollowers": 150000,
    "socialProfiles": {
      "instagram": "url",
      "youtube": "url",
      "tiktok": "url"
    }
  }
}
```

### Outbound (Scraping Concorrentes)

#### Evento: Lead Descoberto
```json
{
  "system": "lead_generation",
  "entity": "outbound",
  "action": "script",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid",
    "name": "Nome do Creator",
    "email": "email@example.com",
    "source": "kiwify|hubla|eduzz",
    "sourceUrl": "url_origem",
    "discoveredAt": "2026-01-30T20:00:00Z",
    "instagramHandle": "@username",
    "instagramFollowers": 150000,
    "productUrl": "url_do_produto",
    "productName": "Nome do Produto",
    "niche": "Educação|Fitness|Negócios"
  }
}
```

### Meta Ads (Facebook Ads Library)

#### Evento: Lead Descoberto via Ads
```json
{
  "system": "lead_generation",
  "entity": "meta_ads",
  "action": "script",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid",
    "announcerName": "Nome do Anunciante",
    "announcerFbId": "123456789",
    "announcerFbCategory": "Educação",
    "instagramHandle": "@username",
    "announcerIgFollowers": 150000,
    "adLibraryId": "1548754272816748",
    "adDescription": "Texto do anúncio",
    "adUrl": "https://landing-page.com",
    "adDate": "19 de out de 2025 a 22 de out de 2025",
    "adStatus": "Ativo",
    "keyword": "mentoria",
    "dateFilter": "2025-10-19",
    "discoveredAt": "2026-01-30T20:00:00Z"
  }
}
```

## Eventos de Enriquecimento

Após a captura inicial, todos os leads passam por enriquecimento:

### Evento: Lead Enriquecido
```json
{
  "system": "lead_generation",
  "entity": "[origem]",
  "action": "enrichment",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid",
    "enrichmentSource": "creator_discovery|manual|api",
    "enrichedAt": "2026-01-30T20:05:00Z",
    "enrichedFields": {
      "instagramFollowers": 150000,
      "instagramEngagementRate": 3.5,
      "youtubeSubscribers": 50000,
      "niche": "Educação",
      "estimatedRevenue": "10k-50k"
    }
  }
}
```

## Eventos de Qualificação

### Evento: Lead Qualificado
```json
{
  "system": "lead_generation",
  "entity": "[origem]",
  "action": "qualification",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid",
    "qualifiedAt": "2026-01-30T20:10:00Z",
    "score": 85,
    "tier": "hot|warm|cold",
    "qualificationCriteria": {
      "hasInstagram": true,
      "followersThreshold": true,
      "nicheMatch": true,
      "investingInAds": true
    },
    "assignedTo": "sdr_team_id"
  }
}
```

## Eventos de Persistência

### Evento: Lead Salvo em Outbound
```json
{
  "system": "lead_generation",
  "entity": "[origem]",
  "action": "persist",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid",
    "persistedAt": "2026-01-30T20:15:00Z",
    "destination": "outbound_table",
    "documentId": "mongodb_id",
    "status": "success|failed",
    "errorMessage": null
  }
}
```

## Fluxo Completo de Eventos - Meta Ads

```
1. Lead Descoberto (meta_ads)
   ↓
2. Lead Enriquecido (meta_ads + enrichment)
   ↓
3. Lead Qualificado (meta_ads + qualification)
   ↓
4. Lead Salvo (meta_ads + persist → outbound_table)
   ↓
5. Lead Disponível para SDR/LDR
```

## Destinos dos Eventos

### DataHub Tracking API
```
POST https://tracking-api.hotmart.com/rest/track/event/json
```
- Recebe todos os eventos
- Armazena para analytics e auditoria
- Disponibiliza para dashboards

### Tabela Outbound (MongoDB)
```
Database: outbound
Collection: leads
```
- Armazena leads qualificados
- Usado pelos times de SDR/LDR
- Inclui campo `source` para identificar origem

## Campos Comuns na Tabela Outbound

Independente da origem (Kiwify, Hubla, Meta Ads), todos os leads salvos na tabela Outbound devem ter:

```javascript
{
  // Identificação
  "_id": "mongodb_id",
  "leadId": "uuid",
  
  // Origem
  "source": "meta_ads|kiwify|hubla|eduzz|seo",
  "sourceDetail": "facebook_ads_library|website_scraping",
  "discoveryMethod": "ads_scraping|web_scraping",
  "discoveredAt": "2026-01-30T20:00:00Z",
  
  // Dados Básicos
  "name": "Nome do Creator",
  "email": "email@example.com",
  "phone": "+5511999999999",
  
  // Redes Sociais
  "instagramHandle": "@username",
  "instagramFollowers": 150000,
  "instagramEngagementRate": 3.5,
  "socialProfiles": {
    "instagram": "url",
    "youtube": "url",
    "tiktok": "url"
  },
  
  // Qualificação
  "score": 85,
  "tier": "hot|warm|cold",
  "qualifiedAt": "2026-01-30T20:10:00Z",
  
  // Enriquecimento
  "niche": "Educação|Fitness|Negócios",
  "category": "Categoria específica",
  "enrichedAt": "2026-01-30T20:05:00Z",
  
  // Campos Específicos por Fonte
  "sourceSpecificData": {
    // Meta Ads
    "adLibraryId": "123456789",
    "adKeyword": "mentoria",
    "fbId": "123456789",
    
    // Kiwify/Hubla
    "productUrl": "url",
    "productName": "nome"
  },
  
  // Controle
  "status": "new|contacted|qualified|converted|rejected",
  "assignedTo": "sdr_id",
  "assignedAt": "2026-01-30T21:00:00Z",
  "createdAt": "2026-01-30T20:00:00Z",
  "updatedAt": "2026-01-30T21:00:00Z"
}
```

## Nomenclatura

### Padrão de Campos
- **camelCase** para todos os campos em eventos e banco
- **snake_case** apenas em dados brutos de scrapers (antes da transformação)
- **ISO 8601** para datas (ex: "2026-01-30T20:00:00Z")
- **null** para campos ausentes (nunca undefined ou string vazia)

### Valores Padronizados

#### Source
- `"meta_ads"` - Facebook Ads Library
- `"kiwify"` - Plataforma Kiwify
- `"hubla"` - Plataforma Hubla
- `"eduzz"` - Plataforma Eduzz
- `"seo"` - Busca via SEO

#### Tier
- `"hot"` - Alta prioridade
- `"warm"` - Média prioridade
- `"cold"` - Baixa prioridade

#### Status
- `"new"` - Lead novo, não contatado
- `"contacted"` - Primeiro contato realizado
- `"qualified"` - Qualificado como oportunidade
- `"converted"` - Convertido em cliente
- `"rejected"` - Rejeitado/não qualificado

## Versionamento

### Event Version
Incrementar quando houver mudanças na estrutura do evento:
- **1.0** → **1.1**: Adição de novos campos opcionais
- **1.1** → **2.0**: Mudanças breaking (campos removidos/renomeados)

### Data Version
Incrementar quando houver mudanças nos dados coletados:
- **1.0** → **1.1**: Novos campos de enriquecimento
- **1.1** → **2.0**: Mudança na estrutura de dados

## Referências

- [[Meta Ads - Facebook Library]]
- [[Outbound - Extração e Enriquecimento]]
- [[Inbound - Typeform]]
- [[Signup - Plataforma Hotmart]]
- [[DataHub]]
- [[Gestão de Bases Históricas]]
