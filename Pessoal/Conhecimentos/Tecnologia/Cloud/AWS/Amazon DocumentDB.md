

## Amazon DocumentDB (com foco na SAA-C03)

Amazon DocumentDB (com compatibilidade MongoDB) é um serviço de banco de dados NoSQL totalmente gerenciado na AWS que é compatível com a API MongoDB.  Ele é projetado para aplicativos que exigem escalabilidade, disponibilidade e desempenho para dados JSON semi-estruturados.

**Para que serve?**

* Armazenar e consultar documentos JSON.
* Construir aplicativos web, mobile e IoT escaláveis.
* Casos de uso com grande volume de dados, como catálogos de produtos, perfis de usuários, sessões de jogos e logs de aplicativos.
* Migrar aplicações MongoDB existentes para a nuvem com poucas ou nenhuma alteração de código.

**Quando utilizar?**

* Quando você precisa da flexibilidade do modelo de dados de documentos.
* Quando a escalabilidade e a disponibilidade são críticas.
* Quando você precisa de compatibilidade com a API MongoDB.
* Quando você quer reduzir o esforço administrativo de gerenciar um banco de dados.

**Principais conceitos:**

* **Compatível com MongoDB:**  Permite usar drivers e ferramentas MongoDB existentes.
* **Escalabilidade:** Facilmente escalável para lidar com cargas de trabalho crescentes.
* **Disponibilidade:** Oferece alta disponibilidade com replicação automática e failover.
* **Durabilidade:** Armazena dados em 6 réplicas em 3 zonas de disponibilidade.
* **Segurança:** Integração com AWS IAM para controle de acesso granular.
* **Custo-benefício:** Modelo de pagamento conforme o uso.
* **Clusters:** Um cluster DocumentDB consiste em um nó de instância primária e até 15 réplicas de leitura.
* **Instâncias:**  As instâncias são os servidores que hospedam o banco de dados.  Você escolhe o tipo de instância com base nas suas necessidades de desempenho.


**Diferença importante em relação ao MongoDB:**

Embora compatível com a API MongoDB, o DocumentDB *não* usa o mecanismo de armazenamento WiredTiger do MongoDB.  Ele usa um mecanismo de armazenamento próprio que é otimizado para desempenho e escalabilidade na AWS.  Isso significa que algumas funcionalidades avançadas do MongoDB podem não estar disponíveis no DocumentDB.  *Este é um ponto crucial para a SAA-C03*.


Em resumo, se você

continue



Em resumo, se você precisa de um banco de dados NoSQL escalável, altamente disponível e compatível com MongoDB na AWS, o DocumentDB é uma excelente opção.  Lembre-se da diferença crucial no mecanismo de armazenamento em relação ao MongoDB original ao preparar-se para o exame SAA-C03.  A compatibilidade se refere à API e aos drivers, não à estrutura interna do banco de dados.


responda a partir daqui

possui algum schema? permite fazer consultas por qualquer campo do documento?
pode ter indices ?



Não, o Amazon DocumentDB, assim como o MongoDB, não possui um schema rígido.  Isso significa que você não precisa definir a estrutura dos documentos antes de inseri-los no banco de dados. Cada documento pode ter uma estrutura diferente dentro da mesma coleção.  Essa flexibilidade é uma das principais características dos bancos de dados NoSQL orientados a documentos.

Sim, você pode fazer consultas por qualquer campo do documento, mesmo que esse campo não exista em todos os documentos da coleção.  O DocumentDB/MongoDB usa um modelo de dados flexível que permite essa funcionalidade.  No entanto, para otimizar o desempenho das consultas, é altamente recomendável criar índices.

Sim, o Amazon DocumentDB suporta índices.  Assim como no MongoDB, os índices ajudam a acelerar as consultas, permitindo que o banco de dados encontre os documentos relevantes de forma mais eficiente. Você pode criar índices em um ou mais campos de um documento, e o DocumentDB suporta diferentes tipos de índices, como índices únicos, índices compostos e índices de texto.  Criar índices em campos frequentemente usados em consultas é uma prática recomendada para melhorar o desempenho do seu aplicativo.

o que tem de diferencas 

3 zonas de disponibilidade

A replica primaria ~e dedicada a leitura e escrita, as replicas secundarias podem ficar 

