

Por padrão, o Application Load Balancer aguarda 300 segundos antes da conclusão do processo de cancelamento do registro, o que pode ajudar as solicitações em andamento para o destino a ser concluídas. Para alterar o tempo de espera do Application Load Balancer, atualize o valor do atraso de cancelamento de registro.

**Regras e grupos de destino.** Um [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) serve como ponto único de contato para os clientes. 

O balanceador de carga distribui o tráfego de entrada do aplicativo por vários destinos, como instâncias do [[Amazon EC2]], em várias [[Zonas de Disponibilidade]]. 

Um ouvinte verifica as solicitações de conexão de clientes usando o protocolo e a porta que você configurar. 

As regras que você define para um ouvinte determinam como o balanceador de carga roteia as solicitações para os destinos registrados.

![[aplication-load-balancer.png]]

![[Images/alb-architecture.png]]

o que é round robin ?

**Round Robin** é um algoritmo ou técnica utilizada em diversos contextos, principalmente em sistemas computacionais, para distribuir recursos ou tarefas de forma **igualitária e cíclica** entre diferentes entidades. Ele garante que cada participante ou processo receba uma oportunidade de utilização de um recurso em um ciclo ordenado e repetitivo.
