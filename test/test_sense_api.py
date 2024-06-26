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
from pastel_gateway_sdk import SenseApi, ApiKeysApi


class TestSenseApi(BaseTestCase):
    """SenseApi unit test stubs"""
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.api: SenseApi = self.client.cascade_api
        api_key_api: ApiKeysApi = self.client.api_keys_api
        api_keys = await api_key_api.api_keys_read_apikeys()
        self.assertIsNotNone(api_keys)
        self.assertIsNot(api_keys, [])
        self.client.set_auth_api_key(api_keys[0].api_key)

    def test_sense_get_all_parsed_output_files_from_request(self) -> None:
        """Test case for sense_get_all_parsed_output_files_from_request

        Get All Parsed Output Files From Request
        """
        pass

    def test_sense_get_all_pastel_registration_tickets_from_request(self) -> None:
        """Test case for sense_get_all_pastel_registration_tickets_from_request

        Get All Pastel Sense Registration Tickets From Request
        """
        pass

    def test_sense_get_all_raw_output_files_from_request(self) -> None:
        """Test case for sense_get_all_raw_output_files_from_request

        Get All Raw Output Files From Request
        """
        pass

    def test_sense_get_all_requests(self) -> None:
        """Test case for sense_get_all_requests

        Get All Requests
        """
        pass

    def test_sense_get_all_results(self) -> None:
        """Test case for sense_get_all_results

        Get All Results
        """
        pass

    def test_sense_get_originally_submitted_file_from_result(self) -> None:
        """Test case for sense_get_originally_submitted_file_from_result

        Get Originally Submitted File By Result Id
        """
        pass

    def test_sense_get_parsed_output_file_from_activation_ticket(self) -> None:
        """Test case for sense_get_parsed_output_file_from_activation_ticket

        Parsed Output File By Activation Ticket
        """
        pass

    def test_sense_get_parsed_output_file_from_pastel_id(self) -> None:
        """Test case for sense_get_parsed_output_file_from_pastel_id

        Parsed Output File By Pastel Id
        """
        pass

    def test_sense_get_parsed_output_file_from_registration_ticket(self) -> None:
        """Test case for sense_get_parsed_output_file_from_registration_ticket

        Get Parsed Output File By Registration Ticket
        """
        pass

    def test_sense_get_parsed_output_file_from_result(self) -> None:
        """Test case for sense_get_parsed_output_file_from_result

        Get Parsed Output File By Result Id
        """
        pass

    def test_sense_get_pastel_activation_ticket_from_txid(self) -> None:
        """Test case for sense_get_pastel_activation_ticket_from_txid

        Get Pastel Activation Ticket By Its Txid
        """
        pass

    def test_sense_get_pastel_activation_ticket_from_result(self) -> None:
        """Test case for sense_get_pastel_activation_ticket_from_result

        Get Pastel Sense Activation Ticket By Result Id
        """
        pass

    def test_sense_get_pastel_registration_ticket_from_txid(self) -> None:
        """Test case for sense_get_pastel_registration_ticket_from_txid

        Get Pastel Registration Ticket By Its Txid
        """
        pass

    def test_sense_get_pastel_registration_ticket_from_result(self) -> None:
        """Test case for sense_get_pastel_registration_ticket_from_result

        Get Pastel Sense Registration Ticket From Result Id
        """
        pass

    def test_sense_get_pastel_registration_ticket_from_media_file_hash(self) -> None:
        """Test case for sense_get_pastel_registration_ticket_from_media_file_hash

        Get Pastel Ticket Data From Media File Hash
        """
        pass

    def test_sense_get_raw_output_file_from_activation_ticket(self) -> None:
        """Test case for sense_get_raw_output_file_from_activation_ticket

        Get Raw Output File By Activation Ticket
        """
        pass

    def test_sense_get_raw_output_file_from_pastel_id(self) -> None:
        """Test case for sense_get_raw_output_file_from_pastel_id

        Get Raw Output File By Pastel Id
        """
        pass

    def test_sense_get_raw_output_file_from_registration_ticket(self) -> None:
        """Test case for sense_get_raw_output_file_from_registration_ticket

        Get Raw Output File By Registration Ticket
        """
        pass

    def test_sense_get_raw_output_file_from_result(self) -> None:
        """Test case for sense_get_raw_output_file_from_result

        Get Raw Output File By Result Id
        """
        pass

    def test_sense_get_request(self) -> None:
        """Test case for sense_get_request

        Get Request By Request Id
        """
        pass

    def test_sense_get_result(self) -> None:
        """Test case for sense_get_result

        Get Result By Result Id
        """
        pass

    def test_sense_process_request(self) -> None:
        """Test case for sense_process_request

        Process Request
        """
        pass

    def test_sense_transfer_pastel_ticket_to_another_pastelid(self) -> None:
        """Test case for sense_transfer_pastel_ticket_to_another_pastelid

        Transfer Pastel Ticket To Another Pastelid
        """
        pass


if __name__ == '__main__':
    unittest.main()
