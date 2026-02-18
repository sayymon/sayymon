

https://docs.google.com/presentation/d/1tc_JNMIjEuPZejZx2AHH1PZnaglrJTp5kQfXMU0uer4/edit#slide=id.p10


[[Push]]

- [push-notification-lib](https://github.com/Hotmart-Org/push-notification-lib)
	- Para que serve : 
		- Encapsula lib do event agent e padroniza envio de eventos para o lambda-push-notification-handler
	- Características Técnicas:
		- Java 8, libs desatualizadas do Event Agent, Pipe Drone 
	- **Quem usa** : 
		- https://github.com/Hotmart-Org/lambda-notification-center-engine-push
		- https://github.com/Hotmart-Org/lambda-notification-center-engine-history
		- https://github.com/Hotmart-Org/sparkle-event-handlers
		- https://github.com/Hotmart-Org/notification-segment-importer
		- https://github.com/Hotmart-Org/lambda-push-onesignal
		- https://github.com/Hotmart-Org/api-sparkle
		- https://github.com/Hotmart-Org/notification-events-job
		- https://github.com/Hotmart-Org/api-cash-advance
		- https://github.com/Hotmart-Org/lambda-push-notification-handler
	- Prós:
		- Padroniza e centraliza o disparo de eventos
	- Contras:
		- Dificulta a manutenção devido enums e VO's compartilhados 
	- O que fazer ?
		-  Descontinuar ? Sim 
		-  Atualizar ? Não pois a ideia é futuramente encapsular o Notification na Lib do Broker
    
- [lambda-push-notification-handler](https://github.com/Hotmart-Org/lambda-push-notification-handler)
	- Para que serve : 
		- Centraliza os eventos de Join,Leave e send Notification e envia para os lambdas responsáveis pelo Providers (lambda-push-onesignal e lambda-feed-stream)
	- Características Técnicas:
		-  Java 11 Lambda AWS, Pipe no Drone, 
	- **Quem Aciona** : 
		- [push-notification-lib](https://github.com/Hotmart-Org/push-notification-lib)
		- Confirmar com o Paulo/Renato se tem mais gente chamando por fora sem ser via Lib
	- Prós:
		- Centraliza o disparo de eventos e orquestra chamadas para os lambdas dos Providers de PUSH(Onesignal) e FEED(GetStream), cadencia as chamadas para os lambdas e possui controle de Fallback em uma DLQ e caso de alta demanda
	- Contras:
		- Atualmente é um ponto de gargalo, concorrencia esta em 35 e esta fazendo em equivalencia com o propósito do Motor de Notificações que é de centralizar e orquestrar entre os canais de comunicação

- [lambda-push-onesignal](https://github.com/Hotmart-Org/lambda-push-onesignal)
	-  Para que serve : 
		- Ponto de Integração com o Onesignal, tem varias responsabilidades, BIND,UNBIND,JOIN,LEAVE Segments,USER TAGS, FORCE UNBIND, armazena e controla os users na base de controle DynamoDB
	- Características Técnicas:
		-  Java 11 Lambda AWS, Micronaut usa Pipe no Drone, 
	- **Quem Aciona** : 
		- [lambda-push-notification-handler](https://github.com/Hotmart-Org/lambda-push-notification-handler)
	- Prós:
		- Ponto unico de Integração com o Onesignal
	- Contras:
		- Ficou muito complexo e dificil de evoluir e dar manutenção devido acoplamento a lib, muitas camadas para um lambda, atualmente esta com muitas responsabilidades e com classes bem grandes
		- 
	 - *** Avaliar custo beneficio - atualizar para Quarkus para manter o padrão
	 - 
 
- [notification-segment-importer](https://github.com/Hotmart-Org/notification-segment-importer)
	-  Para que serve : 
		- atualizar segmentação de usuários na base de notificação baseado no estado do usuário nos serviços que definem tal segmentação
	- Características Técnicas:
		- Java 11 Spring Batch
	- **Quem Aciona** : 
		- É executado sob demanda para importação em massa
	- Prós:
		- 
	- Contras:        
- [api-sparkle](https://github.com/Hotmart-Org/api-sparkle)
	-  Para que serve : 
		- BFF para o App Sparkle
		- Internamente tem varios Modulos incluindo o sparkle-notification/api-notification
			- Essa se integra com a api do Notification center history e inclusive dispara alguns eventos para o Motor do Notification center
	- Características Técnicas:
		- 
	- **Quem Aciona** : 
		- 
	- Prós:
		- 
	- Contras:     
    

[[Feed]] : 

- [lambda-feed-stream](https://github.com/Hotmart-Org/lambda-feed-stream)
    
- [feed-stream-job](https://github.com/Hotmart-Org/feed-stream-job)
    
- [api-feed-stream](https://github.com/Hotmart-Org/api-feed-stream)
    
