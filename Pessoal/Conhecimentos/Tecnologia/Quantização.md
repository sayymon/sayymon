
Quantização refere-se ao processo de converter um modelo de [[rede neural]] com parâmetros de precisão flutuante para um modelo com parâmetros de precisão fixa. Isso pode ser feito reduzindo o número de bits usados para representar os pesos e ativações da rede neural, o que resulta em uma redução no tamanho do modelo e em uma maior eficiência computacional.

A quantização é frequentemente utilizada para comprimir modelos de redes neurais, tornando-os mais leves e mais rápidos para executar em dispositivos com recursos limitados, como smartphones e dispositivos IoT. Além disso, a quantização também pode ajudar a acelerar o treinamento e inferência da rede neural, permitindo que mais cálculos sejam executados simultaneamente.

Em resumo, a quantização é uma técnica importante na área de [[inteligência artificial]] que visa otimizar o desempenho dos modelos de redes neurais, tornando-os mais eficientes e práticos para uma variedade de aplicações.

Solução da Hugging face : [https://huggingface.co/blog/4bit-transformers-bitsandbytes](https://www.google.com/url?q=https%3A%2F%2Fhuggingface.co%2Fblog%2F4bit-transformers-bitsandbytes)

Ainda existem outras soluções para quantização (por exemplo [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) ou o [AutoAWQ](https://github.com/casper-hansen/AutoAWQ)) que podem ou não otimizar mais ainda. Caso não deseje se incomodar com otimização/desempenho e ao mesmo tempo manter a qualidade então avalie a possibilidade de usar uma solução paga.

Exemplo de como Quantizar um modelo para reduzir e conseguir utilizar modelos pezados : 

```
quantization_config = BitsAndBytesConfig(

load_in_4bit=True,

bnb_4bit_quant_type="nf4",

bnb_4bit_use_double_quant=True,

bnb_4bit_compute_dtype=torch.bfloat16

)
```

Explicação dos parâmetros acima:

`load_in_4bit`- Este parâmetro habilita a quantização de 4 bits. Quando definido como True, os pesos do modelo são carregados com precisão de 4 bits, reduzindo significativamente o uso de memória.

- Impacto: Menor uso de memória e cálculos mais rápidos com impacto mínimo na precisão do modelo.

`bnb_4bit_quant_type` - especifica o tipo de quantização de 4 bits a ser usado. "nf4" significa NormalFloat4, um esquema de quantização que ajuda a manter o desempenho do modelo enquanto reduz a precisão.

- Impacto: Equilibra o trade-off entre tamanho e desempenho do modelo.

`bnb_4bit_use_double_quant` - quando definido como True, este parâmetro habilita a quantização dupla, o que reduz ainda mais o erro de quantização e melhora a estabilidade do modelo.

- Impacto: Reduz o erro de quantização, aprimorando a estabilidade do modelo.

`bnb_4bit_compute_dtype` - define o tipo de dados para cálculos. Usar torch.bfloat16 (Brain Floating Point) ajuda a melhorar a eficiência computacional, mantendo a maior parte da precisão dos números de ponto flutuante de 32 bits.

- Impacto: Cálculos eficientes com perda mínima de precisão.

Aplicando efetivamente a quantifização em Modelo mais complexo Ex : 

```
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config)
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

```
prompt = ("Quem foi a primeira pessoa no espaço?")
messages = [{"role": "user", "content": prompt}]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")
model_inputs = encodeds.to(device)
generated_ids = model.generate(model_inputs, max_new_tokens = 1000, do_sample = True,
                               pad_token_id=tokenizer.eos_token_id)
decoded = tokenizer.batch_decode(generated_ids)
res = decoded[0]
res
```




> [!dica]- Quantizacao de livros
> Havia uma cidade onde os habitantes tinham um problema: seus livros estavam ocupando muito espaço nas estantes e era difícil carregá-los para lá e para cá. Um sábio inventor chegou à cidade e propôs uma solução - a quantização dos livros. Ele explicou que poderia reduzir o tamanho dos livros sem perder a essência de suas histórias.
Assim, o inventor pegou um livro comum e aplicou seu conhecimento em quantização, reduzindo o número de páginas e simplificando as palavras sem perder a mensagem original. O resultado foi surpreendente - o livro agora ocupava menos espaço, era mais fácil de transportar e ainda assim mantinha toda a sua sabedoria.
Os habitantes da cidade ficaram maravilhados com a ideia de quantização e logo todos os livros foram transformados dessa maneira. Agora, eles podiam carregar suas histórias favoritas para onde quer que fossem, sem se preocupar com o peso ou o espaço ocupado.
E assim, graças à quantização, os livros se tornaram mais acessíveis e práticos, permitindo que todos desfrutassem da magia da leitura em qualquer lugar.
#storytelling