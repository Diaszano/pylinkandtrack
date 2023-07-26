<header>
    <div align="center">
        <a href="https://github.com/Diaszano">
            <img src=".github/assets/diaszano.png" alt="logo" height="300">
        </a>
        <h1>
            PyLinkAndTrack
        </h1>
        Interface amigável da <a href="https://linketrack.com/">Link & Track</a>: simplifica rastreamento de encomendas nos Correios através de sua poderosa API.
    </div>
</header>

## Como instalar o projeto?

Para a instalação do projeto recomendamos que use o `pipx` para fazer essa instalação:

```bash
pipx install pylinkandtrack
```

# Como usar?

Tu podes importar o pacote em qualquer projeto e fazer a instanciação da classe. Por exemplo:

```python
from asyncio import run

from linkandtrack import LinkAndTrack


async def main() -> None:
    # Crie o seu user e token no site do Link&Track
    # Link: https://linketrack.com/
    linkandtrack = LinkAndTrack(
        user='teste',
        token='1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f',
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