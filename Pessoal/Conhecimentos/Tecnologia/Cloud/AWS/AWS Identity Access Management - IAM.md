
O IAM fornece [[IAM Policys]] gerenciadas pré-construídas da AWS para ajudar você a começar rapidamente. 

Duas políticas pré-construídas fornecem acesso somente leitura ao Amazon EC2 e ao Amazon RDS.

Mas tambem é possivel personalizar as politicas

Ao criar usuários, você pode atribuir a eles permissões para acessar recursos por meio do [[AWS Management Console]], [[AWS CLI]] ou ferramentas de desenvolvedor. 

Você também pode colocar [[IAM users]] em [[IAM grupos]] e atribuir permissões.

IAM Roles serve para delegar acessos especificos para alguns usuarios ou grupos 

o IAM não tem custos adicionais e a AWS recomenda veemente o seu uso.

Permite especificar algumas condicoes como data e hora de utilizacao, tambem como vai se conectar seja via [[SSL]] ou somente via console, tambem permite restringir os ips de origem e pode exigir alguns tipos de autehnticacao adicionais como [[MFA]]

Permite  implementar o conceito de [[Federação de Identidade]]

tambem é possivel gerenciar as identidades com o padrao de [[SAML 2.0]]

### Qual a diferenca de IAM policys, roles e groups ?

IAM Policies são conjuntos de permissões que especificam quais ações um usuário, grupo ou role pode realizar em recursos específicos. 

IAM Roles são entidades que concedem permissões temporárias para usuários, serviços ou aplicativos, permitindo a delegação de acesso. 

IAM Groups são coleções de usuários aos quais políticas podem ser atribuídas em massa, facilitando a gestão de permissões para múltiplos usuários de uma vez. Em resumo, as políticas definem as permissões, os roles delegam acesso e os grupos simplificam a atribuição e gerenciamento de permissões para múltiplos usuários.
