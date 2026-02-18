
O Tech Summit de 2026 foi em fevereiro do dia 02 ao dia 06

Fui de aviao no dia 02 bem cedo do  Aeroporto de Guarulhos até o aeroporto de Cofins, passei por uma experiencia que vai servir como história que foi ficar rodando sobre BH por 30 minutos aguardando a autorizacao para pousar e uma camada bem densa de nuvens que parecia Neve, fiquei hospedado no Hotel Mercure Lourdes na Av do Contorno

Combinei com o André Maia de encontrar ele para conversar e falar sobre o projeto de Lead Generation frentes de Signup, inbound e Outbound que estou trabalhando para automatizar e tornar uma arquitetura escalavel

Além disso combinei com o Gabriel Viana Vulgo GG de nos encontramos e trocar ideia

No primeiro dia consegui antecipar o checkin, me hospedei e me preparei para ir até a Hotmart, sai por volta das 15hs

Cheguei na Hotmart por volta das 15:15 encontrei algumas pessoas, como o Lucas Miranda, Gabriel Snake e o Alisson Lara no 5º andar cumprimentei eles compartilhei um pouco como foi a viagem e até que dia ficaria hospedado.

Depois disso sentei proximo ao novo time que estou entrando de Data, encontrei o Marcelo Szostak do qual conversei com ele e fui apresentado ao Cristian Silva Staff Engineer no time de DAPR - DATA ENGINEERING

Conversamos um pouco compartilhei com eles o que venho trabalhando junto com os meninos Gustavo e Ayrton.

Depois disso encontrei o André Maia conversamos previamente sobre viagem e hospedagem, depois o André foi direto ao ponto compartilhando como estava sendo a migracao do fluxo antigo de Inbound que era no Zapier e planilhas para o novo fluxo que desenhamos juntos e implementamos utilizando o Astroflow eventos e soluções do time de Data.

Alem disso o ajudei a ajustar alguns Bugs e depois extrai e processei uma lista de 1.6 milhoes instagrams para serem processados dentro do Creator discovery.

Feito isso voltei para a baia proximo ao time de Data e retornei para o Hotel do Qual conversei com a minha Familia KGNS compartilhamos como foi o dia

Jantei no Hotel no primeiro dia comi um Bife muito bom com um molho muito bom chamado roti que é um clássico da culinária francesa

2º dia acordei relativamente cedo fiz os meus abdominais diarios

Me troquei e fui tomar meu café da manhã no Hotel, uma variedade de coisas mas para manter a minha dieta e forma optei por um bom omelete, batata doce, ovo cozido café leite e uma salada de frutas e foi o que comi todos os dias corriqueiramente.

Chegando na Hotmart no dia 03/02 encontrei com o Maycon Costa do qual já foi meu cordenador no time de Core API em Software Foundation, conversamos sobre varios assuntos incluindo a mina primeira vez do evento ele compartilhou que o evento é muito bom para trazer uma visao mais holistica das iniciativas e estrategias de varios times, e conectar a todos com a empresa e ter um senso de pertencimento

Das 8h-9h: Café da Manhã (3º andar) tinha uma estrutura de café da manha top, acabei só admirando pq tinha muito pao e carboidratos e optei em ficar só admirando mesmo.

Por volta das 9h-9h30: foi a Abertura do Evento onde se iniciaram as apresentacoes, o nosso Vice presidente Felipe Silvestre(Silver) fez a abertura trouxe com muita alegria e entusiasmo o proposito principal que o evento desde 2024 tem essa caracteristica principal de trazer um ambiente seguro e de extrema conexao e compartilhamento de conhecimento e estratégias.

Onde todos esses topicos estao conectados com os propositos de manter a plataforma ainda mais disponivel estável e rapida

Principais topicos que ele trouxe foram : 

[[OKRs Globais da compania]]
[[OKRs de Tech e Programas]]
[[Goal Settings]]


Quando foi as 9h30-10h30: o Tups (Leonardo Dornellas) apresentou a Visao geral de Estratégia Club , falou da missao de empoderar os creators através do Club  e que a visao é de fazer empreendedores nascerem e crecerem através da Hotmart, e que o Hotmart Club esta com tres principais pilares o de [[BUILD]] [[CONNECT]] e [[AMPLIFY]]

BUILD
Abstrair a complexidade de se criar e testar produtos e experiências baseados na autoridade do creator


CONNECT
Aproximar creators e consumidores transformando conexão e personalização em oportunidades de crescimento


AMPLIFY
Construir jornadas que amplificam a experiência de consumo em momentos nativos de venda para o creator


E que o Club esta se preparando para o Spark que vai ser um evento incrivel agora em Q1 de 2026 em Sao Paulo


Na sequencia tivemos o Diego Campos do time do Club apresentando como vai ser a parte de Build

Dentro de build tem algumas squads Books, PF - Foundation, Expansion, Product Gen , Content Studio e o Club Setup

Para o Sparkle o time do club está focando em manter a plataforma solida , principalmente em relacao a parte de pagamento , acelerar novos canais de crescimento , usar AI para melhorar a experiencia e trabalho dos creators usando o Club, aumentar a presenca do club em todo o ciclo de venda e criacao de conteudo dos creators e ser o time de tecnologia rapido confiavel e inovador

Na sequencia o Marco Aurélio (Matador) Principal na Hotmart e o Charles Silva (Charlin)  Staff engineer compartilharam alguns dos desafios técnicos dessa parte de Build

Trouxeram a solucao de hierarquia flexivel que esta sendo adotada no club para resolver alguns problemas com a rigides atual da estrutura de Produto -> Turmas -> Modulos, onde um produto era obrigado a ter N turmas e a turma ter acesso a apenas aquele produto, e os modulos necessariamente eram criados e replicados entre turmas e isso gerava um esforco e trabalho, onde a solucao nova vai permitir esse reuso e uma diminuicao em volume de novos modulos e turmas criadas inclusive facilitando a gestao dos creators

A tecnologia escolhida foi o Neptune da AWS com um banco orientado a Graph que inclusive é muito util em cenarios de leads pensei inclusive futuramamente de termos isso por nicho

Outra abordagem que estao usando é do Edge Cache uma solucao para otimizar a entrega através de um cache de CDN localizado o mais proximo da solicitacao cacheando dados que antes tinha que ir até virginia e ohio, basicamente trocando a url que batia em um ELB para o CDN que já esta no contexto do front tiveram um reducao medi por chamada de 100ms de latencia com isso, e tbm elminando a necessidade de chamadas de options pois agora o CORS prefligth é adotado

Entre outras de BUILD iniciativas como 

Update wildfly para a versão 26 e jdk 17
Reestruturação do app-space
Performance Club Admin
Depreciar o club-api (início)
Gestão de membros/usuários
Processo de deploy com adocao de uso do Canary

Na sequencia o Victor Freitas gestor de desenvolvimento do time do Club abordou a parte de Connect, trazendo qual a estratégia de conectar os creators aos consumidores

Eles sao organizados em algumas squads : 

Club Plataform, Player, Agent as a Product, LEX (Club AI) , Creator Inteligence

Cada um com uma atuacao mas todos conectados literalmente com esse propósito

Para o [[Spark 2026]] o time esta com foco em expandir o foco e possibilidades para os creators utilizar a AI além do suporte nos produtos com o Tutor AI, mas tambem ter uma solucao que olha para todos os produtos do creator e ajuda o atuar de forma holistica para todo o seu negocio dentro da Hotmart

Além disso analisando Iteracoes e gerando insigths para novos produtos ou melhorias nos produtos atuais

o time de Agent as a Product serao os pioneiros a usar a nova arquitetura de agentes , e tambem implementar o Workflow de agentes que é um novo segmento e nicho que vai entrar em assencao dentro da Hotmart e na creator economy.

