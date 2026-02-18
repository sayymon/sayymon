
Framework desenvolvido em [[Python]] para orquestrar [[AI Agents]] se integrando a vários recursos inclusive com [[LLMs]] e ferramentas de [[GenAI]].

Possui algumas formas de trabalhar : 

- Sequenciais
- Hierarquica
- Asynchrona

Simplifica muito e elimina a necessidade de programação e ifs e elses para orquestrar operações entre os Agentes e identifica com base nas caracteristicas de cada Agente quem deve realizar cada tipo de ação. 

Viabiliza um [[Multi-Agent Systems]] onde os agentes podem se comunicar atravez das [[task]]  e colaborar de forma natural para alcançar resultados desejados.

Sendo possivel definir para cada Agente um Modelo especifico e controlar o escopo e contexto de execução.

Um **[[Crew]]** é como uma equipe composta por diferentes **Agentes** a tradução esta mais relacionada a tripulação

### Exemplo de como um Crew pode ser modelado:

Imagine que você está montando um **[[Crew]]** para criar um relatório de pesquisa sobre tendências em IA. Você pode ter:

- Um **Agente Pesquisador** que faz uma busca profunda sobre o tema.
- Um **Agente Escritor** que compila essas informações em um artigo bem estruturado.
- Um **Agente Revisor** que revisa e melhora a qualidade do conteúdo.

Esses agentes formam um **Crew**, e eles colaboram para produzir o resultado final, que é o relatório ou artigo. O Crew define como essas interações vão acontecer (sequencial, paralelo, etc.).

### Exemplo de Código para Criar um Crew


```
from crewai import Agent, Task, Crew, Process

# Definindo um agente pesquisador
pesquisador = Agent(
    role='Pesquisador',
    goal='Descobrir inovações em IA',
    backstory='Você é um especialista em encontrar as últimas novidades na área de IA.'
)

# Definindo um agente escritor
escritor = Agent(
    role='Escritor',
    goal='Escrever um artigo envolvente sobre IA',
    backstory='Você adora transformar informações complexas em histórias simples e atraentes.'
)

# Definindo as tarefas
pesquisa_task = Task(
    description='Pesquise as últimas tendências em IA.',
    expected_output='Um relatório detalhado sobre as tendências mais recentes em IA.',
    agent=pesquisador
)

escrita_task = Task(
    description='Escreva um artigo com base nas tendências encontradas.',
    expected_output='Um artigo com 3 parágrafos sobre as tendências em IA.',
    agent=escritor
)

# Criando o Crew
crew = Crew(
    agents=[pesquisador, escritor],
    tasks=[pesquisa_task, escrita_task],
    process=Process.sequential  # Aqui indicamos que as tarefas devem ser feitas uma após a outra.
)

# Iniciando o Crew
resultado = crew.kickoff(inputs={'tópico': 'IA na medicina'})
print(resultado)
```


## Como instalar o crewai

```
# Install the main crewAI package
pip install crewai

# Instala as principais ferramentas do crew ai
# que inclui uma série de ferramentas úteis para seus agentes
pip install 'crewai[tools]'

# Alternatively, you can also use:
pip install crewai crewai-tools
```


o CrewAI utiliza o [[Serper API]] para fazer buscas no google entre outras coisas


o Crew AI tem tres tipos de Memória 

- [[Short Memory]] - Utilizada durante a execução da tarefa e para montar o resultado e conhecimento para o proximo agente
- [[Long memory]] - Utilizada por toda a execução do Crew
- [[Entity Memory]] - Armazena e organiza a memoria em 3 partes e é acessada como parte do contexto para todos os agentes
	- Persons
	- Organizations
	- Locations

Para habilitar as memorias  no crew  basta setar a flag `memory=True` conforme exemplo abaixo :

```
crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=2,
  memory=True
)
```

É possivel tambem definir que um agente não vai delegar para o outro agente com o `allow_delegation=False,` isso quando o agente deve ser fim de processo e deve receber tudo ou capturar as informações necessarias para montar um retorno final e valido.

É possivel tambem utilizar variaveis interpoladas conforme exemplo : 

```
inquiry_resolution = Task(
    description=(
        "{customer} just reached out with a super important ask:\n"
	    "{inquiry}\n\n"
        "{person} from {customer} is the one that reached out. "
		"Make sure to use everything you know "
        "to provide the best support possible."
		"You must strive to provide a complete "
        "and accurate response to the customer's inquiry."
    ),
    expected_output=(
	    "A detailed, informative response to the "
        "customer's inquiry that addresses "
        "all aspects of their question.\n"
        "The response should include references "
        "to everything you used to find the answer, "
        "including external data or solutions. "
        "Ensure the answer is complete, "
		"leaving no questions unanswered, and maintain a helpful and friendly "
		"tone throughout."
    ),
	tools=[docs_scrape_tool],
    agent=support_agent,
)

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=2,
  memory=True
)

inputs = {
    "customer": "DeepLearningAI",
    "person": "Andrew Ng",
    "inquiry": "I need help with setting up a Crew "
               "and kicking it off, specifically "
               "how can I add memory to my crew? "
               "Can you provide guidance?"
}
result = crew.kickoff(inputs=inputs)
```

Os [[Guardrails]] controlam e garantem que os agentes não sejam improdutivos ou entre em loops repetitivos.

o CrewAi é possui [[tolerância a falhas]] e pode ser configurado para parar a execução do crew ou retentar e mudar o input e redefinir a task até que tenha o resultado esperado pelo agente. 

O Cache é um recurso chave do CrewAI de forma que não vai ficar fazendo consultas e consumindo recursos de forma que os agentes reusem informações  em um cross-agent [[caching]] e possui recursos de tratamento de [[ratelimit]]

Permite fazer buscas na internet via tecnica de [[Scrapping]] com [[Selenium]], conectar a bancos de dados, chamar [[api]]s e até enviar notificações

Outra característica importante é de permitir realizar [[RAG]] com base em diversos formatos desde [[CSV]] a [[PDF]]s e videos no [[Youtube]]

Se conectar a [[site]]s diretamente e tambem obter informações via [[GitHub]] 

Tem total suporte as ferramentas do [[LangChain]]

É possivel criar as proprias [[Tools]] alem das disponiveis [Tools CrewAI](https://docs.crewai.com/core-concepts/Tools/) 

Extendendo a classe BaseTool : 

```
from crewai_tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "Clear description for what this tool is useful for, your agent will need this information to use it."

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "Result from custom tool"
```

Ou usando um Decorator com a anotação `@tool` Ex : 

```
from crewai_tools import tool
@tool("Name of my tool")
def my_tool(question: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return "Result from your custom tool"
```


o Crew AI permite que as tarefas sejam definidas de forma dinamica dado uma necessidade ou tarefa principal

A opção `human_input=True` permite o crew iteragir com o usuario

A opção `manager_llm` permite definir um gestor de tarefas para orquestrar o trabalho dos agentes.

A opção `process=Process.hierarchical` permite definir de forma hierarquica a execução do crew independente das tarefas

[[MDX]] 

[Artigo](https://arxiv.org/abs/2307.07924) muito relevante para ler sobre como o Crew AI vai revolucionar o Desenvolvimento de Software