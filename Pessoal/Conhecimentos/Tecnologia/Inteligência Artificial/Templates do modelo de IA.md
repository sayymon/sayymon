
Exemplo de template de Modelo de IA

Para descobrir o template adequado, sempre cheque a descrição do modelo, por exemplo: [https://huggingface.co/microsoft/Phi-3-mini-4k-instruct](https://www.google.com/url?q=https%3A%2F%2Fhuggingface.co%2Fmicrosoft%2FPhi-3-mini-4k-instruct)

No caso do Phi 3, os autores recomendam esse template abaixo.

Obs: mais tarde veremos um modo de puxar esse template manual sem ter que copiar e colar ele manualmente aqui.

Essas tags formadas por `<|##nome##|>` são o que chamamos de Tokens especiais (special tokens) e são usadas para delimitar o início e fim de texto e dizer ao modelo como queremos que a mensagem seja interpretada

Os tokens especiais usados para interagir com o Phi 3 são esses:

- `<|system|>, <|user|> e <|assistant|>`: correspondem ao papel (role) das mensagens. Os papéis usados aqui são: [[system]], [[user]] e [[assistant]]
    
- `<|end|>`: Isso é equivalente ao [[Token EOS]] (End of String), usado para marcar o fim do texto/string.
    

Usaremos o .format para concatenar o prompt nesse template, assim não precisamos redigitar ali manualmente

```

template = """<|system|>

You are a helpful assistant.<|end|>

<|user|>

"{}"<|end|>

<|assistant|>""".format(prompt)

output = pipe(template, **generation_args)

print(output[0]['generated_text'])
```