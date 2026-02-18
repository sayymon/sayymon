
No Mac e no Linux para instalar o SDKman basta rodar o seguinte comando no terminal : 

```bash

curl -s "https://get.sdkman.io" | bash
```

Depois rodar :

```bash
source "/Users/saymon.silva/.sdkman/bin/sdkman-init.sh"
```

E verificar se deu bom com :

```bash
sdk version
```


## Java

Para instalar a ultima versão do java por exemplo basta fazer o seguinte : 

```bash
sdk install java
```

Para listar as versões disponíveis : 

```bash
sdk list java
```

Se quiser usar alguma das versões já instaladas basta rodar o comando use

```bash
sdk use java 21.0.4-tem
```

Verificar qual é a versão corrente

```
sdk current java
```

Mais informações no site deles [SDKMAN doc usage](https://sdkman.io/usage)