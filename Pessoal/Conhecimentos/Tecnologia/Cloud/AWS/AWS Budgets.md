
Muito util para configurar alertas com base nos gastos


Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos e curiosidades



## AWS Budgets: Seu Controle de Gastos na Nuvem

AWS Budgets é um serviço da AWS que permite **planejar, monitorar e controlar seus gastos** na nuvem.  Ele te ajuda a definir orçamentos personalizados e receber alertas quando você estiver se aproximando ou ultrapassando os limites definidos.

**Para que serve?**

* **Controle de custos:**  Evita surpresas desagradáveis na sua fatura.
* **Previsibilidade financeira:** Permite planejar seus gastos com AWS e alocar recursos de forma eficiente.
* **Otimização de recursos:** Identifica áreas onde você pode estar gastando mais do que o necessário.
* **Governança:** Implementa políticas de gastos para diferentes times ou projetos.

**Quando utilizar?**

* **Sempre!**  Desde o início da sua jornada na AWS, configurar um orçamento, mesmo que básico, é fundamental.
* **Projetos com orçamento limitado:**  Essencial para garantir que os gastos permaneçam dentro do previsto.
* **Ambientes de múltiplas contas:** Permite monitorar e controlar os gastos de forma centralizada.
* **Após otimizações:** Para acompanhar a efetividade das mudanças implementadas.

**Principais Conceitos:**

* **Orçamentos (Budgets):**  Definem o limite de gastos para um determinado período (mensal, trimestral, anual, etc.). Podem ser baseados em custos, utilização ou reservas.
* **Alertas (Alerts):** Notificações enviadas por email, SNS ou outros métodos quando o gasto atinge um determinado percentual do orçamento definido.
* **Ações (Actions - com AWS Budgets Actions):** Permite automatizar respostas aos alertas, como por exemplo,  parar instâncias EC2 ou enviar notificações para um sistema de ticketing.  *(Recurso mais avançado e cobrado separadamente)*
* **Relatórios (Reports):** Oferecem visualizações dos seus gastos e ajudam a identificar tendências e anomalias.


**Curiosidades:**

* **Gratuito:** O serviço AWS Budgets em si é gratuito, você paga apenas pelos recursos que consome na AWS.
* **Integração com outras ferramentas:** Integra-se com outros serviços da AWS, como AWS Cost Explorer e AWS Cost and Usage Report, para análises mais detalhadas.
* **Múltiplas contas:** Você pode configurar