Preciso perguntar em ingles se o document DB ~e indicado para casos de CQRS

Novas Instances

Cache das instancias sao reutilizadas e quando 

o Custo é por IOPS

Small use in the cache.

Host

Cluster endpoint é o recomendado

Spike CPU when

Instances e 

Backup in s3

TTL no document DB atua no backup ou trabalha em instancias diferentes ? 




Here's a breakdown of the differences you asked about, plus the CQRS question in English:

**Key Differences between Amazon DocumentDB and MongoDB:**

* **Storage Engine:** This is the most significant difference and a crucial point for the SAA-C03 exam.  DocumentDB uses its own custom storage engine optimized for AWS, while MongoDB uses WiredTiger. This means some advanced MongoDB features might not be available in DocumentDB, and performance characteristics can differ.

* **Scaling:** While both databases scale, they do so differently. DocumentDB scales by adding read replicas up to a total of 15,  improving read performance and availability.  MongoDB offers various scaling options, including sharding, which distributes data across multiple servers.  DocumentDB's approach simplifies scaling for many use cases but might not be as flexible as MongoDB's for extremely large or complex deployments.

* **Specific Feature Support:** Due to the different storage engines, certain MongoDB features are not supported in DocumentDB.  Always consult the official documentation for a comprehensive compatibility list.  This is especially important when migrating existing MongoDB applications.

**Three Availability Zones:**

DocumentDB stores data in six replicas across three Availability Zones. This provides high availability and fault tolerance.  The primary instance handles reads and writes.  In the event of a failure, one of the replicas in a different Availability Zone is automatically promoted to primary, ensuring minimal downtime.

**Read Replicas:**

The primary instance handles both reads and writes.  Up to 15 read replicas can be added to a DocumentDB cluster. These replicas asynchronously replicate data from the primary instance and serve read requests, offloading read traffic from the primary and improving read performance.  You can configure your application to direct read requests to these replicas.

**CQRS and DocumentDB (Question in English):**

Is Amazon DocumentDB suitable for CQRS (Command Query Responsibility Segregation) architectures?

**Answer:**

Yes, DocumentDB is suitable for CQRS architectures.  Its ability to scale read replicas independently makes it well-suited for handling the high read volume often seen in CQRS systems. You can direct read queries to the read replicas, separating them from the write operations on the primary instance.  This can improve performance and scalability.  Furthermore, the flexible schema of DocumentDB allows for different data representations optimized for reads and writes, further supporting the CQRS pattern.  However, keep in mind the differences


TTL no document DB atua no backup ou trabalha em instancias diferentes ? 



**New Instances and Cache Reuse:**

When you create a new DocumentDB instance, it doesn't reuse the cache from existing instances. Each instance has its own isolated cache.  This ensures data consistency and prevents interference between different instances.

**Cost:**

You are charged for each instance in your DocumentDB cluster (the primary and each read replica) based on instance size, storage used, and I/O operations.  You also pay for data transfer and backups.

**Cluster Endpoint:**

Using the cluster endpoint is the recommended approach for connecting to your DocumentDB cluster.  The cluster endpoint automatically routes read and write requests to the appropriate instance (primary for writes, and either primary or replicas for reads).  This simplifies application development and improves availability.

**CPU Spikes:**

CPU spikes can occur for various reasons, including heavy query loads, large data imports, or inefficient queries.  Monitoring CPU utilization is crucial.  If you consistently experience high CPU usage, you might need to scale your instance up, optimize your queries, or add read replicas to distribute the load.

**Backups in S3:**

DocumentDB automatically backs up your data to S3.  These backups are continuous and incremental, allowing you to restore your database to any point in time within your backup retention period.

**TTL (Time-to-Live) Indexes:**

TTL indexes in DocumentDB work at the database level, not on backups.  They automatically delete documents in your collections based on a timestamp field in the documents.  This is useful for managing data with a limited lifespan, such as session data or log files. The TTL process runs on the primary instance and the changes are then replicated to the secondary instances.  TTL indexes do *not* affect backups directly; expired documents are removed from the active database, and subsequent backups will reflect those deletions.


Responda em portugues o Document comentam da parte de ACID e que suportam transacao e rollback, mas tava vendo se eles respeitam as anotacoes de transacao