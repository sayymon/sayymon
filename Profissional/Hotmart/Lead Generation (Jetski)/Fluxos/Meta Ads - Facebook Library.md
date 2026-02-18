# Meta Ads - Facebook Library

## Visão Geral

Fluxo de captura semanal de leads através da biblioteca de anúncios do Facebook (Meta Ads Library), identificando creators que estão investindo em tráfego pago.

## Arquitetura

### Fonte de Dados
- **Plataforma:** Meta Ads Library (Facebook)
- **Tipo:** Biblioteca pública de anúncios

### Frequência
- **Periodicidade:** Semanal
- **Janela de Captura:** Últimos 7 dias de anúncios

## Orquestração

### Astroflow Scheduler
- **Ferramenta:** Astroflow
- **Frequência:** Toda terça-feira às 20:00
- **Tipo:** Agendamento automático (scheduler)

## Estratégia de Captura

### Palavras-Chave Monitoradas

#### Grupo 1 - Produtos e Plataformas
- mentoria
- treinamento
- hubla
- eduzz
- kiwify

#### Grupo 2 - Ofertas e Urgência
- vitalicio
- inscricoes abertas
- ultima turma
- vagas limitadas
- Digital
- Vitalício
- Perpétuo
- última+turma

#### Grupo 3 - Nichos e Temas
- aceleração
- método sucesso
- prosperidade
- evento online
- patrimônio
- aprenda investir
- fitness
- treino

### Critérios de Seleção
- Anúncios ativos nos últimos 7 dias (calculado a partir da data atual)
- Indicadores de investimento em tráfego
- País: Brasil (BR)
- Todos os tipos de anúncios e status

## Processo de Coleta

### Etapa 1: Trigger via Bright Data

Para cada palavra-chave, o Astroflow dispara uma requisição ao Bright Data:

#### Endpoint
```
POST https://api.brightdata.com/dca/trigger?queue_next=1&collector=c_mhdw3sjftze6dobdbcom
```

#### Payload
```json
{
  "scroll_number": 50,
  "start_date": "{{data_calculada_ultimos_7_dias}}",
  "keyword": "{{palavra_chave}}",
  "deliver": {
    "type": "webhook",
    "filename": {
      "extension": "json"
    },
    "endpoint": "https://api-astroflow.hotmart.com/v1/webhook/pjuaUoGRFV/cf5a53ef-af24-4d3a-9681-e39303c76e58",
    "auth_header": "",
    "uncompressed_webhook": false
  }
}
```

#### Parâmetros
- **scroll_number:** 50 scrolls na página para carregar mais anúncios
- **start_date:** Data calculada (últimos 7 dias a partir da data atual)
- **keyword:** Palavra-chave sendo processada
- **deliver.endpoint:** Webhook do Astroflow para receber os resultados

### Etapa 2: Scraper Bright Data (meta_ads_jetski_1step)

O scraper executa o seguinte processo:

#### 2.1 Cálculo de Datas
```javascript
// Adiciona 1 dia à data inicial para criar o range
function addOneDay(dateString) {
  const date = new Date(dateString);
  date.setDate(date.getDate() + 1);
  return date.toISOString().split('T')[0];
}

const final_date = addOneDay(input.start_date);
```

#### 2.2 Construção da URL
```javascript
const base_url = "https://www.facebook.com/ads/library/";
const params = {
  'active_status': 'all',
  'ad_type': 'all',
  'country': 'BR',
  'media_type': 'all',
  'q': input.keyword,
  'search_type': 'keyword_unordered',
  'start_date[min]': input.start_date,
  'start_date[max]': final_date,
  'locale': 'en_US'
};
```

#### 2.3 Navegação e Scroll
1. Navega para a URL construída
2. Aguarda 8 segundos para carregamento inicial
3. Executa 50 scrolls até o final da página
4. Aguarda 4 segundos entre cada scroll
5. Aguarda 5 segundos após o último scroll

#### 2.4 Extração de Library IDs
- Faz parse da página para extrair Library IDs únicos
- Constrói URLs individuais para cada anúncio
- Formato: `https://www.facebook.com/ads/library/?id={library_id}`

