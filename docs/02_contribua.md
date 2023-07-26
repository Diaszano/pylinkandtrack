# Como contribuir

Obrigado por se interessar por contribuir no projeto `{{ vars.name }}` :bear::heart:. Nesse documento estão listadas as 
operações mais comuns e que você pode precisar para contribuir.

## Como o projeto funciona?

### Estrutura do projeto

```mermaid
flowchart
    {{ vars.project }} --> docs
	{{ vars.project }} --> {{ vars.module }}
	{{ vars.project }} --> tests
```

O projeto é dividido em três diretórios. `docs`, `{{ vars.module }}` e `tests`. Onde cada diretório tem sua função 
especifica.

#### linkandtrack

```mermaid
flowchart
	{{ vars.project }} --> {{ vars.module }}
	{{ vars.module }} --> linkandtrack.py
	{{ vars.module }} --> client_exceptions
	client_exceptions --> client_error.py
```

O código da biblioteca estão em `{{ vars.module }}`. A documentação da API do código também está sendo feita em 
`{{ vars.module }}`. Com uso da ferramenta [mkdocstrings](https://mkdocstrings.github.io/) e seguem o padrão de 
[docstrings do google](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). Então, caso altere 
alguma coisa no código, lembre-se de atualizar também as docstrings.

#### Sobre a biblioteca

Toda a biblioteca usa python puro, ela tem uma dependência de biblioteca externa a `aiohttp`. O código é bastante 
simples. As resposta das funções foram padronizadas com o retorno sempre sendo tipadas, pois em algum momento alguém 
pode querer expandir isso para uma interface gráfica ou usar em um API REST, dessa forma, acredito que um padrão pode 
ajudar bastante as pessoas.

#### tests

Para os testes estamos usando o [pytest](https://docs.pytest.org/). As configurações dele podem ser encontradas no 
arquivo [pyproject.toml](https://github.com/Diaszano/{{ vars.project }}/blob/master/pyproject.toml) na raiz do nosso projeto.

A cobertura dos testes está sendo gerada automaticamente com [pytest-cov](https://github.com/pytest-dev/pytest-cov) e 
sendo exibidas quando a task de testes é executada:

```bash
task tests
```

Assim como os linters são requisitos para esses testes.

#### Documentação

A documentação toda é baseada no uso de [mkdocs](https://www.mkdocs.org/) com o tema 
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

```mermaid
flowchart
    {{ vars.project }} --> docs
    {{ vars.project }} --> mkdocs.yml
	docs --> arquivos.md
	docs --> api
	docs --> assets
	docs --> templates
	docs --> stylesheets
```

Toda a configuração pode ser encontrada no arquivo 
[mkdocs.yml](https://github.com/Diaszano/{{ vars.project }}/blob/master/mkdocs.yml) na raiz do repositório.

Também estão sendo usados diversos artifícios para complementar a documentação. Como templates do 
[jinja](https://jinja.palletsprojects.com/en/3.1.x/) nos lugares onde instruções podem se repetir. Caso encontre 
blocos como:

```html
{ %  % }
```

Saberá que se trata de um template.

Os templates estão definidos no diretório `/docs/templates`. Em alguns casos, porém, podem estar sendo chamados por 
variáveis com `vars.linketrack` que aparece em quase todos os arquivos de documentação. Essas macros estão sendo feitas 
com [mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) e estão definidas no arquivo de configuração 
do mkdocs:

```yaml
extra:
  vars:
    linketrack: "[Link&Track](https://linketrack.com/)"
```

##### Documentação da API

A documentação da API está sendo feita dentro dos módulos do código. Por isso os arquivos que estão no diretório 
`docs/api` tem uma tag:

```md
::: modulo
```

Isso quer dizer que será usado o código contido nas docstrings nesse bloco. O plugin 
[mkdocstrings](https://mkdocstrings.github.io/) está sendo usado para tomar conta disso.

As documentações nos módulos seguem o formato de 
[docstrings do google](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html), o padrão da 
biblioteca

## Ferramentas

Esse projeto basicamente usa duas ferramentas como base para todo com controle:

- [Poetry](https://python-poetry.org/): Para o gerenciamento do ambiente e instalação de bibliotecas
- [Taskipy](https://github.com/illBeRoy/taskipy): Para automação de tarefas rotineiras. Como executar os testes, 
   linters, documentação e etc...

Então, garanta que tem o poetry instalado para essa contribuição:

```bash
pipx install poetry
```

## Passos para executar tarefas específicas

Aqui estão listados comandos que você pode usar para executar tarefas corriqueiras. Como clonar o repositório, como 
instalar as dependências, executar os testes e etc...

### Como clonar o repositório

```bash
git clone git@github.com:Diaszano/{{ vars.project }}.git
```

### Como instalar as dependências

```bash
poetry install
```

### Como executar a verificação de código

Para ver se o código está no padrão:

```bash
task lint
```

Para colocar o código no padrão:

```bash
task lint-fix
```

### Como executar os testes

```bash
task test
```

### Como executar a documentação

```bash
task docs
```

{% include "templates/todos.md" %}