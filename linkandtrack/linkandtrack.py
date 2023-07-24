from json import loads
from urllib.parse import urlencode

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError as ClientErrorAiohttp
from regex import MULTILINE, search

from .client_execptions import ClientError


class LinkAndTrack:
    __authorized: bool = True
    __regex_tracking_code: str = r'^\D{2}\d{9}\D{2}$'
    __regex_token: str = r'^[\d\D]{64}$'
    __token: str
    __url: str = 'https://api.linketrack.com/track/json?'
    __user: str

    def __init__(self, user: str, token: str):
        """
        :param user: Nome de usuário do Link&Track.
        :param token: Token único do Link&Track.
        """
        self.__user = user
        self.__token = token
        self.__check_token()

    async def tracker(self, tracking_code: str) -> dict:
        """
        Rastreador de encomenda.

        :param tracking_code: Código de Rastreio.
        :return: Dados do rastreio.
        """
        if not self.__authorized:
            raise ClientError(mensagem='Usuário não autorizado!')
        await self.__check_tracking_code(tracking_code=tracking_code)
        url = await self.__create_url(tracking_code=tracking_code)
        return await self.__request(url=url)

    async def __create_url(self, tracking_code: str) -> str:
        """
        Cria a URL

        :param tracking_code: Código de Rastreio.
        :return: Retorna a URL que deve ser requisitada para fazer o rastreio.
        """
        params: dict[str, str] = {
            'user': self.__user,
            'token': self.__token,
            'codigo': tracking_code,
        }
        return f'{self.__url}{urlencode(params)}'

    async def __request(self, url: str) -> dict:
        """
        Requisição para a API do Link&Track.

        :param url: URL que deve ser requisitada para fazer o rastreio.
        :return: Retorna os dados do rastreio.
        """
        try:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 429:
                        raise ClientError(
                            mensagem='Desculpe, mas parece que você excedeu '
                            + 'o número máximo de solicitações por minuto no '
                            + 'Link&Track!'
                        )
                    data_text = await response.text()
                    if data_text == 'Unauthorized':
                        self.__authorized = False
                        raise ClientError(mensagem='Usuário não autorizado!')
            return loads(data_text)
        except ClientErrorAiohttp:
            return dict()

    async def __check_tracking_code(self, tracking_code: str) -> None:
        """
        Checa o código de rastreio.

        :param tracking_code: Código de Rastreio.
        :return: Retorna True se o código é válido e False se inválido.
        """
        result = search(
            pattern=self.__regex_tracking_code,
            string=tracking_code,
            flags=MULTILINE,
        )
        if result is None:
            raise ClientError(mensagem='Código de rastreio inválido!')

    def __check_token(self) -> None:
        """
        Verifica o Token do Usuário
        """
        result = search(
            pattern=self.__regex_token,
            string=self.__token,
            flags=MULTILINE,
        )
        if result is None:
            raise ClientError(mensagem='Token inválido!')
