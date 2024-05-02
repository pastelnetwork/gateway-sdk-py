# pastel_gateway_sdk.ApiKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_keys_create_apikey**](ApiKeysApi.md#api_keys_create_apikey) | **POST** /api/v1/api_keys | Create Apikey
[**api_keys_delete_apikey**](ApiKeysApi.md#api_keys_delete_apikey) | **DELETE** /api/v1/api_keys/{api_key} | Delete Apikey
[**api_keys_read_apikey**](ApiKeysApi.md#api_keys_read_apikey) | **GET** /api/v1/api_keys/{api_key} | Read Apikey
[**api_keys_read_apikeys**](ApiKeysApi.md#api_keys_read_apikeys) | **GET** /api/v1/api_keys | Read Apikeys


# **api_keys_create_apikey**
> ApiKey api_keys_create_apikey(api_key_create)

Create Apikey

Create new api key.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.api_key import ApiKey
from pastel_gateway_sdk.models.api_key_create import ApiKeyCreate
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
    api_instance = pastel_gateway_sdk.ApiKeysApi(api_client)
    api_key_create = pastel_gateway_sdk.ApiKeyCreate() # ApiKeyCreate | 

    try:
        # Create Apikey
        api_response = await api_instance.api_keys_create_apikey(api_key_create)
        print("The response of ApiKeysApi->api_keys_create_apikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_create_apikey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create** | [**ApiKeyCreate**](ApiKeyCreate.md)|  | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_delete_apikey**
> ApiKey api_keys_delete_apikey(api_key)

Delete Apikey

Delete an api key.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.api_key import ApiKey
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
    api_instance = pastel_gateway_sdk.ApiKeysApi(api_client)
    api_key = 'api_key_example' # str | 

    try:
        # Delete Apikey
        api_response = await api_instance.api_keys_delete_apikey(api_key)
        print("The response of ApiKeysApi->api_keys_delete_apikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_delete_apikey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_read_apikey**
> ApiKey api_keys_read_apikey(api_key)

Read Apikey

Get api key by apikey.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.api_key import ApiKey
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
    api_instance = pastel_gateway_sdk.ApiKeysApi(api_client)
    api_key = 'api_key_example' # str | 

    try:
        # Read Apikey
        api_response = await api_instance.api_keys_read_apikey(api_key)
        print("The response of ApiKeysApi->api_keys_read_apikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_read_apikey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_read_apikeys**
> List[ApiKey] api_keys_read_apikeys(skip=skip, limit=limit)

Read Apikeys

Retrieve api key of the user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.api_key import ApiKey
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
    api_instance = pastel_gateway_sdk.ApiKeysApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Read Apikeys
        api_response = await api_instance.api_keys_read_apikeys(skip=skip, limit=limit)
        print("The response of ApiKeysApi->api_keys_read_apikeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->api_keys_read_apikeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[ApiKey]**](ApiKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

