# Bright Data

## Visão Geral

Bright Data é uma plataforma de web scraping e coleta de dados que oferece infraestrutura para extração de dados em larga escala de websites públicos.

## Conceitos Principais

### Collector (Scraper)

Um Collector no Bright Data é dividido em duas partes distintas, cada uma responsável por uma fase diferente do fluxo de scraping:

1. **Interaction Code** - Controla o navegador e interage com a página
2. **Parser Code** - Extrai e transforma os dados da página carregada

## Interaction Code

### O que é

Código que controla o navegador durante o scraping. Ele roda enquanto a sessão está aberta e é responsável pela interação com o site.

### Responsabilidades

#### Navegação
- `navigate()` - Navegar para URLs
- `open_tab()` - Abrir novas abas
- Controlar fluxo entre páginas

#### Interação com a Página
- `click()` - Clicar em elementos
- `type()` - Digitar em campos
- `scroll()` - Fazer scroll na página
- `load_more()` - Carregar mais conteúdo
- `wait_for_element()` - Aguardar elementos aparecerem
- Resolver captchas
- Selecionar filtros e opções

#### Controle de Fluxo
- Definir quando a página está pronta para ser lida
- Chamar `parse()` para extrair dados
- Ir para o próximo estágio com `next_stage()`

#### Tratamento de Erros
- `blocked()` - Marcar quando o site bloqueou o acesso
- `bad_input()` - Indicar entrada inválida
- `console.log()` - Registrar logs para debug

### Analogia

Pense no Interaction Code como o **"bot que mexe no site"** - ele prepara o HTML/DOM final que você quer analisar.

### Exemplo Prático

```javascript
// Navega para a página
navigate('https://example.com/products');

// Aguarda carregamento
wait_page_idle(3000);

// Clica em "Ver Mais" 5 vezes para carregar mais produtos
for (let i = 0; i < 5; i++) {
  click('.load-more-button');
  wait_page_idle(2000);
}

// Página pronta, chama o parser
parse();
```

## Parser Code

### O que é

Código que lê e transforma o conteúdo carregado pela Interaction Code. Ele não clica nem navega; trabalha em cima do HTML já carregado.

### Responsabilidades

#### Recebimento de Dados
- Recebe o DOM/HTML final
- Acessa via `$(...)` (sintaxe Cheerio)
- Usa variáveis globais como `input`

#### Seleção de Elementos
- CSS Selectors: `$('.price').text()`
- Atributos: `$('a.product').attr('href')`
- Navegação no DOM

#### Transformação de Dados
- `text_sane()` - Limpar e normalizar texto
- Converter preços para números
- Formatar datas
- Extrair informações específicas

#### Coleta de Resultados
- Montar objeto final
- Enviar para dataset com `collect({ ... })`
- Definir formato do JSON de saída

### Analogia

Pense no Parser Code como **"o que extrair e como formatar"** - ele define a estrutura final dos dados coletados.

### Exemplo Prático

```javascript
// Seleciona todos os produtos da página
const products = [];

$('.product-card').each((index, element) => {
  const product = {
    title: $(element).find('.title').text().trim(),
    price: parseFloat($(element).find('.price').text().replace('R$', '').trim()),
    url: $(element).find('a').attr('href'),
    image: $(element).find('img').attr('src')
  };
  
  products.push(product);
});

// Envia os dados coletados
collect({
  products: products,
  total_found: products.length
});
```

## Resumo da Diferença

| Aspecto | Interaction Code | Parser Code |
|---------|-----------------|-------------|
| **Função** | Como chegar e interagir com a página | O que extrair e como formatar |
| **Ações** | Navegação, cliques, scroll, espera | Seletores, parsing, transformação |
| **Quando roda** | Durante a sessão do navegador | Após a página estar carregada |
| **Objetivo** | Preparar a página para extração | Extrair e estruturar os dados |
| **Ferramentas** | navigate, click, scroll, wait | $(), text(), attr(), collect() |

## Fluxo Típico

```
1. Interaction Code abre a página
   ↓
2. Interaction Code clica em "ver mais" várias vezes
   ↓
3. Interaction Code chama parse()
   ↓
4. Parser Code percorre $('.product-card').each(...)
   ↓
5. Parser Code extrai campos de cada produto
   ↓
6. Parser Code envia dados com collect()
```

## Exemplo Completo: Meta Ads Scraper

### Interaction Code
```javascript
// Calcula data final
function addOneDay(dateString) {
  const date = new Date(dateString);
  date.setDate(date.getDate() + 1);
  return date.toISOString().split('T')[0];
}

const final_date = addOneDay(input.start_date);

// Constrói URL com parâmetros
const base_url = "https://www.facebook.com/ads/library/";
const params = {
  'active_status': 'all',
  'ad_type': 'all',
  'country': 'BR',
  'q': input.keyword,
  'start_date[min]': input.start_date,
  'start_date[max]': final_date
};

// Navega para a página
navigate(base_url + '?' + buildQueryString(params));

// Aguarda carregamento
wait_page_idle(8000);

// Faz scroll para carregar mais anúncios
for (let i = 1; i <= input.scroll_number; i++) {
  console.log('Scroll ' + i + ' de ' + input.scroll_number);
  scroll_to('bottom');
  wait_page_idle(4000);
}

// Página pronta, chama parser
parse();
```

### Parser Code
```javascript
// Extrai Library IDs dos anúncios
const library_ids = [];

$('[data-library-id]').each((index, element) => {
  const library_id = $(element).attr('data-library-id');
  if (library_id && !library_ids.includes(library_id)) {
    library_ids.push(library_id);
  }
});

// Constrói URLs individuais
const urls = library_ids.map(id => ({
  url: 'https://www.facebook.com/ads/library/?id=' + id,
  keyword: input.keyword,
  date_filter: input.start_date
}));

// Coleta os resultados
collect({
  urls_ads: urls
});
```

## Boas Práticas

### Interaction Code
- Use waits adequados para garantir carregamento completo
- Implemente logs para debug (`console.log()`)
- Trate erros com `blocked()` e `bad_input()`
- Evite scrolls/cliques desnecessários

### Parser Code
- Use seletores CSS específicos e robustos
- Normalize e limpe dados com `text_sane()`
- Valide dados antes de coletar
- Estruture o JSON de saída de forma clara

## Casos de Uso na Hotmart

### Meta Ads - Facebook Library (2 Steps)

Processo completo de coleta de anúncios do Facebook em duas etapas.

#### Step 1 - Descoberta de Anúncios
- **Interaction:** Navega para Facebook Ads Library, aplica filtros, faz 50 scrolls
- **Parser:** Extrai Library IDs únicos e constrói URLs individuais
- **Output:** Lista de URLs de anúncios

#### Step 2 - Coleta Detalhada
- **Interaction:** Navega para página individual, clica em "Ver detalhes", clica em "Sobre o anunciante"
- **Parser:** Extrai dados completos (anunciante, Instagram, descrição, URL, seguidores, etc.)
- **Output:** Dados estruturados de cada anúncio

#### Fluxo Completo
```
Step 1: Busca por palavra-chave → Lista de URLs
  ↓
Webhook → Astroflow processa URLs
  ↓
Step 2: Para cada URL → Dados detalhados
  ↓
Webhook → Base Histórica
```

### [Outros Scrapers]
- [Adicionar conforme implementados]

## Referências

- [[Meta Ads - Facebook Library]]
- [[Lead Generation (Jetski)]]
- Documentação oficial: [Bright Data Docs](https://docs.brightdata.com/)
