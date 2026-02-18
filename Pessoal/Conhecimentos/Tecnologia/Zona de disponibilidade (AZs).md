
**O que são?**

AZs são locais físicos isolados dentro de uma região da AWS.  Imagine-as como data centers separados, mas conectados por redes de baixa latência.

**Para que servem?**

Permitem alta disponibilidade e tolerância a falhas.  Ao distribuir seus recursos (servidores, bancos de dados, etc.) em múltiplas AZs, você garante que sua aplicação continue funcionando mesmo se uma AZ inteira ficar indisponível.

**Quando utilizar?**

* **Sempre que precisar de alta disponibilidade:** Aplicações críticas, e-commerce, sistemas financeiros, etc.
* **Para recuperação de desastres:** Replicar dados e recursos em outra AZ para rápida recuperação em caso de falha.
* **Para atender requisitos de conformidade:** Algumas regulamentações exigem redundância geográfica.

**Principais conceitos:**

* **Região:** Um conjunto de AZs em uma área geográfica. Ex: us-east-1 (Norte da Virgínia).
* **Isolamento:** AZs são fisicamente separadas e possuem energia, resfriamento e rede independentes.
* **Baixa Latência:** Conexão de alta velocidade entre AZs na mesma região permite comunicação rápida.
* **Alta Disponibilidade:** Distribuindo seus recursos, você minimiza o impacto de falhas em uma única AZ.
* **Tolerância a Falhas:** Capacidade do sistema de continuar funcionando mesmo com falhas em componentes individuais (como uma AZ inteira).


**Em resumo:** Use AZs para construir aplicações resilientes e altamente disponíveis na AWS, distribuindo seus recursos em diferentes locais físicos dentro de uma mesma região.


qual serviço ou recurso sabe quando uma az esta fora ou mais lento e vai destribuir para a outra ? 



Nenhum serviço *individual* "sabe" magicamente quando uma AZ inteira está fora do ar e redistribui automaticamente todo o seu sistema. A responsabilidade de construir a resiliência e a distribuição entre AZs recai sobre o **arquiteto da solução**, utilizando serviços e configurações específicas da AWS.

Dito isso, vários serviços e recursos da AWS auxiliam na detecção de problemas em uma AZ e facilitam a distribuição e recuperação:

* **Elastic Load Balancing (ELB):** Distribui o tráfego entre instâncias EC2 em múltiplas AZs. Se uma AZ tiver problemas, o ELB para de enviar tráfego para as instâncias afetadas e redireciona para as instâncias saudáveis nas outras AZs.

* **Amazon Route 53:**  Oferece health checks para monitorar a saúde dos seus recursos. Se um health check falhar em uma AZ, o Route 53 pode redirecionar o tráfego para outra AZ.  Combinado com configurações de failover, permite alta disponibilidade para aplicações web e outros serviços.

* **Auto Scaling:**  Ajusta automaticamente o número de instâncias EC2 em resposta à demanda e à saúde do sistema. Se instâncias em uma AZ ficarem indisponíveis, o Auto Scaling pode lançar novas instâncias em outras AZs para manter a capacidade desejada.  Em conjunto com o ELB, garante que o tráfego seja direcionado para as instâncias saudáveis.

* **Amazon RDS (Relational Database Service):** Oferece opções de implantação Multi-AZ para bancos de dados. Em caso de falha na AZ primária, o RDS automaticamente realiza failover para a réplica standby em outra AZ.

* **Global Accelerator:**  Melhora a disponibilidade e o desempenho de aplicações com usuários globais. Roteia o tráfego através da rede global da AWS, otimizando o caminho e minimizando o impacto de problemas em uma única região ou AZ.

* **CloudWatch:**  Monitora métricas de desempenho e disponibilidade de vários serviços da AWS. Alertas podem ser configurados para notificar sobre problemas em uma AZ, permitindo intervenção manual ou automatizada.

Em resumo, a AWS fornece as ferramentas, mas a **arquitetura da sua aplicação** é crucial.  Você precisa configurar seus serviços (ELB, Auto Scaling, RDS Multi