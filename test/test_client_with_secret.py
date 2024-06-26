# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from pastel_gateway_sdk.models.client_with_secret import ClientWithSecret


class TestClientWithSecret(unittest.TestCase):
    """ClientWithSecret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientWithSecret:
        """Test ClientWithSecret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientWithSecret`
        """
        model = ClientWithSecret()
        if include_optional:
            return ClientWithSecret(
                client_id = '',
                client_secret = ''
            )
        else:
            return ClientWithSecret(
                client_id = '',
                client_secret = '',
        )
        """

    def testClientWithSecret(self):
        """Test ClientWithSecret"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
