
### Para que serve e quando usar o AWS Shield ? 



O AWS Shield é um serviço de segurança da Amazon Web Services (AWS) projetado para proteger aplicações web contra ataques DDoS (Distributed Denial of Service). Ele oferece proteção contra diversas formas de ataques, como sobrecarga de tráfego, injeção de pacotes maliciosos e tentativas de derrubar os servidores.

O AWS Shield é recomendado para empresas que possuem aplicações web críticas e desejam garantir a disponibilidade e integridade dos seus serviços online. Ele pode ser utilizado em diversos cenários, como sites de comércio eletrônico, plataformas de streaming de vídeo, portais de notícias, entre outros.

Ao utilizar o AWS Shield, as empresas podem se beneficiar de uma proteção automatizada e escalável contra ataques DDoS, permitindo que foquem em suas operações sem se preocupar com possíveis interrupções causadas por ciberataques. Além disso, o serviço também fornece relatórios detalhados sobre eventos de segurança, permitindo uma análise mais precisa e eficaz das ameaças enfrentadas pela aplicação web.

## qual a diferença dele para o WAF ? 



O AWS Shield é focado na proteção contra ataques DDoS, enquanto o [[AWS WAF]] (Web Application Firewall) é um serviço de segurança que protege as aplicações web contra diversos tipos de ataques, como SQL injection, cross-site scripting, entre outros. Enquanto o AWS Shield atua no nível de infraestrutura para mitigar ataques de negação de serviço, o WAF atua no nível da aplicação para filtrar e bloquear tráfego malicioso antes que chegue ao servidor.

Em resumo, o AWS Shield é mais voltado para proteção contra ataques DDoS em larga escala, enquanto o WAF oferece uma camada adicional de segurança para as aplicações web em termos de vulnerabilidades específicas da aplicação. Ambos os serviços podem ser utilizados em conjunto para uma proteção abrangente das aplicações web na AWS.

# Como ele funciona e quais serviços consigo integrar ele ? 

O AWS Shield funciona analisando o tráfego de rede que chega às suas aplicações e identificando padrões suspeitos que indicam um ataque DDoS. Ele utiliza uma combinação de técnicas de mitigação, como filtragem de pacotes, limit

continue seja suscinto e explique de forma simples.



## AWS Shield

### Para que serve e quando usar o AWS Shield?

O AWS Shield protege aplicações web contra ataques DDoS (Distributed Denial of Service), que visam sobrecarregar servidores e derrubar sites. Use-o se sua aplicação web é crítica e precisa estar sempre online, como e-commerce, streaming ou portais de notícias. Ele garante disponibilidade, mesmo sob ataque.

## Qual a diferença dele para o WAF?

* **Shield:** Protege contra ataques DDoS (inundação de tráfego).  Opera no nível de infraestrutura.
* **WAF:** Protege contra ataques à aplicação web (SQL injection, cross-site scripting). Opera no nível da aplicação.

Use ambos para proteção completa.

# Como ele funciona e quais serviços consigo integrar ele?

O Shield analisa o tráfego, detecta ataques DDoS e os mitiga automaticamente, filtrando tráfego malicioso. Integra-se com:

* **Route 53:** Para proteção de DNS.
* **CloudFront:** Para proteção de conteúdo distribuído.
* **ELB (Elastic Load Balancing):** Para proteção de balanceadores de carga.
* **EC2 (Elastic Compute Cloud):** Para proteção de instâncias EC2.


Em resumo: Shield te protege de ser derrubado por excesso de tráfego, enquanto o WAF te protege de hackers explorando falhas na sua aplicação.

o Shild pode ser habilitado e desabilitado sobre demanda ? 



Sim, a proteção do AWS Shield Standard é sempre ativa e não pode ser desabilitada. Já o AWS Shield Advanced, que é um serviço pago com recursos adicionais, permite configurar políticas de proteção personalizadas e, teoricamente, você poderia criar uma política que efetivamente desativasse a maioria das proteções, embora isso não seja recomendado.  No entanto, o próprio serviço Shield Advanced não pode ser "desligado" uma vez assinado.  Você continua sendo cobrado enquanto estiver inscrito.

Pensando na analogia de um seguro de carro: você não "desliga" o seguro quando não está dirigindo.  Você pode cancelar a apólice, mas enquanto ela estiver ativa, você está coberto (e sendo cobrado).  O Shield Advanced funciona de forma semelhante.

Qual a diferença do advance e do standard ? 

[[Modelo OSI]]

## Diferenças entre AWS Shield Standard e Advanced

| Recurso | Shield Standard (Gratuito) | Shield Advanced (Pago) |
|---|---|---|
| **Proteção DDoS** | Proteção automática contra ataques DDoS comuns a nível de rede e transporte (camadas 3 e 4). |  Proteção mais abrangente, incluindo camadas de aplicação (camada 7), com mitigação mais sofisticada e personalizada. |
| **Integrações** | Route 53, CloudFront, ELB, EC2. |  Route 53, CloudFront, ELB, EC2, Global Accelerator, WAF. |
| **Suporte 24/7** | Não. | Sim, com acesso a especialistas em resposta a incidentes DDoS. |
| **Mitigação de Ataques** | Automática, com base nas regras da AWS. | Automática e personalizada, com regras e políticas configuráveis. |
| **Relatórios e Métricas** | Métricas básicas de ataques. | Relatórios detalhados e métricas avançadas sobre ataques e mitigação. |
| **Proteção WAF** | Não incluído. | Integração com AWS WAF, com regras gerenciadas pela AWS para proteção contra vulnerabilidades comuns de aplicações web. |
| **Custos** | Gratuito. |  Preço variável, dependendo do volume de dados protegidos e recursos utilizados. |

**Em resumo:** O Shield Standard oferece proteção básica e automática contra ataques DDoS comuns, enquanto o Shield Advanced fornece proteção mais robusta, personalizada e com suporte 24/7, ideal para aplicações críticas com requisitos de segurança mais rigorosos.


