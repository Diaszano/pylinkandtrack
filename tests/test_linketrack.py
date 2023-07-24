from os import getenv

from dotenv import load_dotenv
from pytest import mark, raises

from linketrack import ClientError, LinkETrack

load_dotenv()


@mark.asyncio
async def test_codigo_de_rastreio_invalido():
    user = getenv(key='USER', default='teste')
    token = getenv(
        key='TOKEN',
        default='1abcd00b2731640e886fb41a8a9671ad1434'
        + 'c599dbaa0a0de9a5aa619f29a83f',
    )

    linketrack = LinkETrack(user=user, token=token)

    with raises(ClientError):
        await linketrack.tracker(tracking_code='aa')


@mark.asyncio
async def test_codigo_de_rastreio_valido():
    user = getenv(key='USER', default='teste')
    token = getenv(
        key='TOKEN',
        default='1abcd00b2731640e886fb41a8a9671ad1434'
        + 'c599dbaa0a0de9a5aa619f29a83f',
    )

    linketrack = LinkETrack(user=user, token=token)
    result = await linketrack.tracker(tracking_code='LX632045407CN')

    assert type(result) is dict


@mark.asyncio
async def test_token_invalido():
    with raises(ClientError):
        LinkETrack(user='user', token='token')
