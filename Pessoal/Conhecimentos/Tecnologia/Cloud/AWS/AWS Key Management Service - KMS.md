 o KMS pode ser usado para gerenciar chaves do lado do Servidor SSE-KMS ou do lado do servidor fornecidas pelo Cliente SSE-C com a criptografia no lado do servidor com chaves fornecidas pelo cliente (SSE-C), o Amazon S3 criptografa os objetos no servidor usando uma chave que é fornecida na solicitação PUT. 
 
 É necessário fornecer a mesma chave nas solicitações GET para que o Amazon S3 descriptografe o objeto. 
 
 Os clientes também podem criptografar os dados no seu lado antes do upload para o Amazon S3, de modo que podem descriptografá-los ao fazer download. Os Kits de Desenvolvimento de Software (SDKs) da AWS incluem um cliente de criptografia do S3 que simplifica o processo

De forma sucinta e simples explique o KMS e quando utilizalo ? 



O AWS KMS é um serviço que permite criar e gerenciar chaves criptográficas.  Use-o quando precisar criptografar dados na AWS, seja em repouso (como em um bucket S3) ou em trânsito.  Simplifica o processo de gerenciamento de chaves, oferecendo um local centralizado e seguro para armazená-las e controlá-las.