Outro ponto interessante que achei é o Onboarding novo, logo após o Signup agora vai ter uma anaminese que vai coletar mais informacoes e vai fazer uma analise personalizada daquele  usuario seja Creator ou Buyer, afiliado ou coprodutor para criar uma experiencia personalizada

Alem de criar um guia e insigths do que fazer dentro da plataforma pendencias coisas prioritarias vai ser uma inovacao e tanta dentro da plataforma

Sobre Amplify o Samuca que puxou os principais pontos que envolvem a construcao de jornada do creator que amplificam os motivos e condicoes de venda para o creator

Tem alguns times envolvidos : 

App Experience
Community
Access
Smart Channels
Repurchase experience

Para o Sparkle eles estao criando mecanismos para ir nutrindo o Lead dentro da plataforma, e tem o conceito de uma vez Lead sempre lead que é muito da estratégia que nos temos no teame de Lege Generation mas na perspectiva do Lead como creator

Creators de 8d (Oito digitos) vao poder usar agora o Hotmrt Recomenda 

Centralizacao de acessos com o CAD tende a reduzir em 60% o volume de tickets do time e liberar eles para evolucao e nao manutencao

O Danilo Segura AI Manager que conheci no Kickoff de 2025 iniciou a apresentação proximo das 10h30-11h30 falando da estratégia de AI Estratégia AI e Programa AI Platform

Ele trouxe a evolucao desde 2023 com o Hotmart AI até a versao atual do Hotmart AI v2 lancado no final de 2025

Com destaque teve a migracao de tecnologias como de Java para Python uso do Lhama Index, Guardrails integrados ao Bedrock policys, possibilidade de fallback automatico, tracking e Loggin melhorado e uma assensao na adocao de Rag facilitada com embdings e o Vector DB otimizado

Visao agora para 2026 é muito na linha de agregar o LangFuse na arquitetura e prover um contrato unificado e melhorado para abstrair complexidades com modelos e tambem prover features de selecao automatica do modelo caso o prompt ou completions seja mais simples ou complexa

Com o lancamento do AWS Agent Core eles tem a possibilidade de melhorar inda mais a arquitetura junto ao LiteLLM e a nova arquitetura vai usar dessa nova estrutura

Depois foi a vez do Thiago fonseca compartilhar os detalhes dessa nova arquitetura, desafio do vector DB e como eles conseguiram escalar o uso de RAG mantendo performance, a questao dos Embeddings ingestion e Search

Trouxe varios topicos em perspectiva de produto como : 

- **LLM Gateway:** Possibilita usar diferentes provedores de IA com foco em controle de custo.
    - Multi Providers
    - Mensuração/Custo
- **Agent SDK:** Acelera e padroniza a criação e conexão de agentes nos produtos.
    - Multi Agentes
    - Tool Calling
- **Agent Core:** Centraliza a execução e a colaboração entre múltiplos agentes.
    - Multi Agentes
    - Tool Calling
- **Hotmart Drive:** Habilita multiagentes a lidar com arquivos e outros formatos, como áudio e imagem.
    - Multimodal
    - Multi Agentes
- **Astroflow:** Conecta fluxos de agentes e ferramentas em uma só plataforma.
    - Multi Agentes
    - Workflow / Tools
- **C3PO:** Centraliza a comunicação e integração dos agentes em multicanais.
    - Multicanais
    - Streaming
- **New Chat:** Habilita a criação de novas experiências de conversa interativas.
    - Streaming
    - Widgets
- **Memória:** Permite que agentes compartilhem contexto e aprendizados entre si.
    - Múltiplos Agentes
    - Memória Global

Tambem foi falado sobre o Hotmart Drive que vai ser uma iniciativa de redução de custo e otimização de entrega de conteudo através do CDN e storages com buckets otimizados

O Gateway Hotmart vai poder ser setado via yaml no env respectivo

O Almoco foi as 11h30-12h30 fui almocar com o Maycon Costa, Charles Silva, Gabriel Viana e o Felipe Sena(Seninha) comemos em um restaurante tipo mineiro

Retornamos para a palestra de cyber por volta 12h30-13h30 o Adriano ribeiro apresentou as Estratégias de Cyber Security para tornar a Hotmart mais resiliente e tambem preparada para ataques de diversas origens

O time é dividido por Blue Team, Red Team, NSOC , Red Team que tem como objetivo juntos principalmente habilitar que a Hotmart tenha protecao e esteja sempre disponivel e segura contra ataques e atividdes mal intencionadas.

Compartilhou que existem grupos implantando golpes diversos o principal é o de laranja as a service que procura dados de pessoas dentro de sistemas como a Hotmart dede cretors a Buyers para usar como laranjas em esquemas financeiros diversos.

Exemplo exploracao de contas Blacks da Plataforma sendo vendidas e comercializadas como fonte de lavagem de dinheiro usando o credito da Hotmart para movimentar e depois sacar o dinheiro

Comentou tambem sobre os novos CVEs e que todos os times precisam estar atentos, pois mesmo com algumas protecoes basicas de WAF e ALB interno,  ataques principalmente em apis de stacks como Java, Node e Python sao os principais alvos

Manter a maquina atualizad e cuidado com aplicacoes de terceiros rodando na maquina da empresa 

Foco nos GDVs time de Cyber vai contar com ajuda de todos para Melhoramos indicadores de seguranca , fortalecer a  parceria com os times de Engenharia e Aumento na capacidade de detecção junto com a Governança no processo de Aceite de Riscos e ter uma Melhor adequação com auditorias externas e internas

Eles comentaram que toda e qualquer iteracao com LLM devemos avaliar o uso de policys ou guardrails para mitigar alguns ataques, e que podemos envolver o time de cyper para compartilhar pontos sensiveis em busca de adocao de medidas  inclusive no time de LEGE devemos ter cuidado com injestao de dados via crawlers e tambem via Forms externos.

- **Improve Metrics** (Melhorar Métricas)
    - Migrar de métricas táticas para métricas de risco.
    - Automatizar Dashboards em Tempo Real e quantificar Risco Cibernético.
    - Otimizar MTTD, MTTR e tempo de criação de _postmortem_.
    - Criar KPIs de previsibilidade (risco futuro e exposição acumulada).
- **Security Posture** (Postura de Segurança)
    - Ampliar a adoção de _hardening_ e _baseline_ de segurança.
    - Evoluir o programa de _Vulnerability Management_ para visão por risco.
    - Fortalecer monitoramento 24/7 com mais automação e telemetria.
    - Expandir iniciativas de _pentests_ contínuos e _Red Team Ops_.
- **Security Awareness** (Conscientização em Segurança)
    - Implementar Treinamento Personalizado por Comportamento.
    - Realizar Campanhas trimestrais de _phishing_ e Engenharia Social.
    - Criar trilhas específicas para desenvolvedores, produto, suporte e recém-contratados.
    - Criar um “Security Culture Score” por BU.
- **Security Enabler** (Viabilizador de Segurança)
    - Evoluir o AppSec (_Shift-Left_).
    - Unificar processos com Anti-Fraudes usando _Threat Intel_.
    - Implementar _Self-Service Security_ e simplificar processos de segurança.
    - Participar da priorização estratégica junto a Produto e Engenharia.
- **Risk Management** (Gestão de Riscos)
    - Realizar Mapeamento de Ativos Críticos.
    - Criar comitês de risco cibernético com líderes de negócio.
    - Integrar riscos de terceiros e _supply chain_ no mapa de riscos.
    - Evoluir o processo de _Risk Acceptance_ com padronização e governança.
