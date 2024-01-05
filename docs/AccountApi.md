# gateway_client.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_my_total_balance**](AccountApi.md#account_my_total_balance) | **GET** /api/v1/account/my_total_balance | My Total Balance
[**account_pastelid_claiming_step1**](AccountApi.md#account_pastelid_claiming_step1) | **GET** /api/v1/account/pastelid_claiming_step_1 | Pastelid Claiming Step 1
[**account_pastelid_claiming_step2**](AccountApi.md#account_pastelid_claiming_step2) | **PUT** /api/v1/account/pastelid_claiming_step_2 | Pastelid Claiming Step 2
[**account_set_balance_limit**](AccountApi.md#account_set_balance_limit) | **POST** /api/v1/account/set_balance_limit | Set Balance Limit
[**account_total_balances**](AccountApi.md#account_total_balances) | **GET** /api/v1/account/total_balances | Total Balances


# **account_my_total_balance**
> object account_my_total_balance()

My Total Balance

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import os
import gateway_client
from gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gateway_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.AccountApi(api_client)

    try:
        # My Total Balance
        api_response = await api_instance.account_my_total_balance()
        print("The response of AccountApi->account_my_total_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_my_total_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **account_pastelid_claiming_step1**
> str account_pastelid_claiming_step1(pastel_id=pastel_id)

Pastelid Claiming Step 1

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import os
import gateway_client
from gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gateway_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.AccountApi(api_client)
    pastel_id = '' # str | Pastel ID to claim (optional) (default to '')

    try:
        # Pastelid Claiming Step 1
        api_response = await api_instance.account_pastelid_claiming_step1(pastel_id=pastel_id)
        print("The response of AccountApi->account_pastelid_claiming_step1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_pastelid_claiming_step1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pastel_id** | **str**| Pastel ID to claim | [optional] [default to &#39;&#39;]

### Return type

**str**

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

# **account_pastelid_claiming_step2**
> object account_pastelid_claiming_step2(pastel_id=pastel_id, signature=signature)

Pastelid Claiming Step 2

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import os
import gateway_client
from gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gateway_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.AccountApi(api_client)
    pastel_id = '' # str | Pastel ID to claim (optional) (default to '')
    signature = '' # str | Signature of the message returned by pastelid_claiming_step_1 (optional) (default to '')

    try:
        # Pastelid Claiming Step 2
        api_response = await api_instance.account_pastelid_claiming_step2(pastel_id=pastel_id, signature=signature)
        print("The response of AccountApi->account_pastelid_claiming_step2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_pastelid_claiming_step2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pastel_id** | **str**| Pastel ID to claim | [optional] [default to &#39;&#39;]
 **signature** | **str**| Signature of the message returned by pastelid_claiming_step_1 | [optional] [default to &#39;&#39;]

### Return type

**object**

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

# **account_set_balance_limit**
> float account_set_balance_limit(user_id_or_email, new_balance_limit)

Set Balance Limit

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import os
import gateway_client
from gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gateway_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.AccountApi(api_client)
    user_id_or_email = gateway_client.UserIdOrEmail() # UserIdOrEmail | 
    new_balance_limit = 3.4 # float | 

    try:
        # Set Balance Limit
        api_response = await api_instance.account_set_balance_limit(user_id_or_email, new_balance_limit)
        print("The response of AccountApi->account_set_balance_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_set_balance_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_email** | [**UserIdOrEmail**](.md)|  | 
 **new_balance_limit** | **float**|  | 

### Return type

**float**

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

# **account_total_balances**
> List[object] account_total_balances()

Total Balances

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import os
import gateway_client
from gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gateway_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.AccountApi(api_client)

    try:
        # Total Balances
        api_response = await api_instance.account_total_balances()
        print("The response of AccountApi->account_total_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_total_balances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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

