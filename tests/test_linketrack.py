from os import getenv

from dotenv import load_dotenv
from pytest import mark, raises

from linkandtrack import ClientError, LinkAndTrack

load_dotenv()


@mark.asyncio
async def test_invalid_token():
    """
    Testa a funcionalidade de validação de token inválido para a classe
    LinkAndTrack.

    Contexto:
        A função de teste verifica se a criação de uma instância da classe
        LinkAndTrack com um token inválido gera a exceção ClientError.

    Comportamento esperado:
        Espera-se que, ao tentar criar uma instância de LinkAndTrack com um token
        inválido, seja lançada uma exceção ClientError, indicando que o token
        fornecido é inválido.
    """
    with raises(ClientError):
        LinkAndTrack(user='user', token='token')


@mark.asyncio
async def test_unauthorized_user():
    """
    Testa a funcionalidade de rastreamento (tracker) para um usuário não
    autorizado na classe LinkAndTrack.

    Contexto:
        A função de teste verifica se o rastreamento (tracker) de uma encomenda
        com um usuário não autorizado na classe LinkAndTrack gera a exceção
        ClientError.

    Comportamento esperado:
        Espera-se que, ao tentar realizar o rastreamento (tracker) de uma
        encomenda com um usuário não autorizado, seja lançada uma exceção
        ClientError, indicando que o usuário não possui autorização para
        realizar o rastreamento.
    """
    linketrack = LinkAndTrack(
        user='user',
        token='1abcd00b2731640e886fb41a8a9671ad1434'
        + 'c599dbaa0a0de9a5aa619f29a83f',
    )
    with raises(ClientError):
        await linketrack.tracker(tracking_code='LX632045407CN')


@mark.asyncio
async def test_invalid_tracking_code():
    """
    Testa a funcionalidade de rastreamento (tracker) com um código de
    rastreamento inválido na classe LinkAndTrack.

    Contexto:
        A função de teste obtém o usuário e o token da classe LinkAndTrack a
        partir das variáveis de ambiente, ou utiliza valores padrão caso essas
        variáveis não estejam definidas. Em seguida, cria uma instância da
        classe LinkAndTrack com esses valores.

    Comportamento esperado:
        Espera-se que, ao tentar realizar o rastreamento (tracker) com um
        código de rastreamento inválido, seja lançada uma exceção ClientError,
        indicando que o código de rastreamento é inválido ou não existe.
    """
    user = getenv(key='USER_LINKETRACK', default='teste')
    token = getenv(
        key='TOKEN_LINKETRACK',
        default='1abcd00b2731640e886fb41a8a9671ad1434'
        + 'c599dbaa0a0de9a5aa619f29a83f',
    )

    linketrack = LinkAndTrack(user=user, token=token)

    with raises(ClientError):
        await linketrack.tracker(tracking_code='aa')


@mark.asyncio
async def test_tracking_and_returning_successfully():
    """
    Testa a funcionalidade de rastreamento (tracker) com um código de
    rastreamento válido na classe LinkAndTrack.

    Contexto:
        A função de teste obtém o usuário e o token da classe LinkAndTrack a
        partir das variáveis de ambiente, ou utiliza valores padrão caso essas
        variáveis não estejam definidas. Em seguida, cria uma instância da
        classe LinkAndTrack com esses valores.

    Comportamento esperado:
        Espera-se que, ao tentar realizar o rastreamento (tracker) com um
        código de rastreamento válido 'LX632045407CN', a função retorne um
        dicionário (dict) contendo informações sobre o rastreamento da
        encomenda.

    Verificação:
        O teste utiliza a asserção 'assert type(result) is dict' para verificar
        se o resultado é do tipo dicionário (dict), o que indica que o
        rastreamento foi realizado com sucesso e o resultado contém as
        informações esperadas.
    """
    user = getenv(key='USER_LINKETRACK', default='teste')
    token = getenv(
        key='TOKEN_LINKETRACK',
        default='1abcd00b2731640e886fb41a8a9671ad1434'
        + 'c599dbaa0a0de9a5aa619f29a83f',
    )

    linketrack = LinkAndTrack(user=user, token=token)
    result = await linketrack.tracker(tracking_code='LX632045407CN')

    assert type(result) is dict