- **Regulatory & Compliance** (Regulatório e Conformidade)
    - Implementar Governança de Dados (_Data Discovery_).
    - Manter _compliance_ contínuo com LGPD, PCI, GDPR e regulatórios aplicáveis.
    - Mapear lacunas regulatórias emergentes (IA, operações financeiras, EMI/DORA).

Por fim comentou do programa tecnico de cyber que tem como principal objetivo em 2026


AppSec - Correção de Vulnerabilidades, Mapeamento de ativos críticos

Awareness - Treinamentos de segurança, Materiais de segurança

Diminuir o Risco -  Levar segurança para o início do Desenvolvimento, Segurança em CI/CD, 


As 13h30-14h30 o Allan Andrade tbm conhecido como Menor, meu novo gestor apresentou a  Estratégia Data Platform e Programa Encontrabilidade de Dados

Comecou trazendo um problema a tona com o aumento de dados e crescimento de tabelas e fontes de dados nos Datalakes do Datahub, que atualmente as tabelas Silver estao com mais de 8.5k de tabelas gold com 845 e diamante com 2k , e que muitos acabam duplicando e nao reusando justamente por falta de organizacao e visibilidade dificultando a encontrabilidde de informacoes resultando em retrabalho e trabalho futuro de entendimento e reorganizacao dos dados.

Com isso um dos objetivos de Data agora em 2026 é a Encontrabilidade.

Dividiram em algumas frentes 

- **Governança Conceitual**: Estabelecer um vocabulário comum que unifique a forma como dados e metadados são definidos, interpretados e aplicados em toda a plataforma.
- **Estruturação e Organização**: Organizar ativos e metadados de acordo com os padrões através de evoluções necessárias nas ferramentas que viabilizem essa organização de forma sustentável e governável.
- **Experiência de Consumo**: Garantir que usuários encontrem, acessem, compreendam e confiem nos dados.
- **Comunidade e Educação**: Desenvolver uma comunidade ativa que impulsione a criação, catalogação e o uso correto da plataforma de dados.

A estratégia para melhorar a encontrabilidade (discoverability) de ativos de dados foca na transformação da experiência de localizar, acessar e interpretar os dados, utilizando uma abordagem de estruturação e organização de metadados.

  

**Elementos-Chave da Estratégia de Metadados:**

  
A prioridade no H1 (Primeiro Semestre) inclui focar na definição e aplicação dos seguintes metadados em ativos Gold, Diamante e Prata/Eventos:

- **Domínio:** Para navegação e contextualização no mapa de _datasource_.
- **Owners:** Para definição de controle de acesso e para saber quem é responsável pelo dado.
- **Descrição da Tabela:** Para garantir que os usuários compreendam o dado e confiem nele.
- **Tags:** Para permitir uma busca mais rápida e precisa, e para enriquecimento dos ativos.

**Apoio dos Agentes e Ferramentas na Encontrabilidade:**



A melhoria desses metadados será utilizada pelas seguintes plataformas/agentes para aumentar a eficiência da encontrabilidade:

- **DataHub, Astrobox e Astrolens:** As ferramentas serão evoluídas para viabilizar a organização sustentável e governável dos ativos e metadados, além de exibir mais metadados (como Domínio e Tags) e permitir a navegação por domínios no mapa de _datasource_. O objetivo é transformar a experiência de encontrabilidade, tornando-a direta e intuitiva.
- **DataBot:** As ações visam aumentar a eficiência das respostas através da melhor contextualização e uso dos metadados.

Dentro de Data precisaremos agir em conjunto para tornar essa meta viavel de que forma, primeiramente através de documentacoes e metadados tanto no datahub-schema quanto em documentacoes dentro do Astrobox e no confluence dos times

Teremos um Heimdal de Data que vai extrair metricas dessas documentacoes para pontuar e trazer indicadores dos times sobre suas querys e datasources, ou seja documentacao sincronizada aos fluxos de negócio sao a chave para atingir esses objetivos de Data 


A Plataforma de Dados vai focar nas principais ferramentas para transformar a forma como os dados são organizados, encontrados e consumidos. tudo principalmente no DataHub, Astrolens e Astrobox

  

Como  o núcleo da estratégia de **encontrabilidade e confiança** dos dados. O **DataHub**, por exemplo, é essencial para a **Navegação por Domínios** no mapa de _datasource_, permitindo que os usuários encontrem dados de forma contextualizada. O **Astrolens** complementa ao garantir a **Visibilidade da Qualidade (Heimdall de Dados)** e a **Exibição de mais Metadados**, o que aumenta a **confiança** e o **reuso** dos ativos. O **Astrobox** e o **Cosmos** focam na experiência de consumo, tornando o acesso ao dado mais intuitivo e ágil, o que impulsiona a **adoção** contínua da plataforma com visao de nao usar o PowerBI na compania


O **Astroflow** vai ser a ferramenta-chave para a automação e organização do ciclo de vida dos dados. 

Com iniciativas como :

Nova Arquitetura de Agentes
Multiagents
Construtor facilitado de Agent
Uso dos Steps como Tools
KB Dinâmicos
Workflow Builder AI
Rascunho e Versionamento
Melhorias nas Integrações

o **Astroflow** esse ano tende a ter as principais funcionalidades que hj ainda fazem alguns times usar o n8n, e vai reduz muito a complexidade operacional, o que vai facilita a **adoção** de forma ainda mais organica quebrando as principais objecoes *** destaque

Os times de Automations Unit tem 3 frentes que sao as de Sales BR e Latan, junto com o Time de Growth

Os principais objetivos das automations Units divididos por Colunas de Sales BR Sales Latan e Growth o time de Sales BR e latam estaram apostando no Sales Assistant como principal ferramenta agentica para otimizar iteracao com creators afim de ganhar escala na conversao e encantamento de novos creators para a Hotmart Alem disso vai nascer o CS assistant que é para enriquecer ainda mais a experiencia dos creators dento da plataforma expandindo muito o contato com os creators e trazendo o sentimento de total suporte e direcionamento na jornada de creator O Nosso time de Growth esta com foco em tornar todo o processo de prospeccao, enriquecimento e qualificacao ainda mais potente e inovador, estamos pilotando varias frentes desde inbound, signup e principalmente outbound com abordagens de exploracao de concorrentes com foco no aumento de produtividade do time de LDR e acertividade e maior conversao de creators potenciais , alem de viabilizar um monitoramento preditivo dos creators que vao se tornar ainda mais influentes e trazer esses insigths é um diferencial e tanto, alem disso o nosso time esta em contato com tecnologias ferramentas e conceitos de exploracao de leads que podem ser compartilhados para a compania para ajudar a proteger e tornar a nossa plataforma ainda mais segura

As 14h30-15h30 o Lucas Miranda apresentou a Estratégia Software Found. e Programa Cosmos Adoption

Iniciou compartilhando a importancia do uso do ACL na plataforma para gestao de rotas e acessos

Que vai ter um Risk Score sendo executado em todos os repositórios da compania 

Security and Detection

- Isolar o Security na rede interna
- Criar Score de Segurança do Usuário
- Criar Risk Based Score para uso por demais sistemas
- Fingerprint da máquina de usuário

Esta com uma iniciativa cross de desacoplar o uso da base de dados do Markeplace (MarketplaceDB desacoupling) ou seja se tiver qualquer query ou ETL apontando de lá entenda e procure o time de data para trazer alternativas, inclusive vai rolar uma lista das queryes por complexidade que o Elton vai apresentar e que os times vao ser acionados caso identifiquem acessos a essa base

Trouxe tambem que os produtos internos de comunicacao estaram sendo utilizados em varias frentes como no tutor Club AI e em varios outros mecanismos que dependam de comunicacao via algum canal de comunicacao o C3po vai receber atualizacoes com insigths e sistemas de gestao de templates, preferencias e outras coisas potencializados com AI e muito dado de qualidade desde taxas de entrega e cliques e conversao das mensagens 

