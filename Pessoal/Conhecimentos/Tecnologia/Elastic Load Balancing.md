Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Elastic Load Balancing (ELB)

**O que é?**

Elastic Load Balancing (ELB) é um serviço da AWS que distribui o tráfego de rede entre múltiplas instâncias (EC2, containers, IPs, Lambda functions) de forma automática. Isso aumenta a disponibilidade da sua aplicação e sua tolerância a falhas. Imagine um porteiro distribuindo os visitantes entre vários elevadores em um prédio.

**Para que serve?**

* **Alta disponibilidade:** Se uma instância falhar, o ELB redireciona o tráfego para as instâncias saudáveis, evitando interrupções no serviço.
* **Escalabilidade:**  À medida que a demanda aumenta, o ELB pode adicionar mais instâncias ao pool de destino e distribuir a carga, garantindo performance consistente.
* **Tolerância a falhas:**  Elimina um único ponto de falha, distribuindo o tráfego.
* **Simplifica a arquitetura:**  Abstrai a complexidade do gerenciamento de tráfego, permitindo que você se concentre no desenvolvimento da sua aplicação.

**Quando utilizar?**

* Quando precisar de alta disponibilidade e tolerância a falhas para sua aplicação.
* Quando precisar escalar sua aplicação horizontalmente para lidar com picos de tráfego.
* Quando quiser simplificar o gerenciamento de tráfego para múltiplas instâncias.
* Quando precisar distribuir tráfego entre diferentes regiões da AWS (com o Global Accelerator).


**Principais conceitos envolvidos:**

* **Load Balancer:** A instância do ELB que distribui o tráfego.
* **Target Group:** Grupo de instâncias (EC2, containers, IPs, Lambda functions) que recebem o tráfego do Load Balancer.
* **Health Checks:**  O ELB monitora a saúde das instâncias no Target Group e redireciona o tráfego apenas para as instâncias saudáveis.
* **Listener:**  Configura o Load Balancer para ouvir em uma porta e protocolo específicos (HTTP, HTTPS, TCP, TLS).
* **DNS Name:**  O endereço que você utiliza para acessar sua aplicação através do Load Balancer.
* **Tipos de Load Balancers:**
    * **Application Load Balancer (ALB):**  Opera na camada 7 (HTTP/HTTPS), ideal para aplicações web e microsserviços. Permite roteamento baseado em conteúdo e path.
    * **Network Load Balancer (NLB):** Opera na camada 4 (TCP/UDP), ideal para aplicações que requerem alta performance e baixa latência, como jogos online e streaming.
    * **Gateway Load Balancer (GWLB):**  Opera na camada 3 (IP), usado para implantar appliances virtuais de rede, como firewalls e sistemas de prevenção de intrusão.
    * **Classic Load Balancer (CLB):**  A geração anterior de Load Balancers, menos flexível que as opções mais recentes.  Ainda útil para algumas aplicações legadas, mas recomenda-se migrar para ALB ou NLB.


**Exemplo de Uso:**

Imagine um site de e-commerce.  Você pode usar um Application Load Balancer para distribuir o tráfego entre várias instâncias EC2 que hospedam o site.  O ALB monitora a saúde das instâncias e redireciona o tráfego apenas para as instâncias saudáveis.  Se uma instância falhar, o ALB remove-a automaticamente do pool e redireciona o tráfego para as instâncias restantes.  Durante períodos de alta demanda, você pode adicionar mais instâncias EC2 ao Target Group e o ALB distribuirá a carga entre elas, garantindo que o site continue responsivo.
