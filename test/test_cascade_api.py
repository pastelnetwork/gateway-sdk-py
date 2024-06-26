# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from .base_test import BaseTestCase
from pastel_gateway_sdk import CascadeApi, ApiKeysApi


class TestCascadeApi(BaseTestCase):
    """CascadeApi unit test stubs"""
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.api: CascadeApi = self.client.cascade_api
        api_key_api: ApiKeysApi = self.client.api_keys_api
        api_keys = await api_key_api.api_keys_read_apikeys()
        self.assertIsNotNone(api_keys)
        self.assertIsNot(api_keys, [])
        self.client.set_auth_api_key(api_keys[0].api_key)

    async def test_cascade_get_all_files_from_request(self) -> None:
        """Test case for cascade_get_all_files_from_request

        Get All Files From Request
        """
        pass

    async def test_cascade_get_all_pastel_registration_tickets_from_request(self) -> None:
        """Test case for cascade_get_all_pastel_registration_tickets_from_request

        Get All Pastel Cascade Registration Tickets From Request
        """
        pass

    async def test_cascade_get_all_requests(self) -> None:
        """Test case for cascade_get_all_requests

        Get All Requests
        """
        requests = await self.api.cascade_get_all_requests()
        self.assertIsNotNone(requests)
        self.assertIsNot(requests, [])
        print(requests)

    async def test_cascade_get_all_results(self) -> None:
        """Test case for cascade_get_all_results

        Get All Results
        """
        pass

    async def test_cascade_get_originally_submitted_file_from_result(self) -> None:
        """Test case for cascade_get_originally_submitted_file_from_result

        Get Originally Submitted File By Result Id
        """
        pass

    async def test_cascade_get_pastel_activation_ticket_from_result(self) -> None:
        """Test case for cascade_get_pastel_activation_ticket_from_result

        Get Pastel Cascade Activation Ticket By Result Id
        """
        pass

    async def test_cascade_get_pastel_activation_ticket_from_txid(self) -> None:
        """Test case for cascade_get_pastel_activation_ticket_from_txid

        Get Pastel Activation Ticket By Its Txid
        """
        pass

    async def test_cascade_get_pastel_registration_ticket_from_result(self) -> None:
        """Test case for cascade_get_pastel_registration_ticket_from_result

        Get Pastel Cascade Registration Ticket From Result Id
        """
        pass

    async def test_cascade_get_pastel_registration_ticket_from_txid(self) -> None:
        """Test case for cascade_get_pastel_registration_ticket_from_txid

        Get Pastel Registration Ticket By Its Txid
        """
        pass

    async def test_cascade_get_pastel_registration_ticket_from_stored_file_hash(self) -> None:
        """Test case for cascade_get_pastel_registration_ticket_from_stored_file_hash

        Get Pastel Registration Ticket By Stored File Hash
        """
        pass

    async def test_cascade_get_public_stored_file_from_registration_ticket(self) -> None:
        """Test case for cascade_get_public_stored_file_from_registration_ticket

        Get Public Stored File By Registration Ticket
        """
        pass

    async def test_cascade_get_request(self) -> None:
        """Test case for cascade_get_request

        Get Request By Request Id
        """
        pass

    async def test_cascade_get_result(self) -> None:
        """Test case for cascade_get_result

        Get Result By Result Id
        """
        pass

    async def cascade_get_stored_file_from_result(self) -> None:
        """Test case for cascade_get_stored_file_from_result

        Get Stored File By Result Id
        """
        pass

    async def test_cascade_get_stored_file_from_activation_ticket(self) -> None:
        """Test case for cascade_get_stored_file_from_activation_ticket

        Get Stored File By Activation Ticket
        """
        pass

    async def test_cascade_get_stored_file_from_registration_ticket(self) -> None:
        """Test case for cascade_get_stored_file_from_registration_ticket

        Get Stored File By Registration Ticket
        """
        pass

    async def test_cascade_process_request(self) -> None:
        """Test case for cascade_process_request

        Process Request
        """
        pass

    async def test_cascade_transfer_pastel_ticket_to_another_pastelid(self) -> None:
        """Test case for cascade_transfer_pastel_ticket_to_another_pastelid

        Transfer Pastel Ticket To Another Pastelid
        """
        pass


if __name__ == '__main__':
    unittest.main()