Trouxe as novidades do Cosmos o Design System que tem como propósito facilitar e otimizar o uso do Cosmos Core através do Cosmos Global, temos a implementacao do Figma MCP junto com o Cosmos AI que tem uma funcionalidade muito pratica usando as IDEs como Kiro, Cursor ou manus por exemplo ao configurar o MCP do Cosmos é possivel importar o modelo do figma com o formato do Cosmos e já criar frontends seguindo os padroes e golgenpaths da Hotmart praticamente funcionais 


Por volta das 16h-17h a Rúbia Toledo apresentou a Estratégia Agility e Portfolio Mgmt

Dando enfase para a GislAIne, que analisa as métricas de eficiencia dos times através do uso adequado do Jira considerando cadencia e eficiencia. Que para o time de Governanca e agilidade é importante o uso do Jira

Que o fluxo de Upstream é premissa para os times de produto temos acesso ao Jira Analytics que se bem usado pode ajudar a identificar gargalos e ajudar os times.

O principal desafio para 2026 é aumentar o engajamento no uso do fluxo de upstream. A baixa adesão a este fluxo tem causado a não gestão de métricas de impacto financeiro, como custo e ROI das iniciativas, e a falta de acompanhamento de métricas de eficiência, resultando em retrabalho devido a repriorizações e falhas na definição de negócio. Para reverter esse quadro, estão em andamento iniciativas como um piloto do fluxo para avaliar os motivos da baixa adesão e destravar o entendimento de valor das boas práticas de desenvolvimento para as Lideranças, além da implementação de Agentes de Product Framework e módulos da ferramenta Agilene. *** Destacar isso com o time de LEGE - Growth

O engajamento da equipe é de extrema importância para o sucesso, pois o fluxo de upstream não visa travar, mas sim simplificar, automatizar e garantir a segurança do negócio, que cresceu e possui exigências fiscais e de governança globais. A equipe pode ajudar de forma direta garantindo o uso correto dos itens de _backlog_, melhorando a documentação dos épicos e estabelecendo uma maior parceria com os times de Produtos. O propósito é justamente simplificar e deixar apenas o que gera segurança e previsibilidade, impulsionando a eficiência e os resultados.

O Bruno Mendonca toca as frentes de Tech Data Ops & Community e Programa Hotmart JedAI 

Compartilhou como os principais highlights a Organização e acompanhamento dos Programas Técnicos e definição de critérios de sucesso, 
Vai rolar um acompanhamento dos OKRs globais e estratégicos das áreas compartilhando constantemente com os gestores e principalmente com os times.

Comentou da gestão da iniciativa Hotmart JedAI, especificamente para a VP de Tech.
compartilhando a evolução e fortalecimento do Chapter de Tech como é possivel a evolucao do suporte e realização de eventos importantes como Product Sessions e Tech Summit.

Para community teremos varios eventos durante o ano com foco em fortalecer o senso de pertencimento e colaboracao entre os times.

**Community para 2026** visam o **Fortalecimento do senso de pertencimento e colaboração entre os times**, impulsionando a formação, o desenvolvimento de carreira e o orgulho de fazer parte, e incluem:

- **Hot Hackers:**
    - _All Hands Tech_, _Hot N' Code_, _Hell Code_, _Guest_, Treinamentos e _Hacker Academy.
    - _Pod&Dev_.
    - _Hot N’ Code Conference_.
    - _HackWeek_.
    - Programa de Estágio.
    - Iniciativas para posicionamento externo.
- **JedAI:**
    - _AI Talks_.
    - Trilhas de Desenvolvimento e _AcademIA_.
    - Mais novidades em breve.
- **Comunidade de Dados:**
    - Em construção.

Por volta das 17h e 18h: JedAI para Tech o Bruno Mendonca fez uma breve intrudocao falando das conquistas de 2025 com  o aumento de acessos concedidos a ferramentas de suporte a Codificacao como Cursos, Amazon Q e Kiro

Casos de uso sendo compartilhados SARA (Agente de Suporte a Tickets com RAG), Bifrost Ferramenta para execucao de receitas para atualizacoes de libs e migracoes de versoes

A SARA o Case 1 foi descrita pelo Wallace Oliveira descrita como um **braço operacional** que assume tarefas mecânicas dos times, liberando a equipe para se dedicar a atividades que exigem mais análise, estratégia e criatividade.
 
- **Resolução de Tickets:** Resolveu 27,5% de todos os tickets de Financial Services (FS) desde Dezembro de 2025.
- **Economia de Horas:** Economizou 1024 horas dos Desenvolvedores, representando um salto de eficiência de 24,5%.
- **Redução de Tempo:** Reduziu o _Lead Time_ (Tempo de Espera) para 12 tipos de Serviços Mapeados para apenas 1 dia, e também reduziu em 38% o Tempo de Fila dos Tickets.

Um ponto interessante foi especificamente a integração com o Jira através do Wall-E ferramenta herdada do time do eNotas

Na sequencia o Jonatas Soares (Jowjow) compartilhou o César Morais  do time do Heimdal

O Bifrost é uma solução de inteligência artificial que nasceu como campeã do Hackathon de 2025 com o propósito claro de reduzir o esforço operacional dos times de desenvolvimento. 

Ele se concentra em resolver problemas que exigem a atualização de código em múltiplos contextos ou repositórios, agilizando processos que seriam demorados e repetitivos para os desenvolvedores. 

Seu mecanismo interno se baseia na implementação de assistentes de programação provisionados, o que podemos entender como agentes de desenvolvimento com um alto poder de processamento. 

A arquitetura do Bifrost se apoia em um modelo que pode ser trocado (atualmente via Bedrock Gateway Sonnet 4.5), e sua metodologia é incremental e 100% definida internamente: o processo começa com a documentação da alteração necessária, a criação de uma _Issue_ no repositório do Bifrost no **GitHub** definindo um repositório alvo, e a subsequente execução de um Code Analysis. 

Essa esteira envolve módulos como o Code Builder e o Code Tester. 

A grande sacada do Bifrost é sua poderosa integração com o **Heimdall**. Enquanto o Heimdall atua na avaliação e indicação de problemas predefinidos (_findings_), o Bifrost entra em ação para resolver qualquer problema bem documentado.

Isso significa que a resolução em massa dos _findings_ identificados pelo Heimdall se torna um dos casos de uso mais fortes para o Bifrost, transformando o problema detectado em uma Pull Request aberta e pronta para ser avaliada no **GitHub**, possibilitando até mesmo a abertura em massa dessas alterações em outros repositórios, após o ciclo inicial de análise e melhoria da documentação. 

Isso libera o tempo dos especialistas em determinada área, permitindo que eles se concentrem apenas na revisão final da solução proposta.

Trocando ideia com o Marcelo Leite posteriormente fiquei de fazer uma receita para ajudar nas migracoes do event-agent e tambem a apoiar ele na mensuracao de ganhos se os times migrarem para o novo event-agent

Na sequencia tivemos um churrasco junto ao time de Data, do qual encontrei algumas pessoas como o Michel Ribeiro (Mimi)  do qual conversamos sobre o time de Lead Generation e iniciativas de Growth, encontrei o Gustavo de Faria Lima, encontrei o Marcelo Leite, Marcelo Szostak, falei com o Fernando Bretz (Fefe), Judith, Ana Luisa Sossai, Humberto Morais(Bertao) , o Gabriel Viana com todos consegui conversar falando sobre as iniciativas. Conversei tambem com o Vinicius Fernandes, e Bruno Faria sobre o N8N e como e quando o Astroflow vai conseguir atender as necessidades superando e equiparando as funcionalidades

