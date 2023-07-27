<header>
    <div align="center">
        <a href="https://github.com/Diaszano">
            <img src="https://pylinkandtrack.readthedocs.io/en/latest/assets/logo02.png" alt="logo" height="300">
        </a>
        <h1>
            PyLinkAndTrack
        </h1>
        Interface amigável da <a href="https://linketrack.com/">Link & Track</a>: simplifica rastreamento de encomendas 
        nos Correios através de sua poderosa API.
    </div>
</header>

[![Documentation Status](https://readthedocs.org/projects/pylinkandtrack/badge/?version=latest)](https://pylinkandtrack.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/Diaszano/pylinkandtrack/actions/workflows/check.yaml/badge.svg)](https://github.com/Diaszano/pylinkandtrack/actions/workflows/check.yaml)
[![codecov](https://codecov.io/gh/Diaszano/pylinkandtrack/branch/master/graph/badge.svg?token=VfeUJcEGI7)](https://codecov.io/gh/Diaszano/pylinkandtrack)
[![PyPI version](https://badge.fury.io/py/pylinkandtrack.svg)](https://badge.fury.io/py/pylinkandtrack)


## Como instalar o projeto?

Para a instalação do projeto recomendamos que use o `pipx` para fazer essa instalação:

```bash
pipx install pylinkandtrack
```

Embora isso seja somente uma recomenda uma recomendação! Tu também podes instalar o projeto com o gerenciador de sua 
preferência. Como `pip`:

```bash
pip install pylinkandtrack
```

## Como usar?

Este projeto se baseia nas funcionalidades oferecidas pela API do [Link&Track](https://linketrack.com/), que 
possibilita o rastreamento de encomendas, sujeito a limites de consultas por minuto.

Em nossa implementação, todas as requisições à API do [Link&Track](https://linketrack.com/) são realizadas de forma 
assíncrona, proporcionando um desempenho otimizado em sua aplicação. Abaixo, apresentaremos como é possível realizar o 
rastreamento de uma encomenda por meio da nossa interface:

Exemplo de Rastreamento de Encomenda:

```python
from asyncio import run

from linkandtrack import LinkAndTrack


async def main() -> None:
    # Crie o seu user e token no site do Link&Track
    # Link: https://linketrack.com/
    linkandtrack = LinkAndTrack(
        user='teste',
        token='1abcd00b2731640e886fb41a8a9671ad14'
            + '34c599dbaa0a0de9a5aa619f29a83f',
    )
    result = await linkandtrack.tracker(tracking_code='LX632045407CN')
    print(result)


run(main())
```

E o resultado do print será como este abaixo: 

```python
result = {
    'codigo': 'LX632045407CN',
    'host': 'lt',
    'eventos': [],
    'time': 1.599,
    'quantidade': 0,
    'servico': 'REMESSA INTERNACIONAL',
}
```

Desta forma, ao utilizar nossa interface, você poderá obter informações sobre o rastreamento de encomendas de maneira 
eficiente e otimizada. Lembre-se de respeitar os limites de consultas por minuto estabelecidos pela API do 
[Link&Track](https://linketrack.com/) para garantir o bom funcionamento do serviço.