#### 2.5 Coleta de Dados
```javascript
collect({
  urls_ads: [
    {
      url: 'https://www.facebook.com/ads/library/?id={library_id}',
      keyword: input.keyword,
      date_filter: input.start_date
    }
  ]
});
```

### Etapa 3: Webhook de Retorno (Step 1)

Os dados coletados são enviados via webhook para o Astroflow.

#### Formato do JSON Recebido
```json
{
  "result": [
    {
      "urls_ads": [
        {
          "url": "https://www.facebook.com/ads/library/?id=1548754272816748",
          "keyword": "Perpétuo",
          "date_filter": "2025-11-16"
        }
      ],
      "input": {
        "scroll_number": 50,
        "start_date": "2025-11-16",
        "keyword": "Perpétuo"
      }
    }
  ]
}
```

#### Processamento no Astroflow
1. Recebe o JSON via webhook
2. Extrai as URLs dos anúncios
3. Aciona a segunda etapa do scraping

### Etapa 4: Coleta Detalhada (meta_ads_jetski_2step)

Para cada URL de anúncio coletada na Etapa 1, o Astroflow dispara uma nova requisição ao Bright Data para coletar dados detalhados.

#### Endpoint Step 2
```
POST https://api.brightdata.com/dca/trigger?queue_next=1&collector=c_mhf5zlpd25zfxsjtc8
```

#### Payload Step 2
```json
{
  "meta_ads_url": {
    "url": "https://www.facebook.com/ads/library/?id=1548754272816748",
    "keyword": "Perpétuo",
    "date_filter": "2025-11-16"
  },
  "deliver": {
    "type": "webhook",
    "filename": {
      "extension": "json"
    },
    "endpoint": "https://api-astroflow.hotmart.com/v1/webhook/[webhook_id_step2]",
    "auth_header": "",
    "uncompressed_webhook": false
  }
}
```

#### Interaction Code (Step 2)
```javascript
// Navega para a URL do anúncio específico (com locale pt_BR)
navigate(input.meta_ads_url.url + '&locale=pt_BR');
wait_page_idle(2500);

// Verifica se o botão de detalhes existe antes de clicar
const details_button_XPATH = "//div[@role='dialog']//div[contains(text(), 'Ver detalhes do anúncio')]";
if (!el_exists(details_button_XPATH)) {
  throw new Error('Botão "Ver detalhes do anúncio" não encontrado');
}
click(details_button_XPATH);
wait_page_idle();

// Verifica se o botão "Sobre o anunciante" existe antes de clicar
const about_sponsor_expand_XPATH = "//div[contains(text(), 'Sobre o anunciante')]";
if (!el_exists(about_sponsor_expand_XPATH)) {
  throw new Error('Botão "Sobre o anunciante" não encontrado');
}
click(about_sponsor_expand_XPATH);
wait_page_idle();

// Coleta os dados
const result = parse();
if (!result || !result.announcer_name) {
  dead_page('Dados principais não encontrados');
}
collect(result);
```

#### Parser Code (Step 2)
O parser extrai informações detalhadas do anúncio e do anunciante:

**Funções Helper:**
```javascript
// Limpar texto
const cleanText = (text) => {
  return text ? text.replace(/\s+/g, ' ').trim() : null;
};

// Converter notação (mil, k, mi) para número
function convertNotationToNumber(notation) {
  const notationParts = notation.match(/(\d+([,\.]\d+)?)\s*(mil|mi|[KkMmBbTt])?/);
  if (!notationParts) return parseInt(notation);
  
  const numericPart = parseFloat(notationParts[1].replace(',', '.'));
  const multiplier = notationParts[3] ? notationParts[3].toLowerCase() : '';
  
  let factor = 1;
  switch (multiplier) {
    case 'k': case 'mil': factor = 1000; break;
    case 'm': case 'mi': factor = 1000000; break;
    case 'b': factor = 1000000000; break;
    case 't': factor = 1000000000000; break;
  }
  
  return Math.round(numericPart * factor);
}
```

**Dados Extraídos:**

