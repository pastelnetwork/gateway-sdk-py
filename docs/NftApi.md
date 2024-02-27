# gateway_client.NftApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nft_get_all_files_from_request**](NftApi.md#nft_get_all_files_from_request) | **GET** /api/v1/nft/all_files_from_request/{gateway_request_id} | Get All Files From Request
[**nft_get_all_parsed_dd_result_files_from_request**](NftApi.md#nft_get_all_parsed_dd_result_files_from_request) | **GET** /api/v1/nft/all_parsed_dd_result_files_from_request/{gateway_request_id} | Get All Parsed Dd Result Files From Request
[**nft_get_all_pastel_registration_tickets_from_request**](NftApi.md#nft_get_all_pastel_registration_tickets_from_request) | **GET** /api/v1/nft/pastel_registration_tickets/{gateway_request_id} | Get All Pastel Nft Registration Tickets From Request
[**nft_get_all_raw_dd_result_files_from_request**](NftApi.md#nft_get_all_raw_dd_result_files_from_request) | **GET** /api/v1/nft/all_raw_dd_result_files_from_request/{gateway_request_id} | Get All Raw Dd Result Files From Request
[**nft_get_all_requests**](NftApi.md#nft_get_all_requests) | **GET** /api/v1/nft/gateway_requests | Get All Requests
[**nft_get_all_results**](NftApi.md#nft_get_all_results) | **GET** /api/v1/nft/gateway_results | Get All Results
[**nft_get_originally_submitted_file_from_result_from_result**](NftApi.md#nft_get_originally_submitted_file_from_result_from_result) | **GET** /api/v1/nft/originally_submitted_file/{gateway_result_id} | Get Originally Submitted File By Result Id
[**nft_get_parsed_dd_result_file_from_activation_ticket**](NftApi.md#nft_get_parsed_dd_result_file_from_activation_ticket) | **GET** /api/v1/nft/parsed_dd_result_file_from_activation_ticket/{activation_ticket_txid} | Get Parsed Dd Result File By Activation Txid
[**nft_get_parsed_dd_result_file_from_pastel_id**](NftApi.md#nft_get_parsed_dd_result_file_from_pastel_id) | **GET** /api/v1/nft/parsed_dd_result_file_from_pastel_id/{pastel_id_of_user} | Get Parsed Dd Result File By Pastel Id
[**nft_get_parsed_dd_result_file_from_registration_ticket**](NftApi.md#nft_get_parsed_dd_result_file_from_registration_ticket) | **GET** /api/v1/nft/parsed_dd_result_file_from_registration_ticket/{registration_ticket_txid} | Get Parsed Dd Result File By Registration Ticket
[**nft_get_parsed_dd_result_file_from_result**](NftApi.md#nft_get_parsed_dd_result_file_from_result) | **GET** /api/v1/nft/parsed_dd_result_file/{gateway_result_id} | Get Parsed Dd Result File By Result Id
[**nft_get_pastel_activation_ticket_from_txid**](NftApi.md#nft_get_pastel_activation_ticket_from_txid) | **GET** /api/v1/nft/pastel_activation_ticket_from_txid/{activation_ticket_txid} | Get Pastel Activation Ticket By Its Txid
[**nft_get_pastel_activation_ticket_from_result**](NftApi.md#nft_get_pastel_activation_ticket_from_result) | **GET** /api/v1/nft/pastel_activation_ticket/{gateway_result_id} | Get Pastel Nft Activation Ticket By Result Id
[**nft_get_pastel_registration_ticket_from_txid**](NftApi.md#nft_get_pastel_registration_ticket_from_txid) | **GET** /api/v1/nft/pastel_registration_ticket_from_txid/{registration_ticket_txid} | Get Pastel Registration Ticket By Its Txid
[**nft_get_pastel_registration_ticket_from_result**](NftApi.md#nft_get_pastel_registration_ticket_from_result) | **GET** /api/v1/nft/pastel_registration_ticket/{gateway_result_id} | Get Pastel Nft Registration Ticket By Result Id
[**nft_get_pastel_registration_ticket_from_media_file_hash**](NftApi.md#nft_get_pastel_registration_ticket_from_media_file_hash) | **GET** /api/v1/nft/pastel_registration_ticket_from_media_file_hash/{media_file_sha256_hash} | Get Pastel Ticket Data From Media File Hash
[**nft_get_public_stored_file_from_registration_ticket**](NftApi.md#nft_get_public_stored_file_from_registration_ticket) | **GET** /api/v1/nft/public_stored_file_from_registration_ticket/{registration_ticket_txid} | Get Public Stored File By Registration Ticket
[**nft_get_raw_dd_result_file_from_activation_ticket**](NftApi.md#nft_get_raw_dd_result_file_from_activation_ticket) | **GET** /api/v1/nft/raw_dd_result_file_from_activation_ticket/{activation_ticket_txid} | Get Raw Dd Result File By Activation Ticket
[**nft_get_raw_dd_result_file_from_pastel_id**](NftApi.md#nft_get_raw_dd_result_file_from_pastel_id) | **GET** /api/v1/nft/raw_dd_result_file_from_pastel_id/{pastel_id_of_user} | Get Raw Dd Result File By Pastel Id
[**nft_get_raw_dd_result_file_from_registration_ticket**](NftApi.md#nft_get_raw_dd_result_file_from_registration_ticket) | **GET** /api/v1/nft/raw_dd_result_file_from_registration_ticket/{registration_ticket_txid} | Get Raw Dd Result File By Registration Ticket
[**nft_get_raw_dd_result_file_from_result**](NftApi.md#nft_get_raw_dd_result_file_from_result) | **GET** /api/v1/nft/raw_dd_result_file/{gateway_result_id} | Get Raw Dd Result File By Result Id
[**nft_get_request**](NftApi.md#nft_get_request) | **GET** /api/v1/nft/gateway_requests/{gateway_request_id} | Get Request By Request Id
[**nft_get_result**](NftApi.md#nft_get_result) | **GET** /api/v1/nft/gateway_results/{gateway_result_id} | Get Result By Result Id
[**nft_get_stored_file_from_activation_ticket**](NftApi.md#nft_get_stored_file_from_activation_ticket) | **GET** /api/v1/nft/stored_file_from_activation_ticket/{activation_ticket_txid} | Get Stored File By Activation Ticket
[**nft_get_stored_file_from_registration_ticket**](NftApi.md#nft_get_stored_file_from_registration_ticket) | **GET** /api/v1/nft/stored_file_from_registration_ticket/{registration_ticket_txid} | Get Stored File By Registration Ticket
[**nft_get_stored_file_from_result**](NftApi.md#nft_get_stored_file_from_result) | **GET** /api/v1/nft/stored_file/{gateway_result_id} | Get Stored File By Result Id
[**nft_process_request**](NftApi.md#nft_process_request) | **POST** /api/v1/nft | Process Request
[**nft_step1_upload_image_file**](NftApi.md#nft_step1_upload_image_file) | **POST** /api/v1/nft/step_1_upload_image_file | Step 1 Upload Image File
[**nft_step2_process_nft**](NftApi.md#nft_step2_process_nft) | **POST** /api/v1/nft/step_2_process_nft | Step 2 Process Nft
[**nft_transfer_pastel_ticket_to_another_pastelid**](NftApi.md#nft_transfer_pastel_ticket_to_another_pastelid) | **GET** /api/v1/nft/result/transfer_pastel_ticket | Transfer Pastel Ticket To Another Pastelid


# **nft_get_all_files_from_request**
> object nft_get_all_files_from_request(gateway_request_id)

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Files From Request
        api_response = await api_instance.nft_get_all_files_from_request(gateway_request_id)
        print("The response of NftApi->nft_get_all_files_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_all_files_from_request: %s\n" % e)
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

# **nft_get_all_parsed_dd_result_files_from_request**
> object nft_get_all_parsed_dd_result_files_from_request(gateway_request_id)

Get All Parsed Dd Result Files From Request

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Parsed Dd Result Files From Request
        api_response = await api_instance.nft_get_all_parsed_dd_result_files_from_request(gateway_request_id)
        print("The response of NftApi->nft_get_all_parsed_dd_result_files_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_all_parsed_dd_result_files_from_request: %s\n" % e)
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

# **nft_get_all_pastel_registration_tickets_from_request**
> object nft_get_all_pastel_registration_tickets_from_request(gateway_request_id)

Get All Pastel Nft Registration Tickets From Request

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Pastel Nft Registration Tickets From Request
        api_response = await api_instance.nft_get_all_pastel_registration_tickets_from_request(gateway_request_id)
        print("The response of NftApi->nft_get_all_pastel_registration_tickets_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_all_pastel_registration_tickets_from_request: %s\n" % e)
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

# **nft_get_all_raw_dd_result_files_from_request**
> object nft_get_all_raw_dd_result_files_from_request(gateway_request_id)

Get All Raw Dd Result Files From Request

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get All Raw Dd Result Files From Request
        api_response = await api_instance.nft_get_all_raw_dd_result_files_from_request(gateway_request_id)
        print("The response of NftApi->nft_get_all_raw_dd_result_files_from_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_all_raw_dd_result_files_from_request: %s\n" % e)
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

# **nft_get_all_requests**
> List[RequestResult] nft_get_all_requests(status_requested=status_requested, offset=offset, limit=limit)

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
    api_instance = gateway_client.NftApi(api_client)
    status_requested = gateway_client.ReqStatus() # ReqStatus |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10000 # int |  (optional) (default to 10000)

    try:
        # Get All Requests
        api_response = await api_instance.nft_get_all_requests(status_requested=status_requested, offset=offset, limit=limit)
        print("The response of NftApi->nft_get_all_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_all_requests: %s\n" % e)
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

# **nft_get_all_results**
> List[ResultRegistrationResult] nft_get_all_results(status_requested=status_requested, offset=offset, limit=limit)

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
    api_instance = gateway_client.NftApi(api_client)
    status_requested = gateway_client.ReqStatus() # ReqStatus |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10000 # int |  (optional) (default to 10000)

    try:
        # Get All Results
        api_response = await api_instance.nft_get_all_results(status_requested=status_requested, offset=offset, limit=limit)
        print("The response of NftApi->nft_get_all_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_all_results: %s\n" % e)
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

# **nft_get_originally_submitted_file_from_result_from_result**
> object nft_get_originally_submitted_file_from_result_from_result(gateway_result_id)

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Originally Submitted File By Result Id
        api_response = await api_instance.nft_get_originally_submitted_file_from_result_from_result(gateway_result_id)
        print("The response of NftApi->nft_get_originally_submitted_file_from_result_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_originally_submitted_file_from_result_from_result: %s\n" % e)
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

# **nft_get_parsed_dd_result_file_from_activation_ticket**
> object nft_get_parsed_dd_result_file_from_activation_ticket(activation_ticket_txid)

Get Parsed Dd Result File By Activation Txid

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
    api_instance = gateway_client.NftApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Parsed Dd Result File By Activation Txid
        api_response = await api_instance.nft_get_parsed_dd_result_file_from_activation_ticket(activation_ticket_txid)
        print("The response of NftApi->nft_get_parsed_dd_result_file_from_activation_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_parsed_dd_result_file_from_activation_ticket: %s\n" % e)
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

# **nft_get_parsed_dd_result_file_from_pastel_id**
> object nft_get_parsed_dd_result_file_from_pastel_id(pastel_id_of_user)

Get Parsed Dd Result File By Pastel Id

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
    api_instance = gateway_client.NftApi(api_client)
    pastel_id_of_user = 'pastel_id_of_user_example' # str | 

    try:
        # Get Parsed Dd Result File By Pastel Id
        api_response = await api_instance.nft_get_parsed_dd_result_file_from_pastel_id(pastel_id_of_user)
        print("The response of NftApi->nft_get_parsed_dd_result_file_from_pastel_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_parsed_dd_result_file_from_pastel_id: %s\n" % e)
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

# **nft_get_parsed_dd_result_file_from_registration_ticket**
> object nft_get_parsed_dd_result_file_from_registration_ticket(registration_ticket_txid)

Get Parsed Dd Result File By Registration Ticket

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
    api_instance = gateway_client.NftApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Parsed Dd Result File By Registration Ticket
        api_response = await api_instance.nft_get_parsed_dd_result_file_from_registration_ticket(registration_ticket_txid)
        print("The response of NftApi->nft_get_parsed_dd_result_file_from_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_parsed_dd_result_file_from_registration_ticket: %s\n" % e)
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

# **nft_get_parsed_dd_result_file_from_result**
> object nft_get_parsed_dd_result_file_from_result(gateway_result_id)

Get Parsed Dd Result File By Result Id

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Parsed Dd Result File By Result Id
        api_response = await api_instance.nft_get_parsed_dd_result_file_from_result(gateway_result_id)
        print("The response of NftApi->nft_get_parsed_dd_result_file_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_parsed_dd_result_file_from_result: %s\n" % e)
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

# **nft_get_pastel_activation_ticket_from_txid**
> object nft_get_pastel_activation_ticket_from_txid(activation_ticket_txid)

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
    api_instance = gateway_client.NftApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Pastel Activation Ticket By Its Txid
        api_response = await api_instance.nft_get_pastel_activation_ticket_from_txid(activation_ticket_txid)
        print("The response of NftApi->nft_get_pastel_activation_ticket_from_txid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_pastel_activation_ticket_from_txid: %s\n" % e)
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

# **nft_get_pastel_activation_ticket_from_result**
> object nft_get_pastel_activation_ticket_from_result(gateway_result_id)

Get Pastel Nft Activation Ticket By Result Id

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Pastel Nft Activation Ticket By Result Id
        api_response = await api_instance.nft_get_pastel_activation_ticket_from_result(gateway_result_id)
        print("The response of NftApi->nft_get_pastel_activation_ticket_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_pastel_activation_ticket_from_result: %s\n" % e)
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

# **nft_get_pastel_registration_ticket_from_txid**
> object nft_get_pastel_registration_ticket_from_txid(registration_ticket_txid)

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
    api_instance = gateway_client.NftApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Pastel Registration Ticket By Its Txid
        api_response = await api_instance.nft_get_pastel_registration_ticket_from_txid(registration_ticket_txid)
        print("The response of NftApi->nft_get_pastel_registration_ticket_from_txid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_pastel_registration_ticket_from_txid: %s\n" % e)
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

# **nft_get_pastel_registration_ticket_from_result**
> object nft_get_pastel_registration_ticket_from_result(gateway_result_id)

Get Pastel Nft Registration Ticket By Result Id

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Pastel Nft Registration Ticket By Result Id
        api_response = await api_instance.nft_get_pastel_registration_ticket_from_result(gateway_result_id)
        print("The response of NftApi->nft_get_pastel_registration_ticket_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_pastel_registration_ticket_from_result: %s\n" % e)
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

# **nft_get_pastel_registration_ticket_from_media_file_hash**
> object nft_get_pastel_registration_ticket_from_media_file_hash(media_file_sha256_hash)

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
    api_instance = gateway_client.NftApi(api_client)
    media_file_sha256_hash = 'media_file_sha256_hash_example' # str | 

    try:
        # Get Pastel Ticket Data From Media File Hash
        api_response = await api_instance.nft_get_pastel_registration_ticket_from_media_file_hash(media_file_sha256_hash)
        print("The response of NftApi->nft_get_pastel_registration_ticket_from_media_file_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_pastel_registration_ticket_from_media_file_hash: %s\n" % e)
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

# **nft_get_public_stored_file_from_registration_ticket**
> object nft_get_public_stored_file_from_registration_ticket(registration_ticket_txid)

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
    api_instance = gateway_client.NftApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Public Stored File By Registration Ticket
        api_response = await api_instance.nft_get_public_stored_file_from_registration_ticket(registration_ticket_txid)
        print("The response of NftApi->nft_get_public_stored_file_from_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_public_stored_file_from_registration_ticket: %s\n" % e)
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

# **nft_get_raw_dd_result_file_from_activation_ticket**
> object nft_get_raw_dd_result_file_from_activation_ticket(activation_ticket_txid)

Get Raw Dd Result File By Activation Ticket

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
    api_instance = gateway_client.NftApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Raw Dd Result File By Activation Ticket
        api_response = await api_instance.nft_get_raw_dd_result_file_from_activation_ticket(activation_ticket_txid)
        print("The response of NftApi->nft_get_raw_dd_result_file_from_activation_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_raw_dd_result_file_from_activation_ticket: %s\n" % e)
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

# **nft_get_raw_dd_result_file_from_pastel_id**
> object nft_get_raw_dd_result_file_from_pastel_id(pastel_id_of_user)

Get Raw Dd Result File By Pastel Id

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
    api_instance = gateway_client.NftApi(api_client)
    pastel_id_of_user = 'pastel_id_of_user_example' # str | 

    try:
        # Get Raw Dd Result File By Pastel Id
        api_response = await api_instance.nft_get_raw_dd_result_file_from_pastel_id(pastel_id_of_user)
        print("The response of NftApi->nft_get_raw_dd_result_file_from_pastel_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_raw_dd_result_file_from_pastel_id: %s\n" % e)
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

# **nft_get_raw_dd_result_file_from_registration_ticket**
> object nft_get_raw_dd_result_file_from_registration_ticket(registration_ticket_txid)

Get Raw Dd Result File By Registration Ticket

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
    api_instance = gateway_client.NftApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Raw Dd Result File By Registration Ticket
        api_response = await api_instance.nft_get_raw_dd_result_file_from_registration_ticket(registration_ticket_txid)
        print("The response of NftApi->nft_get_raw_dd_result_file_from_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_raw_dd_result_file_from_registration_ticket: %s\n" % e)
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

# **nft_get_raw_dd_result_file_from_result**
> object nft_get_raw_dd_result_file_from_result(gateway_result_id)

Get Raw Dd Result File By Result Id

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Raw Dd Result File By Result Id
        api_response = await api_instance.nft_get_raw_dd_result_file_from_result(gateway_result_id)
        print("The response of NftApi->nft_get_raw_dd_result_file_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_raw_dd_result_file_from_result: %s\n" % e)
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

# **nft_get_request**
> RequestResult nft_get_request(gateway_request_id)

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_request_id = 'gateway_request_id_example' # str | 

    try:
        # Get Request By Request Id
        api_response = await api_instance.nft_get_request(gateway_request_id)
        print("The response of NftApi->nft_get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_request: %s\n" % e)
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

# **nft_get_result**
> ResultRegistrationResult nft_get_result(gateway_result_id)

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Result By Result Id
        api_response = await api_instance.nft_get_result(gateway_result_id)
        print("The response of NftApi->nft_get_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_result: %s\n" % e)
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

# **nft_get_stored_file_from_activation_ticket**
> object nft_get_stored_file_from_activation_ticket(activation_ticket_txid)

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
    api_instance = gateway_client.NftApi(api_client)
    activation_ticket_txid = 'activation_ticket_txid_example' # str | 

    try:
        # Get Stored File By Activation Ticket
        api_response = await api_instance.nft_get_stored_file_from_activation_ticket(activation_ticket_txid)
        print("The response of NftApi->nft_get_stored_file_from_activation_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_stored_file_from_activation_ticket: %s\n" % e)
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

# **nft_get_stored_file_from_registration_ticket**
> object nft_get_stored_file_from_registration_ticket(registration_ticket_txid)

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
    api_instance = gateway_client.NftApi(api_client)
    registration_ticket_txid = 'registration_ticket_txid_example' # str | 

    try:
        # Get Stored File By Registration Ticket
        api_response = await api_instance.nft_get_stored_file_from_registration_ticket(registration_ticket_txid)
        print("The response of NftApi->nft_get_stored_file_from_registration_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_stored_file_from_registration_ticket: %s\n" % e)
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

# **nft_get_stored_file_from_result**
> object nft_get_stored_file_from_result(gateway_result_id)

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 

    try:
        # Get Stored File By Result Id
        api_response = await api_instance.nft_get_stored_file_from_result(gateway_result_id)
        print("The response of NftApi->nft_get_stored_file_from_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_get_stored_file_from_result: %s\n" % e)
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

# **nft_process_request**
> RequestResult nft_process_request(file, nft_details_payload, make_publicly_accessible=make_publicly_accessible, collection_act_txid=collection_act_txid, open_api_group_id=open_api_group_id, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)

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
    api_instance = gateway_client.NftApi(api_client)
    file = None # bytearray | 
    nft_details_payload = 'nft_details_payload_example' # str | 
    make_publicly_accessible = True # bool | Make the file publicly accessible (optional) (default to True)
    collection_act_txid = 'collection_act_txid_example' # str | Transaction ID of the collection, if any (optional)
    open_api_group_id = 'open_api_group_id_example' # str | Group ID for the NFT, in most cases you don't need to change it (optional)
    after_activation_transfer_to_pastelid = 'after_activation_transfer_to_pastelid_example' # str | PastelID to transfer the NFT to after activation, if any (optional)

    try:
        # Process Request
        api_response = await api_instance.nft_process_request(file, nft_details_payload, make_publicly_accessible=make_publicly_accessible, collection_act_txid=collection_act_txid, open_api_group_id=open_api_group_id, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)
        print("The response of NftApi->nft_process_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_process_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **nft_details_payload** | **str**|  | 
 **make_publicly_accessible** | **bool**| Make the file publicly accessible | [optional] [default to True]
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

# **nft_step1_upload_image_file**
> ResultRegistrationResult nft_step1_upload_image_file(file)

Step 1 Upload Image File

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
    api_instance = gateway_client.NftApi(api_client)
    file = None # bytearray | 

    try:
        # Step 1 Upload Image File
        api_response = await api_instance.nft_step1_upload_image_file(file)
        print("The response of NftApi->nft_step1_upload_image_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_step1_upload_image_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

[**ResultRegistrationResult**](ResultRegistrationResult.md)

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

# **nft_step2_process_nft**
> RequestResult nft_step2_process_nft(nft_properties_external, file_id=file_id, make_publicly_accessible=make_publicly_accessible, collection_act_txid=collection_act_txid, open_api_group_id=open_api_group_id, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)

Step 2 Process Nft

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.nft_properties_external import NftPropertiesExternal
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
    api_instance = gateway_client.NftApi(api_client)
    nft_properties_external = gateway_client.NftPropertiesExternal() # NftPropertiesExternal | 
    file_id = 'file_id' # str | File ID from the upload endpoint (optional) (default to 'file_id')
    make_publicly_accessible = True # bool | Make the file publicly accessible (optional) (default to True)
    collection_act_txid = 'collection_act_txid_example' # str | Transaction ID of the collection, if any (optional)
    open_api_group_id = 'open_api_group_id_example' # str | Group ID for the NFT, in most cases you don't need to change it (optional)
    after_activation_transfer_to_pastelid = 'after_activation_transfer_to_pastelid_example' # str | PastelID to transfer the NFT to after activation, if any (optional)

    try:
        # Step 2 Process Nft
        api_response = await api_instance.nft_step2_process_nft(nft_properties_external, file_id=file_id, make_publicly_accessible=make_publicly_accessible, collection_act_txid=collection_act_txid, open_api_group_id=open_api_group_id, after_activation_transfer_to_pastelid=after_activation_transfer_to_pastelid)
        print("The response of NftApi->nft_step2_process_nft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_step2_process_nft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nft_properties_external** | [**NftPropertiesExternal**](NftPropertiesExternal.md)|  | 
 **file_id** | **str**| File ID from the upload endpoint | [optional] [default to &#39;file_id&#39;]
 **make_publicly_accessible** | **bool**| Make the file publicly accessible | [optional] [default to True]
 **collection_act_txid** | **str**| Transaction ID of the collection, if any | [optional] 
 **open_api_group_id** | **str**| Group ID for the NFT, in most cases you don&#39;t need to change it | [optional] 
 **after_activation_transfer_to_pastelid** | **str**| PastelID to transfer the NFT to after activation, if any | [optional] 

### Return type

[**RequestResult**](RequestResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nft_transfer_pastel_ticket_to_another_pastelid**
> object nft_transfer_pastel_ticket_to_another_pastelid(gateway_result_id, pastel_id)

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
    api_instance = gateway_client.NftApi(api_client)
    gateway_result_id = 'gateway_result_id_example' # str | 
    pastel_id = 'pastel_id_example' # str | 

    try:
        # Transfer Pastel Ticket To Another Pastelid
        api_response = await api_instance.nft_transfer_pastel_ticket_to_another_pastelid(gateway_result_id, pastel_id)
        print("The response of NftApi->nft_transfer_pastel_ticket_to_another_pastelid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->nft_transfer_pastel_ticket_to_another_pastelid: %s\n" % e)
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

