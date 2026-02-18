
SAML 2.0 (Security Assertion Markup Language 2.0) é um padrão de autenticação baseado em XML que permite a troca de informações de autenticação entre sistemas diferentes de forma segura. 

Ele é comumente utilizado em cenários de autenticação federada, onde uma organização confia em outra para autenticar seus usuários. 

Com o SAML 2.0, é possível estabelecer um processo de login único (SSO) entre diferentes sistemas e aplicações, garantindo uma experiência de usuário mais simplificada e segura.

Exemplo de XML : 

```xml
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_d71a3f6e-4d2e-4c2a-b5a1-1f2514b7f336" IssueInstant="2022-01-01T12:00:00Z" Version="2.0">
   <Issuer>https://www.example.com</Issuer>
   <Subject>
      <NameID>user123@example.com</NameID>
   </Subject>
   <Conditions NotBefore="2022-01-01T12:00:00Z" NotOnOrAfter="2022-01-01T13:00:00Z"/>
</Assertion>
```

