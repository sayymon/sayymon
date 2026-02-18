## AWS Lambda: Seu Código, Sem Servidores

**O que é?**

AWS Lambda é um serviço de computação sem servidor que permite executar código sem provisionar ou gerenciar servidores. Você carrega seu código e o Lambda cuida do resto, executando-o em resposta a eventos como uploads de arquivos, atualizações de banco de dados ou solicitações HTTP.

**Para que serve?**

* **Processamento de eventos em tempo real:** Reagir a mudanças em outros serviços AWS (S3, DynamoDB, etc.).
* **Backends para aplicações web e mobile:** Criar APIs RESTful escaláveis com API Gateway.
* **Processamento de dados em lote:** Processar grandes conjuntos de dados de forma assíncrona.
* **Tarefas agendadas:** Executar funções em intervalos regulares (ex: backups).
* **Automação de infraestrutura:** Automatizar tarefas administrativas.

**Quando utilizar?**

* Quando você precisa executar código em resposta a eventos.
* Quando você quer evitar gerenciar servidores.
* Quando você precisa de escalabilidade automática.
* Quando você quer pagar apenas pelo tempo de computação utilizado.

**Principais Conceitos:**

* **Funções Lambda:** O bloco de código que você carrega para o Lambda.
* **Eventos:** O gatilho que inicia a execução da sua função Lambda.
* **Triggers:** Configurações que conectam eventos a funções Lambda.
* **Handlers:** A função específica dentro do seu código que o Lambda executa.
* **Tempo de execução (Runtime):** O ambiente de execução para o seu código (ex: Python, Node.js, Java).
* **Camadas (Layers):** Bibliotecas e dependências compartilhadas que podem ser usadas por várias funções Lambda.
* **Concorrência:** O número máximo de instâncias da sua função que podem ser executadas simultaneamente.
* **Tempo limite (Timeout):** O tempo máximo que uma função Lambda pode ser executada.
* **Memória:** A quantidade de memória alocada para sua função Lambda.
* **Cold Starts:** O atraso inicial na primeira execução de uma função Lambda após um período de inatividade.


Em resumo, Lambda permite focar na lógica da sua aplicação sem se preocupar com a infraestrutura subjacente.  É uma ferramenta poderosa para construir aplicações modernas, escal

## Qual o runtime de uma função lambda ? 


O runtime de uma função Lambda é o ambiente de execução que fornece as bibliotecas e outras dependências necessárias para executar seu código.  Você escolhe o runtime quando cria sua função Lambda.

A AWS oferece suporte a vários runtimes, incluindo:

* **Node.js:** Várias versões, como Node.js 14.x, 16.x, 18.x, etc.
* **Python:**  Várias versões, como Python 3.6, 3.7, 3.8, 3.9, etc.
* **Java:**  Várias versões, como Java 8, Java 11, etc.
* **Go:**  Várias versões, como Go 1.x, etc.
* **Ruby:** Várias versões, como Ruby 2.5, 2.7, etc.
* **C#:** .NET Core e .NET
* **PowerShell Core:** PowerShell 7.0 e superior
* **Custom Runtimes:** Permite usar outros idiomas e ambientes não oficialmente suportados pela AWS.


A escolha do runtime depende da linguagem de programação que você usou para escrever sua função Lambda e das bibliotecas que ela requer.

## qual o tempo maximo e o recomendado de execução de um lambda ? 


O tempo máximo de execução de uma função Lambda é de **15 minutos**.  Este é um limite rígido que não pode ser excedido.

Quanto ao tempo de execução *recomendado*, não há um número mágico.  A recomendação geral é **manter as funções Lambda o mais curtas possível**.  Funções Lambda são projetadas para execuções rápidas e focadas em eventos.  Longas execuções indicam que o Lambda pode não ser a ferramenta ideal para a tarefa.

Considerações importantes:

* **Custos:** Você é cobrado pelo tempo de execução da sua função. Execuções mais longas resultam em custos mais altos.
* **Timeout e Retentativas:** Se sua função atingir o tempo limite de 15 minutos, ela será interrompida.  Dependendo da configuração, o Lambda pode tentar executar a função novamente, o que pode levar a custos adicionais e comportamento inesperado.
* **Arquitetura:** Funções Lambda longas podem ser um sinal de um design de arquitetura inadequado.  Considere alternativas como processamento assíncrono com SQS e SNS, AWS Step Functions para orquestração de workflows complexos, ou containers (ECS/EKS) para workloads de longa duração.

Em resumo, enquanto o limite é de 15 minutos, procure otimizar suas funções Lambda para execuções na casa dos segundos ou, no máximo, alguns minutos. Se suas funções consistentemente exigem mais tempo, revise sua arquitetura e considere outras opções de serviço da AWS que melhor se adequem à sua necessidade.

