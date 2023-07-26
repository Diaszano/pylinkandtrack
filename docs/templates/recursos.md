# Como usar?

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