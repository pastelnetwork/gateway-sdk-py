# pastel_gateway_sdk.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_api_v1_admin_create_client_post**](AdminApi.md#create_client_api_v1_admin_create_client_post) | **POST** /api/v1/admin/create_client | Create Client


# **create_client_api_v1_admin_create_client_post**
> ClientWithSecret create_client_api_v1_admin_create_client_post()

Create Client

Create new client.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.client_with_secret import ClientWithSecret
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
    api_instance = pastel_gateway_sdk.AdminApi(api_client)

    try:
        # Create Client
        api_response = await api_instance.create_client_api_v1_admin_create_client_post()
        print("The response of AdminApi->create_client_api_v1_admin_create_client_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_client_api_v1_admin_create_client_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientWithSecret**](ClientWithSecret.md)

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

