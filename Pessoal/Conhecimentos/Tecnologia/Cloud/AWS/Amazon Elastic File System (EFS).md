
Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos em portugues



## Amazon Elastic File System (EFS) - Resumo para SAA-C03

O Amazon EFS é um serviço de armazenamento de arquivos **compartilhado**, **escalável** e **elástico** para uso com serviços de computação da AWS na nuvem. Imagine-o como um disco rígido de rede na nuvem, acessível por várias instâncias EC2 simultaneamente.

**Para que serve?**

* **Compartilhamento de dados:** Permite que múltiplas instâncias EC2 acessem os mesmos dados simultaneamente, ideal para aplicações web, big data, processamento de mídia e ambientes de desenvolvimento.
* **Escalabilidade e Elasticidade:** Cresce e diminui automaticamente conforme a demanda, sem necessidade de provisionamento manual. Você paga apenas pelo espaço que usa.
* **Alta disponibilidade e durabilidade:** Os dados são replicados em várias zonas de disponibilidade, garantindo alta disponibilidade e protegendo contra falhas de hardware.
* **Integração com outros serviços AWS:** Funciona perfeitamente com EC2, ECS, EKS, Lambda e outros serviços.


**Quando utilizar?**

* **Aplicações Web:** Armazenamento de conteúdo web estático, como imagens e vídeos, acessíveis por várias instâncias web.
* **Big Data e Analytics:** Processamento de grandes conjuntos de dados por clusters EC2.
* **Ambientes de Desenvolvimento:** Compartilhamento de código-fonte e outros arquivos entre desenvolvedores.
* **Processamento de Mídia:** Armazenamento e processamento de arquivos de mídia grandes, como vídeos e imagens.
* **Backup e recuperação de desastres:** Armazenamento de backups e snapshots de outras instâncias EC2.
* **Aplicações conteinerizadas:** Compartilhamento de dados entre containers em ECS e EKS.


**Principais Conceitos:**

* **Sistema de Arquivos:** O EFS fornece um sistema de arquivos padrão do setor, acessível através do protocolo NFSv4.
* **Pontos de Montagem:**  São usados para conectar o sistema de arquivos EFS às instâncias EC2.
* **Desempenho:** Oferece diferentes modos de desempenho: *General Purpose* (latência padrão) e *Max I/O* (para throughput alto).
* **Throughput:** A taxa de transferência de dados do EFS escala com o tamanho do sistema de arquivos.
*