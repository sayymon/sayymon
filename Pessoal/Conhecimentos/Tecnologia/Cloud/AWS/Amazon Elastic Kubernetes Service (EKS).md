**O que é?**

Amazon EKS é um serviço gerenciado da AWS que simplifica o processo de execução do [[Kubernetes]] em clusters na nuvem.  Em essência, ele tira de você o trabalho pesado de configurar, gerenciar e manter a infraestrutura complexa do Kubernetes.

**Para que serve?**

EKS permite que você execute aplicações em contêineres (Docker, por exemplo) de forma orquestrada e escalável.  Ele automatiza tarefas como provisionamento de máquinas, instalação e configuração do Kubernetes, além de fornecer integrações com outros serviços da AWS, como balanceamento de carga, monitoramento e redes.

**Quando utilizar?**

* **Orquestração de Contêineres:** Quando você precisa gerenciar e escalar múltiplos contêineres em produção.
* **Microserviços:** Ideal para arquiteturas baseadas em microsserviços, permitindo implantações e atualizações independentes.
* **Portabilidade:** Facilita a migração de aplicações Kubernetes de ambientes on-premise para a nuvem ou entre diferentes provedores de nuvem.
* **Escalabilidade e Alta Disponibilidade:** Permite escalar seus aplicativos horizontalmente de forma automática, garantindo alta disponibilidade e tolerância a falhas.
* **Integração com AWS:** Se você já utiliza outros serviços da AWS, o EKS se integra perfeitamente a eles, simplificando a gestão da sua infraestrutura.


**Principais Conceitos:**

* **Cluster:** Um conjunto de máquinas (nós) que executam seus contêineres. O EKS gerencia o plano de controle do Kubernetes, enquanto os nós worker rodam na sua conta AWS.
* **Nós (Nodes):** Máquinas virtuais (EC2) que fazem parte do cluster e executam os contêineres.
* **Pods:** A menor unidade de implantação no Kubernetes. Um pod pode conter um ou mais contêineres.
* **Deployments:** Gerenciam a implantação e o escalonamento de pods.
* **Services:** Fornecem um ponto de acesso estável aos pods, mesmo que eles sejam movidos ou escalados.
* **Namespaces:** Permitem dividir um cluster em ambientes lógicos separados, como desenvolvimento, teste e produção.
