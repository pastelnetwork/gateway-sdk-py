# pastel_gateway_sdk.KeyAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_authentication_clear_wallet_key**](KeyAuthApi.md#key_authentication_clear_wallet_key) | **PUT** /api/v1/key_auth/user/clear_key | Clear Wallet Key
[**key_authentication_create_user**](KeyAuthApi.md#key_authentication_create_user) | **POST** /api/v1/key_auth/user | Create User
[**key_authentication_login_get**](KeyAuthApi.md#key_authentication_login_get) | **GET** /api/v1/key_auth/login/get_params | Get Login With Key Params
[**key_authentication_login_post**](KeyAuthApi.md#key_authentication_login_post) | **POST** /api/v1/key_auth/login | Login With Key
[**key_authentication_set_wallet_key**](KeyAuthApi.md#key_authentication_set_wallet_key) | **PUT** /api/v1/key_auth/user/set_key | Set Wallet Key


# **key_authentication_clear_wallet_key**
> UserWithKey key_authentication_clear_wallet_key()

Clear Wallet Key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user_with_key import UserWithKey
from pastel_gateway_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pastel_gateway_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with pastel_gateway_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pastel_gateway_sdk.KeyAuthApi(api_client)

    try:
        # Clear Wallet Key
        api_response = await api_instance.key_authentication_clear_wallet_key()
        print("The response of KeyAuthApi->key_authentication_clear_wallet_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthApi->key_authentication_clear_wallet_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserWithKey**](UserWithKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_authentication_create_user**
> UserWithKey key_authentication_create_user(client_id, client_secret, user_create_with_key)

Create User

Create new user with key auth, returns user object with funding address. limit=0 means no limit

### Example


```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user_create_with_key import UserCreateWithKey
from pastel_gateway_sdk.models.user_with_key import UserWithKey
from pastel_gateway_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pastel_gateway_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pastel_gateway_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pastel_gateway_sdk.KeyAuthApi(api_client)
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 
    user_create_with_key = pastel_gateway_sdk.UserCreateWithKey() # UserCreateWithKey | 

    try:
        # Create User
        api_response = await api_instance.key_authentication_create_user(client_id, client_secret, user_create_with_key)
        print("The response of KeyAuthApi->key_authentication_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthApi->key_authentication_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **user_create_with_key** | [**UserCreateWithKey**](UserCreateWithKey.md)|  | 

### Return type

[**UserWithKey**](UserWithKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_authentication_login_get**
> UserWithKey key_authentication_login_get(wallet_id, signature, validation_token, timestamp, client_id, client_secret)

Get Login With Key Params

### Example


```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user_with_key import UserWithKey
from pastel_gateway_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pastel_gateway_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pastel_gateway_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pastel_gateway_sdk.KeyAuthApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    signature = 'signature_example' # str | 
    validation_token = 'validation_token_example' # str | 
    timestamp = 'timestamp_example' # str | 
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 

    try:
        # Get Login With Key Params
        api_response = await api_instance.key_authentication_login_get(wallet_id, signature, validation_token, timestamp, client_id, client_secret)
        print("The response of KeyAuthApi->key_authentication_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthApi->key_authentication_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **signature** | **str**|  | 
 **validation_token** | **str**|  | 
 **timestamp** | **str**|  | 
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 

### Return type

[**UserWithKey**](UserWithKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_authentication_login_post**
> Token key_authentication_login_post(wallet_id, signature, timestamp, client_id, client_secret)

Login With Key

### Example


```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.token import Token
from pastel_gateway_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pastel_gateway_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pastel_gateway_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pastel_gateway_sdk.KeyAuthApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    signature = 'signature_example' # str | 
    timestamp = 'timestamp_example' # str | 
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 

    try:
        # Login With Key
        api_response = await api_instance.key_authentication_login_post(wallet_id, signature, timestamp, client_id, client_secret)
        print("The response of KeyAuthApi->key_authentication_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthApi->key_authentication_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **signature** | **str**|  | 
 **timestamp** | **str**|  | 
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_authentication_set_wallet_key**
> UserWithKey key_authentication_set_wallet_key(wallet_id, signature1, signature2, wallet_key, timestamp, client_id, client_secret)

Set Wallet Key

### Example


```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user_with_key import UserWithKey
from pastel_gateway_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pastel_gateway_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pastel_gateway_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pastel_gateway_sdk.KeyAuthApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    signature1 = 'signature1_example' # str | 
    signature2 = 'signature2_example' # str | 
    wallet_key = 'wallet_key_example' # str | 
    timestamp = 'timestamp_example' # str | 
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 

    try:
        # Set Wallet Key
        api_response = await api_instance.key_authentication_set_wallet_key(wallet_id, signature1, signature2, wallet_key, timestamp, client_id, client_secret)
        print("The response of KeyAuthApi->key_authentication_set_wallet_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthApi->key_authentication_set_wallet_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **signature1** | **str**|  | 
 **signature2** | **str**|  | 
 **wallet_key** | **str**|  | 
 **timestamp** | **str**|  | 
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 

### Return type

[**UserWithKey**](UserWithKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

