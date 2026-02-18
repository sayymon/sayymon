
## Via terminal

## Exemplo de query : 

```
bq query --use_legacy_sql=false \
'SELECT
   word,
   SUM(word_count) AS count
 FROM
   `bigquery-public-data`.samples.shakespeare
 WHERE
   word LIKE "%raisin%"
 GROUP BY
   word'
```
Criando uma tabela no BigQuery 

```
bq mk babynames
```

Visualizar [[datasets]]

```
bq ls
```


Preencher e criar uma tabela com base em um arquivo : 

```
curl -LO http://www.ssa.gov/OACT/babynames/names.zip

unzip names.zip

bq load babynames.names2010 yob2010.txt name:string,gender:string,count:integer
```

Executando uma query 

```
bq query "SELECT name,count FROM babynames.names2010 WHERE gender = 'M' ORDER BY count ASC LIMIT 5"
```

Remover o dataset : 

```
bq rm -r babynames
```

# Via API's

Documentação : 

https://cloud.google.com/bigquery/docs/reference/rest

BigQuery ML

Principal função é para criar e treinar modelos utilizando [[SQL]]


Criar e treinar um Modelo :

```
#standardSQL

CREATE OR REPLACE MODEL `bqml_lab.sample_model`

OPTIONS(model_type='logistic_reg') AS

SELECT

IF(totals.transactions IS NULL, 0, 1) AS label,

IFNULL(device.operatingSystem, "") AS os,

device.isMobile AS is_mobile,

IFNULL(geoNetwork.country, "") AS country,

IFNULL(totals.pageviews, 0) AS pageviews

FROM

`bigquery-public-data.google_analytics_sample.ga_sessions_*`

WHERE

_TABLE_SUFFIX BETWEEN '20160801' AND '20170631'

LIMIT 100000;
```

Validar um Modelo `ML.EVALUATE`: 

```
#standardSQL
SELECT
  *
FROM
  ml.EVALUATE(MODEL `bqml_lab.sample_model`, (
SELECT
  IF(totals.transactions IS NULL, 0, 1) AS label,
  IFNULL(device.operatingSystem, "") AS os,
  device.isMobile AS is_mobile,
  IFNULL(geoNetwork.country, "") AS country,
  IFNULL(totals.pageviews, 0) AS pageviews
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20170701' AND '20170801'));
  ```

Fazer predições com base nos dados 

```
#standardSQL
SELECT
  fullVisitorId,
  SUM(predicted_label) as total_predicted_purchases
FROM
  ml.PREDICT(MODEL `bqml_lab.sample_model`, (
SELECT
  IFNULL(device.operatingSystem, "") AS os,
  device.isMobile AS is_mobile,
  IFNULL(totals.pageviews, 0) AS pageviews,
  IFNULL(geoNetwork.country, "") AS country,
  fullVisitorId
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20170701' AND '20170801'))
GROUP BY fullVisitorId
ORDER BY total_predicted_purchases DESC
LIMIT 10;
```

É bem comum criar tabelas temporarias para fazer subsets `all_visitor_stats` de dados Ex : 

```
# visitors who bought on a return visit (could have bought on first as well

WITH all_visitor_stats AS (

SELECT

fullvisitorid, # 741,721 unique visitors

IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit

FROM `data-to-insights.ecommerce.web_analytics`

GROUP BY fullvisitorid

)

  

SELECT

COUNT(DISTINCT fullvisitorid) AS total_visitors,

will_buy_on_return_visit

FROM all_visitor_stats

GROUP BY will_buy_on_return_visit
```


Query para avaliar se o modelo esta bom ou ruim : 

```
SELECT
  roc_auc,
  CASE
    WHEN roc_auc > .9 THEN 'good'
    WHEN roc_auc > .8 THEN 'fair'
    WHEN roc_auc > .7 THEN 'decent'
    WHEN roc_auc > .6 THEN 'not great'
  ELSE 'poor' END AS model_quality
FROM
  ML.EVALUATE(MODEL ecommerce.classification_model,  (

SELECT
  * EXCEPT(fullVisitorId)
FROM

  # features
  (SELECT
    fullVisitorId,
    IFNULL(totals.bounces, 0) AS bounces,
    IFNULL(totals.timeOnSite, 0) AS time_on_site
  FROM
    `data-to-insights.ecommerce.web_analytics`
  WHERE
    totals.newVisits = 1
    AND date BETWEEN '20170501' AND '20170630') # eval on 2 months
  JOIN
  (SELECT
    fullvisitorid,
    IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit
  FROM
      `data-to-insights.ecommerce.web_analytics`
  GROUP BY fullvisitorid)
  USING (fullVisitorId)

));
```

Pela recomendação tem que ser maior do que 0.8 ,se for abaixo disso o modelo precisa de mais features.

Dentro do modelo é possivel avaliar o Evaluation traz metricas interessantes que é bacana conferir, como a [[Matrix de confusão]]

Chegar no equilibrio que é o desafio para evitar o overfitting

### Outros conjuntos de dados para analisar

Se quiser saber mais sobre a criação de modelos em outros conjuntos de dados, como na previsão de tarifas para corridas de táxi, use o projeto **bigquery-public-data**.

1. Para abrir o conjunto de dados **bigquery-public-data**, clique em **+Adicionar**. Clique em **Marcar um projeto com estrela por nome** em Outras fontes.
2. Em seguida, digite o nome `bigquery-public-data`.
3. Clique em **Marcar com estrela**.

O projeto `bigquery-public-data` será listado na seção Explorer.

Ambos projetos `data-to-insights` são projetos legais para treinar Machine Learning com BigQuery.