import os
import asyncio
from pastel_gateway_sdk.rest import ApiException
from pastel_gateway_sdk import GatewayApiClientAsync, AccountApi, ApiKeysApi
from pprint import pprint  # add pprint import here


async def main():
    client = GatewayApiClientAsync(network="testnet")
    try:
        await client.authenticate("test@example.com", "string")

        # My Total Balance
        account_api: AccountApi = client.account_api
        balance = await account_api.account_my_total_balance()
        print(f"My balance = {balance}")

        # My API Keys
        api_keys_api: ApiKeysApi = client.api_keys_api
        api_keys = await api_keys_api.api_keys_read_apikeys()
        if not api_keys:
            return 0
        client.set_auth_api_key(api_keys[0].api_key)
        print(api_keys[0].api_key)

        # Get All Requests
        cascade_api = client.cascade_api
        requests = await cascade_api.cascade_get_all_requests()
        pprint(requests)  # use pprint here instead of print

    except ApiException as e:
        print("Exception when using Gateway SDK: %s\n" % e)

# Run the main function.
asyncio.run(main())
