
## [[Github Actions]]

Criar o arquivo feature.yml na pasta .github/workflow/feature.yml

Ex : 

```yaml

name: feature

on:
  push:
    branches:
      - feature/*

concurrency: pipeline-feature

jobs:
  base-module:
    uses: Hotmart-Org/actions/.github/workflows/base.yaml@master
    secrets: inherit
    with:
      runs-on: "buildstaging-iac"
      file: "feature.yml"
      environment: "staging"
      cluster: "buildstaging"
      namespace: "hotintegration"

  pipeline-feature:
    runs-on: [ self-hosted, buildstaging-iac ]
    needs: base-module
    env:
      AWS_DEFAULT_REGION: us-east-1
      VAULT_ROLE: "ga"
    steps:
      - name: Clone code
        uses: actions/checkout@v3

      - name: Retrieve cache
        uses: Hotmart-Org/actions/cache@master
        with:
          bucket: buildstaging-pipeline-cache
          cache-key: "${{ hashFiles('pom.xml') }}"
          restore: true
          mount: .m2
        env:
          GH_TOKEN: ${{ secrets.CI_GH_TOKEN }}

      - name: Build application
        uses: Hotmart-Org/actions/maven@master
        with:
          gh-token: ${{ secrets.CI_GH_TOKEN }}
          java-version: "17"
          command: clean package -DskipTests

      - name: Save cache
        uses: Hotmart-Org/actions/cache@master
        with:
          bucket: buildstaging-pipeline-cache
          cache-key: "${{ hashFiles('pom.xml') }}"
          rebuild: true
          mount: .m2
        env:
          GH_TOKEN: ${{ secrets.CI_GH_TOKEN }}

      - name: Build image
        uses: Hotmart-Org/actions/docker@master
        with:
          file: "feature.yml"

      - name: Deploy
        uses: Hotmart-Org/actions/helm@master
        with:
          file: "feature.yml"
          environment: "staging"
          cluster: "buildstaging"
          namespace: "hotintegration"



```

Criar outro arquivo feature.yml no mesmo nivel do staging.yaml e production.yml 

Adicionar as seguintes proriedades : 

```
# Feature branch deploy
branchRelease: true
branchReleaseCollapseTime: 1 # days
```

Com isso ao criar uma branch com o padrão `feature\FC-*`  sera criada uma infra aparte de staging através dessa feature-branch