1. **Instagram Handle** - Extrai @username do texto da página
2. **Announcer Name** - Nome do anunciante
3. **Ad Description** - Descrição do anúncio
4. **Ad URL** - URL de destino do anúncio
5. **Announcer IG Followers** - Número de seguidores no Instagram (convertido)
6. **Announcer FB ID** - ID do Facebook do anunciante
7. **Announcer FB Category** - Categoria do anunciante no Facebook
8. **Ad Date** - Data/período de veiculação do anúncio
9. **Ad Library ID** - ID único na biblioteca de anúncios
10. **Ad Status** - Status do anúncio (ativo/inativo)

**Estrutura de Retorno:**
```javascript
return {
  announcer_ig_followers,      // Número de seguidores IG (convertido)
  ad_url,                       // URL de destino
  ad_description,               // Descrição do anúncio
  announcer_name,               // Nome do anunciante
  instagram_handle,             // @username
  announcer_fb_id,              // ID Facebook
  announcer_fb_category,        // Categoria FB
  ad_date,                      // Data de veiculação
  ad_library_id,                // Library ID
  ad_status,                    // Status
  keyword: input.meta_ads_url.keyword,           // Palavra-chave original
  date_filter: input.meta_ads_url.date_filter    // Data do filtro
};
```

### Etapa 5: Webhook de Retorno (Step 2)

Os dados detalhados são enviados via webhook para o Astroflow.

#### Webhook Step 2
```
POST https://api-astroflow.hotmart.com/v1/webhook/IfpezpSiez/dd310c8b-7953-4cc4-b817-cb22167564e7
```

### Etapa 6: Envio para DataHub

O Astroflow processa os dados recebidos e envia para a API de tracking do DataHub.

#### Endpoint DataHub
```
POST https://tracking-api.hotmart.com/rest/track/event/json
```

#### Evento 1: Lead Descoberto

Primeiro evento gerado quando o lead é identificado:

```javascript
{
  "system": "lead_generation",
  "entity": "meta_ads",
  "action": "script",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid_gerado",
    "announcerName": item.announcer_name,
    "announcerFbId": item.announcer_fb_id,
    "announcerFbCategory": item.announcer_fb_category,
    "instagramHandle": item.instagram_handle,
    "announcerIgFollowers": item.announcer_ig_followers,
    "adLibraryId": item.ad_library_id,
    "adDescription": item.ad_description,
    "adUrl": item.ad_url,
    "adDate": item.ad_date,
    "adStatus": item.ad_status ? item.ad_status.replace(/(\w+).*/, '$1') : null,
    "keyword": item.keyword,
    "dateFilter": item.date_filter,
    "discoveredAt": new Date().toISOString()
  }
}
```

### Etapa 7: Enriquecimento (Opcional)

Se necessário, enriquecer dados via Creator Discovery:

#### Evento 2: Lead Enriquecido