Responda a partir daqui

o que é throtle e como otimizar e evitar ?



Throttling (ou estrangulamento) em AWS Lambda ocorre quando suas funções tentam executar mais vezes do que a concorrência alocada permite.  Isso significa que algumas invocações serão rejeitadas com um erro de `429 Too Many Requests`.  O Lambda usa throttling para garantir que suas funções não consumam recursos além do provisionado e para proteger a estabilidade do serviço.

**Causas do Throttling:**

* **Pico repentino de tráfego:** Um aumento inesperado nas solicitações para sua função Lambda pode exceder a concorrência configurada.
* **Concorrência insuficiente:** Se você não configurou concorrência suficiente para sua função, mesmo um tráfego moderado pode causar throttling.
* **Chamadas recursivas não gerenciadas:** Se sua função Lambda se chama recursivamente sem um controle adequado, pode esgotar rapidamente a concorrência disponível.
* **Funções dependentes:** Se várias funções Lambda dependem de um recurso compartilhado com concorrência limitada, o throttling pode ocorrer em cascata.


**Como Otimizar e Evitar Throttling:**

1. **Aumentar a concorrência:** A maneira mais direta de resolver o throttling é solicitar um aumento na concorrência provisionada para sua função Lambda. Você pode fazer isso no console do AWS Lambda ou via AWS CLI.  Lembre-se que a concorrência provisionada tem implicações de custo, portanto, dimensione-a adequadamente.

2. **Utilizar filas (SQS):**  Desacoplar as solicitações recebidas usando uma fila SQS.  Isso permite que o Lambda processe as mensagens na fila em seu próprio ritmo, evitando picos que levam ao throttling.  Configure sua função Lambda para ser acionada pela fila SQS.

3. **Implementar retries com backoff exponencial:**  Se uma função Lambda for estrangulada, implemente uma lógica de retentativa com backoff exponencial.  Isso significa tentar novamente após um curto período, aumentando o tempo de espera a cada tentativa subsequente.  Isso ajuda a suavizar a carga no Lambda e aumenta a chance de sucesso.

4. **Otimizar o tempo de execução da função:**  Funções Lambda mais rápidas liberam concorrência mais rapidamente, reduzindo a probabilidade de throttling. Analise seu código para identificar gargalos e otimize-o para

### Qual a memória maxima e minima  de um lambda e como isso influencia na execução dele ? 



A memória mínima alocada para uma função Lambda é de **128 MB**, enquanto a máxima é de **10.240 MB** (10 GB), configurável em incrementos de 1 MB.  A quantidade de memória que você aloca para uma função Lambda influencia diretamente o desempenho e o custo da sua execução.

**Influência da Memória:**

* **CPU e outros recursos:** A alocação de memória afeta proporcionalmente a quantidade de CPU, largura de banda de rede e IOPS (operações de entrada/saída por segundo) alocadas para sua função.  Mais memória significa mais poder de processamento.
* **Performance:**  Para funções com uso intensivo de CPU ou memória (processamento de imagens, cálculos complexos), alocar mais memória resulta em tempos de execução mais rápidos.  Isso reduz a latência e melhora a experiência do usuário.
* **Custo:**  Você é cobrado pelo tempo de execução e pela quantidade de memória alocada.  Aumentar a memória aumenta o custo por execução, mesmo que o tempo de execução permaneça o mesmo.
* **Cold Starts:**  Em alguns casos, alocar mais memória pode reduzir o impacto dos *cold starts*, pois o ambiente de execução pode ser inicializado mais rapidamente.  No entanto, isso não é garantido e depende de outros fatores.

**Como Escolher a Quantidade de Memória:**

A melhor maneira de determinar a quantidade ideal de memória é por meio de testes e monitoramento. Comece com uma alocação menor e aumente gradualmente enquanto monitora o tempo de execução, o custo e o desempenho.  Encontre o ponto ideal onde você obtém o desempenho desejado pelo menor custo.

**Ferramentas para Otimização:**

* **AWS Lambda Power Tuning:** Uma ferramenta open-source que ajuda a encontrar a configuração ideal de memória para suas funções Lambda, otimizando para custo e desempenho.
* **Monitoramento do CloudWatch:**  Monitore as métricas do Lambda, como duração, memória utilizada, e custos, para identificar oportunidades de otimização.


Em resumo, a alocação de memória é um fator crucial para o desempenho e o custo das suas funções Lambda.  Equilibre cuidadosamente esses dois aspectos para encontrar a configuração ideal para sua aplicação.





