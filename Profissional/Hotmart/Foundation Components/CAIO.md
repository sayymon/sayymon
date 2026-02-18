# CAIO - Agente de IA de Atendimento ao Cliente

## Visão Geral
Agente de inteligência artificial focado na resolução de tickets e atendimento ao cliente (creators e buyers) da Hotmart.

## Contexto
- **Apresentado por**: Leandro Pereira, Lucas Pestana, Italo Chesley
- **Evento**: [[Tech Summit 2026]]
- **Área**: CX Products (Internal Platform)

## Fluxos Implementados

### Atendimento a Creators
1. **Troca de email de compra**
2. **Importação de alunos no Club**
3. **Triagem da Troca de Titularidade BR**
4. **FAQ e suporte geral**

### Canais Disponíveis

#### Chat BW (Backoffice Web)
- Nacional e Internacional
- Disponibilizado para 100% dos creators ativos
- Liberação gradual como N0

#### WhatsApp
- Mecanismos de autenticação implementados (não existia antes)
- Beta em andamento com 40 creators
- Expansão planejada

#### Email
- Em desenvolvimento
- Creators e buyers
- Substituirá atendimento da Claudia / BPO

### Internacionalização
- **EN** (Inglês): Disponível
- **ES** (Espanhol): Disponível
- **PT** (Português): Disponível

## Apostas Mapeadas 2026

### Expansão de Canais
- [ ] Encerramento chat async para creators
- [ ] Unificação dos widgets via Orquestrador
- [ ] Expansão para emails (creators e buyers)
- [ ] CAIO como N0 para troca de email de compradores
- [ ] CAIO como N0 para importação de alunos
- [ ] Ativação CAIO como N0 no WhatsApp

### Melhorias
- [ ] Insights de melhoria via CAIO Admin
- [ ] Maior cobertura de casos de uso
- [ ] Integração com mais sistemas

## Arquitetura

### Integração
- APIs de comunicação via [[C3PO]]
- Base de conhecimento (RAG)
- Sistemas internos (Club, Accounts, etc.)

### Colaboração Cross-Área
Atuação conjunta entre:
- CX
- CX Products
- Data
- IA
- Club
- Outras áreas conforme motivo de contato

## Tecnologias

### IA/ML
- RAG (Retrieval-Augmented Generation)
- NLP (Natural Language Processing)
- Modelos de linguagem

### Comunicação
- [[C3PO]] (centralização de comunicação)
- WhatsApp Business API
- Email
- Chat Web

## Benefícios

### Para Creators
- Atendimento 24/7
- Respostas rápidas
- Múltiplos canais
- Suporte em 3 idiomas

### Para Buyers
- Resolução rápida de problemas
- Acesso fácil
- Experiência consistente

### Para a Organização
- Redução de tickets humanos
- Escalabilidade
- Economia de custos
- Melhor experiência do cliente

## Métricas

### Cobertura
- 100% creators ativos (chat BW)
- 40 creators (beta WhatsApp)
- Expansão contínua

### Eficiência
- Resolução automática de casos comuns
- Redução de tempo de atendimento
- Liberação de equipe para casos complexos

## Relacionado
- [[Tech Summit 2026]]
- [[C3PO]]
- [[Internal Platform]]
- [[CX Products]]
- [[Hotmart AI]]

## Tags
#ai #customer-service #chatbot #automation #cx