```javascript
{
  "system": "lead_generation",
  "entity": "meta_ads",
  "action": "enrichment",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid_do_lead",
    "enrichmentSource": "creator_discovery",
    "enrichedAt": new Date().toISOString(),
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

### Etapa 8: Qualificação

Aplicar regras de qualificação para determinar prioridade:

#### Evento 3: Lead Qualificado

```javascript
{
  "system": "lead_generation",
  "entity": "meta_ads",
  "action": "qualification",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid_do_lead",
    "qualifiedAt": new Date().toISOString(),
    "score": 85,
    "tier": "hot|warm|cold",
    "qualificationCriteria": {
      "hasInstagram": true,
      "followersThreshold": true,
      "nicheMatch": true,
      "investingInAds": true,
      "adActive": true
    },
    "assignedTo": "sdr_team_id"
  }
}
```

### Etapa 9: Persistência na Tabela Outbound

Salvar o lead na tabela Outbound (MongoDB) para uso dos times de SDR/LDR:

#### Evento 4: Lead Salvo

```javascript
{
  "system": "lead_generation",
  "entity": "meta_ads",
  "action": "persist",
  "event_version": "1.1",
  "data_version": "1.0",
  "event": {
    "leadId": "uuid_do_lead",
    "persistedAt": new Date().toISOString(),
    "destination": "outbound_table",
    "documentId": "mongodb_id",
    "status": "success",
    "errorMessage": null
  }
}
```

#### Estrutura na Tabela Outbound

```javascript
{
  // Identificação
  "_id": "mongodb_id",
  "leadId": "uuid",
  
  // Origem
  "source": "meta_ads",
  "sourceDetail": "facebook_ads_library",
  "discoveryMethod": "ads_scraping",
  "discoveredAt": "2026-01-30T20:00:00Z",
  
  // Dados Básicos
  "name": item.announcer_name,
  "email": null, // A ser enriquecido
  "phone": null, // A ser enriquecido
  
  // Redes Sociais
  "instagramHandle": item.instagram_handle,
  "instagramFollowers": item.announcer_ig_followers,
  "socialProfiles": {
    "facebook": `https://facebook.com/${item.announcer_fb_id}`,
    "instagram": item.instagram_handle ? `https://instagram.com/${item.instagram_handle.replace('@', '')}` : null
  },
  
  // Qualificação
  "score": 85,
  "tier": "hot",
  "qualifiedAt": "2026-01-30T20:10:00Z",
  
  // Enriquecimento
  "niche": null, // A ser enriquecido
  "category": item.announcer_fb_category,
  "enrichedAt": null,
  
  // Campos Específicos Meta Ads
  "sourceSpecificData": {
    "adLibraryId": item.ad_library_id,
    "adKeyword": item.keyword,
    "adDescription": item.ad_description,
    "adUrl": item.ad_url,
    "adDate": item.ad_date,
    "adStatus": item.ad_status,
    "fbId": item.announcer_fb_id,
    "dateFilter": item.date_filter
  },
  
  // Controle
  "status": "new",
  "assignedTo": null,
  "assignedAt": null,
  "createdAt": "2026-01-30T20:00:00Z",
  "updatedAt": "2026-01-30T20:00:00Z"
}
```

#### Transformação de Dados

O Astroflow transforma dados recebidos do Step 2 antes de salvar:

```javascript
var meta_ads = {{$trigger_webhook_1}}
var eventos = []

meta_ads.forEach((item) => {
  const leadId = generateUUID(); // Gerar UUID único
  
  // Evento 1: Lead Descoberto
  eventos.push({
    "system": "lead_generation",
    "entity": "meta_ads",
    "action": "script",
    "event_version": "1.1",
    "data_version": "1.0",
    "event": {
      "leadId": leadId,
      "announcerName": item.announcer_name ?? null,
      "announcerFbId": item.announcer_fb_id ?? null,
      "announcerFbCategory": item.announcer_fb_category ?? null,
      "instagramHandle": item.instagram_handle ?? null,
      "announcerIgFollowers": item.announcer_ig_followers ?? null,
      "adLibraryId": item.ad_library_id ?? null,
      "adDescription": item.ad_description ?? null,
      "adUrl": item.ad_url ?? null,
      "adDate": item.ad_date ?? null,
      "adStatus": item.ad_status ? item.ad_status.replace(/(\w+).*/, '$1') : null,
      "keyword": item.keyword ?? null,
      "dateFilter": item.date_filter ?? null,
      "discoveredAt": new Date().toISOString()
    }
  });
  
  // Evento 2: Lead Qualificado (se passar nos critérios)
  const qualificationScore = calculateScore(item);
  if (qualificationScore > 50) {
    eventos.push({
      "system": "lead_generation",
      "entity": "meta_ads",
      "action": "qualification",
      "event_version": "1.1",
      "data_version": "1.0",
      "event": {
        "leadId": leadId,
        "qualifiedAt": new Date().toISOString(),
        "score": qualificationScore,
        "tier": getTier(qualificationScore),
        "qualificationCriteria": {
          "hasInstagram": !!item.instagram_handle,
          "followersThreshold": item.announcer_ig_followers > 10000,
          "investingInAds": true,
          "adActive": item.ad_status?.toLowerCase().includes('ativo')
        }
      }
    });
  }
  
  // Evento 3: Lead Salvo na Outbound
  eventos.push({
    "system": "lead_generation",
    "entity": "meta_ads",
    "action": "persist",
    "event_version": "1.1",
    "data_version": "1.0",
    "event": {
      "leadId": leadId,
      "persistedAt": new Date().toISOString(),
      "destination": "outbound_table",
      "status": "pending"
    }
  });
});

