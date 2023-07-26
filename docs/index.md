![Logo do Diaszano](assets/logo01.png){width="300" .center}
# PyLinkAndTrack

Interface amigável da [Link & Track](https://linketrack.com/): simplificando rastreamento de encomendas nos Correios através de sua poderosa API.

{% include "templates/cards.html" %}

{% include "templates/instalacao.md" %}

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