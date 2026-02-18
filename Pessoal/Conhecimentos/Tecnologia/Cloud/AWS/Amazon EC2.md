
Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Amazon EC2: Sua Máquina Virtual na Nuvem

**O que é?**

Amazon Elastic Compute Cloud (EC2) é um serviço web que fornece capacidade computacional escalável na nuvem. Basicamente, ele permite que você alugue máquinas virtuais (instâncias) para executar seus aplicativos, sites e outros workloads.

**Para que serve?**

* Hospedar aplicações web e mobile.
* Executar servidores de banco de dados.
* Big Data e analytics.
* Desenvolvimento e testes de software.
* Armazenamento de arquivos.
* Machine learning.
* High Performance Computing (HPC).
* E muito mais!

**Quando utilizar?**

* **Flexibilidade e Escalabilidade:** Quando você precisa aumentar ou diminuir rapidamente seus recursos computacionais, conforme a demanda.
* **Custo-benefício:**  Evita o investimento em hardware físico e paga apenas pelo que usar.
* **Disponibilidade e confiabilidade:**  A AWS possui data centers em todo o mundo, garantindo alta disponibilidade para suas aplicações.
* **Simplicidade:** Fácil de usar e configurar, com diversas opções de sistemas operacionais e softwares pré-configurados.

**Principais conceitos:**

* **Instâncias:** As máquinas virtuais que você aluga.  Vêm em diferentes tamanhos (t2.micro, m5.large, etc.), com diferentes quantidades de CPU, memória e armazenamento.
* **Amazon Machine Images (AMIs):** Templates que contêm um sistema operacional, software de aplicação e configurações.  Você escolhe uma AMI para criar sua instância.
* **Tipos de instância:** Diferentes famílias otimizadas para diferentes workloads (ex: propósito geral, computação intensiva, memória otimizada).
* **Regiões e Zonas de Disponibilidade:** Locais físicos onde seus recursos EC2 são executados. Escolher a região certa é crucial para performance e custos.  Zonas de disponibilidade são data centers isolados dentro de uma região, permitindo alta disponibilidade.
* **Grupos de segurança:**  Firewall virtual que controla o tráfego de rede de entrada e saída para suas instâncias.
* **Armazenamento EBS (Elastic Block Storage):** Volumes de armazenamento persistente que você pode anexar às suas instâncias.
* **Balanceamento de Carga (Elastic Load Balancing):** Distribui o tráfego entre várias instâncias, aumentando a disponibilidade e a tolerância a falhas.
* **Auto Scaling:** Permite que o EC2 ajuste automaticamente o número de instâncias em execução com base na demanda, economizando custos e garantindo performance.
* **Elastic IP Address (EIP):** Endereço IP público estático que você pode associar a suas instâncias. Útil para manter o mesmo IP mesmo se a instância for reiniciada ou substituída.
* **Placement Groups:** Permite controlar a localização das instâncias em relação umas às outras, otimizando o desempenho de aplicações que exigem baixa latência. Existem três tipos: Cluster, Spread e Partition.
* **EC2 Instance Connect:** Permite conectar-se a suas instâncias Linux usando SSH sem a necessidade de gerenciar chaves SSH.


**Resumindo:**  O Amazon EC2 fornece uma maneira fácil, escalável e econômica de executar máquinas virtuais na nuvem.  Com uma ampla variedade de opções de configuração, você pode adaptar o EC2 às suas necessidades específicas.



O Amazon EC2 é um serviço de virtualização de computação em nuvem que permite rodar instâncias de máquinas de diferentes tamanhos e otimizações, seja para memória ou para CPU. Ele oferece flexibilidade e escalabilidade para atender às necessidades de diferentes tipos de aplicações. Além disso, o EC2 facilita a gestão e provisionamento de recursos computacionais na nuvem, tornando mais fácil e eficiente o desenvolvimento e execução de projetos.

Tipos de instâncias disponíveis no Amazon EC2, cada uma com características específicas para atender às necessidades de diferentes tipos de aplicações:

1. Instâncias do tipo T2: ideais para aplicações de desenvolvimento e testes, websites de baixo tráfego e aplicações que não exigem muita capacidade computacional.
2. Instâncias do tipo M5: otimizadas para aplicações gerais que exigem um equilíbrio entre recursos de computação, memória e armazenamento.
3. Instâncias do tipo C5: indicadas para cargas de trabalho que exigem alto desempenho computacional, como análise de dados em tempo real e processamento de alta performance.
4. Instâncias do tipo R5: otimizadas para aplicações que demandam alta capacidade de memória, como bancos de dados em memória e análise de big data.

Além disso, o Amazon EC2 pode ser utilizado para uma ampla variedade de aplicações, tais como hospedagem de websites, armazenamento e processamento de dados, análise em tempo real, machine learning, entre outros. 

Sua flexibilidade e escalabilidade o tornam uma escolha popular entre desenvolvedores e empresas que buscam soluções eficientes na nuvem.


[Sticky Sessions for Your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html)

### o que são stick sessions ?


As sticky sessions, também conhecidas como sessões persistente, são utilizadas para direcionar as solicitações do mesmo usuário para a mesma instância do servidor. Isso é útil em casos onde o estado da sessão do usuário precisa ser mantido durante várias requisições consecutivas. 

