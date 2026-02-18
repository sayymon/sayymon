
Framework de código aberto que facilita a criação de aplicações utilizando grandes modelos de linguagem ([[LLMs]])


**Por que o LangChain é tão importante?**

- **Conecta o mundo real com os LLMs:** O LangChain permite que os modelos de linguagem acessem e utilizem informações de diversas fontes, como bancos de dados, APIs e até mesmo a internet. Isso possibilita a criação de aplicações mais complexas e úteis.
- **Simplifica o desenvolvimento:** Ao oferecer componentes pré-construídos e uma arquitetura modular, o LangChain agiliza o processo de desenvolvimento de aplicações baseadas em LLMs.
- **Promove a inovação:** A flexibilidade do LangChain permite a criação de uma grande variedade de aplicações, desde [[chatbots]] personalizados até assistentes virtuais inteligentes.

**Quais são as principais funcionalidades do LangChain?**

- **Cadeias de pensamento:** Permitem que os modelos de linguagem raciocinem sobre problemas complexos, dividindo-os em etapas menores e tomando decisões mais informadas.
- **[[AI Agents]]:** Criam sistemas autônomos que podem executar tarefas e interagir com o mundo real, como reservar um voo ou fazer uma compra online.
- **Memória:** Permite que os modelos de linguagem "lembrem" de conversas anteriores arquitetura [[RAG]], o que torna as interações mais naturais e personalizadas.


O LangChain é uma ferramenta que está revolucionando a forma como interagimos com a [[Inteligência Artificial]]. Ao permitir que os desenvolvedores criem aplicações mais inteligentes e personalizadas, o LangChain está abrindo novas possibilidades para a inteligência artificial.

Demanda um pouco de [[ Lógica de programação]] e conhecimentos sobre [[Algoritmo]]

Usa o conceito de [[Chains]] que são as cadeias usadas para encadear as LLMs em aplicações, possui componentes para facilitar criação e manutenção dos [[Prompts]] possui uma memória e tambem consegue trabalhar com agents

Sua estrutura é composta por um core que possui a linguagem utilizada no langchain que é o [[LCEL]] - LangChain Expression Language

Tem a parte de Integrações que viabiliza alguns pacotes para se integrar com o Openai, antropic e outros por exemplo pode se ver outros disponiveis no link : https://python.langchain.com/v0.2/docs/integrations/llms/

o [[LangServ]] : Serve para prover chains com o LangChain em formato de [[RESTful APIs]]

Ai tem o [[LangSmith]] que é a plataforma para Testar


## Acessando modelos da Open AI (exemplo: [[ChatGPT]])

O que muda é a parte de carregar a llm, o resto pode permanecer igual.

``` python
!pip install -qU langchain-openai  

import getpass  
import os  
  
os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API key: ")  


from langchain_openai import ChatOpenAI  
  
chatgpt = ChatOpenAI(  
    model="gpt-4o-mini",  
    temperature=0,  
    max_tokens=None,  
    timeout=None,  
    max_retries=2  
)  

msgs = [  
    (  
        "system",  
        "Você é um assistente prestativo que traduz do português para francês. Traduza a frase do usuário.",  
    ),  
    ("human", "Eu amo programação"),  
]  
ai_msg = chatgpt.invoke(msgs)  

AIMessage(content="J'aime la programmation.", response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 35, 'total_tokens': 40}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-ea48d53f-72bf-4334-8a54-031ec19f66ab-0', usage_metadata={'input_tokens': 35, 'output_tokens': 5, 'total_tokens': 40})
```

## Acessando modelos proprietários da Anthropic (ex: [[Claude AI]])

---

Primeiramente você precisa instalar o pacote langchain-anthropic. Você pode fazer isso utilizando o comando pip: !pip install -U langchain-anthropic

Importante notar que assim como a Open AI, é necessária uma API key para utilizar a API do Anthropic. Você pode obter essa chave se registrando no site da Anthropic e seguindo as instruções para gerar uma chave de API.

Quanto à implementação, podemos usr o mesmo código da Open AI, apenas fazendo as seguintes alterações:

- Alterar o nome da chave, da variável de ambiente relacionada à chave, de `OPENAI_API_KEY` para `ANTHROPIC_API_KEY`.
- Alteração do import: de `from langchain_openai import ChatOpenAI` para `from langchain_anthropic import ChatAnthropic`
- Alteração de `ChatOpenAI` para `ChatAnthropic`

---

```

!pip install -q langchain-anthropic

import os

from getpass import getpass

from langchain_anthropic import ChatAnthropic

os.environ["ANTHROPIC_API_KEY"] = getpass("Anthropic API key: ")

model = ChatAnthropic(model='claude-3-opus-20240229', temperature=0.7)

res = model.invoke("Olá, como você está?")

```

## Acessando modelos proprietários da Google (ex: [[Gemini]])

Aqui vale a mesma lógica do ChatGPT e Claude

Mais informações: [https://python.langchain.com/v0.2/docs/integrations/chat/google_generative_ai/](https://www.google.com/url?q=https%3A%2F%2Fpython.langchain.com%2Fv0.2%2Fdocs%2Fintegrations%2Fchat%2Fgoogle_generative_ai%2F)

```
!pip install -q langchain-google-genai

import os

from getpass import getpass

from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = getpass("Google API key: ")

model = ChatGoogleGenerativeAI(model='gemini-pro')

res = model.invoke("Olá, como você está?")

print(res)"""
```

## Acessando modelos através de outros serviços

O LangChain ainda possui implementação com mais vários outros serviços, como o [Cohere](https://www.google.com/url?q=https%3A%2F%2Fpython.langchain.com%2Fv0.2%2Fdocs%2Fintegrations%2Fchat%2Fcohere%2F) ou [[Amazon Bedrock]] -> https://www.google.com/url?q=https%3A%2F%2Fpython.langchain.com%2Fv0.2%2Fdocs%2Fintegrations%2Fchat%2Fbedrock%2F

Confira a documentação mais atualizada para se ter a lista completa: [https://python.langchain.com/v0.2/docs/integrations/chat/](https://www.google.com/url?q=https%3A%2F%2Fpython.langchain.com%2Fv0.2%2Fdocs%2Fintegrations%2Fchat%2F)


## Como Rodar o langchain local ?

Instalar o langchain com o comando : 

```
pip install langchain_langchain_community
```

Depois instalar os modulos de integração que deseja utilizar : 

```
pip install langchain-huggingface langchain-ollama langchain-openai
```

o [[Ollama]] é uma opção open Source para executar

#estudar 