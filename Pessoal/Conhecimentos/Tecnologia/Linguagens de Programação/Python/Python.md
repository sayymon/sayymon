
[[Linguagem de Programação]]

# AWS

Para integrar com a AWS temos a lib [[boto3]]

### Como usar o boto3

Rodar o `pip install boto3` 

criar a instancia  de sessão ai pode passar o profile

```
session = boto3.Session(profile_name='sparkle')
```


com boto3 como filtrar usando o dynamodb uma coluna que contenha o valor igual a "player#123" ? 



Para filtrar usando o DynamoDB com boto3 e encontrar uma coluna que contenha o valor "player#123", você pode usar a expressão de filtro do DynamoDB. Aqui está um exemplo de como fazer isso:

```python
import boto3

# Criar a instância da sessão
session = boto3.Session(profile_name='sparkle')

# Conectar-se ao DynamoDB
dynamodb = session.client('dynamodb')

# Definir a expressão de filtro
filtro = {
    'TableName': 'NomeDaTabela',
    'FilterExpression': 'contains(NomeDaColuna, :valor)',
    'ExpressionAttributeValues': {
        ':valor': {'S': 'player#123'}
    }
}

# Fazer a consulta no DynamoDB
response = dynamodb.scan(**filtro)

# Imprimir os resultados
for item in response['Items']:
    print(item)
```

Certifique-se de substituir "NomeDaTabela" pelo nome da sua tabela no DynamoDB e "NomeDaColuna" pelo nome da coluna que você deseja filtrar. Isso deve retornar os itens que possuem o valor "player#123" na coluna especificada.


Configurar os certificados do Zscaler

cat ~/Downloads/ZscalerRootCertificate-2048-SHA256.crt >> $(python -m certifi)


## Configurar as variaveis de ambiente


Configurar variáveis de ambiente em um projeto Python é uma prática comum para gerenciar configurações sensíveis, como credenciais, chaves de API e outras informações que não devem ser hardcoded no código.

Para utilizar um arquivo `.env` em seu projeto Python, você pode usar a biblioteca `python-dotenv`, que facilita o carregamento das configurações de ambiente a partir desse arquivo.

Aqui estão os passos para configurar e utilizar variáveis de ambiente com um arquivo `.env`:

1. **Instalar a biblioteca [[python-dotenv]]**:

Você pode instalar a biblioteca usando pip. Execute o seguinte comando no terminal:

```bash

pip install python-dotenv

```

2. **Criar um arquivo `.env`**:

Na raiz do seu projeto, crie um arquivo chamado `.env`. Nele, você pode definir suas variáveis de ambiente no seguinte formato:

```plaintext

APP_SECRET_KEY=your_secret_key

DATABASE_URL=mysql://user:password@localhost/dbname

DEBUG=True

```

3. **Carregar as variáveis de ambiente no seu script Python**:

No início do seu arquivo Python, você pode carregar essas variáveis usando a biblioteca `python-dotenv`. Aqui está um exemplo simples de como fazer isso:

```python

import os

from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env

load_dotenv()

# Agora você pode acessar as variáveis de ambiente

secret_key = os.getenv('APP_SECRET_KEY')

database_url = os.getenv('DATABASE_URL')

debug = os.getenv('DEBUG') == 'True' # Convertendo para booleano

print(f'Secret Key: {secret_key}')

print(f'Database URL: {database_url}')

print(f'Debug Mode: {debug}')

```

4. **Executar seu script**:

Agora, sempre que você executar seu script Python, as variáveis de ambiente definidas no arquivo `.env` estarão disponíveis para uso.

### Benefícios de usar .env

- **Segurança**: Mantém informações sensíveis fora do código-fonte.

- **Facilidade**: Permite alterar configurações sem modificar o código.

- **Portabilidade**: Facilita a configuração em diferentes ambientes (desenvolvimento, teste, produção).

Comandinho maroto para copiar para o terminal : 

```shell
 export $(grep -v '^#' .env | xargs)
 ```


## Como criar um ambiente Virtual do Python?



Basta sar a ferramenta integrada `venv`. Aqui estão os passos para criar e ativar um ambiente virtual:

1. **Criar um novo ambiente virtual**:
   Abra o Terminal e navegue até a pasta onde deseja criar o ambiente virtual. Em seguida, execute o seguinte comando para criar um novo ambiente virtual:

   ```bash
   python3 -m venv nome_do_ambiente
   ```

   Isso criará uma nova pasta com o nome especificado (`nome_do_ambiente`) que conterá todos os arquivos necessários para o ambiente virtual.

2. **Ativar o ambiente virtual**:
   Após criar o ambiente virtual, você precisa ativá-lo. Para isso, execute o seguinte comando no Terminal:

   ```bash
   source nome_do_ambiente/bin/activate
   ```

   Você verá que agora seu prompt de comando mudou para indicar que você está no ambiente virtual.

3. **Instalar pacotes e trabalhar dentro do ambiente virtual**:
   Agora que seu ambiente virtual está ativado, você pode instalar pacotes Python usando o `pip` como de costume. Todos os pacotes instalados serão específicos para este ambiente virtual e não afetarão outros projetos.

4. **Desativar o ambiente virtual**:
   Quando terminar de trabalhar no seu projeto, você pode desativar o ambiente virtual executando o seguinte comando no Terminal:

   ```bash
   deactivate
   ```

Isso irá sair do ambiente virtual e voltar ao ambiente padrão do sistema.

Utilizar ambientes virtuais é uma prática recomendada ao desenvolver projetos em Python, pois ajuda a manter as dependências organizadas e isoladas entre diferentes projetos. O uso do `venv` é uma maneira conveniente e nativa de criar ambientes virtuais no macOS sem a necessidade de instalar ferramentas adicionais como o `virtualenv`.


#estudar 