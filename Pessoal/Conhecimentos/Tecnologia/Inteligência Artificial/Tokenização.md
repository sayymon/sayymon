
Gera [[Tokens]] que são representações de palavras convertidas em numeros vetoriais.

Podemos extrair partes importantes como o radical, prefixo e sufixo.

de exemplo de tokenização da seguinte frase :

"Programação será substituída por inteligência artificial".

Tokens:
1. Programação
2. será
3. substituida
4. por
5. inteligência
6. artificial

[[Radicais]]:
1. Programação - Programa
2. será - será
3. substituída - substitu
4. por - por
5. inteligência - inteligênc
6. artificial - artificial

[[Sufixos]]:
1. Programação - ção
2. será - será
3. substituída - ída
4. por - por
5. inteligência - ência
6. artificial - ial

Ferramenta da [[OpenAI]] para quantificar os tokens de um texto : 

https://platform.openai.com/tokenizer

Pelo [[Hugging face]] é possivel utilizar o Tokenizer

```
id_model = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(id_model)
pipe = pipeline("text-generation", model = model, tokenizer = tokenizer)
```