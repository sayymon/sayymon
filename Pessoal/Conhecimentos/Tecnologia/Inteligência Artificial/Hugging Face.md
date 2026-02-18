 É o repositório de [[Modelos de IA]]  [[Open Source]] e [[Closed Source]]
Alem de possuir bases de dados([[Dataset]]s) para utilizar em treinamentos como também ferramentas

Ficou bem conhecido por possuir a lib de [[Transformers]] Ex : 

```python
from transformers import pipeline
generator = pipeline('text-generation', model = 'HuggingFaceH4/zephyr-7b-beta')
generator("Hello, I'm a language model", max_length = 30, num_return_sequences=3)
## [{'generated_text': "Hello, I'm a language modeler. So while writing this, when I went out to meet my wife or come home she told me that my"},
##  {'generated_text': "Hello, I'm a language modeler. I write and maintain software in Python. I love to code, and that includes coding things that require writing"}, ...
```

Token de leitura: 

> ⚠️ Token movido para arquivo local `sensitive-data.md` (não versionado)

Use variáveis de ambiente:
```python
import os
os.environ["HF_TOKEN"] = getpass.getpass()
```


Tem alguns tipos de Modelos organizados pelos sufixos:
- [[Base Models]] : São Modelos base com pré treinamento em [[PLN]] utilizados como base para outros modelos como de chat ou de instruções
- [[Instruct Models]] : São Modelos Otimizados para receber instruções e realizar ações
- [[Chat Models]] : Como o proprio nome indica são modelos otimizados para chats iterações diretas com o usuarios

Dar preferencia sempre a modelos com o final da terminologia -Instruct 

Ex : `Meta-llama-3-8b-Instruct`


Vamos importar alguns componentes da biblioteca transformers

- [[AutoModelForCausalLM]]: Uma classe que fornece um modelo de linguagem causal (ou autoregressivo) pré-treinado (por exemplo, GPT-2, GPT-3) que são adequados para tarefas de geração de texto.
- [[AutoTokenizer]]: Uma classe que fornece um tokenizador que corresponde ao modelo. O tokenizador é responsável por converter texto em tokens (numéricos) que o modelo pode entender.
- [[pipeline]]: fornece uma interface simples e unificada para várias tarefas de PNL, facilitando a execução de tarefas como geração de texto, classificação e tradução.
- [[BitsAndBytesConfig]]: Uma classe para configuração de [[Quantização]] e outras otimizações de baixo nível para melhorar a eficiência computacional.


Também estamos definindo a variável device, que especifica o dispositivo de computação a ser usado:

- Esta linha verifica se uma GPU habilitada para [[CUDA]] está disponível. Se estiver, o código define o dispositivo para cuda:0 (a primeira GPU). Se não estiver, ele volta a usar a CPU.

Lembrando que o uso de GPU pode acelerar significativamente o treinamento e a inferência de modelos de aprendizado profundo. Vamos aproveitar da GPU gratuita do Colab (T4).

Para importar um modelo pelo Hugging face : 

```
model = AutoModelForCausalLM.from_pretrained(

"microsoft/Phi-3-mini-4k-instruct",

device_map = "cuda", // Especifica que o modelo deve ser carregado em uma GPU

torch_dtype = "auto", // Define automaticamente o tipo de dados apropriado para os tensores

trust_remote_code = True, // Permite o carregamento de código personalizado do repositório de modelos no HuggingFace

attn_implementation="eager" // Especifica o método de implementação para o mecanismo de atenção

)
```

Depois é necessario definir a [[tokenização]]  

```
tokenizer = AutoTokenizer.from_pretrained(id_model)
```

E a pipeline : 

```
pipe = pipeline("text-generation", model = model, tokenizer = tokenizer)
```

Depois configurar os [[Hiperparametros]] como [[Temperatura do modelo de IA]] podemos definir o prompt conforme exemplo : 

```python
prompt = "Explique o que é computação quântica"
output = pipe(prompt, **generation_args)
```
o Modelo pode retornar informações além da pergunta mas é necessário definir o [[Token de Parada]]  ou utilizar [[Templates do modelo de IA]] para evitar tais respostas adicionais e inoportunas


Importar o HF_TOKEN sem colocar no projeto : 

```
os.environ["HF_TOKEN"] = getpass.getpass()
```