return eventos
```

## Fluxo de Dados Completo

```
STEP 1 - Coleta de Library IDs:
Astroflow (Scheduler) 
  → Bright Data API (Trigger Step 1)
    → Scraper (meta_ads_jetski_1step)
      → Facebook Ads Library (Scraping + Scroll)
        → Extração de Library IDs
          → Webhook Astroflow (JSON com URLs)

STEP 2 - Coleta de Dados Detalhados:
Astroflow (Processa URLs)
  → Para cada URL
    → Bright Data API (Trigger Step 2)
      → Scraper (meta_ads_jetski_2step)
        → Página Individual do Anúncio
          → Clica "Ver detalhes"
          → Clica "Sobre o anunciante"
          → Extração de Dados Completos
            → Webhook Astroflow (JSON com dados)

STEP 3 - Envio para DataHub e Persistência:
Astroflow (Processa dados)
  → Webhook Step 3
    → Gera Eventos:
      1. Lead Descoberto (meta_ads + script)
      2. Lead Qualificado (meta_ads + qualification)
      3. Lead Salvo (meta_ads + persist)
    → DataHub Tracking API (eventos de tracking)
    → Tabela Outbound MongoDB (lead completo)
      → Base Histórica
      → Disponível para SDR/LDR
```

### Detalhamento do Fluxo

#### Step 1 - Descoberta
1. **Terça-feira 20:00:** Astroflow inicia o processo
2. **Para cada palavra-chave:** Dispara requisição ao Bright Data (Step 1)
3. **Para cada data (últimos 7 dias):** Executa scraping
4. **Bright Data:** Executa scraper na Facebook Ads Library
5. **Extração:** Coleta Library IDs dos anúncios encontrados
6. **Webhook:** Envia JSON com URLs de volta ao Astroflow

#### Step 2 - Detalhamento
7. **Astroflow:** Extrai URLs do JSON recebido
8. **Para cada URL:** Dispara requisição ao Bright Data (Step 2)
9. **Bright Data:** Navega para página individual do anúncio
10. **Interação:** Clica em botões para expandir informações
11. **Extração:** Coleta dados detalhados (anunciante, descrição, Instagram, etc.)
12. **Webhook:** Envia dados completos de volta ao Astroflow

#### Step 3 - Persistência e Eventos
13. **Astroflow:** Recebe dados do Step 2
14. **Webhook Step 3:** Processa e transforma dados
15. **Geração de Eventos:**
    - Evento 1: Lead Descoberto (tracking)
    - Evento 2: Lead Qualificado (se passar critérios)
    - Evento 3: Lead Salvo (confirmação de persistência)
16. **DataHub API:** Envia eventos estruturados para tracking/analytics
17. **MongoDB:** Salva lead completo na tabela Outbound
18. **Disponibilização:** Lead fica disponível para times de SDR/LDR

## Dados Coletados

### Step 1 - meta_ads_jetski_1step (Descoberta)

#### Library IDs
- IDs únicos dos anúncios encontrados
- URL completa: `https://www.facebook.com/ads/library/?id={library_id}`

#### Metadados
- **keyword:** Palavra-chave utilizada na busca
- **date_filter:** Data do filtro aplicado (start_date)
- **url:** URL individual de cada anúncio

#### Estrutura de Saída (Step 1)
```json
{
  "result": [
    {
      "urls_ads": [
        {
          "url": "https://www.facebook.com/ads/library/?id=123456789",
          "keyword": "mentoria",
          "date_filter": "2026-01-23"
        }
      ],
      "input": {
        "scroll_number": 50,
        "start_date": "2026-01-23",
        "keyword": "mentoria"
      }
    }
  ]
}
```

### Step 2 - meta_ads_jetski_2step (Detalhamento)

