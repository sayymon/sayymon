
Você é um engenheiro de software estudando para certificação SAA-C03 da AWS, descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Amazon S3: Armazenamento de Objetos Simples e Escalável

**O que é?**

Amazon S3 (Simple Storage Service) é um serviço de armazenamento de objetos na nuvem oferecido pela AWS.  Em vez de armazenar arquivos em um sistema de arquivos tradicional, o S3 armazena dados como "objetos" dentro de "buckets" (baldes).  Imagine um balde como uma pasta principal e os objetos como os arquivos dentro dela.

**Para que serve?**

S3 é usado para armazenar virtualmente qualquer tipo de dado, como:

* **Backup e recuperação:** Armazenamento de backups de servidores, bancos de dados e aplicações.
* **Armazenamento de dados de aplicações:** Imagens, vídeos, logs, documentos, etc.
* **Hospedagem estática de sites:** HTML, CSS, JavaScript e outros arquivos para sites estáticos.
* **Big data analytics:** Armazenamento de grandes conjuntos de dados para processamento e análise.
* **Data lakes:** Repositório centralizado para dados brutos de diversas fontes.
* **Distribuição de conteúdo:** Armazenamento de arquivos para distribuição global através da AWS CloudFront.
* **Arquivamento de dados:** Armazenamento de dados a longo prazo com custos reduzidos.

**Quando utilizar?**

* Quando precisar de alta disponibilidade e durabilidade para seus dados.
* Quando precisar de escalabilidade para armazenar grandes volumes de dados.
* Quando precisar de acesso programático aos seus dados.
* Quando precisar de diferentes opções de custo e performance para diferentes tipos de dados.

**Principais Conceitos:**

* **Buckets:** Contêineres para objetos. Devem ter nomes globalmente únicos.
* **Objetos:** Arquivos e seus metadados (informações sobre o arquivo).
* **Chaves:** Identificadores únicos para cada objeto dentro de um bucket.  É como o nome do arquivo + caminho da pasta em um sistema tradicional.
* **Regiões:** Localização geográfica onde o bucket e seus objetos são armazenados.
* **Classes de Armazenamento:** Diferentes opções de custo e performance (S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval e S3 Glacier Deep Archive).
* **





O S3 é um servico super util para armazenar qualquer tipo de arquivo, como um bucket.


O Amazon S3 oferece diferentes tipos de armazenamento, como o Standard, o Standard-IA (Infrequent Access), o One Zone-IA, o Intelligent-Tiering e o Glacier. 

Cada tipo de armazenamento possui características específicas e é cobrado de acordo com a quantidade de dados armazenados, as requisições feitas e a transferência de dados.

No modelo de cobrança do Amazon S3, os clientes pagam pelos recursos que utilizam, como o armazenamento dos arquivos, as requisições feitas para acessar ou mover os dados e a transferência de dados realizada. 

Os preços variam de acordo com o tipo de armazenamento escolhido e a região onde os dados estão armazenados.
## S3 Transfer Acceleration

facilita uploads mais rápidos usando locais de borda para copiar dados para o Amazon S3

## Mult part Upload

Você pode usar um multipart upload para fazer upload de arquivos maiores, como os arquivos nesse cenário. Se a transmissão de alguma parte falhar, você poderá retransmitir essa parte sem afetar as outras.

Para obter mais informações sobre uploads multiparte, consulte [Carregar e copiar objetos usando multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html).

O S3 tem recurso que permite ativare o [[CORS]] diretamente para que os navegadores web não bloqueiam a execução de scripts originários de servidores com nome de domínio diferente da página web

Tem como configurar uma replicação entre rergiões no S3 : 

[Amazon S3 Cross-Region Replication (CRR)](http://aws.amazon.com/s3/features/replication/)

Qual a vantagem e quando usar replicação entre regiões no S3 ?



A vantagem de usar a replicação entre regiões no Amazon S3 é garantir a disponibilidade e durabilidade dos seus dados, mesmo em caso de falhas em uma região específica. Isso pode ser útil para empresas que precisam cumprir requisitos de conformidade ou que desejam ter uma estratégia de recuperação de desastres eficaz. Além disso, ao replicar os dados entre regiões, você pode reduzir a latência para usuários localizados em diferentes partes do mundo.

Em resumo, a replicação entre regiões no Amazon S3 é recomendada quando você precisa garantir alta disponibilidade e durabilidade dos seus dados, melhorar o desempenho para usuários globais e/ou implementar uma estratégia eficaz de recuperação de desastres.

Você pode usar o recurso [Notificações de eventos do Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) para receber notificações quando determinados eventos ocorrerem no seu bucket do S3. Os destinos com suporte incluem o Amazon SNS, o Amazon SQS e o Lambda.