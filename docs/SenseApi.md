# gateway_client.SenseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sense_get_all_parsed_output_files_from_request**](SenseApi.md#sense_get_all_parsed_output_files_from_request) | **GET** /api/v1/sense/all_parsed_output_files_from_request/{gateway_request_id} | Get All Parsed Output Files From Request
[**sense_get_all_pastel_registration_tickets_from_request**](SenseApi.md#sense_get_all_pastel_registration_tickets_from_request) | **GET** /api/v1/sense/pastel_registration_tickets/{gateway_request_id} | Get All Pastel Sense Registration Tickets From Request
[**sense_get_all_raw_output_files_from_request**](SenseApi.md#sense_get_all_raw_output_files_from_request) | **GET** /api/v1/sense/all_raw_output_files_from_request/{gateway_request_id} | Get All Raw Output Files From Request
[**sense_get_all_requests**](SenseApi.md#sense_get_all_requests) | **GET** /api/v1/sense/gateway_requests | Get All Requests
[**sense_get_all_results**](SenseApi.md#sense_get_all_results) | **GET** /api/v1/sense/gateway_results | Get All Results
[**sense_get_originally_submitted_file_by_result_id**](SenseApi.md#sense_get_originally_submitted_file_by_result_id) | **GET** /api/v1/sense/originally_submitted_file/{gateway_result_id} | Get Originally Submitted File By Result Id
[**sense_get_parsed_output_file_by_activation_ticket**](SenseApi.md#sense_get_parsed_output_file_by_activation_ticket) | **GET** /api/v1/sense/parsed_output_file_by_activation_txid/{activation_ticket_txid} | Parsed Output File By Activation Ticket
[**sense_get_parsed_output_file_by_pastel_id**](SenseApi.md#sense_get_parsed_output_file_by_pastel_id) | **GET** /api/v1/sense/parsed_output_file_by_pastel_id/{pastel_id_of_user} | Parsed Output File By Pastel Id
[**sense_get_parsed_output_file_by_registration_ticket**](SenseApi.md#sense_get_parsed_output_file_by_registration_ticket) | **GET** /api/v1/sense/parsed_output_file_by_registration_ticket/{registration_ticket_txid} | Get Parsed Output File By Registration Ticket
[**sense_get_parsed_output_file_by_result_id**](SenseApi.md#sense_get_parsed_output_file_by_result_id) | **GET** /api/v1/sense/parsed_output_file/{gateway_result_id} | Get Parsed Output File By Result Id
[**sense_get_pastel_activation_ticket_by_its_txid**](SenseApi.md#sense_get_pastel_activation_ticket_by_its_txid) | **GET** /api/v1/sense/pastel_activation_ticket_from_txid/{activation_ticket_txid} | Get Pastel Activation Ticket By Its Txid
[**sense_get_pastel_activation_ticket_by_result_id**](SenseApi.md#sense_get_pastel_activation_ticket_by_result_id) | **GET** /api/v1/sense/pastel_activation_ticket/{gateway_result_id} | Get Pastel Sense Activation Ticket By Result Id
[**sense_get_pastel_registration_ticket_by_its_txid**](SenseApi.md#sense_get_pastel_registration_ticket_by_its_txid) | **GET** /api/v1/sense/pastel_registration_ticket_from_txid/{registration_ticket_txid} | Get Pastel Registration Ticket By Its Txid
[**sense_get_pastel_registration_ticket_by_result_id**](SenseApi.md#sense_get_pastel_registration_ticket_by_result_id) | **GET** /api/v1/sense/pastel_registration_ticket/{gateway_result_id} | Get Pastel Sense Registration Ticket By Result Id
[**sense_get_pastel_ticket_by_media_file_hash**](SenseApi.md#sense_get_pastel_ticket_by_media_file_hash) | **GET** /api/v1/sense/pastel_ticket_by_media_file_hash/{media_file_sha256_hash} | Get Pastel Ticket Data From Media File Hash
[**sense_get_raw_output_file_by_activation_ticket**](SenseApi.md#sense_get_raw_output_file_by_activation_ticket) | **GET** /api/v1/sense/raw_output_file_by_activation_ticket/{activation_ticket_txid} | Get Raw Output File By Activation Ticket
[**sense_get_raw_output_file_by_pastel_id**](SenseApi.md#sense_get_raw_output_file_by_pastel_id) | **GET** /api/v1/sense/raw_output_file_by_pastel_id/{pastel_id_of_user} | Get Raw Output File By Pastel Id
[**sense_get_raw_output_file_by_registration_ticket**](SenseApi.md#sense_get_raw_output_file_by_registration_ticket) | **GET** /api/v1/sense/raw_output_file_by_registration_ticket/{registration_ticket_txid} | Get Raw Output File By Registration Ticket
[**sense_get_raw_output_file_by_result_id**](SenseApi.md#sense_get_raw_output_file_by_result_id) | **GET** /api/v1/sense/raw_output_file/{gateway_result_id} | Get Raw Output File By Result Id
[**sense_get_request_by_id**](SenseApi.md#sense_get_request_by_id) | **GET** /api/v1/sense/gateway_requests/{gateway_request_id} | Get Request By Request Id
[**sense_get_result_by_id**](SenseApi.md#sense_get_result_by_id) | **GET** /api/v1/sense/gateway_results/{gateway_result_id} | Get Result By Result Id
[**sense_submit_request**](SenseApi.md#sense_submit_request) | **POST** /api/v1/sense | Process Request
[**sense_transfer_pastel_ticket_to_another_pastelid**](SenseApi.md#sense_transfer_pastel_ticket_to_another_pastelid) | **GET** /api/v1/sense/result/transfer_pastel_ticket | Transfer Pastel Ticket To Another Pastelid


# **sense_get_all_parsed_output_files_from_request**
> object sense_get_all_parsed_output_files_from_request(gateway_request_id)

Get All Parsed Output Files From Request

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Parsed Output Files From Request
        api_response = await api_instance.sense_get_all_parsed_output_files_from_request(gateway_request_id)
        print("The response of SenseApi->sense_get_all_parsed_output_files_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_all_parsed_output_files_from_request: %s\n" % e)
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

# **sense_get_all_pastel_registration_tickets_from_request**
> object sense_get_all_pastel_registration_tickets_from_request(gateway_request_id)

Get All Pastel Sense Registration Tickets From Request

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Pastel Sense Registration Tickets From Request
        api_response = await api_instance.sense_get_all_pastel_registration_tickets_from_request(gateway_request_id)
        print("The response of SenseApi->sense_get_all_pastel_registration_tickets_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_all_pastel_registration_tickets_from_request: %s\n" % e)
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

# **sense_get_all_raw_output_files_from_request**
> object sense_get_all_raw_output_files_from_request(gateway_request_id)

Get All Raw Output Files From Request

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Raw Output Files From Request
        api_response = await api_instance.sense_get_all_raw_output_files_from_request(gateway_request_id)
        print("The response of SenseApi->sense_get_all_raw_output_files_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_all_raw_output_files_from_request: %s\n" % e)
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

# **sense_get_all_requests**
> List[RequestResult] sense_get_all_requests(status_requested=status_requested, offset=offset, limit=limit)

Get All Requests

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
    api_instance = gateway_client.SenseApi(api_client)
    status_requested = gateway_client.ReqStatus() # ReqStatus |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10000 # int |  (optional) (default to 10000)

    try:
        # Get All Requests
        api_response = await api_instance.sense_get_all_requests(status_requested=status_requested, offset=offset, limit=limit)
        print("The response of SenseApi->sense_get_all_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_all_requests: %s\n" % e)
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

# **sense_get_all_results**
> List[ResultRegistrationResult] sense_get_all_results(status_requested=status_requested, offset=offset, limit=limit)

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
    api_instance = gateway_client.SenseApi(api_client)
    status_requested = gateway_client.ReqStatus() # ReqStatus |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10000 # int |  (optional) (default to 10000)

    try:
        # Get All Results
        api_response = await api_instance.sense_get_all_results(status_requested=status_requested, offset=offset, limit=limit)
        print("The response of SenseApi->sense_get_all_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_all_results: %s\n" % e)
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

# **sense_get_originally_submitted_file_by_result_id**
> object sense_get_originally_submitted_file_by_result_id(gateway_result_id)

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Originally Submitted File By Result Id
        api_response = await api_instance.sense_get_originally_submitted_file_by_result_id(gateway_result_id)
        print("The response of SenseApi->sense_get_originally_submitted_file_by_result_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_originally_submitted_file_by_result_id: %s\n" % e)
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

# **sense_get_parsed_output_file_by_activation_ticket**
> object sense_get_parsed_output_file_by_activation_ticket(activation_ticket_txid)

Parsed Output File By Activation Ticket

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
    api_instance = gateway_client.SenseApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Parsed Output File By Activation Ticket
        api_response = await api_instance.sense_get_parsed_output_file_by_activation_ticket(activation_ticket_txid)
        print("The response of SenseApi->sense_get_parsed_output_file_by_activation_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_parsed_output_file_by_activation_ticket: %s\n" % e)
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

# **sense_get_parsed_output_file_by_pastel_id**
> object sense_get_parsed_output_file_by_pastel_id(pastel_id_of_user)

Parsed Output File By Pastel Id

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
    api_instance = gateway_client.SenseApi(api_client)
    pastel_id_of_user = 'pastel_id_of_user_example' # str | 

    try:
        # Parsed Output File By Pastel Id
        api_response = await api_instance.sense_get_parsed_output_file_by_pastel_id(pastel_id_of_user)
        print("The response of SenseApi->sense_get_parsed_output_file_by_pastel_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_parsed_output_file_by_pastel_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pastel_id_of_user** | **str**|  | 

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

# **sense_get_parsed_output_file_by_registration_ticket**
> object sense_get_parsed_output_file_by_registration_ticket(registration_ticket_txid)

Get Parsed Output File By Registration Ticket

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
    api_instance = gateway_client.SenseApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Parsed Output File By Registration Ticket
        api_response = await api_instance.sense_get_parsed_output_file_by_registration_ticket(registration_ticket_txid)
        print("The response of SenseApi->sense_get_parsed_output_file_by_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_parsed_output_file_by_registration_ticket: %s\n" % e)
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

# **sense_get_parsed_output_file_by_result_id**
> object sense_get_parsed_output_file_by_result_id(gateway_result_id)

Get Parsed Output File By Result Id

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Parsed Output File By Result Id
        api_response = await api_instance.sense_get_parsed_output_file_by_result_id(gateway_result_id)
        print("The response of SenseApi->sense_get_parsed_output_file_by_result_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_parsed_output_file_by_result_id: %s\n" % e)
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

# **sense_get_pastel_activation_ticket_by_its_txid**
> object sense_get_pastel_activation_ticket_by_its_txid(activation_ticket_txid)

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
    api_instance = gateway_client.SenseApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Pastel Activation Ticket By Its Txid
        api_response = await api_instance.sense_get_pastel_activation_ticket_by_its_txid(activation_ticket_txid)
        print("The response of SenseApi->sense_get_pastel_activation_ticket_by_its_txid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_pastel_activation_ticket_by_its_txid: %s\n" % e)
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

# **sense_get_pastel_activation_ticket_by_result_id**
> object sense_get_pastel_activation_ticket_by_result_id(gateway_result_id)

Get Pastel Sense Activation Ticket By Result Id

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Pastel Sense Activation Ticket By Result Id
        api_response = await api_instance.sense_get_pastel_activation_ticket_by_result_id(gateway_result_id)
        print("The response of SenseApi->sense_get_pastel_activation_ticket_by_result_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_pastel_activation_ticket_by_result_id: %s\n" % e)
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

# **sense_get_pastel_registration_ticket_by_its_txid**
> object sense_get_pastel_registration_ticket_by_its_txid(registration_ticket_txid)

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
    api_instance = gateway_client.SenseApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Pastel Registration Ticket By Its Txid
        api_response = await api_instance.sense_get_pastel_registration_ticket_by_its_txid(registration_ticket_txid)
        print("The response of SenseApi->sense_get_pastel_registration_ticket_by_its_txid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_pastel_registration_ticket_by_its_txid: %s\n" % e)
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

# **sense_get_pastel_registration_ticket_by_result_id**
> object sense_get_pastel_registration_ticket_by_result_id(gateway_result_id)

Get Pastel Sense Registration Ticket By Result Id

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Pastel Sense Registration Ticket By Result Id
        api_response = await api_instance.sense_get_pastel_registration_ticket_by_result_id(gateway_result_id)
        print("The response of SenseApi->sense_get_pastel_registration_ticket_by_result_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_pastel_registration_ticket_by_result_id: %s\n" % e)
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

# **sense_get_pastel_ticket_by_media_file_hash**
> object sense_get_pastel_ticket_by_media_file_hash(media_file_sha256_hash)

Get Pastel Ticket Data From Media File Hash

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
    api_instance = gateway_client.SenseApi(api_client)
    media_file_sha256_hash = 'media_file_sha256_hash_example' # str | 

    try:
        # Get Pastel Ticket Data From Media File Hash
        api_response = await api_instance.sense_get_pastel_ticket_by_media_file_hash(media_file_sha256_hash)
        print("The response of SenseApi->sense_get_pastel_ticket_by_media_file_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_pastel_ticket_by_media_file_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file_sha256_hash** | **str**|  | 

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

# **sense_get_raw_output_file_by_activation_ticket**
> object sense_get_raw_output_file_by_activation_ticket(activation_ticket_txid)

Get Raw Output File By Activation Ticket

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
    api_instance = gateway_client.SenseApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Raw Output File By Activation Ticket
        api_response = await api_instance.sense_get_raw_output_file_by_activation_ticket(activation_ticket_txid)
        print("The response of SenseApi->sense_get_raw_output_file_by_activation_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_raw_output_file_by_activation_ticket: %s\n" % e)
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

# **sense_get_raw_output_file_by_pastel_id**
> object sense_get_raw_output_file_by_pastel_id(pastel_id_of_user)

Get Raw Output File By Pastel Id

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
    api_instance = gateway_client.SenseApi(api_client)
    pastel_id_of_user = 'pastel_id_of_user_example' # str | 

    try:
        # Get Raw Output File By Pastel Id
        api_response = await api_instance.sense_get_raw_output_file_by_pastel_id(pastel_id_of_user)
        print("The response of SenseApi->sense_get_raw_output_file_by_pastel_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_raw_output_file_by_pastel_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pastel_id_of_user** | **str**|  | 

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

# **sense_get_raw_output_file_by_registration_ticket**
> object sense_get_raw_output_file_by_registration_ticket(registration_ticket_txid)

Get Raw Output File By Registration Ticket

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
    api_instance = gateway_client.SenseApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Raw Output File By Registration Ticket
        api_response = await api_instance.sense_get_raw_output_file_by_registration_ticket(registration_ticket_txid)
        print("The response of SenseApi->sense_get_raw_output_file_by_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_raw_output_file_by_registration_ticket: %s\n" % e)
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

# **sense_get_raw_output_file_by_result_id**
> object sense_get_raw_output_file_by_result_id(gateway_result_id)

Get Raw Output File By Result Id

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Raw Output File By Result Id
        api_response = await api_instance.sense_get_raw_output_file_by_result_id(gateway_result_id)
        print("The response of SenseApi->sense_get_raw_output_file_by_result_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_raw_output_file_by_result_id: %s\n" % e)
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

# **sense_get_request_by_id**
> RequestResult sense_get_request_by_id(gateway_request_id)

Get Request By Request Id

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get Request By Request Id
        api_response = await api_instance.sense_get_request_by_id(gateway_request_id)
        print("The response of SenseApi->sense_get_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_request_by_id: %s\n" % e)
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

# **sense_get_result_by_id**
> ResultRegistrationResult sense_get_result_by_id(gateway_result_id)

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Result By Result Id
        api_response = await api_instance.sense_get_result_by_id(gateway_result_id)
        print("The response of SenseApi->sense_get_result_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_get_result_by_id: %s\n" % e)
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

# **sense_submit_request**
> RequestResult sense_submit_request(files, collection_act_txid=collection_act_txid, open_api_group_id=open_api_group_id, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)

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
    api_instance = gateway_client.SenseApi(api_client)
    files = None # List[bytearray] | 
    collection_act_txid = 'collection_act_txid_example' # str | Transaction ID of the collection, if any (optional)
    open_api_group_id = 'open_api_group_id_example' # str | Group ID for the NFT, in most cases you don't need to change it (optional)
    after_activation_transfer_to_pastelid = 'after_activation_transfer_to_pastelid_example' # str | PastelID to transfer the NFT to after activation, if any (optional)

    try:
        # Process Request
        api_response = await api_instance.sense_submit_request(files, collection_act_txid=collection_act_txid, open_api_group_id=open_api_group_id, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)
        print("The response of SenseApi->sense_submit_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_submit_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 
 **collection_act_txid** | **str**| Transaction ID of the collection, if any | [optional] 
 **open_api_group_id** | **str**| Group ID for the NFT, in most cases you don&#39;t need to change it | [optional] 
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

# **sense_transfer_pastel_ticket_to_another_pastelid**
> object sense_transfer_pastel_ticket_to_another_pastelid(gateway_result_id, pastel_id)

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
    api_instance = gateway_client.SenseApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 
    pastel_id = 'pastel_id_example' # str | 

    try:
        # Transfer Pastel Ticket To Another Pastelid
        api_response = await api_instance.sense_transfer_pastel_ticket_to_another_pastelid(gateway_result_id, pastel_id)
        print("The response of SenseApi->sense_transfer_pastel_ticket_to_another_pastelid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenseApi->sense_transfer_pastel_ticket_to_another_pastelid: %s\n" % e)
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