#### Dados do Anunciante
- **announcer_name:** Nome do anunciante/página
- **announcer_fb_id:** ID do Facebook do anunciante
- **announcer_fb_category:** Categoria do anunciante no Facebook
- **instagram_handle:** Username do Instagram (@username)
- **announcer_ig_followers:** Número de seguidores no Instagram (convertido de notação)

#### Dados do Anúncio
- **ad_library_id:** ID único na biblioteca de anúncios
- **ad_description:** Descrição/texto do anúncio
- **ad_url:** URL de destino do anúncio (call-to-action)
- **ad_date:** Data ou período de veiculação
- **ad_status:** Status do anúncio (ativo/inativo)

#### Metadados Preservados
- **keyword:** Palavra-chave original da busca
- **date_filter:** Data do filtro aplicado

#### Estrutura de Saída (Step 2)
```json
{
  "announcer_name": "Nome do Creator",
  "announcer_fb_id": "123456789",
  "announcer_fb_category": "Educação",
  "instagram_handle": "@creator_username",
  "announcer_ig_followers": 150000,
  "ad_library_id": "1548754272816748",
  "ad_description": "Texto completo do anúncio...",
  "ad_url": "https://example.com/landing-page",
  "ad_date": "19 de out de 2025 a 22 de out de 2025",
  "ad_status": "Ativo",
  "keyword": "mentoria",
  "date_filter": "2025-10-19"
}
```

### Conversões e Transformações

#### Seguidores do Instagram
- Converte notações: "150 mil", "1,5 mi", "150k" → 150000
- Suporta: mil, k, mi, m, b, t
- Aceita vírgula como separador decimal

#### Extração de Instagram
- Busca padrão @username no texto da página
- Prioriza segunda ocorrência (mais confiável)
- Formato: 1-30 caracteres alfanuméricos, ponto e underscore

#### Datas
- Suporta múltiplos formatos:
  - Range: "19 de out de 2025 a 22 de out de 2025"
  - Com tempo ativo: "4 de nov de 2025 · Tempo total ativo: 4h"
  - Data simples: "Veiculação iniciada em 4 de nov de 2025"

## Indicadores de Qualidade

### Bons Indicadores

#### Investimento em Tráfego
- Anúncios ativos nos últimos 7 dias
- Múltiplos anúncios para mesma palavra-chave
- Período de veiculação consistente

#### Presença Digital
- Instagram ativo com seguidores significativos
- Categoria relevante no Facebook
- URL de destino profissional

#### Conteúdo
- Descrição clara do produto/serviço
- Relacionado a produtos digitais/educação
- Palavras-chave estratégicas (mentoria, treinamento, etc.)

### Sinais de Alerta

#### Dados Incompletos
- Sem Instagram identificado
- Sem URL de destino
- Descrição vazia ou genérica

#### Baixo Engajamento
- Poucos seguidores no Instagram
- Categoria não relacionada a educação/negócios

#### Anúncios Inativos
- Status: Inativo
- Período de veiculação muito curto

## Integração com Bright Data

### Step 1 - Descoberta de Anúncios

#### Autenticação
- Endpoint requer autenticação via parâmetros da URL
- Collector ID: `c_mhdw3sjftze6dobdbcom`

#### Endpoint
```
POST https://api.brightdata.com/dca/trigger?queue_next=1&collector=c_mhdw3sjftze6dobdbcom
```

#### Scraper
- **Nome:** meta_ads_jetski_1step
- **Função:** Coleta de Library IDs através de busca por palavras-chave

#### Webhook de Retorno
```
POST https://api-astroflow.hotmart.com/v1/webhook/pjuaUoGRFV/cf5a53ef-af24-4d3a-9681-e39303c76e58
```

#### Configurações de Scraping

**Parâmetros de Navegação:**
- **Scroll Number:** 50 (quantidade de scrolls)
- **Wait Page Idle:** 8000ms (carregamento inicial)
- **Wait Between Scrolls:** 4000ms
- **Final Wait:** 5000ms

**Filtros Facebook Ads Library:**
- **active_status:** all
- **ad_type:** all
- **country:** BR
- **media_type:** all
- **search_type:** keyword_unordered
- **locale:** en_US (Step 1)