Fiz o Social e por fim conversei com o Allan Andrade e o André Maia sobre estratégia de growth e resultados que estamos alcancando com os fluxos de outbound, inbound e signup

Depois disso fui para o Hotel descancar do dia intenso e me preparar para o outro dia

No outro dia fui para o Evento encontrei o Valter Pereira do qual compartilhei a iniciativa de apresentarmos no Hot'code a frente de LEGE com as ferramentas e iniciativas quemos para captura de creators para a Hotmart e que podemos junto com o time de Cyber montar uma apresentacao bacana para compartilhr um pouco disso e impactar os times com as tecnicas exploradas

Encontrei o Danili Segura do qual conversamos sobre a palestra dele do dia anterior e tambem compartilhei sobre o Moltbot que esta em assencao e logo mais podemos internalizar essa ideia para os troopers. Alem disso alguns navegadores como o Commet da Perplexity e o Atlas da OpenAI estao tornando a automacao de tarefas em navegadores algo muito pratico e funcional

Iniciou o segundo dia de palestras por volta das 9hs com o Arley Campos falando sobre Growth Products

Apresentou a visao Its time to make things happen

Em busca de mais Creators com habilidades para construir, monetizar e gerir negócios digitais, o time pretende prover as ferramentas para acelerar a estruturacao do negócio para escalar as vendas, com uma conversao e retencao muito melhor dados as inovacoes e plataforma integrada com jornadas eficientes.

Ter Maior LTV com creators mais engajados e direcionados através da plataforma

Falou sobre a frente e time de PXP Plataform Experience

Fazer da plataforma da Hotmart uma vantagem competitiva, acelerando a jornada dos creators, impulsionando adoção de produtos, aumentando retenção e crescimento mútuo.
Nosso objetivo é ampliar o moat da Hotmart por meio de experiências simples, consistentes e encantadoras.

Mais Creators × Mais Produtos × Maior Adoção × Melhor Retenção × Maior LTV + Operação Saudável

o time de PXP tem algumas squads que sao as seguintes Activation Engagement , IA companion Rebase e alguns times cross

Apresentou as metricas de sucesso e objetivos do time de PXP

- Fazer da plataforma Hotmart uma **vantagem competitiva**, acelerando a jornada dos creators, impulsionando a adoção de produtos, aumentando a retenção e o crescimento mútuo. O objetivo é ampliar o _moat_ da Hotmart por meio de experiências simples, consistentes e encantadoras (Slide 6).
- **Objetivo Específico (Objective 1):** Traduzir a proposta de valor da Hotmart no processo de Onboarding, permitindo que mais Novos Produtores testem sua adequação ao mercado e atinjam o marco de **USD 200 em vendas** nos primeiros 30 dias após o cadastro (Slide 8).

Este objetivo específico é medido por Key Results (KRs) como:

- **KR 1.1:** Aumentar a conversão de _Sign-ups_ para Novos Produtores com produtos disponíveis para venda em 5 dias.
- **KR 1.2:** Aumentar a conversão de _Sign-ups_ para Novos Produtores com uma venda em 10 dias.
- **KR 1.3:** Aumentar a conversão de _Sign-ups_ para Produtores Ativados em 30 dias.

Alguns indicadores do time de PXP 

330K 
média de SignUps na plataforma nos últimos 3 meses

1.5MM média de pageviews na home da plataforma
nos últimos 3 meses

350K 
média de pesquisas no menu da plataforma 
nos últimos 3 meses

As prioridades do time de **Platform Experience (PXP)** para o **Q1** (Primeiro Trimestre) estão estruturadas em três pilares principais, com foco em otimizar a experiência do creator e impulsionar a adoção de funcionalidades:**Prioridades do PXP para Q1****1. Activation (Ativação)**

  
Foco em simplificar e otimizar a jornada de compra e configuração inicial, visando a ativação mais rápida dos novos creators.

- **Checkout Config:** Melhorias na configuração do checkout.
- **Checkout Turbo:** Otimização para um processo de checkout mais rápido e eficiente.
- **End to end journey (Jornada Ponta a Ponta):** Garantir uma experiência fluida e completa desde o cadastro até a primeira venda.

**2. Engagement & Retention (Engajamento e Retenção)**
 
O objetivo é reter o creator e mantê-lo engajado com a plataforma, garantindo que ele utilize as ferramentas que potencializam seu crescimento.

- **Performance Component 2.0:** Projeto para aumentar o _awareness_ (consciência) e _adoption_ (adoção) de ferramentas-chave, como:
    - Fast Buy (Compra Rápida).
    - Insights Club (Tutor).
    - Sales Agent (Agente de Vendas).
    - Collections (Cobranças).
    - Parcelado Hotmart e Vendas Internacionais.
- **Descomissionar Home Antiga:** Substituição da versão anterior da página inicial para garantir que todos os usuários estejam em uma experiência mais otimizada e com as novas funcionalidades.

**3. AI Companion (Assistente de IA)**
 
Introdução de uma inteligência artificial para servir como um assistente pessoal, acelerando a jornada do creator.

- **Hotmart IA Companion (MVP):** Lançamento do Produto Mínimo Viável (MVP) do assistente de IA, que atuará como um **concierge** para orquestrar agentes especialistas e guiar o creator no caminho mais eficaz para a ativação.

O time de New Personas conecta muito com o time de LEGE generation , **

Com foco em Expandir o crescimento da Hotmart identificando e ativando novos públicos com alto potencial na Creator Economy, usando Product-Led Growth como motor de aquisição, ativação e retenção.

Nossa missão é descobrir e priorizar o TAM, dentro e fora da Hotmart, para acelerar a fórmula de crescimento.  Compartilhar com a Julia Athayde as iniciativas e como o time de LEGE pode ajudar e conecar com esse time

Temos o time de Account Collaborators Center Afilliates e CRI

O Flávio Tavares e o Gabriel Balbio da apresentaram o case de All In One para otimizacao de carregamento da pagina da Home da Hotmart

Onde conseguirma otimizar muito usando cache e eliminando consultas demasiadas no astrobox do qual trouxeram muito mais estabilidade simplesmente adicionando um Redis no meio , e tambem agrupando os dados e retornando de uma vez ao invés de varias chamadas

Pois a Home é a primeira impressao do Creator com a plataforma entao ser rapido estavel e encatadora é uma das premissas do time

Depois disso o Jackson Duarte apresentou a iniciativa do Hotmart AI Companion
eles estao focando no fluxo de ativacao dos **330 mil novos creators mensais, mas apenas 0,41% atingem a Ativação**

Comentou que alem disso tem Bots e Agents sendo criados mas sem uma sinergia e acoes cordenadas e direcionadas para os creators exemplo o CAIO que é um agente focado em FAQ

o Jackson apresentou o Concierge - Hotmart AI

O objetivo principal é evoluir a experiência do Creator com Inteligência Artificial, transformando a interação na plataforma:
Interface Conversacional Única: A meta é ter uma única e transparente interface conversacional que acelere a ativação e o direcionamento do creator.
Fim dos "Chatbots Isolados": Mudar a percepção de "vários chatbots" para uma interface conversacional inteligente centralizada.

O Papel do Hotmart AI: O Hotmart AI será o fio condutor da jornada do Creator.
Como Ele Vai Ajudar:
Assistente Pessoal: Ele atuará como um assistente pessoal inteligente.
Orquestração de Agentes: Ele será o "concierge" que orquestra agentes especialistas (como Club, Sales, etc.), direcionando o creator para o melhor caminho e para o agente correto, garantindo que o usuário avance em sua jornada de maneira mais rápida e eficaz.

Dependen da Nova arquitetura de agentes com o projeto de Dinamic agents que esta sendo construido pelo time do Gabriel Viana e liberado até o fim do Q1

