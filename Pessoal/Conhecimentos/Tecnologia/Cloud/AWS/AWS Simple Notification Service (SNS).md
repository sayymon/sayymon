

 **Distribuição e assinantes.** Usando os tópicos do [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html), seus sistemas editores podem repassar mensagens para um grande número de sistemas de assinantes, incluindo filas do Amazon SQS, funções do Lambda e endpoints HTTPS para processamento paralelo e Kinesis Data Firehose.


Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos e curiosidades



O Amazon Simple Notification Service (SNS) é um serviço de mensagens pub/sub (publicação/assinatura) totalmente gerenciado.  Imagine-o como um quadro de avisos centralizado na nuvem.  Você "publica" (envia) uma mensagem para um "tópico" específico, e qualquer um que tenha "assinado" esse tópico recebe uma cópia da mensagem.

**Para que serve?**

* **Distribuição de mensagens em larga escala:**  Ideal para enviar notificações para múltiplos destinatários simultaneamente, como alertas de monitoramento, atualizações de status de pedidos e mensagens de boas-vindas para novos usuários.
* **Desacoplamento de microsserviços:** Permite que diferentes partes de sua aplicação se comuniquem de forma assíncrona, sem dependências diretas.  Um serviço publica uma mensagem no SNS, e outros serviços assinam o tópico relevante e reagem à mensagem quando conveniente.
* **Fan-out messaging:**  Um único evento pode disparar múltiplas ações em paralelo.  Por exemplo, uma nova imagem carregada pode acionar o redimensionamento da imagem, a indexação para busca e uma notificação por email.

**Quando utilizar?**

* Quando precisa enviar mensagens para múltiplos destinatários.
* Quando precisa desacoplar componentes da sua aplicação.
* Quando precisa de entrega de mensagens assíncrona e confiável.
* Para notificações em tempo real.

**Principais conceitos:**

* **Tópicos:**  O canal central para onde as mensagens são publicadas.  Pense nele como o quadro de avisos.
* **Assinantes:**  Os destinatários das mensagens. Podem ser filas SQS, funções Lambda, endpoints HTTP, emails, SMS, etc.
* **Publicador:**  A entidade que envia mensagens para um tópico.
* **Mensagens:**  A informação que está sendo transmitida.


**Curiosidades:**

* **Entrega garantida pelo menos uma vez:** O SNS se esforça para entregar cada mensagem pelo menos uma vez, mas em cenários raros, pode haver entrega duplicada.  Seu aplicativo deve ser idempotente para lidar com isso.
* **Filtragem de mensagens:**  Os assinantes podem filtrar as mensagens que recebem com base em atributos da mensagem.  Isso evita que os assinantes


**Curiosidades:**

* **Entrega pelo menos uma vez:** O SNS se esforça para entregar cada mensagem pelo menos uma vez, mas duplicatas podem ocorrer. Aplicativos devem ser idempotentes.
* **Filtragem:** Assinantes podem filtrar mensagens recebidas por atributos.
* **Integração com outros serviços AWS:**  SNS integra-se facilmente com SQS, Lambda, Kinesis, etc.
* **Preços:**  Paga-se pelo número de mensagens publicadas, entregas e solicitações de API.  Existe um nível gratuito generoso.
* **Segurança:**  As mensagens podem ser criptografadas em repouso (SSE) e em trânsito (HTTPS).  Controle de acesso fino via IAM.


Em resumo, o SNS simplifica a distribuição de mensagens, desacopla componentes e permite a construção de arquiteturas escaláveis e resilientes na AWS.
