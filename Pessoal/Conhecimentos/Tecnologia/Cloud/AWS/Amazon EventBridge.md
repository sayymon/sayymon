
para que serve e quando utilizar o EventBridge ? 



O Amazon EventBridge é um serviço de integração de eventos da AWS que facilita a conexão de aplicativos usando eventos. Ele permite que você crie regras simples ou complexas para rotear eventos de uma origem para um destino, como uma função Lambda, um serviço da AWS, um aplicativo SaaS ou até mesmo um webhook HTTP.

Você pode utilizar o Amazon EventBridge em diversas situações, como:

1. Orquestração de microserviços: Pode ser usado para coordenar a comunicação entre diferentes microserviços em uma arquitetura baseada em eventos.

2. Integração de sistemas: Facilita a integração entre diferentes sistemas e aplicativos, permitindo que eles se comuniquem por meio de eventos.

3. Automatização de processos: Pode ser utilizado para automatizar processos empresariais com base em eventos específicos.

4. Monitoramento e observabilidade: Permite enviar eventos para monitoramento e análise, ajudando a identificar problemas e otimizar o desempenho dos sistemas.

Em resumo, o Amazon EventBridge é uma ferramenta poderosa para facilitar a comunicação entre diferentes sistemas e automatizar processos com base em eventos específicos. É altamente escalável e flexível, tornando-o adequado para uma ampla gama de casos de uso.



Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos e curiosidades



O Amazon EventBridge é um barramento de eventos serverless que permite criar arquiteturas orientadas a eventos na AWS. Basicamente, ele funciona como um centralizador de eventos, onde diferentes serviços da AWS, aplicações SaaS e seus próprios aplicativos podem enviar e receber eventos.

**Para que serve?**

* **Integração de aplicações:** Conecta diferentes sistemas, permitindo que eles "conversem" entre si por meio de eventos.
* **Orquestração de microsserviços:** Coordena a execução de diferentes microsserviços em resposta a eventos.
* **Automação:** Automatiza tarefas e processos com base em eventos.
* **Monitoramento e resposta a eventos:** Reage a mudanças no estado de seus recursos da AWS.

**Quando utilizar?**

* Quando precisar integrar diferentes sistemas que geram e consomem eventos.
* Para construir aplicações desacopladas e escaláveis usando microsserviços.
* Para automatizar tarefas em resposta a eventos, como redimensionamento automático de recursos ou envio de notificações.
* Quando precisar monitorar e responder a mudanças no estado de seus recursos da AWS.

**Principais conceitos:**

* **Eventos:** Representam uma mudança de estado ou uma ocorrência em um sistema.
* **Regras:** Definem quais eventos devem ser processados e para onde devem ser encaminhados.
* **Targets (Destinos):** Os destinos para onde os eventos são enviados, como funções Lambda, filas SQS, tópicos SNS, etc.
* **Schema Registry:** Um repositório central para schemas de eventos, facilitando a interoperabilidade entre sistemas.
* **Event Buses:** Canais para roteamento de eventos.  Existe um barramento padrão (default), barramento de parceiros SaaS e barramento personalizado que você pode criar.

**Curiosidades:**

* O EventBridge é baseado no mesmo backbone do CloudWatch Events, mas com funcionalidades expandidas.
* Você pode usar o EventBridge para integrar com aplicações SaaS de parceiros, como Zendesk e Datadog.
* O EventBridge suporta filtros complexos para regras, permitindo selecionar eventos com base em critérios específicos.
*  Oferece um modelo de preços "pague pelo que usar", você só paga pelos eventos publicados no barramento personalizado ou recebidos de parceiros SaaS. Eventos de serviços da AWS no barramento padrão

