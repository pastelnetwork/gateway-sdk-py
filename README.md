# pastel-gateway-sdk
Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.
cd
[![gateway_client Python package](https://github.com/pastelnetwork/gateway-sdk-py/actions/workflows/python.yml/badge.svg)](https://github.com/pastelnetwork/gateway-sdk-py/actions/workflows/python.yml)

Pastel Network’s Gateway provides Web3 developers with easy, robust,<br/> 
and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> 
For more information on Pastel Network,<br/> 
review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

- API version: 1.0.0
- Package version: 1.0.4
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/pastelnetwork/gateway-sdk-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/pastelnetwork/gateway-sdk-py.git`)

Then import the package:
```python
import pastel_gateway_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pastel_gateway_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import os, asyncio
from pastel_gateway_sdk.rest import ApiException
from pastel_gateway_sdk import GatewayApiClientAsync, AccountApi, ApiKeysApi

async def main():
    # Enter a context with an instance of the API client
    async with GatewayApiClientAsync(network="testnet") as client:
        try:
            await client.authenticate(os.env["psl-gateway-username"], os.env["psl-gateway-password"])
            
            # My Total Balance
            account_api: AccountApi = client.account_api
            balance = await account_api.account_my_total_balance()
            print(f"My balance = {balance}")

            # My API Keys
            api_keys_api: ApiKeysApi = client.api_keys_api
            api_keys = await api_keys_api.api_keys_read_apikeys()
            print(api_keys)
            
        except ApiException as e:
            print("Exception when using Gateway SDK: %s\n" % e)

# Run the main function.
asyncio.run(main())
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_my_total_balance**](docs/AccountApi.md#account_my_total_balance) | **GET** /api/v1/account/my_total_balance | My Total Balance
*AccountApi* | [**account_pastelid_claiming_step1**](docs/AccountApi.md#account_pastelid_claiming_step1) | **GET** /api/v1/account/pastelid_claiming_step_1 | Pastelid Claiming Step 1
*AccountApi* | [**account_pastelid_claiming_step2**](docs/AccountApi.md#account_pastelid_claiming_step2) | **PUT** /api/v1/account/pastelid_claiming_step_2 | Pastelid Claiming Step 2
*AccountApi* | [**account_set_balance_limit**](docs/AccountApi.md#account_set_balance_limit) | **POST** /api/v1/account/set_balance_limit | Set Balance Limit
*AccountApi* | [**account_total_balances**](docs/AccountApi.md#account_total_balances) | **GET** /api/v1/account/total_balances | Total Balances
*AdminApi* | [**create_client_api_v1_admin_create_client_post**](docs/AdminApi.md#create_client_api_v1_admin_create_client_post) | **POST** /api/v1/admin/create_client | Create Client
*ApiKeysApi* | [**api_keys_create_apikey**](docs/ApiKeysApi.md#api_keys_create_apikey) | **POST** /api/v1/api_keys | Create Apikey
*ApiKeysApi* | [**api_keys_delete_apikey**](docs/ApiKeysApi.md#api_keys_delete_apikey) | **DELETE** /api/v1/api_keys/{api_key} | Delete Apikey
*ApiKeysApi* | [**api_keys_read_apikey**](docs/ApiKeysApi.md#api_keys_read_apikey) | **GET** /api/v1/api_keys/{api_key} | Read Apikey
*ApiKeysApi* | [**api_keys_read_apikeys**](docs/ApiKeysApi.md#api_keys_read_apikeys) | **GET** /api/v1/api_keys | Read Apikeys
*CascadeApi* | [**cascade_get_all_files_from_request**](docs/CascadeApi.md#cascade_get_all_files_from_request) | **GET** /api/v1/cascade/all_files_from_request/{gateway_request_id} | Get All Files From Request
*CascadeApi* | [**cascade_get_all_pastel_registration_tickets_from_request**](docs/CascadeApi.md#cascade_get_all_pastel_registration_tickets_from_request) | **GET** /api/v1/cascade/pastel_registration_tickets/{gateway_request_id} | Get All Pastel Cascade Registration Tickets From Request
*CascadeApi* | [**cascade_get_all_requests**](docs/CascadeApi.md#cascade_get_all_requests) | **GET** /api/v1/cascade/gateway_requests | Get All Requests
*CascadeApi* | [**cascade_get_all_results**](docs/CascadeApi.md#cascade_get_all_results) | **GET** /api/v1/cascade/gateway_results | Get All Results
*CascadeApi* | [**cascade_get_originally_submitted_file_from_result**](docs/CascadeApi.md#cascade_get_originally_submitted_file_from_result) | **GET** /api/v1/cascade/originally_submitted_file/{gateway_result_id} | Get Originally Submitted File From Result
*CascadeApi* | [**cascade_get_pastel_activation_ticket_from_result**](docs/CascadeApi.md#cascade_get_pastel_activation_ticket_from_result) | **GET** /api/v1/cascade/pastel_activation_ticket/{gateway_result_id} | Get Pastel Cascade Activation Ticket From Result
*CascadeApi* | [**cascade_get_pastel_activation_ticket_from_txid**](docs/CascadeApi.md#cascade_get_pastel_activation_ticket_from_txid) | **GET** /api/v1/cascade/pastel_activation_ticket_from_txid/{activation_ticket_txid} | Get Pastel Activation Ticket From Txid
*CascadeApi* | [**cascade_get_pastel_registration_ticket_from_result**](docs/CascadeApi.md#cascade_get_pastel_registration_ticket_from_result) | **GET** /api/v1/cascade/pastel_registration_ticket/{gateway_result_id} | Get Pastel Registration Ticket From Result
*CascadeApi* | [**cascade_get_pastel_registration_ticket_from_stored_file_hash**](docs/CascadeApi.md#cascade_get_pastel_registration_ticket_from_stored_file_hash) | **GET** /api/v1/cascade/pastel_registration_ticket_from_stored_file_hash/{stored_file_sha256_hash_as_hex} | Get Pastel Registration Ticket From Stored File Hash
*CascadeApi* | [**cascade_get_pastel_registration_ticket_from_txid**](docs/CascadeApi.md#cascade_get_pastel_registration_ticket_from_txid) | **GET** /api/v1/cascade/pastel_registration_ticket_from_txid/{registration_ticket_txid} | Get Pastel Registration Ticket From Txid
*CascadeApi* | [**cascade_get_public_stored_file_from_registration_ticket**](docs/CascadeApi.md#cascade_get_public_stored_file_from_registration_ticket) | **GET** /api/v1/cascade/public_stored_file_from_registration_ticket/{registration_ticket_txid} | Get Public Stored File From Registration Ticket
*CascadeApi* | [**cascade_get_request**](docs/CascadeApi.md#cascade_get_request) | **GET** /api/v1/cascade/gateway_requests/{gateway_request_id} | Get Request
*CascadeApi* | [**cascade_get_result**](docs/CascadeApi.md#cascade_get_result) | **GET** /api/v1/cascade/gateway_results/{gateway_result_id} | Get Result
*CascadeApi* | [**cascade_get_stored_file_from_activation_ticket**](docs/CascadeApi.md#cascade_get_stored_file_from_activation_ticket) | **GET** /api/v1/cascade/stored_file_from_activation_ticket/{activation_ticket_txid} | Get Stored File From Activation Ticket
*CascadeApi* | [**cascade_get_stored_file_from_registration_ticket**](docs/CascadeApi.md#cascade_get_stored_file_from_registration_ticket) | **GET** /api/v1/cascade/stored_file_from_registration_ticket/{registration_ticket_txid} | Get Stored File From Registration Ticket
*CascadeApi* | [**cascade_get_stored_file_from_result**](docs/CascadeApi.md#cascade_get_stored_file_from_result) | **GET** /api/v1/cascade/stored_file/{gateway_result_id} | Get Stored File From Result
*CascadeApi* | [**cascade_process_request**](docs/CascadeApi.md#cascade_process_request) | **POST** /api/v1/cascade | Process Request
*CascadeApi* | [**cascade_transfer_pastel_ticket_to_another_pastelid**](docs/CascadeApi.md#cascade_transfer_pastel_ticket_to_another_pastelid) | **GET** /api/v1/cascade/result/transfer_pastel_ticket | Transfer Pastel Ticket To Another Pastelid
*CollectionApi* | [**collection_create_nft_collection**](docs/CollectionApi.md#collection_create_nft_collection) | **POST** /api/v1/collection/nft | Create Nft Collection
*CollectionApi* | [**collection_create_sense_collection**](docs/CollectionApi.md#collection_create_sense_collection) | **POST** /api/v1/collection/sense | Create Sense Collection
*CollectionApi* | [**collection_get_all_nft_collections**](docs/CollectionApi.md#collection_get_all_nft_collections) | **GET** /api/v1/collection/nft/collections | Get All Nft Collections
*CollectionApi* | [**collection_get_all_sense_collections**](docs/CollectionApi.md#collection_get_all_sense_collections) | **GET** /api/v1/collection/sense/collections | Get All Sense Collections
*CollectionApi* | [**collection_get_nft_collections_from_collection_id**](docs/CollectionApi.md#collection_get_nft_collections_from_collection_id) | **GET** /api/v1/collection/nft/collections/{collection_id} | Get Nft Collections From Collection Id
*CollectionApi* | [**collection_get_sense_collections_from_collection_id**](docs/CollectionApi.md#collection_get_sense_collections_from_collection_id) | **GET** /api/v1/collection/sense/collections/{collection_id} | Get Sense Collections From Collection Id
*KeyAuthApi* | [**key_authentication_clear_wallet_key**](docs/KeyAuthApi.md#key_authentication_clear_wallet_key) | **PUT** /api/v1/key_auth/user/clear_key | Clear Wallet Key
*KeyAuthApi* | [**key_authentication_create_user**](docs/KeyAuthApi.md#key_authentication_create_user) | **POST** /api/v1/key_auth/user | Create User
*KeyAuthApi* | [**key_authentication_login_get**](docs/KeyAuthApi.md#key_authentication_login_get) | **GET** /api/v1/key_auth/login/get_params | Get Login With Key Params
*KeyAuthApi* | [**key_authentication_login_post**](docs/KeyAuthApi.md#key_authentication_login_post) | **POST** /api/v1/key_auth/login | Login With Key
*KeyAuthApi* | [**key_authentication_set_wallet_key**](docs/KeyAuthApi.md#key_authentication_set_wallet_key) | **PUT** /api/v1/key_auth/user/set_key | Set Wallet Key
*LoginApi* | [**login_access_token**](docs/LoginApi.md#login_access_token) | **POST** /api/v1/login/access-token | Login Access Token
*LoginApi* | [**login_password_recovery**](docs/LoginApi.md#login_password_recovery) | **POST** /api/v1/password-recovery/{email} | Recover Password
*LoginApi* | [**login_reset_password**](docs/LoginApi.md#login_reset_password) | **POST** /api/v1/reset-password/ | Reset Password
*LoginApi* | [**login_test_token**](docs/LoginApi.md#login_test_token) | **POST** /api/v1/login/test-token | Test Token
*NftApi* | [**nft_get_all_files_from_request**](docs/NftApi.md#nft_get_all_files_from_request) | **GET** /api/v1/nft/all_files_from_request/{gateway_request_id} | Get All Files From Request
*NftApi* | [**nft_get_all_parsed_dd_result_files_from_request**](docs/NftApi.md#nft_get_all_parsed_dd_result_files_from_request) | **GET** /api/v1/nft/all_parsed_dd_result_files_from_request/{gateway_request_id} | Get All Parsed Dd Result Files From Request
*NftApi* | [**nft_get_all_pastel_registration_tickets_from_request**](docs/NftApi.md#nft_get_all_pastel_registration_tickets_from_request) | **GET** /api/v1/nft/pastel_registration_tickets/{gateway_request_id} | Get All Pastel Nft Registration Tickets From Request
*NftApi* | [**nft_get_all_raw_dd_result_files_from_request**](docs/NftApi.md#nft_get_all_raw_dd_result_files_from_request) | **GET** /api/v1/nft/all_raw_dd_result_files_from_request/{gateway_request_id} | Get All Raw Dd Result Files From Request
*NftApi* | [**nft_get_all_requests**](docs/NftApi.md#nft_get_all_requests) | **GET** /api/v1/nft/gateway_requests | Get All Requests
*NftApi* | [**nft_get_all_results**](docs/NftApi.md#nft_get_all_results) | **GET** /api/v1/nft/gateway_results | Get All Results
*NftApi* | [**nft_get_originally_submitted_file_from_result**](docs/NftApi.md#nft_get_originally_submitted_file_from_result) | **GET** /api/v1/nft/originally_submitted_file/{gateway_result_id} | Get Originally Submitted File From Result
*NftApi* | [**nft_get_parsed_dd_result_file_from_activation_ticket**](docs/NftApi.md#nft_get_parsed_dd_result_file_from_activation_ticket) | **GET** /api/v1/nft/parsed_dd_result_file_from_activation_ticket/{activation_ticket_txid} | Get Parsed Dd Result File From Activation Ticket
*NftApi* | [**nft_get_parsed_dd_result_file_from_pastel_id**](docs/NftApi.md#nft_get_parsed_dd_result_file_from_pastel_id) | **GET** /api/v1/nft/parsed_dd_result_file_from_pastel_id/{pastel_id_of_user} | Get Parsed Dd Result File From Pastel Id
*NftApi* | [**nft_get_parsed_dd_result_file_from_registration_ticket**](docs/NftApi.md#nft_get_parsed_dd_result_file_from_registration_ticket) | **GET** /api/v1/nft/parsed_dd_result_file_from_registration_ticket/{registration_ticket_txid} | Get Parsed Dd Result File From Registration Ticket
*NftApi* | [**nft_get_parsed_dd_result_file_from_result**](docs/NftApi.md#nft_get_parsed_dd_result_file_from_result) | **GET** /api/v1/nft/parsed_dd_result_file/{gateway_result_id} | Get Parsed Dd Result File From Result
*NftApi* | [**nft_get_pastel_activation_ticket_from_result**](docs/NftApi.md#nft_get_pastel_activation_ticket_from_result) | **GET** /api/v1/nft/pastel_activation_ticket/{gateway_result_id} | Get Pastel Nft Activation Ticket From Result
*NftApi* | [**nft_get_pastel_activation_ticket_from_txid**](docs/NftApi.md#nft_get_pastel_activation_ticket_from_txid) | **GET** /api/v1/nft/pastel_activation_ticket_from_txid/{activation_ticket_txid} | Get Pastel Activation Ticket From Txid
*NftApi* | [**nft_get_pastel_registration_ticket_from_media_file_hash**](docs/NftApi.md#nft_get_pastel_registration_ticket_from_media_file_hash) | **GET** /api/v1/nft/pastel_registration_ticket_from_media_file_hash/{media_file_sha256_hash} | Get Pastel Registration Ticket From Media File Hash
*NftApi* | [**nft_get_pastel_registration_ticket_from_result**](docs/NftApi.md#nft_get_pastel_registration_ticket_from_result) | **GET** /api/v1/nft/pastel_registration_ticket/{gateway_result_id} | Get Pastel Nft Registration Ticket From Result
*NftApi* | [**nft_get_pastel_registration_ticket_from_txid**](docs/NftApi.md#nft_get_pastel_registration_ticket_from_txid) | **GET** /api/v1/nft/pastel_registration_ticket_from_txid/{registration_ticket_txid} | Get Pastel Registration Ticket From Txid
*NftApi* | [**nft_get_public_stored_file_from_registration_ticket**](docs/NftApi.md#nft_get_public_stored_file_from_registration_ticket) | **GET** /api/v1/nft/public_stored_file_from_registration_ticket/{registration_ticket_txid} | Get Public Stored File From Registration Ticket
*NftApi* | [**nft_get_raw_dd_result_file_from_activation_ticket**](docs/NftApi.md#nft_get_raw_dd_result_file_from_activation_ticket) | **GET** /api/v1/nft/raw_dd_result_file_from_activation_ticket/{activation_ticket_txid} | Get Raw Dd Result File From Activation Ticket
*NftApi* | [**nft_get_raw_dd_result_file_from_pastel_id**](docs/NftApi.md#nft_get_raw_dd_result_file_from_pastel_id) | **GET** /api/v1/nft/raw_dd_result_file_from_pastel_id/{pastel_id_of_user} | Get Raw Dd Result File From Pastel Id
*NftApi* | [**nft_get_raw_dd_result_file_from_registration_ticket**](docs/NftApi.md#nft_get_raw_dd_result_file_from_registration_ticket) | **GET** /api/v1/nft/raw_dd_result_file_from_registration_ticket/{registration_ticket_txid} | Get Raw Dd Result File From Registration Ticket
*NftApi* | [**nft_get_raw_dd_result_file_from_result**](docs/NftApi.md#nft_get_raw_dd_result_file_from_result) | **GET** /api/v1/nft/raw_dd_result_file/{gateway_result_id} | Get Raw Dd Result File From Result
*NftApi* | [**nft_get_request**](docs/NftApi.md#nft_get_request) | **GET** /api/v1/nft/gateway_requests/{gateway_request_id} | Get Request
*NftApi* | [**nft_get_result**](docs/NftApi.md#nft_get_result) | **GET** /api/v1/nft/gateway_results/{gateway_result_id} | Get Result
*NftApi* | [**nft_get_stored_file_from_activation_ticket**](docs/NftApi.md#nft_get_stored_file_from_activation_ticket) | **GET** /api/v1/nft/stored_file_from_activation_ticket/{activation_ticket_txid} | Get Stored File From Activation Ticket
*NftApi* | [**nft_get_stored_file_from_registration_ticket**](docs/NftApi.md#nft_get_stored_file_from_registration_ticket) | **GET** /api/v1/nft/stored_file_from_registration_ticket/{registration_ticket_txid} | Get Stored File From Registration Ticket
*NftApi* | [**nft_get_stored_file_from_result**](docs/NftApi.md#nft_get_stored_file_from_result) | **GET** /api/v1/nft/stored_file/{gateway_result_id} | Get Stored File From Result
*NftApi* | [**nft_process_request**](docs/NftApi.md#nft_process_request) | **POST** /api/v1/nft | Process Request
*NftApi* | [**nft_step1_upload_image_file**](docs/NftApi.md#nft_step1_upload_image_file) | **POST** /api/v1/nft/step_1_upload_image_file | Step 1 Upload Image File
*NftApi* | [**nft_step2_process_nft**](docs/NftApi.md#nft_step2_process_nft) | **POST** /api/v1/nft/step_2_process_nft | Step 2 Process Nft
*NftApi* | [**nft_transfer_pastel_ticket_to_another_pastelid**](docs/NftApi.md#nft_transfer_pastel_ticket_to_another_pastelid) | **GET** /api/v1/nft/result/transfer_pastel_ticket | Transfer Pastel Ticket To Another Pastelid
*SenseApi* | [**sense_get_all_parsed_output_files_from_request**](docs/SenseApi.md#sense_get_all_parsed_output_files_from_request) | **GET** /api/v1/sense/all_parsed_output_files_from_request/{gateway_request_id} | Get All Parsed Output Files From Request
*SenseApi* | [**sense_get_all_pastel_registration_tickets_from_request**](docs/SenseApi.md#sense_get_all_pastel_registration_tickets_from_request) | **GET** /api/v1/sense/pastel_registration_tickets/{gateway_request_id} | Get All Pastel Registration Tickets From Request
*SenseApi* | [**sense_get_all_raw_output_files_from_request**](docs/SenseApi.md#sense_get_all_raw_output_files_from_request) | **GET** /api/v1/sense/all_raw_output_files_from_request/{gateway_request_id} | Get All Raw Output Files From Request
*SenseApi* | [**sense_get_all_requests**](docs/SenseApi.md#sense_get_all_requests) | **GET** /api/v1/sense/gateway_requests | Get All Requests
*SenseApi* | [**sense_get_all_results**](docs/SenseApi.md#sense_get_all_results) | **GET** /api/v1/sense/gateway_results | Get All Results
*SenseApi* | [**sense_get_originally_submitted_file_from_result**](docs/SenseApi.md#sense_get_originally_submitted_file_from_result) | **GET** /api/v1/sense/originally_submitted_file/{gateway_result_id} | Get Originally Submitted File From Result
*SenseApi* | [**sense_get_parsed_output_file_from_activation_ticket**](docs/SenseApi.md#sense_get_parsed_output_file_from_activation_ticket) | **GET** /api/v1/sense/parsed_output_file_from_activation_ticket/{activation_ticket_txid} | Parsed Output File From Activation Ticket
*SenseApi* | [**sense_get_parsed_output_file_from_pastel_id**](docs/SenseApi.md#sense_get_parsed_output_file_from_pastel_id) | **GET** /api/v1/sense/parsed_output_file_from_pastel_id/{pastel_id_of_user} | Parsed Output File From Pastel Id
*SenseApi* | [**sense_get_parsed_output_file_from_registration_ticket**](docs/SenseApi.md#sense_get_parsed_output_file_from_registration_ticket) | **GET** /api/v1/sense/parsed_output_file_from_registration_ticket/{registration_ticket_txid} | Get Parsed Output File From Registration Ticket
*SenseApi* | [**sense_get_parsed_output_file_from_result**](docs/SenseApi.md#sense_get_parsed_output_file_from_result) | **GET** /api/v1/sense/parsed_output_file/{gateway_result_id} | Get Parsed Output File From Result
*SenseApi* | [**sense_get_pastel_activation_ticket_from_result**](docs/SenseApi.md#sense_get_pastel_activation_ticket_from_result) | **GET** /api/v1/sense/pastel_activation_ticket/{gateway_result_id} | Get Pastel Activation Ticket From Result
*SenseApi* | [**sense_get_pastel_activation_ticket_from_txid**](docs/SenseApi.md#sense_get_pastel_activation_ticket_from_txid) | **GET** /api/v1/sense/pastel_activation_ticket_from_txid/{activation_ticket_txid} | Get Pastel Activation Ticket From Txid
*SenseApi* | [**sense_get_pastel_registration_ticket_from_media_file_hash**](docs/SenseApi.md#sense_get_pastel_registration_ticket_from_media_file_hash) | **GET** /api/v1/sense/pastel_registration_ticket_from_media_file_hash/{media_file_sha256_hash} | Get Pastel Registration Ticket Data From Media File Hash
*SenseApi* | [**sense_get_pastel_registration_ticket_from_result**](docs/SenseApi.md#sense_get_pastel_registration_ticket_from_result) | **GET** /api/v1/sense/pastel_registration_ticket/{gateway_result_id} | Get Pastel Registration Ticket From Result
*SenseApi* | [**sense_get_pastel_registration_ticket_from_txid**](docs/SenseApi.md#sense_get_pastel_registration_ticket_from_txid) | **GET** /api/v1/sense/pastel_registration_ticket_from_txid/{registration_ticket_txid} | Get Pastel Registration Ticket From Txid
*SenseApi* | [**sense_get_raw_output_file_from_activation_ticket**](docs/SenseApi.md#sense_get_raw_output_file_from_activation_ticket) | **GET** /api/v1/sense/raw_output_file_from_activation_ticket/{activation_ticket_txid} | Get Raw Output File From Activation Ticket
*SenseApi* | [**sense_get_raw_output_file_from_pastel_id**](docs/SenseApi.md#sense_get_raw_output_file_from_pastel_id) | **GET** /api/v1/sense/raw_output_file_from_pastel_id/{pastel_id_of_user} | Get Raw Output File From Pastel Id
*SenseApi* | [**sense_get_raw_output_file_from_registration_ticket**](docs/SenseApi.md#sense_get_raw_output_file_from_registration_ticket) | **GET** /api/v1/sense/raw_output_file_from_registration_ticket/{registration_ticket_txid} | Get Raw Output File From Registration Ticket
*SenseApi* | [**sense_get_raw_output_file_from_result**](docs/SenseApi.md#sense_get_raw_output_file_from_result) | **GET** /api/v1/sense/raw_output_file/{gateway_result_id} | Get Raw Output File From Result
*SenseApi* | [**sense_get_request**](docs/SenseApi.md#sense_get_request) | **GET** /api/v1/sense/gateway_requests/{gateway_request_id} | Get Request
*SenseApi* | [**sense_get_result**](docs/SenseApi.md#sense_get_result) | **GET** /api/v1/sense/gateway_results/{gateway_result_id} | Get Result
*SenseApi* | [**sense_process_request**](docs/SenseApi.md#sense_process_request) | **POST** /api/v1/sense | Process Request
*SenseApi* | [**sense_transfer_pastel_ticket_to_another_pastelid**](docs/SenseApi.md#sense_transfer_pastel_ticket_to_another_pastelid) | **GET** /api/v1/sense/result/transfer_pastel_ticket | Transfer Pastel Ticket To Another Pastelid
*UsersApi* | [**users_create_user**](docs/UsersApi.md#users_create_user) | **POST** /api/v1/users | Create User
*UsersApi* | [**users_create_user_open**](docs/UsersApi.md#users_create_user_open) | **POST** /api/v1/users/open | Create User Open
*UsersApi* | [**users_delete_user**](docs/UsersApi.md#users_delete_user) | **DELETE** /api/v1/users/{user_id} | Delete Apikey
*UsersApi* | [**users_read_user_by_id**](docs/UsersApi.md#users_read_user_by_id) | **GET** /api/v1/users/{user_id} | Read User By Id
*UsersApi* | [**users_read_user_me**](docs/UsersApi.md#users_read_user_me) | **GET** /api/v1/users/me | Read User Me
*UsersApi* | [**users_read_users**](docs/UsersApi.md#users_read_users) | **GET** /api/v1/users | Read Users
*UsersApi* | [**users_update_user**](docs/UsersApi.md#users_update_user) | **PUT** /api/v1/users/{user_id} | Update User
*UsersApi* | [**users_update_user_me**](docs/UsersApi.md#users_update_user_me) | **PUT** /api/v1/users/me | Update User Me


## Documentation For Models

 - [ApiKey](docs/ApiKey.md)
 - [ApiKeyCreate](docs/ApiKeyCreate.md)
 - [BodyLoginResetPassword](docs/BodyLoginResetPassword.md)
 - [BodyUsersCreateUserOpen](docs/BodyUsersCreateUserOpen.md)
 - [BodyUsersUpdateUserMe](docs/BodyUsersUpdateUserMe.md)
 - [ClientWithSecret](docs/ClientWithSecret.md)
 - [CollectionRegistrationResult](docs/CollectionRegistrationResult.md)
 - [CollectionRegistrationResultStatusMessagesInner](docs/CollectionRegistrationResultStatusMessagesInner.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [Msg](docs/Msg.md)
 - [NftPropertiesExternal](docs/NftPropertiesExternal.md)
 - [ReqStatus](docs/ReqStatus.md)
 - [RequestResult](docs/RequestResult.md)
 - [ResultRegistrationResult](docs/ResultRegistrationResult.md)
 - [Status](docs/Status.md)
 - [Token](docs/Token.md)
 - [User](docs/User.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserCreateWithKey](docs/UserCreateWithKey.md)
 - [UserIdOrEmail](docs/UserIdOrEmail.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [UserWithKey](docs/UserWithKey.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="OAuth2PasswordBearer"></a>
### OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A

<a id="APIKeyHeader"></a>
### APIKeyHeader

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author