Neste dia o ALmoco foi rapido nesse dia Almocei com o proprio Gabriel Viana do qual conversamos sobre o desafio dele, ele tinha uma reuniao do qual conversei com o time que esta atuando com os CS eles estao querendo criar uma plataforma para gestao do ciclo de atendimento dos Creators com mais de 100k demos algumas sugestoes eles queriam usar o Bubble para desenvolver eles mesmos , ms recomendamos implementar um microfrontend no backoffice da plataforma da Hotmart para garantir seguranca e reuso futuro

Voltando para o evento, encontrei com o Gabriel Snake e o Lucas Miranda eles comentaram da iniciativa do Cosmos que eles etao super empolgados em democratizar a criacao de front ends usando o figma

Voltamos as palestras o Vagner Clementino com a nova cordenadora do time de Afiliados a Júlia Pontello falaram sobre o programa de débitos tecnicos e como o time de Afiliados precisa encarar esse desafio dado o contexto atua deles de aplicacoes legadas uso massivo da base legada do marketplace

o Elton na sequencia falou sobre a importancia do Low Coppling trouxe a quantidade de consultas ainda que usam a base legada do Marketplace e que a estratégia vai ser a de Strangler Fig Pattern e que quando nos identificarmos nesse cenário é o melhor a ser feito com foco em desacoplar e tornar tudo mais organico e otimizado.

O Maycon Costa na sequencia compartilhou como o time de Accounts esta fazendo issoe dos desafios encontrados até o efetivo descomissionamento de tabelas de usuarios que passaram a estar todos agora dentro de uma base centralizada do accounts garantindo ainda mais aderencia e complience com as leis de protecao de dados LGPD e GPDR

O Objetivo final é retirar a base do markeplace do centro da operacao, leituras analiticas e de relatorios  nao dependem de bases transacionais 

Fizeram alguns finds para buscar e analisar quais sao os principais ofensores e classificaram entre facil, medio e de dificil, onde facil é para informacoes que o account já tem endpoint e pode ser usado sem complexidade e mudanca residual de código e logica de negocio

Medias onde demanda um entendimento e segregacao da consulta e chamada de api e precisa de uma refatoracao

Dificil fluxos totalmente dependentes que precisam de uma reearquitetura e remodelgem mais completa para conseguir entregar os dados de forma segura e escalavel

Depois do Maycon o Luis Leite Principal veio trazer como tecnicamente o Low Coupling afeta a evolucao dos sistemas e principais vantagens 

Falou sobre taxonomia dos eventos baseadas no dominio de negocio, uso do datahub como principal gestor de eventos e que tudo estej complience documentado e no modelo proposto em golden paths para eventos na plataforma

Evitar uso de Liquibase pois acaba afetando os eventos, sempre se preocupar com isso e quando necesario reprocessar os eventos com apoio do time de Data

Compartilhou tbm o padrao SAGA sendo implementado tanto no Accounts como em outras frentes, a ferramenta adotada foi o Temporal IO, explicou sobre o conceito de compensassao e que ele pode ser usado em diversos conceitos onde é necessario garantir a consistencia tnto a nivel de base de dados e eventos

Depois disso o Rafael Mayrink veio falar de Plataform Reliability, onde compartilhou que a plataforma tem mais de 40 microfront ends hj em dia, que desde 2024 eles vem trabalhando no LCP e que evoluiram de 22s para 16s em 2024, e 2025 de 16 para 6.9s

E agora o principal desafio é depreciar de vez o app.vulcano que trbalha com iframes e dificulta a adocao de SSR, bloqueando a execucao independente dos microfrontends 

O Programa de Plataform Reliability vai focar em eliminar ofensores de performance, melhorar os indicadores de LCP em P75 com o conceito de monorepo

Com foco em carregamento instantanio site mais leve e tambem menos tempo configurando projeto para coisas que precisam conversar

Deixaram claro que nao vai ser um monolito, vai ter build e deploy separado por modulo e tambem vai ter otimizacoes e premissas. Em conjunto o objetivo é atualizar as versoes do React e adocao massiva ao Cosmos como Design System

Na sequencia perto das 16hs a Gabrielle Rioga, veio com forca falando sobre as inicativas do time de DevOps para 2026

Falou sobre Tech Reliability no foco de permitir implantacoes e mitigar problemas de desincronizacao de código e maior estabilidade em todos os ambientes da Hotmart

o Canary é uma aposta e que com o Trafic shifiting e tbm com o ArgoCD tudo isso ai se casar

Comentou que a arquitetura atual esta amarrada ao Helm e o base-module , orquestramos com o Github Actions, mais o Docker e o EKS da Aws, mas ainda temos problemas de sincronismo quando é necessário fazer um rollback  sao gerados dois pacotes e pode ocorrem em um rollback a infra aferada nao sofrer o rollback junto com o software e gerar dessincronismo

A solucao que a Gabrielle Rioga trouxe se baseia no ArgoCD como principal ferramenta  

Outra iniciativa é de expandir o uso do TeckDeck como start de criacao de recursos de forma padronizada e facilitada, como criacao de fila, recursos tudo via techdeck junto com a aplicacao

Outro ponto sendo tratado é a parte de Multregion com foco em mitigacao de problemas por exemplo em Virginia e Ohio e tambem permitir uso mais adequado de servicoes com esse suporte

O foco para 2026 será rollout do argo em produtos fisicos , garantir que a SDK da AWS esta atualizada e sincronizada em todos os projetos para habilitar o pod identify , construtor de migracao de de arquiteturas legado com o Bifrost Ex Drog para Github actions 

Tambem apresentaram a proposta de Rollout Global com o Reliable EKS, e o conceito de GitOps que vai entrar forte em 2026

Aviso importante o Drone sera desligado oficialmente em 31 de Marco

E o time de Cyber demandou para Devops a atualizacao de imagens base que afetam a seguranca global e receitas via bifrost serao executadas junto aos finds do Heimdal

Depois disso o Caio Souza de IT Governance & IAM Manager , falou sobre o JiraOps que já migrou o uso do Pager Duty e teve uma economia de aproximadamente 20k dol de licencas

Depois falou das Iniciativas de SOC NOC que conseguimos tirar a certificacao de AICPA e SOC 2 que é premissa para a teachable expandir seus negocios na Uniao européia 

Depois falou sobre o SAP , que finalmente o time de Financial decidiu investir no SAP 4/hana

E que o OKTA vai continuar expandido a centralizacoa de acessos e configuracoes OTP , atualmente temos mais de 400 sistemas integrados e temos volta de 13 mil pacessos já sendo controlados pelo OKTA

E que tem planos ambiciosos junto a ITOps para tornar o OKTA a ferramenta central de acessos, com Credencial única para os diferentes sistemas, sendo a Solução única de MFA, com  Políticas e gestão centralizados,  Recuperação de senha self-service
E até na autenticação dos equipamentos integranco com acessos biometricos no mac

Ai comecou a parte de Data Governance, comecaram a mapear os riscos e analisar os contextos de acesso a dados que cada time deve ter com ajuda dos proprios times para falarem quem pode ou nao ter acesso aos seus dados, através de querys datasources, dashboards, apis e diretórios

Na sequencia iniciou outra apresentacao do Afonso Costa(Tonhao) e do Leandro Teixeira, falando do Spark , do programa de Debito Técnicos de 2026 e da nova api FlexPay.

O Leandro iniciou falando dos três pilares essenciais: Commerce, Credit e Trust. Juntos eles garantem o processamento de milhões de compras, emissão de notas, validação de documentos, payouts, antecipações de recebíveis etc

Garantem as operações críticas da empresa.
Commerce (Motor das Vendas): Garante o processamento de milhões de compras, a emissão de notas e os payouts.
Credit (Soluções de Capital): Permite as antecipações de recebíveis.
Trust (Credibilidade e Proteção): Assegura a validação de documentos, contribuindo para a segurança e a credibilidade das transações.

