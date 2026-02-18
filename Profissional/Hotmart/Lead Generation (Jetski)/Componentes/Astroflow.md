# Astroflow

## Visão Geral

Plataforma de automação e orquestração de fluxos de trabalho utilizada para agendar e executar processos de captura de leads.

## Responsabilidades

- Agendamento de tarefas (scheduler)
- Orquestração de fluxos complexos
- Integração com APIs externas
- Recebimento de webhooks
- Processamento de dados

## Fluxos Implementados

### Meta Ads - Facebook Library

#### Configuração do Scheduler
- **Frequência:** Semanal (toda terça-feira às 20:00)
- **Fluxo:** meta_ads_jetski_1step

#### Processo
1. **Loop de Palavras-Chave**
   - Itera sobre lista de palavras-chave
   - Variável: `$foreach_1.[instance]`

2. **Loop de Datas**
   - Calcula últimos 7 dias
   - Variável: `$foreach_2.[instance]`

3. **Trigger Bright Data**
   - Endpoint: `https://api.brightdata.com/dca/trigger`
   - Payload dinâmico com palavra-chave e data

#### Webhook de Retorno
```
POST https://api-astroflow.hotmart.com/v1/webhook/pjuaUoGRFV/cf5a53ef-af24-4d3a-9681-e39303c76e58
```

## Especificações Técnicas

### Endpoints

#### Webhook Receiver
- **URL:** `https://api-astroflow.hotmart.com/v1/webhook/{flow_id}/{webhook_id}`
- **Método:** POST
- **Formato:** JSON
- **Autenticação:** Via URL (flow_id e webhook_id)

### Variáveis de Fluxo

#### Foreach Variables
- `$foreach_1.[instance]` - Palavra-chave atual
- `$foreach_2.[instance]` - Data atual

### Integrações

#### Bright Data
- Trigger de collectors
- Recebimento de resultados via webhook

#### DataHub Tracking API
- Envio de eventos estruturados
- Persistência de dados de leads

## DataHub Integration

### Endpoint
```
POST https://tracking-api.hotmart.com/rest/track/event/json
```

### Webhook Step 3 (Meta Ads)
```
POST https://api-astroflow.hotmart.com/v1/webhook/IfpezpSiez/dd310c8b-7953-4cc4-b817-cb22167564e7
```

### Transformação de Dados

O Astroflow transforma dados recebidos dos scrapers em eventos estruturados para o DataHub:

```javascript
var meta_ads = {{$trigger_webhook_1}}
var eventos = []

meta_ads.forEach((item) => 
  eventos.push({
    "system": "lead_generation",
    "entity": "meta_ads",
    "action": "script",
    "event_version": "1.1",
    "data_version": "1.0",
    "event": {
      "announcerIgFollowers": item.announcer_ig_followers ?? null,
      "adUrl": item.ad_url ?? null,
      "adDescription": item.ad_description ?? null,
      "announcerName": item.announcer_name ?? null,
      "instagramHandle": item.instagram_handle ?? null,
      "announcerFbId": item.announcer_fb_id ?? null,
      "announcerFbCategory": item.announcer_fb_category ?? null,
      "adDate": item.ad_date ?? null,
      "adStatus": item.ad_status ? item.ad_status.replace(/(\w+).*/, '$1') : null,
      "keyword": item.keyword ?? null,
      "dateFilter": item.date_filter ?? null
    }
  })
);

return eventos
```

### Estrutura de Evento DataHub

- **system:** Identificador do sistema (lead_generation)
- **entity:** Entidade rastreada (meta_ads, signup, etc.)
- **action:** Ação realizada (script, manual, etc.)
- **event_version:** Versão do formato do evento
- **data_version:** Versão dos dados
- **event:** Dados específicos da entidade (camelCase)

## Configurações

### Scheduler
- Timezone: [Adicionar timezone]
- Retry policy: [Adicionar política]
- Timeout: [Adicionar timeout]

### Webhooks
- Formato: JSON
- Compressão: Desabilitada (uncompressed_webhook: false)
- Autenticação: Via URL

## Monitoramento

### Métricas
- Execuções bem-sucedidas
- Falhas por tipo
- Tempo de execução
- Volume de dados processados

### Logs
- Início de execução
- Cada iteração do loop
- Chamadas a APIs externas
- Recebimento de webhooks
- Erros e exceções

### Alertas
- Falha na execução agendada
- Timeout em integrações
- [Adicionar outros alertas]

## Tratamento de Erros

### Retry Policies
- [Adicionar políticas de retry]

### Fallback
- [Adicionar estratégias de fallback]

### Notificações
- [Adicionar canais de notificação]

## Roadmap 2026 (Tech Summit)

### Iniciativas Planejadas
- **Nova Arquitetura de Agentes**: Suporte a multiagentes
- **Construtor Facilitado de Agent**: Interface simplificada para criação
- **Uso dos Steps como Tools**: Reutilização de steps como ferramentas
- **KB Dinâmicos**: Knowledge bases dinâmicas
- **Workflow Builder AI**: Construtor de workflows com IA
- **Rascunho e Versionamento**: Controle de versões de workflows
- **Melhorias nas Integrações**: Expansão de conectores

### Objetivo Estratégico
O Astroflow em 2026 tende a ter as principais funcionalidades que hoje ainda fazem alguns times usar o n8n, reduzindo muito a complexidade operacional e facilitando a adoção de forma ainda mais orgânica, quebrando as principais objeções.

### Ferramenta-Chave
O Astroflow será a ferramenta-chave para a automação e organização do ciclo de vida dos dados, conectando fluxos de agentes e ferramentas em uma só plataforma.

## Melhorias Futuras

- [ ] Dashboard de monitoramento
- [ ] Alertas proativos
- [ ] Substituir completamente o n8n
- [ ] Implementar todas as features do roadmap 2026

## Referências

- [[Meta Ads - Facebook Library]]
- [[Lead Generation - Visão Geral]]
- [[DataHub]]
- [[Tech Summit 2026]]
