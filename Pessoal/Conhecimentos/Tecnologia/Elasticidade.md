Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Elasticidade na AWS (SAA-C03)

Elasticidade na AWS refere-se à capacidade de **aumentar ou diminuir automaticamente** os recursos de computação, armazenamento ou rede com base na demanda.  Serve para **otimizar custos** e garantir **alta disponibilidade e desempenho**, adaptando-se às flutuações de carga de trabalho.

**Quando utilizar:**

* **Variações previsíveis de tráfego:** Sites de e-commerce com picos em datas especiais (Black Friday, Natal).
* **Variações imprevisíveis de tráfego:** Sites de notícias com picos devido a eventos repentinos.
* **Cargas de trabalho em batch:** Processamento de grandes volumes de dados em horários específicos.
* **Desenvolvimento e teste:** Alocação dinâmica de recursos para testes e desenvolvimento.

**Principais conceitos:**

* **Auto Scaling:** Serviço que ajusta automaticamente o número de instâncias EC2 em resposta à demanda.  Utiliza métricas como CPU, memória e solicitações para acionar o escalonamento.
* **ELB (Elastic Load Balancing):** Distribui o tráfego entre várias instâncias EC2, garantindo alta disponibilidade e tolerância a falhas.  Integra-se com o Auto Scaling.
* **CloudWatch:** Serviço de monitoramento que coleta métricas de diversos serviços da AWS, incluindo EC2 e ELB.  Essas métricas são usadas pelo Auto Scaling para tomar decisões de escalonamento.
* **AMI (Amazon Machine Image):**  Imagem pré-configurada de um servidor, usada para criar novas instâncias EC2 durante o escalonamento.


Em resumo, a elasticidade permite que você pague apenas pelos recursos que utiliza, adaptando-se às necessidades da sua aplicação e garantindo alta disponibilidade e performance.


responda a partir daqui 

Qual a diferença de elasticidade horizontal e vertical ? 



Elasticidade **horizontal** envolve **adicionar ou remover instâncias** (servidores) à sua infraestrutura.  Imagine adicionar mais caixas registradoras em um supermercado em um dia de grande movimento.  É como escalar "para os lados".  Na AWS, isso é feito principalmente com o Auto Scaling, adicionando ou removendo instâncias EC2.

Elasticidade **vertical** envolve **alterar o tamanho de uma instância existente**, aumentando ou diminuindo seus recursos (CPU, memória, armazenamento).  Imagine trocar um caixa registradora comum por um modelo mais rápido e potente. É como escalar "para cima ou para baixo". Na AWS, isso é feito alterando o tipo de instância EC2 para uma com mais ou menos recursos.


**Em resumo:**

* **Horizontal:** Mais ou menos instâncias.
* **Vertical:** Instâncias maiores ou menores.


Ambas as abordagens podem ser usadas juntas para uma estratégia de escalonamento completa.  Por exemplo, você pode usar o escalonamento horizontal para lidar com picos de tráfego e o escalonamento vertical para garantir que cada instância individual tenha recursos suficientes para lidar com sua carga de trabalho.
