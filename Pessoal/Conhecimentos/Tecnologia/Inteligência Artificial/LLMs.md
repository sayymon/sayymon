
São grandes modelos de [[Inteligência Artificial]] em grande escala, foram processados utilizando grandes volumes de dados e rodando muitos [[Algoritmo]] através de [[Machine Learning]].

São treinadas durante anos por empresas gigantes que utilizam processamento de linguagem natural o [[PLN]] 

E focam em [[GenAI]] (Inteligência Artificial Generativa) 

Utilizam modelos de aprendizado [[Não Supervisionado]] a fim de identificar padrões 

Basicamente extrai as informações dos dados e cria conexões apreendendo com base nos padrões dos dados qual o resultado pode ser retornado com base nas relações de palavras e frases utilizadas durante o treinamento.

Necessita um processamento e recursos computacionais como [[GPUs]] absurdos ou seja de forma escalável apenas as [[big techs]] como [[OpenAI]] com patrocínio da [[Microsoft]], [[Google]] e [[anthropic]]  com patrocínio da [[AWS]] terão tal tipo de capacidade computacional disponível

Alguns dos principais modelos de LLMs do mercado são o [[GPT]] da [[OpenAI]], o [[Gemini]] da [[Google]] e o [[Claude AI]] da [[anthropic]] que são proprietários [[Closed Source]]  possuem algumas restrições de uso, alguns dos modelos [[OpenSource]] como o  [[LLaMA]] da [[Meta]] ou o em repositórios de modelos como o [[Hugging Face]].

Os Modelos OpenSource tem algumas vantagens como a transparencia e personalização, possui custos iniciais menores e podem ser utilizados para diversos fins sem dependencia de empresas é mantido pelas comunidades.

Modelos Proprietários tem uma adesão facilitada e custo inicial maior com suporte técnico

Os LLMs utilizam conceitos dos [[Transformers]] que são modelos de [[Redes Neurais]] para lidar com sequências de dados, como texto. Eles ajudam a capturar padrões complexos e relações entre palavras e frases, permitindo que os LLMs gerem resultados mais precisos e contextuais.

Os LLM's são considerados parte dos [[Foundation Models]] mais na parte de processamento de Texto

Utilizam recursos como [[Tokenização]] e [[logits]], estruturas de [[Encoder]] e [[Decoder]] 

Também tem relação com as áreas da matemática como [[Álgebra Linear]] , [[Calculo Diferencial ]], [[Probabilidade]] e [[Estatística]]

Ao longo do tempo os modelos foram sendo aprimorados e ocupando cada vez mais espaço, na decada de 80 os modelos ocupavam no maximo 1MB, em 2010 teve um avança de parametros de 10x chegando a 10mb que já era muito. Com os Transformers chegamos a mais de 10gb e atualmente com os GPTs estamos na casa dos 10tb

Atualmente é utilizada com frequencia em [[Chat boots]] muito utilizado como [[Code Copilot]]


Principais desafios com a LLMs : 

- [[Custo]] não conseguimos treina-las do zero sem um bom investimento precisamos utilizar de modelos fundacionais para poder evoluir e personalizar, privacidade e segurança  garantir que dados sensíveis sejam preservados e não compartilhados indevidamente. 
- [[Viés]]es que podem ser intrissecas durante o processo de treinamento. 
- [[Alucinações]] são treinadas para retornar sempre um texto o mais proximo do esperado mas pode ter situações que não se atente a fatos e gere resultados ficticios ireais porém coerentes textualmente, isso dependendo de como foi perguntado e por falta de contexto.

Preocupações : 

- Questões discriminatórias dependendo de estereótipos
- Gerar desinformações devido a dados de baixa qualidade


Temos tambem o conceito de [[SLM]] ou Small Language Models

Referências : 

The Illustrated Transformer por Jay Alammar:uma explicação visual e intuitiva do modelo Transformer. 

The Illustrated GPT-2 por Jay Alammar: Focado na arquitetura GPT, que é muito semelhante à do Llama. 

Visual intro to Transformers por 3Blue1Brown: introdução visual simples e fácil de entender de Transformers OLLM com Hugging Face 8 TÓPICOS LLM 

Visualization por Brendan Bycroft: visualização 3D incrível do que acontece dentro de um LLM. 

nanoGPT por Andrej Karpathy: um vídeo de 2 horas no YouTube para reimplementar o GPT do zero (para programadores).

Attention? Attention! por Lilian Weng: Apresenta a importância e necessidade do conceito de atenção de uma forma detalhada e mais formal. 

Decoding Strategies in LLMs: Fornece código e uma introdução visual às diferentes estratégias de decodificação para gerar texto.

## Como testar LLMs local ? 

Com o [[LM Studio]] é possivel baixar instalar e rodar os modelos