Compartilharam que trabalharam em evolucao tecnologiaca para mitigar problemas de seguranca e dividas tecnicas

Falaram sobre a Sinergia do Lead Scoring o Sales Agent , o Parcelado hotmart (BNPL), expansao do mercado de parcelado 

Na sequencia o Afonso Costa(Tonhao) comecou a compartilhar o propósito da api Flex Pay, que tem como foco flexibilizar a criacao de planos principalmente para o Higth Ticket e eliminar a barreira tecnica para eles criarem planos de pagamento


O FlexPay atua como o "cérebro", definindo a gestão de planos e renegociação.
Ele é responsável por decidir as regras de "Quem, Quanto, Quando" pagar.

O HotPay Core funciona como o "músculo", executando a transação financeira.

O HotPay também garante a integração com adquirentes e a segurança PCI.


Na sequencia tivemos o Tulio Carneiro falando sobre o Sap 4/Hana e o time de Internal Platafform

O time de Internal Platafform é organizado por 4 frentes :  CX Products Financial Supports , Growth Support e Heimdall

Financial Support

Suporta a emissão de ~60 mil NFS-e mensais.
Mantém o SAP b1 operando, atendendo ˜110 tickets/mês.
Habilita que novas formas de pagamento/adquirentes e receitas tenham visibilidade contábil.
Apoia a área de negócio a estar em compliance com os órgãos reguladores.

CX Products

Mantém e evolui o nosso backoffice, a nossa "plataforma invertida".
Mantém a nossa Help Center e os demais canais de comunicação com os Buyers, inclusive o de Refund.
Cuida das apis e os canais de comunicação do CAIO, nosso agente de IA de atendimento ao cliente.

sales Support

Mantém o Salesforce operando, atendendo ˜96 tickets/mês.
Customiza telas/flows para atender as particularidades da área de negócio.
Time híbrido: 1 trooper + 2 consultores.

Dev Marketing

Mantém a nossa Home institucional em 3 idiomas.
Habilita as campanhas digitais de Growth, dentro do marketing da Hotmart.
 Mantém e evolui alguns componentes de touchpoints de ativação na plataforma (banners e market screen)

heimdall

Mantém o heimdall, o nosso farol da qualidade.
Mantém nossa status pages, que agora será o indicador de disponibilidade.
Está em fase de rollout do bifrost, nosso agente de IA de resolução de findings.


O Tulio Chamou o Jackson que tem uma expertise grande no SAP e trouxe as principais vantagens e cenario atual do time de Financial Services em relacao ao desafio de conseguir virar a pagina dos problemas devido ao Sap Businees One 

SAP Business One (B1): Focado em pequenas e médias empresas, com cobertura básica de finanças e vendas.

SAP S/4HANA: Voltado a grandes operações, oferece solução abrangente com IA, automação e análise em tempo real.

B1 tem baixa aderência aos processos da Hotmart, enquanto S/4HANA é altamente customizável para processos complexos.

A manutenção do S/4HANA é automática na nuvem, oferecendo melhor performance e escalabilidade.

B1 apresenta suporte fragmentado, dependência de parceiro para atualização e restrições tecnológicas para integrações.

Além disso o Tulio compartilhou uma nova iniciativa de Financial DataHub de ter uma frente focada em entregar dados confiaveis e de alta disponibilidade para relatorios financeiros da compania de forma organizada centralizada e principalmente confiaveis

Túlio Carneiro: Dev Sr. Manager
Jackson Duarte: Staff Engineer
Grasielle Martins: APM Consultor
Marina Santos: FSBU Consultor*
Luis Dias: Software Engineer
Carolina Pinheiro: Estrategista de Dados
Débora Maia: Analytics Engineering
Andressa Vilela: Analytics Engineering
Catharina Oliveira: Staff Analytics Engineering
Gutemberg Sousa: Controllership Manager
Thiago Barner: Tax Director
William Feller: Finance Manager*
Marcelo Garcia: Dev Sr. Manager
Rafael Narduche: Controllership Director
Karla Fernandes: Analytics Engineer Manager
Cris Vilar: Dev. Coordinator
Delma Caires: Tax
Antônio Júnior: Controllership
Lindomar Fontes: Controllership
Maggie Corassari: Controllership Specialist



Depois disso o time de Growth Support e Dev Marketing com apresentacao da Daphine Mariano trouxe , o foco em potencializar a adocao de novos creators High Potencial com as iniciativas de marketing através das campanhas , onde os usuarios que atingem acima de 10 mil após 30 dias da 1a venda serao potencializados pelos times de taxa exclusiva e gerentes de contas
, com campanhas giando para chegar nos 30k e depois 100k 

Trabalharam em varios entry points quando entra na plataforma com beneficios exclusivos e direcionamentos pra faturar ainda mais

Além disso pretendem trabalhar forte no Marketing Screen que vai trazer varias perspectivas em uma pagina trazendo uma experiancia unica e simplificada

Resultados do time de Dev Marketing NPS de 91 (com 95% dos usuários votando 10);

Geração de ~400 SHP (+R$ 10 mil reais), gerando uma receita de ~30M reais apenas no Q4’25 com encarteiramento de ~60% dos usuários (e escalando MoM);


Parceria com parceiros externos (Canva e Manychat) gerando para nossos clientes até 1M em benefícios, além de conteúdos nas redes sociais (YT, Instagram e Tik Tok);


O projeto contribuiu para o atingimento do OKR de H2’25, que fechamos com +5% (723 vs 692) em SHP;

Principais apostas Marketing Screen de uma entrega pontual em um produto escalável de ativação, capaz de sustentar múltiplas estratégias da Hotmart simultaneamente, com velocidade, autonomia e personalização.

- Estrutura para múltiplas campanhas rodando em paralelo, atendendo diferentes objetivos de negócio (ativação, retenção, upsell, engajamento).
    
- Frontend modular com Cosmos Global, baseado em componentes reutilizáveis para compor diferentes experiências.
    
- Backend orientado à configuração, permitindo cadastrar benefícios exclusivos e definir mecânicas de gamificação customizadas por campanha.
    
- Camada de dados dedicada (D-1) para consulta rápida de informações, viabilizando experiências personalizadas com alta performance.
    
- Mudança de modelo
    
1. De campanhas tratadas como projetos sob medida → para um motor de campanhas “plug-and-play”, configurável e escalável.
    
- Meta: Excelência em Time-to-Market
    
1. H1: campanhas no ar em até 10 dias úteis
2. H2: reduzir para 5 dias úteis
    
Reforcar como Highligts para a Julia Athayde e o André Maia


Na sequencia o time do Heimdall com o Tiago Cunha e o Guilherme Dantas , falaram das principais iniciativas e novas funcionalidades do Heimdal, com foco em KR score e metricas qualitativas para o time de engenharia conseguir traduzir indicadores tecnicos em coisas paupaveis para os times de produto

Evolução de Findings e Novos Dados

Sponsor para cada finding:
Qual time definiu / requisitou o finding? Quem são as pessoas de referência? 
KR para o sponsor criar a solução Bifrost? Ajudar os times evoluírem?
Disponibilizar dados do Heimdall de maneira facilitada para consumo
RDSs, Buckets, LB, Hosts, PODs, etc..
Criação de novos findings
Front-end 
Infraestrutura (Action adoption, outdate images, base-modules)
Bifrost PR Open
Deprecated and EOL Libs, images, frameworks

Outra parte importante é a visao de custos no proprio Heimdall

Foco em Custo AWS

Visão de custo no Techdeck, considerando recursos pelo uso e não apenas por TAG.
Custo diário por serviço e aplicação
Notificação de variações de custo no chat (diário)
Findings de custo:
Extended Support
Alto percentual de Idle Cost

