


A regressão logística é um tipo de modelo estatístico usado para prever a probabilidade de uma variável dependente binária com base em uma ou mais variáveis independentes. Ela é amplamente utilizada em campos como ciência de dados, análise de dados e machine learning para problemas de classificação.

Na regressão logística, a variável dependente é transformada em uma escala logarítmica para que o modelo possa estimar as chances ou probabilidades da variável dependente ocorrer. O modelo calcula a probabilidade de ocorrência da variável dependente com base nos valores das variáveis independentes.

A regressão logística é especialmente útil quando se trata de problemas com duas categorias, como sim ou não, verdadeiro ou falso, positivo ou negativo. Ela fornece uma maneira de quantificar a relação entre as variáveis independentes e a probabilidade da ocorrência da variável dependente.

Em resumo, a regressão logística é uma técnica estatística poderosa para modelar e prever variáveis binárias com base em outras variáveis independentes. Ela é amplamente aplicada em diversas áreas, incluindo medicina, finanças, marketing e muitas outras.


Exemplo de modelo de regressão logistica no BigQuery : 

```
CREATE OR REPLACE MODEL `ecommerce.classification_model`

OPTIONS

(

model_type='logistic_reg',

labels = ['will_buy_on_return_visit']

)

AS
```