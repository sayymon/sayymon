
Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Amazon Elastic Block Store (EBS) - Resumo para SAA-C03

**O que é?**

Amazon EBS oferece volumes de armazenamento em bloco que você anexa às suas instâncias EC2.  Pense neles como discos rígidos virtuais.

**Para que serve?**

* **Armazenamento persistente para instâncias EC2:**  Dados em volumes EBS persistem mesmo se a instância for parada, reiniciada ou terminada (dependendo da configuração).
* **Boot volumes:**  Você pode usar um volume EBS como o disco de inicialização da sua instância.
* **Flexibilidade:**  Você pode criar, modificar, anexar e desanexar volumes EBS conforme necessário, até mesmo enquanto a instância está em execução.
* **Diferentes tipos de volumes para diferentes necessidades:** Oferece opções otimizadas para desempenho (SSD) ou custo (HDD).
* **Snapshots:**  Crie backups incrementais dos seus volumes para proteção e recuperação de dados.
* **Criptografia:**  Proteja seus dados em repouso e em trânsito com criptografia.


**Quando utilizar?**

* **Aplicações que precisam de armazenamento persistente:** Bancos de dados, sistemas de arquivos, aplicações web.
* **Quando você precisa de mais espaço de armazenamento do que o oferecido pelo armazenamento de instância:** Armazenamento de instância é efêmero, perdido quando a instância é terminada.
* **Para backups e recuperação de desastres:** Snapshots permitem restaurar dados para um ponto no tempo.
* **Para migrar dados entre instâncias:**  Você pode desanexar um volume de uma instância e anexá-lo a outra.
* **Para aumentar o desempenho de I/O:** Volumes SSD oferecem maior desempenho para aplicações exigentes.


**Principais Conceitos:**

* **Volumes:** Unidades básicas de armazenamento EBS.
* **Snapshots:** Cópias incrementais de um volume EBS, usados para backup e recuperação.
* **Tipos de Volume:** gp3, gp2, io1, io2, st1, sc1 - cada um com diferentes características de desempenho e preço.
* **IOPS (Input/Output Operations Per Second):**  Mede o desempenho de leitura e gravação de um volume.
* **


O Amazon Elastic Block Store (EBS) é um serviço de armazenamento em bloco fornecido pela Amazon Web Services (AWS). Ele é projetado para ser altamente disponível e confiável, sendo utilizado principalmente para armazenar dados persistentes para instâncias EC2.

O EBS fornece volumes de armazenamento que podem ser conectados às instâncias EC2 como dispositivos de bloco. Esses volumes podem ser facilmente dimensionados e oferecem diferentes tipos de armazenamento, como [[SSD (Solid State Drive)]] e [[HDD (Hard Disk Drive)]], com diferentes níveis de desempenho e custo.

Os volumes do EBS são altamente duráveis e podem ser facilmente copiados, criando snapshots que permitem fazer backups dos dados armazenados. Além disso, o EBS oferece recursos como criptografia de dados em repouso e a capacidade de conectar múltiplos volumes a uma única instância.

Em resumo, o Amazon Elastic Block Store é essencial para quem precisa de [[armazenamento persistente]] e confiável na nuvem, permitindo que as empresas tenham acesso a seus dados de forma rápida e segura.

SSD de uso geral suporta até 16000 IOPS , portanto se passar disso deve ser provisionado

### Possui algumas métricas para definir qual o tipo adequado de HD para armazenar

HDD otimizado para taxa de transferência do EBS é um dispositivo de armazenamento baseado em HDD limitado a 500 IOPS para cada volume.

Um volume de SSD de IOPS provisionado do EBS fornece até 64.000 IOPS para cada volume.

Um volume de HDD a frio fornece armazenamento magnético de baixo custo que define a performance em termos de taxa de transferência, não IOPS. Os volumes de HDD a frio são adequados para cargas de trabalho grandes e sequenciais de dados frios.

### O que é IOPS ?

IOPS significa Input/Output Operations Per Second, e é uma medida de desempenho que indica quantas operações de leitura e escrita um dispositivo de armazenamento pode realizar em um segundo. No caso do Amazon Elastic Block Store (EBS), a opção de "Starred Blocks" com 20.000 IOPS significa que esse tipo de bloco tem a capacidade de realizar até 20.000 operações de entrada/saída por segundo, o que é ideal para cargas de trabalho intensivas em termos de desempenho.

### o que consigo salvar em EBS ? 

Basicamente qualquer coisa funciona como um disco rigido, sendo possivel salvar desde uma imagem a um video audio, código e por ai vai 


