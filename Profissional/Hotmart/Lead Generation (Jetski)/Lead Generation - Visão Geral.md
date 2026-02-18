# Lead Generation (Jetski) - Visão Geral

## Sobre o Time

**Nome:** Lead Generation (Jetski)  
**BU:** Growth  
**Missão:** Estruturar e otimizar os fluxos de geração de leads, trazendo resiliência, automação e eliminando dependências de processos manuais (planilhas)

## Papel como Staff Engineer

- Tornar os fluxos mais resilientes
- Eliminar dependências de planilhas
- Trazer uma pegada de engenharia robusta
- Garantir escalabilidade e manutenibilidade dos sistemas

## Fluxos Principais

### 1. [[Inbound - Typeform]]
Leads que chegam através de formulários Typeform, integrados ao AstroboxAutomations via webhook, com qualificação automática (Paid, Organic, Cold).

### 2. [[Signup - Plataforma Hotmart]]
Usuários que se cadastram na plataforma, passando por processo de qualificação e enriquecimento usando Creator Discovery para extração de dados do Instagram e outras redes sociais.

### 3. [[Outbound - Extração e Enriquecimento]]
Fluxo de captura de leads através de listas da internet (SEO, sites de concorrentes como Kiwify, Hubla), processados pelos componentes:
- **api-lead-outbound-extractor** (Extrator)
- **api-lead-outbound-enricher** (Enriquecedor/Orquestrador)

### 4. [[Meta Ads - Facebook Library]]
Captura semanal de leads através da biblioteca de anúncios do Facebook, identificando creators investindo em tráfego pago nos últimos 7 dias.

## Bases de Dados

- **Bases Históricas:** Armazenamento de todos os leads processados
- **Utilização:** Reutilização pelos times de SDR e LDR

## Estrutura de Documentação

```
Lead Generation (Jetski)/
├── Lead Generation - Visão Geral.md (este arquivo)
├── Fluxos/
│   ├── Inbound - Typeform.md
│   ├── Signup - Plataforma Hotmart.md
│   ├── Outbound - Extração e Enriquecimento.md
│   └── Meta Ads - Facebook Library.md
├── Componentes/
│   ├── api-lead-outbound-extractor.md
│   ├── api-lead-outbound-enricher.md
│   ├── AstroboxAutomations.md
│   └── Creator Discovery.md
├── Processos/
│   ├── Qualificação de Leads.md
│   ├── Enriquecimento de Dados.md
│   └── Gestão de Bases Históricas.md
└── Arquitetura/
    ├── Visão Técnica Geral.md
    ├── Integrações.md
    └── Resiliência e Monitoramento.md
```

## Próximos Passos

- [ ] Documentar especificações técnicas de cada fluxo
- [ ] Mapear integrações e dependências
- [ ] Definir métricas de resiliência
- [ ] Estabelecer processos de manutenção
