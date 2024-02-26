import unittest
from pastel_gateway_sdk import AccountApi
from pastel_gateway_sdk import GatewayApiClientAsync
from conftest import get_config

VALID_ENVIRONMENTS = ['mainnet', 'testnet', 'devnet']


class BaseTestCase(unittest.IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        self.config = get_config()
        super().__init__(*args, **kwargs)

    async def asyncSetUp(self) -> None:
        self.client = GatewayApiClientAsync(network=self.config['network'])
        await self.client.authenticate(username=self.config['username'],
                                       password=self.config['password'])
        self.api: AccountApi = self.client.account_api

    async def asyncTearDown(self) -> None:
        pass