### Step 2 - Coleta Detalhada

#### Autenticação
- Endpoint requer autenticação via parâmetros da URL
- Collector ID: `c_mhf5zlpd25zfxsjtc8`

#### Endpoint
```
POST https://api.brightdata.com/dca/trigger?queue_next=1&collector=c_mhf5zlpd25zfxsjtc8
```

#### Scraper
- **Nome:** meta_ads_jetski_2step
- **Função:** Coleta de dados detalhados de cada anúncio individual

#### Webhook de Retorno Step 2
```
POST https://api-astroflow.hotmart.com/v1/webhook/IfpezpSiez/dd310c8b-7953-4cc4-b817-cb22167564e7
```

#### DataHub Tracking API
```
POST https://tracking-api.hotmart.com/rest/track/event/json
```

**Payload:** Eventos estruturados com metadados do sistema lead_generation

#### Configurações de Scraping

**Parâmetros de Navegação:**
- **Wait Page Idle:** 2500ms (carregamento inicial)
- **Locale:** pt_BR (adicionado à URL)

**Interações:**
1. Clica em "Ver detalhes do anúncio"
2. Aguarda carregamento
3. Clica em "Sobre o anunciante"
4. Aguarda carregamento
5. Extrai dados

**Validações:**
- Verifica existência de botões antes de clicar
- Lança erro se botões não encontrados
- Valida dados principais (announcer_name) antes de coletar
- Marca como dead_page se dados não encontrados

### Step 3 - Persistência no DataHub

#### Webhook Step 3
```
POST https://api-astroflow.hotmart.com/v1/webhook/IfpezpSiez/dd310c8b-7953-4cc4-b817-cb22167564e7
```

#### Função
- Recebe dados do Step 2
- Transforma em eventos estruturados
- Envia para DataHub Tracking API

#### DataHub Tracking API
```
POST https://tracking-api.hotmart.com/rest/track/event/json
```

#### Estrutura do Evento
- **system:** lead_generation
- **entity:** meta_ads
- **action:** script
- **event_version:** 1.1
- **data_version:** 1.0
- **event:** Dados do anúncio (camelCase)

#### Transformações
- Conversão de snake_case para camelCase
- Garantia de null para campos vazios (`?? null`)
- Limpeza de ad_status (primeira palavra apenas)

### Rate Limits
- Limitado pelo Bright Data
- Step 1: Processamento sequencial por palavra-chave
- Step 2: Processamento sequencial por URL de anúncio
- Step 3: Batch de eventos para DataHub
- Execução semanal (terças-feiras)

## Regras de Negócio

### Critérios de Qualificação
- [Adicionar critérios específicos]

### Priorização
- Creators com maior investimento
- Nichos estratégicos
- [Adicionar outros critérios]

### Deduplicação
- Verificação com base histórica
- [Adicionar estratégias]

## Tratamento de Erros

### Cenários de Falha

#### Bright Data API
- API indisponível
- Timeout na requisição
- Collector não encontrado
- Rate limit excedido

#### Scraper Step 1
- Facebook Ads Library indisponível
- Mudanças na estrutura da página
- Timeout durante scrolls
- Nenhum Library ID encontrado

#### Scraper Step 2
- Botão "Ver detalhes do anúncio" não encontrado
- Botão "Sobre o anunciante" não encontrado
- Dados principais (announcer_name) não encontrados
- Mudanças na estrutura da página individual

#### Webhook Step 3
- DataHub indisponível
- Falha no envio de eventos
- Validação de estrutura falhou
- Timeout na API

### Estratégias de Resiliência

#### Step 1 - Verificação de Dados
```javascript
// Verificação de dados antes de coletar
if (!data || !data.library_ids) {
  console.log('Nenhum dado encontrado');
  collect({urls_ads: []});
} else {
  // Processa normalmente
}
```

#### Step 2 - Validação de Elementos
```javascript
// Verifica existência de botões antes de clicar
const details_button_XPATH = "//div[@role='dialog']//div[contains(text(), 'Ver detalhes do anúncio')]";
if (!el_exists(details_button_XPATH)) {
  throw new Error('Botão "Ver detalhes do anúncio" não encontrado');
}

// Valida dados principais antes de coletar
const result = parse();
if (!result || !result.announcer_name) {
  dead_page('Dados principais não encontrados');
}
```

