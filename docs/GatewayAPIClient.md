# GatewayApiClient

`GatewayApiClient` is a custom client for interacting with Pastel Gateway APIs.

## Initialization

- To use the client, first create an instance of `GatewayApiClient`:

  ```python
  client = GatewayApiClient(network="mainnet")
  ```
  `network` can be "mainnet" or "testnet". Alternatively, you can specify a `custom_url`.

## Authentication

- You can authenticate the client with a username and password:

  ```python
  client.authenticate(username="your_username", password="your_password")
  ```

## Accessing APIs

After successful authentication, you can access the `AccountApi`, `ApiKeysApi`, `UsersApi` and `LoginApi`.

- To access `AccountApi`:

  ```python
  account_api = client.account_api
  ```

- To access `ApiKeysApi`:

  ```python
  api_keys_api = client.api_keys_api
  ```

- To access `UsersApi`:

  ```python
  users_api = client.users_api
  ```

- To access `LoginApi`:

  ```python
  login_api = client.login_api
  ```

## Setting API keys

For APIs that require an API key for authentication, you can use `set_auth_api_key` and `clear_auth_api_key` methods.

- To set an API key:

  ```python
  client.set_auth_api_key("your_api_key")
  ```
  
- To clear an API key:

  ```python
  client.clear_auth_api_key()
  ```
  
- APIs that require API Key authentication: `CascadeApi`, `CollectionApi`, `NftApi`, `SenseApi`.

  ```python
  # Set the API Key before accessing the API
  client.set_auth_api_key("your_api_key")
  # Access the API (NftApi for example)
  nft_api = client.nft_api
  # Optionally, you can clear the API Key once done
  client.clear_auth_api_key()
  ```

## Error Handling

The clients and their methods may raise exceptions upon errors. Ensure to properly handle these in your implementation.