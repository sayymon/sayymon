Amazon web services prove serviços em [[Cloud Computing ]]
## Serviços


![[AWS Computação]]

![[AWS Armazenamento]]

![[AWS Bancos de Dados]]

![[AWS Rede e Conectividade]]

![[AWS Integração e Mensageria]]

![[AWS Análise de Dados]]

![[AWS Machine Learning IA]]

![[AWS Serviços Gerenciados]]

![[AWS Serviços de Gerenciamento de Custos e governança]]

![[AWS Segurança, identidade e conformidade]]

![[AWS Dev Ops]]

![[AWS Migração e transferência]]
Estes são apenas alguns dos serviços oferecidos pela AWS em diversas categorias para atender às necessidades de diferentes tipos de negócios e aplicações.


 A AWS tem alguns recursos bem legais como o [[AWS Cloud Quest]] -> https://explore.skillbuilder.aws/learn/course/external/view/elearning/7636/cloud-quest
 Que possibilita fazer testes praticos junto com o [[AWS SimuLearn]] que achei bem legal onde tem ambientes virtuais para simularmos o que aprendemos sem ter que ficar criando recursos passiveis de custos nas nossas contas pessoais.
### Como usando a cli da aws consigo obter a seguinte credencial do secret manager sem ter que entrar no console : 

Ex : `rds/notification-center-management/admin`

Para obter a credencial do [[AWS Secret Manager]] `rds/notification-center-management/admin` usando a [[AWS CLI]], você pode seguir os seguintes passos:

1. Certifique-se de que você tenha configurado corretamente suas credenciais da AWS na AWS CLI. Você pode fazer isso executando o comando `aws configure` e inserindo suas informações de acesso (Access Key ID, Secret Access Key, região padrão e formato de saída).

2. Em seguida, você pode usar o comando `aws secretsmanager get-secret-value` para obter o valor do segredo desejado. Por exemplo, execute o seguinte comando na sua linha de comando:

```
aws secretsmanager get-secret-value --secret-id rds/notification-center-management/admin
```

Isso retornará o valor do segredo `rds/notification-center-management/admin` armazenado no AWS Secret Manager.

Ex : 

```
{
    "ARN": "arn:aws:secretsmanager:us-east-1:449466460580:secret:rds/notification-center-management/admin-dDgBc1",
    "Name": "rds/notification-center-management/admin",
    "VersionId": "7f36196a-26b9-4c89-be91-87e5fae793cd",
    "SecretString": "{\"engine\": \"mysql\", \"port\": 3306, \"host\": \"notification-center-management-db.buildstaging.aws.hotmart\", \"username\": \"root\", \"password\": \"7oxI44D16zDVg3gNKIADmgYelgUM6u8v\"}",
    "VersionStages": [
        "AWSCURRENT"
    ],
    "CreatedDate": "2024-07-18T21:14:43.999000-03:00"
}
```

A AWS lançou uma versão do console simplificada chamada [[Lightsail]] que é uma interface mais simplificada para focar na implementação tem planos interessantes de baixo custo para criação da sua infra


Os fundamentos e conceitos que envolvem a AWS são abrangentes e interconectados, permitindo a construção e gerenciamento de uma ampla gama de aplicações e infraestruturas na nuvem.  Aqui estão alguns dos principais:

**1. Computação em Nuvem (Cloud Computing):** A base de tudo.  A AWS oferece diferentes modelos de serviço de cloud computing:

* **Infraestrutura como Serviço (IaaS):**  Você controla os recursos de computação, armazenamento e rede (ex: EC2, S3, VPC).  Oferece o maior nível de controle e flexibilidade.
* **Plataforma como Serviço (PaaS):**  Você gerencia suas aplicações e dados, enquanto a AWS cuida da infraestrutura subjacente (ex: Beanstalk, RDS). Simplifica o desenvolvimento e a implantação.
* **Software como Serviço (SaaS):** Você usa aplicações prontas fornecidas pela AWS (ex: WorkMail, Chime).  A AWS gerencia tudo, desde a infraestrutura até a aplicação.

**2. Alta Disponibilidade e Tolerância a Falhas:** A AWS possui múltiplas [[Zona de disponibilidade (AZs)]] dentro de cada região. Distribuindo seus recursos em diferentes AZs, você garante que sua aplicação continue funcionando mesmo se uma AZ falhar.  Serviços como Elastic Load Balancing e Auto Scaling ajudam a manter a disponibilidade e escalabilidade.

**3. Escalabilidade e Elasticidade:**  A AWS permite escalar seus recursos para cima ou para baixo conforme a demanda, pagando apenas pelo que usar.  Auto Scaling ajusta automaticamente a capacidade de computação com base nas métricas definidas.

**4. Segurança:**  A AWS oferece uma ampla gama de serviços de segurança, incluindo gerenciamento de identidade e acesso (IAM), firewalls (WAF, Security Groups), e monitoramento de segurança (CloudTrail, GuardDuty). A responsabilidade pela segurança é compartilhada: a AWS é responsável pela segurança *da* nuvem, enquanto o usuário é responsável pela segurança *na* nuvem.

**5. Armazenamento:** A AWS oferece diversas opções de armazenamento, cada uma com características e custos diferentes, como:

* **S3 (Simple Storage Service):** Armazenamento de objetos para dados não estruturados (imagens, vídeos, arquivos).
* **EBS (Elastic Block Storage):** Armazenamento em