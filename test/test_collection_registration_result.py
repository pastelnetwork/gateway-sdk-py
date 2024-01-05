# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from pastel_gateway_sdk.models.collection_registration_result import CollectionRegistrationResult

class TestCollectionRegistrationResult(unittest.TestCase):
    """CollectionRegistrationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionRegistrationResult:
        """Test CollectionRegistrationResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionRegistrationResult`
        """
        model = CollectionRegistrationResult()
        if include_optional:
            return CollectionRegistrationResult(
                result_status = 'PENDING',
                file_name = '',
                file_type = '',
                file_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_messages = [
                    null
                    ],
                retry_num = 56,
                registration_ticket_txid = '',
                activation_ticket_txid = '',
                original_file_ipfs_link = '',
                stored_file_ipfs_link = '',
                stored_file_aws_link = '',
                stored_file_other_links = None,
                make_publicly_accessible = True,
                offer_ticket_txid = '',
                offer_ticket_intended_rcpt_pastel_id = '',
                error = '',
                collection_id = ''
            )
        else:
            return CollectionRegistrationResult(
                result_status = 'PENDING',
        )
        """

    def testCollectionRegistrationResult(self):
        """Test CollectionRegistrationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()