Area de Libs utilizadas na companhia chamada Tech Radar

Teremos o Hub de OKRs Tecnicos e Globais da Companhia para ajudar nas plannings 

Na proxima apresentacao inicou com o Time de CX Products , o Leandro Pereira Lucas Pestana e o Italo Chesley 

Falaram do CAIO Agente de IA focado na resolucao de tickets, Fluxos implementados no CAIO
Troca de email de compra 
Importação de alunos no club
Triagem da Troca de Titularidade BR
Disponibilização do CAIO no contexto  internacional (EN e ES)
Liberação gradual do CAIO como N0 no chat BW (nacional e internacional) -> disponibilizado para 100% dos creators ativos
Mecanismos de autenticação para o WhatsApp (não existia na plataforma ainda)
Beta em andamento com 40 creators no canal do Whatsapp


Apostas Mapeadas

Encerramento chat async para creators, com unificação dos widgets via Orquestrador
Expansão do CAIO respondendo emails (creators e buyers), encerrando tickets hoje atendidos pela Claudia / BPO 
CAIO como N0 para troca de email de compradores e importação de alunos
Ativação CAIO como N0 no whatsapp 
Insights de melhoria via CAIO Admin

Nota: atuação conjunta entre áreas como CX, CX Products, Data, IA, Club e outras áreas a depender do motivo de contato


Outras apostas compartilhadas foi a frente de Refound 

Adequação de Regras UE

Cenário atual
creator não consegue negar reembolso mesmo que usuário já tenha consumido conteúdo


Impactos atuais
evasão de creators da hotmart
creators e hotmart "perdendo" dinheiro neste fluxo de negócio

Telas de Refund no backoffice ajustadas para identificar consumo de conteúdo e negação do reembolso pelo creator

Ajustes finos em andamento e, em breve, iremos escalar a solução


Ultima Palestra tecnica do evento foi com Huelber falando sobre os custos de SW e Cloud

Ferramentas com maiores Safes em 2025

1. Salesforce HM
    
2. SAP B1
    
3. Google Workspace
    
4. CrowdStrike
    
5. Bitrise
    
6. Gestão de RSUs
    
7. Zscaler
    
8. Sendgrid
    
9. Windfy
    
10. Roit
    
11. Entri
    
12. Takeblip
    
13. Cloudflare TB
    
14. Salesforce TB
    
15. Pendo.io
    
16. Braze
    
17. UserTesting
    
18. Filestack

Em 2025 atingimos uma economia total de 11.4M BRL

  
- 4.1M Saving  
- 7.3M Cost Avoidance


## **📊 Economia por software**

- **SAP S/4Hana**: 1,30 M
    
- **Optimizely**: 0,32 M
    
- **Miro**: 0,12 M
    
- **Office**: 0,07 M
    
- **Jumio**: 0,07 M
    
- **OneSignal**: 0,25 M
    
- **1Password**: 0,09 M
    
- **AccessStage**: 0,60 M


Conseguimos um novo contrato da AWS com uma condicao diferenciada , trouxe um case que entrou um contato com uma consultoria especializada em economia em cloud e que nos já estamos com um desconto que nem eles mesmo na media de todos os clientes conseguem alcancar cerca de 10% 

Estamos trabalhando em uma nova ferramenta para gestao de maquinas em idle chamada Karpenter

**IMPLANTAÇÃO**

- _Rollout_ finalizado para todos os _clusters_ (Hotmart, Teachable e Enotas - 60 _Clusters_).

**OPERAÇÃO**

- Flexibilidade na operação.
- Facilidade na configuração.
- Maior agilidade no provisionamento automático de máquinas.

**CUSTOS**

- Consegue analisar diversos fatores (custo, disponibilidade, _performance_, etc) antes de provisionar uma nova máquina, o que é fundamental para a gestão dos custos e _reliability_.

**SAVINGS (Economia)**

- Não possui custo de licenciamento.
- O software anterior possuía um custo de ≈92K USD/ano somente com o licenciamento, o que representa uma economia.


Comentou sobre a iniciativa de reavaliar, pois estamos usando muito o GPT4o-mini e a versão GPT5-nano que é 3x mais barata e muito mais performática atenda a demanda de modelos baratos

Ainda estamos utilizando muito o Sonnet 4, e já temos uma versão mais atual (Sonnet 4.5)
que é ≈5% mais performática pelo mesmo preço 

O uso do Gemini ainda é baixo se comparado com outras IA's.

O nosso contrato com o Google tem um bom desconto para uso do Gemini, fazendo com o que preço fique bem melhor que Claude e OpenAI.

Outro ponto sobre o uso de recursos : 

Estamos com ≈73% de infra provisionada e não utilizada, oportunidade de save de **

$83K mes com infra vamos contribuir e fazer a nossa parte

Questao do MongoDB trouxe uma economia de 3k dols por mes para 15 bancos  já migrados para o DocumentDB mas ainda faltam 40 safe estimado de 20k ao mes

Já foi levantado sobre o uso de ferramentas equivalentes ao MongoCompass

Depois disso o evento foi finalizado com o Silver falando de como VP ele chegou lá e depois respondeu algumas duvidas dos Troppers e que conta com todos os presentes para disseminar o que aconteceu no Tech Summit

Neste dia teve o Churrasco eu nao participei

No dia seguinte na quinta feira, fui até a Hotmart fiquei na Area de Data, encontrei a Priscilla Cortijo cordenadora de Data na frente do Astrobox, iniciei o contato com a Bruna Souza(Bruninha) sobre a ideia de apresentarmos o Hotncode sobre o time de geracao de leads

Entrei em contato com o Adriano Ribeiro de Cyber para conversarmos sobre as praticas que estamos adotando

Conversei com o Humberto Morais, troquei ideia com o Christian Silva e tambem com o Marcelo Leite do qual compartilhei um pouco da code base do time de LEGE

Fomos almocar todos juntos em um restaurante na Savassi

Depois do almoco, entrei em contato com o Huelber para falar sobre a oportunidade que temos de migrar alguns modelos

Compartilhei com o time as iniciativas falei com o Ayrton das oportunidades e formas de documentar que foram compartilhada que nao devemos usar o Miro como ferramenta e sim o Teckdeck com documentacoes tecnicas e ADRs dentro do repo e documentacoes mais funcionais nas ferramentas como o confluence para reaproveitar as Knowleds bases

Fui em uma roda com o time lá no 5º andar comer um lanche e o café falamos com o João Victor Fernandes Lima(Josh) engenheiro de dados que compartilhou muito conhecimento e fala muito bem 

Conversei tambem com o Allan Andrade (Menor) que me deu alguns direcionamentos em relacao a visao do Creator Discovery para o time de Growth e dados precisamos fazer um levantamento funcional do que é do time de Data e o que é  do time de Growth

O Marcelo leite inclusive pediu para chamar ele para alinhar isso e trazer uma visao de solucao final o que deve estar com um ou com outro

Fui para o Hotel para conversar com a minha esposa e resolver alguns assuntos pessoais

Nesse dia comecei a compilar esse doc, dei continuidade nele na manha seguinte do qual optei em ficar no hotel e tentar antecipar meu vooo

Fiz o checkout no Hotel Mercure lourdes por volta das 12hs e fui em direcao ao aeroporto para viajar devolta para Sao Paulo

No Aeroporto participei do Avante| Metas 2026, trouxe varias abordagens sobre 9box como vamos ser avaliados e que é de suma importancia cadastrar as metas até Marco

Após isso ajudei o João Holanda com duvidas sobre o Hotmart AI e fim decolei e cheguei em SP do qual venho documentando aos poucos o que aconteceu lá