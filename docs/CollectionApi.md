# gateway_client.CollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_create_nft_collection**](CollectionApi.md#collection_create_nft_collection) | **POST** /api/v1/collection/nft | Create Nft Collection
[**collection_create_sense_collection**](CollectionApi.md#collection_create_sense_collection) | **POST** /api/v1/collection/sense | Create Sense Collection
[**collection_get_all_nft_collections**](CollectionApi.md#collection_get_all_nft_collections) | **GET** /api/v1/collection/nft/collections | Get All Nft Collections
[**collection_get_all_sense_collections**](CollectionApi.md#collection_get_all_sense_collections) | **GET** /api/v1/collection/sense/collections | Get All Sense Collections
[**collection_get_nft_collections_from_collection_id**](CollectionApi.md#collection_get_nft_collections_from_collection_id) | **GET** /api/v1/collection/nft/collections/{collection_id} | Get Nft Collections By Collection Id
[**collection_get_sense_collections_from_collection_id**](CollectionApi.md#collection_get_sense_collections_from_collection_id) | **GET** /api/v1/collection/sense/collections/{collection_id} | Get Sense Collections By Collection Id


# **collection_create_nft_collection**
> CollectionRegistrationResult collection_create_nft_collection(collection_name=collection_name, max_collection_entries=max_collection_entries, collection_item_copy_count=collection_item_copy_count, list_of_pastelids_of_authorized_contributors=list_of_pastelids_of_authorized_contributors, max_permitted_open_nsfw_score=max_permitted_open_nsfw_score, minimum_similarity_score_to_first_entry_in_collection=minimum_similarity_score_to_first_entry_in_collection, no_of_days_to_finalize_collection=no_of_days_to_finalize_collection, royalty=royalty, green=green)

Create Nft Collection

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.collection_registration_result import CollectionRegistrationResult
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
    api_instance = gateway_client.CollectionApi(api_client)
    collection_name = '' # str | Collection name (optional) (default to '')
    max_collection_entries = 1 # int | Maximum number of items allowed in a collection (optional) (default to 1)
    collection_item_copy_count = 1 # int | Allowed number of copies for all items in a collection (optional) (default to 1)
    list_of_pastelids_of_authorized_contributors = [] # List[str] | List of pastelids of authorized contributors (optional) (default to [])
    max_permitted_open_nsfw_score = 0.0 # float | Maximum permitted open NSFW score. Where: 0.0 means - 0% chance of NSFW content. 1.0 means - 100% chance of NSFW content (optional) (default to 0.0)
    minimum_similarity_score_to_first_entry_in_collection = 0.0 # float | Minimum similarity score to first entry in collection. Where: 0.0 means - 0% similarity. And 1.0 means - 100% similarity (optional) (default to 0.0)
    no_of_days_to_finalize_collection = 0 # int | Number of days to finalize collection (optional) (default to 0)
    royalty = 0.0 # float | Royalty percentage (optional) (default to 0.0)
    green = False # bool | Green (optional) (default to False)

    try:
        # Create Nft Collection
        api_response = await api_instance.collection_create_nft_collection(collection_name=collection_name, max_collection_entries=max_collection_entries, collection_item_copy_count=collection_item_copy_count, list_of_pastelids_of_authorized_contributors=list_of_pastelids_of_authorized_contributors, max_permitted_open_nsfw_score=max_permitted_open_nsfw_score, minimum_similarity_score_to_first_entry_in_collection=minimum_similarity_score_to_first_entry_in_collection, no_of_days_to_finalize_collection=no_of_days_to_finalize_collection, royalty=royalty, green=green)
        print("The response of CollectionApi->collection_create_nft_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collection_create_nft_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Collection name | [optional] [default to &#39;&#39;]
 **max_collection_entries** | **int**| Maximum number of items allowed in a collection | [optional] [default to 1]
 **collection_item_copy_count** | **int**| Allowed number of copies for all items in a collection | [optional] [default to 1]
 **list_of_pastelids_of_authorized_contributors** | [**List[str]**](str.md)| List of pastelids of authorized contributors | [optional] [default to []]
 **max_permitted_open_nsfw_score** | **float**| Maximum permitted open NSFW score. Where: 0.0 means - 0% chance of NSFW content. 1.0 means - 100% chance of NSFW content | [optional] [default to 0.0]
 **minimum_similarity_score_to_first_entry_in_collection** | **float**| Minimum similarity score to first entry in collection. Where: 0.0 means - 0% similarity. And 1.0 means - 100% similarity | [optional] [default to 0.0]
 **no_of_days_to_finalize_collection** | **int**| Number of days to finalize collection | [optional] [default to 0]
 **royalty** | **float**| Royalty percentage | [optional] [default to 0.0]
 **green** | **bool**| Green | [optional] [default to False]

### Return type

[**CollectionRegistrationResult**](CollectionRegistrationResult.md)

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

# **collection_create_sense_collection**
> CollectionRegistrationResult collection_create_sense_collection(collection_name=collection_name, max_collection_entries=max_collection_entries, collection_item_copy_count=collection_item_copy_count, list_of_pastelids_of_authorized_contributors=list_of_pastelids_of_authorized_contributors, max_permitted_open_nsfw_score=max_permitted_open_nsfw_score, minimum_similarity_score_to_first_entry_in_collection=minimum_similarity_score_to_first_entry_in_collection, no_of_days_to_finalize_collection=no_of_days_to_finalize_collection, royalty=royalty, green=green)

Create Sense Collection

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.collection_registration_result import CollectionRegistrationResult
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
    api_instance = gateway_client.CollectionApi(api_client)
    collection_name = '' # str | Collection name (optional) (default to '')
    max_collection_entries = 1 # int | Maximum number of items allowed in a collection (optional) (default to 1)
    collection_item_copy_count = 1 # int | Allowed number of copies for all items in a collection (optional) (default to 1)
    list_of_pastelids_of_authorized_contributors = [""] # List[str] | List of pastelids of authorized contributors (optional) (default to [""])
    max_permitted_open_nsfw_score = 0.0 # float | Maximum permitted open NSFW score (optional) (default to 0.0)
    minimum_similarity_score_to_first_entry_in_collection = 0.0 # float | Minimum similarity score to first entry in collection (optional) (default to 0.0)
    no_of_days_to_finalize_collection = 0 # int | Number of days to finalize collection (optional) (default to 0)
    royalty = 0.0 # float | Royalty percentage (optional) (default to 0.0)
    green = False # bool | Green (optional) (default to False)

    try:
        # Create Sense Collection
        api_response = await api_instance.collection_create_sense_collection(collection_name=collection_name, max_collection_entries=max_collection_entries, collection_item_copy_count=collection_item_copy_count, list_of_pastelids_of_authorized_contributors=list_of_pastelids_of_authorized_contributors, max_permitted_open_nsfw_score=max_permitted_open_nsfw_score, minimum_similarity_score_to_first_entry_in_collection=minimum_similarity_score_to_first_entry_in_collection, no_of_days_to_finalize_collection=no_of_days_to_finalize_collection, royalty=royalty, green=green)
        print("The response of CollectionApi->collection_create_sense_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collection_create_sense_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Collection name | [optional] [default to &#39;&#39;]
 **max_collection_entries** | **int**| Maximum number of items allowed in a collection | [optional] [default to 1]
 **collection_item_copy_count** | **int**| Allowed number of copies for all items in a collection | [optional] [default to 1]
 **list_of_pastelids_of_authorized_contributors** | [**List[str]**](str.md)| List of pastelids of authorized contributors | [optional] [default to [&quot;&quot;]]
 **max_permitted_open_nsfw_score** | **float**| Maximum permitted open NSFW score | [optional] [default to 0.0]
 **minimum_similarity_score_to_first_entry_in_collection** | **float**| Minimum similarity score to first entry in collection | [optional] [default to 0.0]
 **no_of_days_to_finalize_collection** | **int**| Number of days to finalize collection | [optional] [default to 0]
 **royalty** | **float**| Royalty percentage | [optional] [default to 0.0]
 **green** | **bool**| Green | [optional] [default to False]

### Return type

[**CollectionRegistrationResult**](CollectionRegistrationResult.md)

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

# **collection_get_all_nft_collections**
> List[CollectionRegistrationResult] collection_get_all_nft_collections()

Get All Nft Collections

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.collection_registration_result import CollectionRegistrationResult
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
    api_instance = gateway_client.CollectionApi(api_client)

    try:
        # Get All Nft Collections
        api_response = await api_instance.collection_get_all_nft_collections()
        print("The response of CollectionApi->collection_get_all_nft_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collection_get_all_nft_collections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CollectionRegistrationResult]**](CollectionRegistrationResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_get_all_sense_collections**
> List[CollectionRegistrationResult] collection_get_all_sense_collections()

Get All Sense Collections

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.collection_registration_result import CollectionRegistrationResult
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
    api_instance = gateway_client.CollectionApi(api_client)

    try:
        # Get All Sense Collections
        api_response = await api_instance.collection_get_all_sense_collections()
        print("The response of CollectionApi->collection_get_all_sense_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collection_get_all_sense_collections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CollectionRegistrationResult]**](CollectionRegistrationResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_get_nft_collections_from_collection_id**
> CollectionRegistrationResult collection_get_nft_collections_from_collection_id(collection_id)

Get Nft Collections By Collection Id

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.collection_registration_result import CollectionRegistrationResult
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
    api_instance = gateway_client.CollectionApi(api_client)
    collection_id = 'collection_id_example' # str | 

    try:
        # Get Nft Collections By Collection Id
        api_response = await api_instance.collection_get_nft_collections_from_collection_id(collection_id)
        print("The response of CollectionApi->collection_get_nft_collections_from_collection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collection_get_nft_collections_from_collection_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 

### Return type

[**CollectionRegistrationResult**](CollectionRegistrationResult.md)

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

# **collection_get_sense_collections_from_collection_id**
> CollectionRegistrationResult collection_get_sense_collections_from_collection_id(collection_id)

Get Sense Collections By Collection Id

### Example

* Api Key Authentication (APIKeyHeader):

```python
import time
import os
import gateway_client
from gateway_client.models.collection_registration_result import CollectionRegistrationResult
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
    api_instance = gateway_client.CollectionApi(api_client)
    collection_id = 'collection_id_example' # str | 

    try:
        # Get Sense Collections By Collection Id
        api_response = await api_instance.collection_get_sense_collections_from_collection_id(collection_id)
        print("The response of CollectionApi->collection_get_sense_collections_from_collection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collection_get_sense_collections_from_collection_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 

### Return type

[**CollectionRegistrationResult**](CollectionRegistrationResult.md)

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

