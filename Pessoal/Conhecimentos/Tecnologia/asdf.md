O asdf é um ótimo gerenciador de versões seja de libs, sdks, jdks e por ai vai

### Instalação

Para baixar e instalar o asdf no Mac:

Execute o seguinte comando no terminal para baixar e instalar o asdf:
   ```
   git clone https://github.com/asdf-vm/asdf.git ~/.asdf
   ```
Adicionar o asdf ao seu arquivo de configuração:

 Abra o arquivo de configuração do seu shell (por exemplo, ~/.bashrc, ~/.zshrc) usando um editor de texto como o nano:
   ```
   nano ~/.bashrc
   ```
Adicione a seguinte linha ao final do arquivo:
   ```
   . $HOME/.asdf/asdf.sh
   . $HOME/.asdf/completions/asdf.bash
   ```

## Java

Instalar o plugin do Java no asdf:

Execute o seguinte comando para instalar o plugin do Java:
```
asdf plugin add java
```
Instalar uma versão do Java usando o asdf:

Execute o seguinte comando para listar todas as versões disponíveis do Java para instalação:
```
asdf list all java
```
 Escolha a versão desejada e execute o seguinte comando para instalá-la (substitua "versao_java" pela versão escolhida):

```
asdf install java versao_java
```
Definir a versão do Java a ser usada globalmente:

Execute o seguinte comando para definir a versão instalada como a versão global do Java:
```
asdf global java versao_instalada
```


Alacrity