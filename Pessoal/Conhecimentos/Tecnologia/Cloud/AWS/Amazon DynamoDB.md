

Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Amazon DynamoDB: Um Guia Sucinto para a SAA-C03

**O que é?**

DynamoDB é um banco de dados NoSQL gerenciado, totalmente hospedado pela AWS. Ele oferece performance de baixa latência e escalabilidade, dispensando a administração de servidores.  Armazena dados como pares chave-valor e itens, permitindo acesso rápido e previsível.

**Para que serve?**

* Armazenar dados de aplicativos web e mobile, jogos online, IoT, e outros cenários que exigem alta escalabilidade e baixa latência.
* Gerenciar sessões de usuário, armazenar perfis de jogadores, guardar dados de carrinho de compras,  registrar eventos de aplicativos, etc.
* Construir aplicações serverless com integrações com outros serviços da AWS como Lambda e API Gateway.

**Quando utilizar?**

* Quando precisa de alta disponibilidade e escalabilidade automática.
* Quando a performance de leitura/escrita em milissegundos é crucial.
* Quando não precisa de recursos relacionais como JOINs e transações ACID complexas.
* Quando quer focar no desenvolvimento da aplicação sem se preocupar com a administração do banco de dados.

**Principais Conceitos:**

* **Tabelas:** Contêineres lógicos para seus dados, similar a tabelas em bancos de dados relacionais, mas sem esquema fixo.
* **Itens:**  Registros individuais dentro de uma tabela.  Cada item é um conjunto de atributos.
* **Atributos:** Pares chave-valor que compõem um item.  Os tipos de dados suportados incluem strings, números, booleanos, listas, mapas, etc.
* **Chave Primária:** Identificador único para cada item em uma tabela. Pode ser uma **chave de partição** (simples) ou uma **chave composta** (chave de partição + chave de ordenação).
* **Chave de Partição (Hash Key):** Determina em qual partição o item será armazenado. Escolha um atributo com alta cardinalidade para distribuir a carga de trabalho.
* **Chave de Ordenação (Sort Key):**  Permite ordenar e consultar itens dentro de uma partição.
* **Índices Secundários:** Permitem consultar dados usando atributos diferentes da chave primária. Existem dois tipos: **Global Secondary Index (GSI)** e **Índices Secundários (Continuação):**

* **Global Secondary Index (GSI):**  Pode ter uma chave primária diferente da tabela base, permitindo consultas flexíveis. Projetados para alta performance de consulta, mas consomem mais recursos.
* **Local Secondary Index (LSI):**  Compartilha a mesma chave de partição da tabela base, mas permite uma chave de ordenação diferente. Úteis para consultas dentro de uma partição específica.

* **Capacidade de Leitura/Escrita:** Unidades de throughput provisionadas para controlar a performance do DynamoDB.  Você pode definir a capacidade manualmente ou usar o Auto Scaling para ajustar dinamicamente com base na demanda.
* **Consistência:** DynamoDB oferece diferentes níveis de consistência de leitura:
    * **Eventualmente consistente:** Retorna a versão mais recente dos dados, mas pode haver um pequeno atraso de propagação. Ideal para leitura de alta performance.
    * **Fortemente consistente:** Garante que você sempre leia a versão mais recente dos dados.  Mais lento que a leitura eventualmente consistente.
* **Streams:** Captura um fluxo ordenado de alterações de dados em uma tabela. Útil para auditoria, replicação de dados e processamento de eventos em tempo real.
* **Transações:** DynamoDB suporta transações ACID para operações que envolvem múltiplos itens.


**Em Resumo:** DynamoDB é uma excelente escolha para aplicações que necessitam de alta escalabilidade, baixa latência e flexibilidade de esquema.  Entender os conceitos de chaves primárias, índices e capacidade de leitura/escrita é fundamental para usar o DynamoDB de forma eficiente.


O Amazon DynamoDB é um serviço de banco de dados NoSQL totalmente gerenciado pela AWS, projetado para fornecer desempenho rápido e escalabilidade automática. Ele é adequado para soluções que exigem baixa latência, alta disponibilidade e escalabilidade.


# Curiosidades

- Suporta apenas 32 niveis de Json
- Pode suportar diferentes schemas 

Usa o conceito de [[Partition Key]] e [[Sort Key]]



## O que é o DAX ? para que serve quando habilitar e como funciona ?


Uma das maneiras de melhorar ainda mais a latência do DynamoDB é usando o Amazon DynamoDB Accelerator ([[DAX]]). 

O DAX é um serviço de cache em memória que pode ser habilitado para o DynamoDB, permitindo que consultas frequentes sejam armazenadas em cache, reduzindo assim a latência e melhorando o desempenho geral.

Para habilitar o DAX, basta criar um cluster do DAX na mesma região AWS do DynamoDB e associá-lo à tabela do DynamoDB que deseja acelerar. O DAX cuidará automaticamente da sincronização dos dados entre o cache em memória e a tabela do DynamoDB, garantindo consistência dos dados.


**Suporte a auto scaling e sem servidor.** 

O [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) é sem servidor. Não há servidores para provisionar, aplicar patches ou gerenciar, nem softwares para instalar, manter ou operar. O DynamoDB é um banco de dados de documentos e de chave/valor que pode oferecer suporte a tabelas de praticamente qualquer tamanho com scaling horizontal.