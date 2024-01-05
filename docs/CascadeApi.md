# gateway_client.CascadeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cascade_get_all_files_from_request**](CascadeApi.md#cascade_get_all_files_from_request) | **GET** /api/v1/cascade/all_files_from_request/{gateway_request_id} | Get All Files From Request
[**cascade_get_all_pastel_registration_tickets_from_request**](CascadeApi.md#cascade_get_all_pastel_registration_tickets_from_request) | **GET** /api/v1/cascade/pastel_registration_tickets/{gateway_request_id} | Get All Pastel Cascade Registration Tickets From Request
[**cascade_get_all_requests**](CascadeApi.md#cascade_get_all_requests) | **GET** /api/v1/cascade/gateway_requests | Get All Requests
[**cascade_get_all_results**](CascadeApi.md#cascade_get_all_results) | **GET** /api/v1/cascade/gateway_results | Get All Results
[**cascade_get_originally_submitted_file**](CascadeApi.md#cascade_get_originally_submitted_file) | **GET** /api/v1/cascade/originally_submitted_file/{gateway_result_id} | Get Originally Submitted File By Result Id
[**cascade_get_pastel_activation_ticket_from_result**](CascadeApi.md#cascade_get_pastel_activation_ticket_from_result) | **GET** /api/v1/cascade/pastel_activation_ticket/{gateway_result_id} | Get Pastel Cascade Activation Ticket By Result Id
[**cascade_get_pastel_activation_ticket_from_txid**](CascadeApi.md#cascade_get_pastel_activation_ticket_from_txid) | **GET** /api/v1/cascade/pastel_activation_ticket_from_txid/{activation_ticket_txid} | Get Pastel Activation Ticket By Its Txid
[**cascade_get_pastel_registration_ticket_from_result**](CascadeApi.md#cascade_get_pastel_registration_ticket_from_result) | **GET** /api/v1/cascade/pastel_registration_ticket/{gateway_result_id} | Get Pastel Cascade Registration Ticket By Result Id
[**cascade_get_pastel_registration_ticket_from_txid**](CascadeApi.md#cascade_get_pastel_registration_ticket_from_txid) | **GET** /api/v1/cascade/pastel_registration_ticket_from_txid/{registration_ticket_txid} | Get Pastel Registration Ticket By Its Txid
[**cascade_get_pastel_ticket_from_stored_file_hash**](CascadeApi.md#cascade_get_pastel_ticket_from_stored_file_hash) | **GET** /api/v1/cascade/pastel_ticket_from_stored_file_hash/{stored_file_sha256_hash_as_hex} | Get Pastel Registration Ticket By Stored File Hash
[**cascade_get_public_stored_file_from_registration_ticket**](CascadeApi.md#cascade_get_public_stored_file_from_registration_ticket) | **GET** /api/v1/cascade/public_stored_file_from_registration_ticket/{registration_ticket_txid} | Get Public Stored File By Registration Ticket
[**cascade_get_request**](CascadeApi.md#cascade_get_request) | **GET** /api/v1/cascade/gateway_requests/{gateway_request_id} | Get Request By Request Id
[**cascade_get_result**](CascadeApi.md#cascade_get_result) | **GET** /api/v1/cascade/gateway_results/{gateway_result_id} | Get Result By Result Id
[**cascade_get_stored_file**](CascadeApi.md#cascade_get_stored_file) | **GET** /api/v1/cascade/stored_file/{gateway_result_id} | Get Stored File By Result Id
[**cascade_get_stored_file_from_activation_ticket**](CascadeApi.md#cascade_get_stored_file_from_activation_ticket) | **GET** /api/v1/cascade/stored_file_from_activation_ticket/{activation_ticket_txid} | Get Stored File By Activation Ticket
[**cascade_get_stored_file_from_registration_ticket**](CascadeApi.md#cascade_get_stored_file_from_registration_ticket) | **GET** /api/v1/cascade/stored_file_from_registration_ticket/{registration_ticket_txid} | Get Stored File By Registration Ticket
[**cascade_process_request**](CascadeApi.md#cascade_process_request) | **POST** /api/v1/cascade | Process Request
[**cascade_transfer_pastel_ticket_to_another_pastelid**](CascadeApi.md#cascade_transfer_pastel_ticket_to_another_pastelid) | **GET** /api/v1/cascade/result/transfer_pastel_ticket | Transfer Pastel Ticket To Another Pastelid


# **cascade_get_all_files_from_request**
> object cascade_get_all_files_from_request(gateway_request_id)

Get All Files From Request

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Files From Request
        api_response = await api_instance.cascade_get_all_files_from_request(gateway_request_id)
        print("The response of CascadeApi->cascade_get_all_files_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_all_files_from_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_request_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_all_pastel_registration_tickets_from_request**
> object cascade_get_all_pastel_registration_tickets_from_request(gateway_request_id)

Get All Pastel Cascade Registration Tickets From Request

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Pastel Cascade Registration Tickets From Request
        api_response = await api_instance.cascade_get_all_pastel_registration_tickets_from_request(gateway_request_id)
        print("The response of CascadeApi->cascade_get_all_pastel_registration_tickets_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_all_pastel_registration_tickets_from_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_request_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_all_requests**
> List[RequestResult] cascade_get_all_requests(status_requested=status_requested, offset=offset, limit=limit)

Get All Requests

Return the status of the submitted request

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.req_status import ReqStatus
from gateway_client.models.request_result import RequestResult
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    status_requested = gateway_client.ReqStatus() # ReqStatus |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10000 # int |  (optional) (default to 10000)

    try:
        # Get All Requests
        api_response = await api_instance.cascade_get_all_requests(status_requested=status_requested, offset=offset, limit=limit)
        print("The response of CascadeApi->cascade_get_all_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_all_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_requested** | [**ReqStatus**](.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10000]

### Return type

[**List[RequestResult]**](RequestResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_all_results**
> List[ResultRegistrationResult] cascade_get_all_results(status_requested=status_requested, offset=offset, limit=limit)

Get All Results

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.req_status import ReqStatus
from gateway_client.models.result_registration_result import ResultRegistrationResult
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    status_requested = gateway_client.ReqStatus() # ReqStatus |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10000 # int |  (optional) (default to 10000)

    try:
        # Get All Results
        api_response = await api_instance.cascade_get_all_results(status_requested=status_requested, offset=offset, limit=limit)
        print("The response of CascadeApi->cascade_get_all_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_all_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_requested** | [**ReqStatus**](.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10000]

### Return type

[**List[ResultRegistrationResult]**](ResultRegistrationResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_originally_submitted_file**
> object cascade_get_originally_submitted_file(gateway_result_id)

Get Originally Submitted File By Result Id

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Originally Submitted File By Result Id
        api_response = await api_instance.cascade_get_originally_submitted_file(gateway_result_id)
        print("The response of CascadeApi->cascade_get_originally_submitted_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_originally_submitted_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_result_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_pastel_activation_ticket_from_result**
> object cascade_get_pastel_activation_ticket_from_result(gateway_result_id)

Get Pastel Cascade Activation Ticket By Result Id

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Pastel Cascade Activation Ticket By Result Id
        api_response = await api_instance.cascade_get_pastel_activation_ticket_from_result(gateway_result_id)
        print("The response of CascadeApi->cascade_get_pastel_activation_ticket_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_pastel_activation_ticket_from_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_result_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_pastel_activation_ticket_from_txid**
> object cascade_get_pastel_activation_ticket_from_txid(activation_ticket_txid)

Get Pastel Activation Ticket By Its Txid

### Example


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


# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Pastel Activation Ticket By Its Txid
        api_response = await api_instance.cascade_get_pastel_activation_ticket_from_txid(activation_ticket_txid)
        print("The response of CascadeApi->cascade_get_pastel_activation_ticket_from_txid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_pastel_activation_ticket_from_txid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_ticket_txid** | **str**|  | 

### Return type

**object**

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

# **cascade_get_pastel_registration_ticket_from_result**
> object cascade_get_pastel_registration_ticket_from_result(gateway_result_id)

Get Pastel Cascade Registration Ticket By Result Id

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Pastel Cascade Registration Ticket By Result Id
        api_response = await api_instance.cascade_get_pastel_registration_ticket_from_result(gateway_result_id)
        print("The response of CascadeApi->cascade_get_pastel_registration_ticket_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_pastel_registration_ticket_from_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_result_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_pastel_registration_ticket_from_txid**
> object cascade_get_pastel_registration_ticket_from_txid(registration_ticket_txid)

Get Pastel Registration Ticket By Its Txid

### Example


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


# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Pastel Registration Ticket By Its Txid
        api_response = await api_instance.cascade_get_pastel_registration_ticket_from_txid(registration_ticket_txid)
        print("The response of CascadeApi->cascade_get_pastel_registration_ticket_from_txid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_pastel_registration_ticket_from_txid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_ticket_txid** | **str**|  | 

### Return type

**object**

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

# **cascade_get_pastel_ticket_from_stored_file_hash**
> object cascade_get_pastel_ticket_from_stored_file_hash(stored_file_sha256_hash_as_hex)

Get Pastel Registration Ticket By Stored File Hash

### Example


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


# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    stored_file_sha256_hash_as_hex = 'stored_file_sha256_hash_as_hex_example' # str | 

    try:
        # Get Pastel Registration Ticket By Stored File Hash
        api_response = await api_instance.cascade_get_pastel_ticket_from_stored_file_hash(stored_file_sha256_hash_as_hex)
        print("The response of CascadeApi->cascade_get_pastel_ticket_from_stored_file_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_pastel_ticket_from_stored_file_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stored_file_sha256_hash_as_hex** | **str**|  | 

### Return type

**object**

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

# **cascade_get_public_stored_file_from_registration_ticket**
> object cascade_get_public_stored_file_from_registration_ticket(registration_ticket_txid)

Get Public Stored File By Registration Ticket

### Example


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


# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Public Stored File By Registration Ticket
        api_response = await api_instance.cascade_get_public_stored_file_from_registration_ticket(registration_ticket_txid)
        print("The response of CascadeApi->cascade_get_public_stored_file_from_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_public_stored_file_from_registration_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_ticket_txid** | **str**|  | 

### Return type

**object**

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

# **cascade_get_request**
> RequestResult cascade_get_request(gateway_request_id)

Get Request By Request Id

Return the status of the submitted Work

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.request_result import RequestResult
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get Request By Request Id
        api_response = await api_instance.cascade_get_request(gateway_request_id)
        print("The response of CascadeApi->cascade_get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_request_id** | **str**|  | 

### Return type

[**RequestResult**](RequestResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_result**
> ResultRegistrationResult cascade_get_result(gateway_result_id)

Get Result By Result Id

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.result_registration_result import ResultRegistrationResult
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Result By Result Id
        api_response = await api_instance.cascade_get_result(gateway_result_id)
        print("The response of CascadeApi->cascade_get_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_result_id** | **str**|  | 

### Return type

[**ResultRegistrationResult**](ResultRegistrationResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_stored_file**
> object cascade_get_stored_file(gateway_result_id)

Get Stored File By Result Id

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Stored File By Result Id
        api_response = await api_instance.cascade_get_stored_file(gateway_result_id)
        print("The response of CascadeApi->cascade_get_stored_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_stored_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_result_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_stored_file_from_activation_ticket**
> object cascade_get_stored_file_from_activation_ticket(activation_ticket_txid)

Get Stored File By Activation Ticket

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Stored File By Activation Ticket
        api_response = await api_instance.cascade_get_stored_file_from_activation_ticket(activation_ticket_txid)
        print("The response of CascadeApi->cascade_get_stored_file_from_activation_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_stored_file_from_activation_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_ticket_txid** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_get_stored_file_from_registration_ticket**
> object cascade_get_stored_file_from_registration_ticket(registration_ticket_txid)

Get Stored File By Registration Ticket

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Stored File By Registration Ticket
        api_response = await api_instance.cascade_get_stored_file_from_registration_ticket(registration_ticket_txid)
        print("The response of CascadeApi->cascade_get_stored_file_from_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_get_stored_file_from_registration_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_ticket_txid** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_process_request**
> RequestResult cascade_process_request(files, make_publicly_accessible=make_publicly_accessible, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)

Process Request

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.request_result import RequestResult
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    files = None # List[bytearray] | 
    make_publicly_accessible = True # bool | Make the file publicly accessible (optional) (default to True)
    after_activation_transfer_to_pastelid = 'after_activation_transfer_to_pastelid_example' # str | PastelID to transfer the NFT to after activation, if any (optional)

    try:
        # Process Request
        api_response = await api_instance.cascade_process_request(files, make_publicly_accessible=make_publicly_accessible, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)
        print("The response of CascadeApi->cascade_process_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_process_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 
 **make_publicly_accessible** | **bool**| Make the file publicly accessible | [optional] [default to True]
 **after_activation_transfer_to_pastelid** | **str**| PastelID to transfer the NFT to after activation, if any | [optional] 

### Return type

[**RequestResult**](RequestResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cascade_transfer_pastel_ticket_to_another_pastelid**
> object cascade_transfer_pastel_ticket_to_another_pastelid(gateway_result_id, pastel_id)

Transfer Pastel Ticket To Another Pastelid

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_client.CascadeApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 
    pastel_id = 'pastel_id_example' # str | 

    try:
        # Transfer Pastel Ticket To Another Pastelid
        api_response = await api_instance.cascade_transfer_pastel_ticket_to_another_pastelid(gateway_result_id, pastel_id)
        print("The response of CascadeApi->cascade_transfer_pastel_ticket_to_another_pastelid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CascadeApi->cascade_transfer_pastel_ticket_to_another_pastelid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_result_id** | **str**|  | 
 **pastel_id** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

