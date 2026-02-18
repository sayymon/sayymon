
## O que são templates de restauração no cloud formation ?


 Templates de restauração no AWS CloudFormation são modelos que definem a infraestrutura necessária para recuperar um ambiente ou aplicação em caso de falhas ou desastres. Esses templates incluem recursos como instâncias EC2, bancos de dados RDS, grupos de segurança, entre outros, e são usados ​​para provisionar rapidamente uma infraestrutura de backup em um ambiente de nuvem. Ao utilizar templates de restauração no CloudFormation, as organizações podem automatizar o processo de recuperação e minimizar o tempo de inatividade em situações de emergência.

 [Os modelos do CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html) incluem várias seções principais. A seção Resources (Recursos) é a única obrigatória.

Exemplo. : 

```
{
    "AWSTemplateFormatVersion": "version date",
    "Description": "JSON string",
    "Parameters": {
        set of parameters
    },
    "Conditions": {
        set of conditions
    },
    "Resources": {
        set of resources
        },
}
```