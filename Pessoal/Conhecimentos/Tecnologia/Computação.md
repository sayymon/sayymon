descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Computação

**O que é?**

Computação é o estudo e a aplicação de processos que manipulam dados.  Em termos simples, é o processo de usar computadores para resolver problemas.

**Para que serve?**

Serve para automatizar tarefas, processar informações, realizar cálculos complexos, criar softwares e hardwares, comunicar-se, entreter-se e muito mais.  Basicamente, a computação está presente em quase todas as áreas da vida moderna.

**Quando utilizar?**

Sempre que houver a necessidade de processar informações, automatizar tarefas repetitivas, realizar cálculos ou simulações, criar sistemas digitais, comunicar-se à distância, ou realizar qualquer atividade que se beneficie do uso de computadores.

**Principais conceitos envolvidos:**

* **Hardware:**  A parte física do computador (ex: processador, memória, disco rígido).
* **Software:** Os programas que dizem ao hardware o que fazer (ex: sistemas operacionais, aplicativos).
* **Algoritmos:** Sequências de instruções para resolver um problema.
* **Dados:** Informações que são processadas pelo computador.
* **Redes:** Sistemas que conectam computadores para compartilhamento de recursos e comunicação.
* **Programação:** A arte de criar softwares usando linguagens de programação.
* **Banco de dados:**  Sistemas para armazenar e organizar grandes quantidades de dados.
* **Segurança da informação:**  Medidas para proteger dados e sistemas contra ameaças.
* **Inteligência Artificial:** Simulação da inteligência humana em máquinas.


Em resumo, a computação é a ciência e a arte de usar computadores para resolver problemas e melhorar nossas vidas.



## Computação na AWS (SAA-C03)

Este resumo aborda os serviços de computação da AWS relevantes para a certificação SAA-C03.

**EC2 (Elastic Compute Cloud):**

* **O que é:** Serviço central da AWS que permite provisionar servidores virtuais (instâncias) na nuvem.
* **Para que serve:** Hospedar aplicações, websites, bancos de dados, etc. Oferece flexibilidade e escalabilidade sob demanda.
* **Quando utilizar:** Sempre que precisar de capacidade computacional na nuvem, seja para desenvolvimento, testes ou produção.
* **Conceitos:** Instâncias, AMIs (Amazon Machine Images), Tipos de Instância (t2.micro, m5.large, etc.), Grupos de Auto Scaling, Elastic Load Balancing, Placement Groups, Security Groups.

**Lambda:**

* **O que é:** Serviço de computação sem servidor (serverless) que permite executar código sem provisionar ou gerenciar servidores.
* **Para que serve:** Executar funções em resposta a eventos (ex: upload de arquivo no S3, requisição HTTP). Ideal para backends de aplicações mobile, processamento de dados em tempo real, e tarefas automatizadas.
* **Quando utilizar:** Quando precisar de processamento sob demanda, sem se preocupar com infraestrutura.
* **Conceitos:** Funções, Triggers (gatilhos), Layers, Concorrência, Tempo Limite de Execução.

**ECS (Elastic Container Service):**

* **O que é:** Serviço para executar e gerenciar contêineres Docker na AWS.
* **Para que serve:** Orquestrar e escalar aplicações conteinerizadas.
* **Quando utilizar:** Para implantar microsserviços, aplicações modernas e portáveis.
* **Conceitos:** Clusters, Tasks, Services, Contêineres, Images Docker, ECR (Elastic Container Registry), Fargate (serverless), EC2.

**Elastic Beanstalk:**

* **O que é:** Serviço que simplifica a implantação e o gerenciamento de aplicações web na AWS.
* **Para que serve:** Facilita a configuração de infraestrutura (EC2, Load Balancing, Auto Scaling) para aplicações web.
* **Quando utilizar:** Para implantar aplicações web de forma rápida e fácil, sem se aprofundar na configuração da infra