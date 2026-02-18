
o que é o Helm e para que serve ?



O Helm é um gerenciador de pacotes para o Kubernetes, que facilita a instalação, atualização e gerenciamento de aplicativos dentro de um cluster Kubernetes. Ele permite a definição e configuração dos recursos necessários para implantar um aplicativo de forma consistente e reutilizável. Com o Helm, é possível empacotar um conjunto de recursos do Kubernetes em um único pacote chamado "chart", que pode ser compartilhado e reutilizado por outros usuários. Ele simplifica o processo de implantação e gerenciamento de aplicativos no Kubernetes, tornando-o uma ferramenta essencial para os desenvolvedores que trabalham com essa plataforma.


```bash
hotctl eks context --profile integration  
  
helm history api-notification-center-engine -n hotintegration  

helm rollback api-notification-center-engine 63 -n hotintegration
```
