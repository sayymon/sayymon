É um executor de [[LLMs]] criado pela [[Meta]] que permite utilizar via terminal varios modelos

Para baixar o Ollama basta ir no site e baixar : 

https://ollama.com/

Para rodar o ollama localmente : 

```
ollama run llama3.1
```

Ou um modelo menorzinho [[SLM]]

```
ollama run phi3
```

É possive visualizar opções e setar algguns parametros com : 

```shell

/set

Available Commands:
  /set parameter ...     Set a parameter
  /set system <string>   Set system message
  /set history           Enable history
  /set nohistory         Disable history
  /set wordwrap          Enable wordwrap
  /set nowordwrap        Disable wordwrap
  /set format json       Enable JSON mode
  /set noformat          Disable formatting
  /set verbose           Show LLM stats
  /set quiet             Disable LLM stats
```

