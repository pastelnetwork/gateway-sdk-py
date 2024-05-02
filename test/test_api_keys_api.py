# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from pastel_gateway_sdk.api.api_keys_api import ApiKeysApi
from .base_test import BaseTestCase


class TestApiKeysApi(BaseTestCase):
    """ApiKeysApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.api: ApiKeysApi = self.client.api_keys_api

    async def test_api_keys_create_apikey(self) -> None:
        """Test case for api_keys_create_apikey

        Create Apikey
        """
        pass

    async def test_api_keys_delete_apikey(self) -> None:
        """Test case for api_keys_delete_apikey

        Delete Apikey
        """
        pass

    def test_api_keys_read_apikey(self) -> None:
        """Test case for api_keys_read_apikey

        Read Apikey
        """
        pass

    async def test_api_keys_read_apikeys(self) -> None:
        """Test case for api_keys_read_apikeys

        Read Apikeys
        """
        api_keys = await self.api.api_keys_read_apikeys()
        self.assertIsNotNone(api_keys)
        self.assertIsNot(api_keys, [])
        print(api_keys)


if __name__ == '__main__':
    unittest.main()
