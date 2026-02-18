
o que é e para que serve o AWS Guard Duty ? 



Amazon GuardDuty é um serviço de segurança da Amazon Web Services (AWS) que ajuda a proteger sua infraestrutura na nuvem detectando atividades suspeitas e potenciais ameaças de segurança. 

Ele monitora continuamente sua conta da AWS em busca de comportamentos maliciosos, como tentativas de invasão, comunicações não autorizadas ou atividades de mineração de criptomoedas.

Este serviço utiliza análise de machine learning e inteligência artificial para identificar padrões incomuns ou suspeitos em logs e dados de tráfego da rede. Ele fornece alertas em tempo real sobre possíveis ameaças, permitindo que você tome medidas imediatas para mitigar o risco.

Em resumo, o Amazon GuardDuty ajuda a proteger sua infraestrutura na nuvem, mantendo-a segura contra ameaças cibernéticas em constante evolução. É uma ferramenta essencial para empresas que desejam garantir a segurança de seus dados e sistemas na nuvem da AWS.

que tipos de ataque o guardDuty consegue previnir e detectar ?



Title: Amazon GuardDuty

Starred Blocks: 
	  

o que é e para que serve o AWS Guard Duty ? 



Amazon GuardDuty é um serviço de segurança da AWS que monitora continuamente suas contas e workloads em busca de atividade maliciosa. Ele usa machine learning, anomalia detection e threat intelligence para identificar ameaças e fornecer alertas acionáveis.  Em essência, ele atua como um sistema de detecção de intrusão (IDS) para sua infraestrutura na AWS, ajudando a proteger seus dados e recursos.


que tipos de ataque o guardDuty consegue previnir e detectar ?



O GuardDuty se concentra principalmente na **detecção**, não na prevenção direta de ataques.  Ele alerta sobre atividades suspeitas, permitindo que você tome medidas para remediar a situação.  Embora não impeça ativamente um ataque inicial, a detecção rápida permite mitigar o impacto e prevenir danos maiores.

Os tipos de ameaças que o GuardDuty detecta incluem:

* **Acesso não autorizado a recursos da AWS:**  Identifica tentativas de login suspeitas, credenciais comprometidas, escalonamento de privilégios e acesso a recursos de locais incomuns. Exemplos: tentativas de login com MFA desabilitado, acesso de IPs conhecidos por atividades maliciosas.

* **Malware:** Detecta instâncias EC2 que estão se comunicando com domínios ou IPs associados a malware, botnets ou command-and-control servers.  Isso ajuda a identificar instâncias comprometidas que podem estar sendo usadas para atividades maliciosas, como mineração de criptomoedas ou distribuição de malware.

* **Reconhecimento:** Identifica atividades de reconhecimento, como varreduras de portas, enumeração de recursos e tentativas de identificar vulnerabilidades em seus sistemas.  Essas atividades geralmente precedem ataques mais direcionados.

* **Exfiltração de dados:** Detecta tentativas de copiar dados confidenciais para fora do seu ambiente AWS, como transferências incomuns de dados para locais externos ou acesso não autorizado a buckets S3.

* **Comportamento suspeito de contas:** Detecta anomalias no comportamento das contas da AWS, como alterações inesperadas nas configurações de segurança, criação de usuários suspeitos ou atividades incomuns de API.

* **Uso indevido de recursos:** Identifica o uso de recursos da AWS para atividades malicios