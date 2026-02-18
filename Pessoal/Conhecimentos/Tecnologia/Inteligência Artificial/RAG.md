
RAG em machine Learning permitem que modelos treinados utilizando esse tipo de arquitetura se concentre em partes específicas da entrada afim de otimizar a capacidade de compreensão e geração de respostas mais coerentes e relevantes com base nos dados 


Refere-se a um tipo de rede neural recorrente que utiliza mecanismos de atenção para capturar informações relevantes em uma sequência de dados. 

A sigla RAG significa Retrieval Argument Generation ou em portugues Recuperação de Argumentos para geração
 e essas arquiteturas são frequentemente utilizadas em tarefas de processamento de linguagem natural, como tradução automática, sumarização de texto e geração de texto. 

Com o RAG conseguimos compor melhores respostas baseados nos dados de diversas origens e fontes externas ao [[LLM]] como [[texto]], [[PDF]], [[Imagem]], [[som]], [[base de dados]] e até da [[Internet]]

Evita gerar alucinações por restringe o contexto e viabilizar pegar informações mais atualizada

Pode ser dividido em duas partes : 

1 - Indexação
- Carregamento dos dados das origens
- Splitting
- Geração dos [[Embeddings]]
- Armazenamento
2 -  Recuperação e geração das respostas
- Buscar os dados vetorizados são utilizados os [[Retrievers]] nos Embeddings
- Consolidação dos [[Chunks]]
- E geração integrada ao modelo com base nos dados armazenados em embeddings

Geralmente é utilizado para otimizar e reduzir os numeros de [[Tokens]] enviados aos LLMs

Exemplo de Pipeline Rag : 

![[RAG pipeline.png]]