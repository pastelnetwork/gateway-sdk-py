# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pastel_gateway_sdk.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_users_create_user(self) -> None:
        """Test case for users_create_user

        Create User
        """
        pass

    def test_users_create_user_open(self) -> None:
        """Test case for users_create_user_open

        Create User Open
        """
        pass

    def test_users_delete_user(self) -> None:
        """Test case for users_delete_user

        Delete Apikey
        """
        pass

    def test_users_read_user_by_id(self) -> None:
        """Test case for users_read_user_by_id

        Read User By Id
        """
        pass

    def test_users_read_user_me(self) -> None:
        """Test case for users_read_user_me

        Read User Me
        """
        pass

    def test_users_read_users(self) -> None:
        """Test case for users_read_users

        Read Users
        """
        pass

    def test_users_update_user(self) -> None:
        """Test case for users_update_user

        Update User
        """
        pass

    def test_users_update_user_me(self) -> None:
        """Test case for users_update_user_me

        Update User Me
        """
        pass


if __name__ == '__main__':
    unittest.main()