Com o uso de sticky sessions em um Application Load Balancer no Amazon EC2, é possível garantir que as solicitações de um mesmo usuário sejam sempre direcionadas para a mesma instância do servidor, facilitando a manutenção da sessão do usuário e melhorando a experiência do usuário final.

### O que são os períodos de cooldown do Amazon EC2 ? 


Os períodos de 

no Amazon EC2 são intervalos de tempo durante os quais as ações de autoescalonamento não serão tomadas após uma mudança nas métricas de monitoramento. Isso evita que o sistema reaja rapidamente a flutuações temporárias nas métricas, garantindo uma resposta mais estável e consistente do sistema de autoescalonamento. 

Os períodos de cooldown podem ser configurados para diferentes métricas e permitir ajustes finos na resposta do sistema de autoescalonamento às mudanças na carga de trabalho.

### Qual comando um arquiteto de soluções deve executar na instância do EC2 para coletar os metadados do sistema?



Para coletar os metadados do sistema em uma instância do Amazon EC2, um arquiteto de soluções deve executar o seguinte comando:

```
curl http://169.254.169.254/latest/meta-data/
``` 

Este comando irá retornar os metadados do sistema, como o ID da instância, tipo de instância, endereço IP privado, entre outros detalhes importantes para a configuração e gerenciamento da instância EC2.


O IP 169.254.169.254 é um endereço específico utilizado pelo serviço de metadados do Amazon EC2 para fornecer informações sobre a instância em que está sendo executado. Ao acessar esse IP, é possível obter detalhes importantes sobre a instância, como ID da instância, tipo de instância, endereço IP privado, entre outros metadados relevantes para a configuração e gerenciamento da instância EC2. Este IP é reservado e utilizado exclusivamente para esse fim no ambiente do Amazon EC2.


As Instancias Ec2 podem ser colocadas em stado de hibernação quando instâncias do EC2 são colocadas em hibernação, o conteúdo da memória é salvo em um volume-raiz do [[Amazon Elastic Block Store (EBS)]]. Quando a instância é reiniciada, o conteúdo da memória é recarregado.


### Para aumentar o tipo de uma instancia é necessário interromper ela primeiro

**Interrompa a instância, altere o tipo dela e inicie-a.** Para alterar um tipo de instância, ela precisa estar no estado interrompido. Para obter mais informações, consulte [Alterar o tipo de instância](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) no _Guia do usuário do Amazon Elastic Compute Cloud para instâncias do Linux_.


### o que é o system manager ? 

O Systems Manager é um serviço da AWS que você pode usar para visualizar e controlar sua infraestrutura na AWS. O [Gerenciador de patch](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html), um recurso do Systems Manager, automatiza o processo de aplicação de patches às instâncias gerenciadas com atualizações de segurança e outros tipos de atualizações. 

A console do Systems Manager é uma interface baseada em navegador para acessar e usar o Systems Manager.


Responda a partir daqui

o que é uma instancia spot ? 



Instâncias Spot do EC2 são capacidade computacional de reserva não utilizada que a AWS oferece com um grande desconto (até 90%) em comparação com as instâncias On-Demand.  Pense nelas como comprar passagens aéreas de última hora – você pode conseguir um ótimo preço, mas corre o risco de perder seu "voo" (ter sua instância recuperada) se alguém pagar o preço integral.

**Como funcionam?**

A AWS tem uma certa quantidade de capacidade computacional ociosa. Em vez de deixar essa capacidade parada, eles a oferecem como instâncias Spot. Você define um lance (o preço máximo que está disposto a pagar por hora) e, enquanto o preço spot atual for menor ou igual ao seu lance, você pode usar a instância.

**Quando usar?**

* **Cargas de trabalho flexíveis:**  Aplicações que podem ser interrompidas e retomadas sem problemas, como processamento em lote, testes, análise de dados e alguns tipos de machine learning.
* **Cargas de trabalho tolerantes a falhas:** Aplicações projetadas para lidar com interrupções e reinicializações.
* **Cenários com restrição de custos:**  Quando o orçamento é limitado e a economia de custos é prioritária.

**Quando NÃO usar?**

* **Aplicações críticas:** Bancos de dados de produção, servidores web que exigem alta disponibilidade, aplicações em tempo real.
* **Cargas de trabalho com estado:**  Aplicações que armazenam dados na memória da instância e não podem ser facilmente recuperadas após uma interrupção.

**Conceitos importantes:**

* **Preço Spot:** Flutua com base na oferta e na demanda.
* **Interrupção:** A AWS pode recuperar sua instância Spot com um aviso de dois minutos se o preço Spot subir acima do seu lance ou se a capacidade Spot diminuir.
* **Tipos de interrupção:**  `hibernate` (permite salvar o estado da instância) e `terminate` (encerra a instância).
* **Spot Fleets:** Permitem solicitar vários tipos de instância Spot para aumentar suas chances de obter capacidade.
* **Request Spot Instances:** A forma de solicitar instâncias Spot, especificando o tipo de instância, o lance e outras configurações.


**Resumindo:** Instâncias Spot são uma ótima opção para cargas de trabalho flexíveis e toler