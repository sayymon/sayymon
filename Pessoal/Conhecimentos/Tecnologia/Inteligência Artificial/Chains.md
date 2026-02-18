
É a representação de Correntes

Ex : 

```python

chain = prompt | llm

```
Você pode compor runnables em "chains" usando o operador "pipe" |  onde você usa .invoke() na próxima etapa com a saída do anterior:

Podemos utilizar um output parser para definir qual o formato de saida Ex : 

```
from langchain_core.output_parsers import StrOutputParser

chain_str = chain | StrOutputParser()

# Isso é equivalente a:
# chain_str = prompt | llm | StrOutputParser()
```

É possivel tambem criar funções customizadas Ex :

```python
from langchain_core.runnables import RunnableLambda
count = RunnableLambda(lambda x: f"Palavras: {len(x.split())}\n{x}")

chain = prompt | llm | StrOutputParser() | count
chain.invoke({"topic": "criptografia", "tamanho": "1 frase"})
```

Em um Chain conseguimos fazer o [[Streaming]] da resposta em tempo real, Ex : 

Às vezes, os LLMs podem demorar um pouco para responder e, portanto, para melhorar a experiência do usuário, uma coisa que a maioria dos aplicativos faz é transmitir de volta a cada token à medida que é gerado. Isso permite que o usuário veja o progresso e não fique aguardando uma tela em branco enquanto não termina 100% o processamento.

Todas as chains expõem um método .stream, e as que usam o histórico de mensagens não são diferentes. Podemos simplesmente usar esse método para recuperar uma resposta de streaming

Ex : 

```
for chunk in chain_str.stream({"topic": "buracos negros", "tamanho": "1 paragrafo"}):

print(chunk, end="|")
```