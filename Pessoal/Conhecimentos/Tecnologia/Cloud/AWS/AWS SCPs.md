
o que são SCPS na AWS de forma suscinta e bem clara de facil entendimento? 



Title: AWS SCPs

AWS SCPs (**Service Control Policies**) são como guarda-corpos para sua conta da AWS.  Imagine que sua organização tem várias contas na AWS.  SCPs permitem que você defina regras centrais que se aplicam a todas essas contas (ou a grupos específicos delas), impedindo que ações indesejadas sejam realizadas, mesmo que os usuários dentro dessas contas tenham permissões para fazê-las.

Em resumo: SCPs são políticas no nível da organização que **restringem** as ações permitidas nas contas da AWS.  Eles agem como um "não pode fazer isso", independentemente das permissões concedidas dentro das contas individuais.  Isso ajuda a garantir a conformidade com políticas de segurança, regulamentações e melhores práticas.
