
Fazer login no console da AWS 

```bash
hotctl sso login
```
Atualizar credenciais e artefatos no profile de staging

```bash
hotctl codeartifact token --profile buildstaging
```

Setar a conta default em staging

```bash
hotctl sso accounts apply -n buildstaging=staging -n buildstaging=local -n buildstaging=default

export AWS_PROFILE=buildstaging
```