#### Waits Configurados

**Step 1:**
- 8000ms para carregamento inicial
- 4000ms entre scrolls
- 5000ms após último scroll

**Step 2:**
- 2500ms para carregamento inicial
- wait_page_idle() após cada clique

#### Logs Detalhados

**Step 1:**
- Log de navegação
- Log de cada scroll (progresso)
- Log de quantidade de Library IDs encontrados
- Log de URLs coletadas

**Step 2:**
- Log de cada campo extraído
- Console.log de todos os valores principais
- Identificação de campos nulos

#### Tratamento de Dados Ausentes

Todos os campos têm tratamento de erro com try-catch e retornam `null` se não encontrados:
```javascript
try {
  // Extração do campo
} catch (error) {
  campo = null;
}
```

### Monitoramento de Falhas
- Alertas de falha no Step 1 (nenhum anúncio encontrado)
- Alertas de falha no Step 2 (botões não encontrados)
- Notificação de falhas críticas
- Tracking de taxa de sucesso por step
- [Adicionar retry policies]

### Monitoramento

### Métricas

#### Step 1 - Descoberta
- Volume de anúncios analisados por palavra-chave
- Número de Library IDs únicos encontrados
- Taxa de sucesso de scraping
- Tempo médio de execução por palavra-chave

#### Step 2 - Detalhamento
- Número de anúncios processados
- Taxa de sucesso na coleta de dados
- Campos com maior taxa de preenchimento
- Tempo médio de processamento por anúncio

#### Step 3 - DataHub
- Eventos enviados com sucesso
- Taxa de erro no envio
- Latência da API do DataHub
- Volume de dados persistidos

#### Geral
- Cobertura de palavras-chave
- Taxa de conversão (Library IDs → Dados completos)
- Qualidade dos dados (completude)

### Alertas
- Falhas na coleta semanal (qualquer step)
- Queda significativa no volume de anúncios
- Taxa de erro > 10% em qualquer step
- DataHub indisponível
- Botões não encontrados (Step 2)
- Dados principais ausentes

## Compliance

### Termos de Uso Meta
- [Adicionar considerações legais]

### LGPD/GDPR
- Dados públicos
- [Adicionar considerações de privacidade]

## Automação

### Agendamento via Astroflow

#### Configuração do Scheduler
- **Ferramenta:** Astroflow
- **Frequência:** Semanal
- **Dia:** Terça-feira
- **Horário:** 20:00 (horário do servidor)
- **Tipo:** Scheduler automático

#### Processo de Execução
1. Scheduler dispara o fluxo
2. Loop através das palavras-chave (foreach)
3. Para cada palavra-chave, calcula últimos 7 dias
4. Loop através das datas (foreach)
5. Dispara requisição ao Bright Data
6. Aguarda retorno via webhook

### Loops Aninhados
```
foreach palavra_chave in [lista_palavras_chave]:
  foreach data in [ultimos_7_dias]:
    trigger_bright_data(palavra_chave, data)
```

### Notificações
- Webhook de retorno com resultados
- [Adicionar notificações de sucesso/falha]
- Relatório semanal de resultados
- [Adicionar outras notificações]

## Melhorias Futuras

- [ ] Expandir lista de palavras-chave baseado em performance
- [ ] Análise de sentimento dos anúncios
- [ ] Integração automática com Creator Discovery para enriquecimento
- [ ] Deduplicação automática com base histórica
- [ ] Score automático de qualificação
- [ ] Notificações para SDR quando leads hot são identificados
- [ ] Dashboard de performance por palavra-chave
- [ ] Análise de tendências de anúncios por nicho

## Referências

- [[Lead Generation - Visão Geral]]
- [[Qualificação de Leads]]
- [[Enriquecimento de Dados]]
- [[Padrão de Eventos]]
- [[Gestão de Bases Históricas]]
- [[Astroflow]]
- [[DataHub]]
- [[Bright Data]]
