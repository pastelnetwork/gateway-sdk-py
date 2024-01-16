import asyncio
import argparse
from pastel_gateway_sdk.rest import ApiException
from pastel_gateway_sdk import GatewayApiClientAsync, AccountApi, ApiKeysApi


async def main():
    parser = argparse.ArgumentParser(description='Process file path.')
    parser.add_argument('--file-path', type=str, help='Provide file path here', required=True)
    parser.add_argument('--api-key', type=str, help='OPTIONAL: Provide API Key')
    args = parser.parse_args()

    client = GatewayApiClientAsync(network="testnet")
    try:
        ok = await client.authenticate("test@example.com", "string")
        if not ok:
            print("Authentication failed")
            return 0

        # Find API Keys for cascade
        api_keys_api: ApiKeysApi = client.api_keys_api
        api_keys = await api_keys_api.api_keys_read_apikeys()
        if not api_keys:
            return 0
        api_key = None
        for key in api_keys:
            if args.api_key and key.api_key == args.api_key and key.can_cascade:
                api_key = key.api_key
                break
            if key.can_cascade:
                api_key = key.api_key
                break
        if not api_key:
            if args.api_key:
                print(f"API Key '{args.api_key}' not found or doesn't have cascade permission")
            else:
                print("No API Key with cascade permission found")
            return 0
        client.set_auth_api_key(api_key)

        print(f"Will register Cascade ticket for file '{args.file_path}' with APY Key: {api_key}")

        # Register Cascade ticket
        cascade_api = client.cascade_api
        result = await cascade_api.cascade_process_request([args.file_path], make_publicly_accessible=True)
        print(f"Cascade ticket registration started. Request status: {result.to_str()}")

    except ApiException as e:
        print("Exception when using Gateway SDK: %s\n" % e)


# Run the main function.
asyncio.run(main())
