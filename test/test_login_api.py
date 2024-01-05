# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pastel_gateway_sdk import GatewayApiClientAsync


class TestLoginApi(unittest.IsolatedAsyncioTestCase):
    """LoginApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.client = GatewayApiClientAsync(network="testnet")
        self.username = "test@example.com"
        self.password = "string"

    async def asyncTearDown(self) -> None:
        pass

    async def test_login_access_token(self) -> None:
        """Test case for login_access_token

        Login Access Token
        """
        # Authenticate the client
        await self.client.authenticate(self.username, self.password)
        # Assert that token is successfully set
        self.assertIsNotNone(self.client._token)
        return

    async def test_login_password_recovery(self) -> None:
        """Test case for login_password_recovery

        Recover Password
        """
        pass

    async def test_login_reset_password(self) -> None:
        """Test case for login_reset_password

        Reset Password
        """
        pass

    async def test_login_test_token(self) -> None:
        """Test case for login_test_token

        Test Token
        """
        await self.test_login_access_token()
        login_api = self.client.login_api
        user = await login_api.login_test_token()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, self.username)


if __name__ == '__main__':
    unittest.main()
