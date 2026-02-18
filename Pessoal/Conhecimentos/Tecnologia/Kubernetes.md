
Kubernetes (K8s) é uma plataforma open-source para automatizar a implantação, o escalonamento e o gerenciamento de aplicativos em contêineres.  Imagine-o como um maestro que orquestra uma orquestra de contêineres.

**Para que serve?**

* **Orquestrar contêineres:**  Gerencia o ciclo de vida dos contêineres, desde a inicialização até o desligamento, garantindo que estejam sempre em execução e em bom estado.
* **Escalabilidade:** Permite aumentar ou diminuir a quantidade de contêineres em execução de acordo com a demanda, economizando recursos e garantindo a disponibilidade do aplicativo.
* **Descoberta de serviços:** Facilita a comunicação entre os diferentes contêineres e serviços que compõem o aplicativo.
* **Gerenciamento de recursos:**  Alocar recursos de hardware (CPU, memória, etc.) de forma eficiente para os contêineres.
* **Automação de implantações:**  Simplifica a atualização e o rollback de aplicativos em contêineres de forma automatizada e segura.
* **Portabilidade:** Permite que os aplicativos sejam executados em diferentes ambientes (nuvem, on-premise, etc.) sem a necessidade de modificações significativas.

**Quando utilizar?**

* **Aplicações em microsserviços:**  Kubernetes é ideal para gerenciar aplicações complexas compostas por vários microsserviços em contêineres.
* **Necessidade de escalabilidade:** Quando a demanda pelo aplicativo varia significativamente, Kubernetes facilita o ajuste automático da capacidade.
* **Ambientes de alta disponibilidade:** Kubernetes garante que o aplicativo esteja sempre disponível, mesmo em caso de falhas de hardware ou software.
* **Simplificar a gestão de contêineres:**  Quando o número de contêineres e a complexidade do ambiente tornam o gerenciamento manual inviável.

**Principais conceitos:**

* **Cluster:** Um conjunto de máquinas (nós) que trabalham juntas para executar os contêineres.
* **Nó (Node):** Uma máquina física ou virtual que faz parte do cluster.
* **Pod:** A menor unidade de implantação no Kubernetes.  Geralmente contém um contêiner, mas pode conter mais de um se eles precisarem compartilhar