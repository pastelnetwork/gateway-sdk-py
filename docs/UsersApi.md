# pastel_gateway_sdk.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create_user**](UsersApi.md#users_create_user) | **POST** /api/v1/users | Create User
[**users_create_user_open**](UsersApi.md#users_create_user_open) | **POST** /api/v1/users/open | Create User Open
[**users_delete_user**](UsersApi.md#users_delete_user) | **DELETE** /api/v1/users/{user_id} | Delete Apikey
[**users_read_user_by_id**](UsersApi.md#users_read_user_by_id) | **GET** /api/v1/users/{user_id} | Read User By Id
[**users_read_user_me**](UsersApi.md#users_read_user_me) | **GET** /api/v1/users/me | Read User Me
[**users_read_users**](UsersApi.md#users_read_users) | **GET** /api/v1/users | Read Users
[**users_update_user**](UsersApi.md#users_update_user) | **PUT** /api/v1/users/{user_id} | Update User
[**users_update_user_me**](UsersApi.md#users_update_user_me) | **PUT** /api/v1/users/me | Update User Me


# **users_create_user**
> User users_create_user(user_create)

Create User

Create new user, returns user object with funding address. limit=0 means no limit

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user import User
from pastel_gateway_sdk.models.user_create import UserCreate
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    user_create = pastel_gateway_sdk.UserCreate() # UserCreate | 

    try:
        # Create User
        api_response = await api_instance.users_create_user(user_create)
        print("The response of UsersApi->users_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**User**](User.md)

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

# **users_create_user_open**
> User users_create_user_open(body_users_create_user_open)

Create User Open

Create new user without the need to be logged in.

### Example


```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.body_users_create_user_open import BodyUsersCreateUserOpen
from pastel_gateway_sdk.models.user import User
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    body_users_create_user_open = pastel_gateway_sdk.BodyUsersCreateUserOpen() # BodyUsersCreateUserOpen | 

    try:
        # Create User Open
        api_response = await api_instance.users_create_user_open(body_users_create_user_open)
        print("The response of UsersApi->users_create_user_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_user_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_users_create_user_open** | [**BodyUsersCreateUserOpen**](BodyUsersCreateUserOpen.md)|  | 

### Return type

[**User**](User.md)

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

# **users_delete_user**
> User users_delete_user(user_id)

Delete Apikey

Delete user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user import User
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Delete Apikey
        api_response = await api_instance.users_delete_user(user_id)
        print("The response of UsersApi->users_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**User**](User.md)

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

# **users_read_user_by_id**
> User users_read_user_by_id(user_id)

Read User By Id

Get a specific user by id.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user import User
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Read User By Id
        api_response = await api_instance.users_read_user_by_id(user_id)
        print("The response of UsersApi->users_read_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_read_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**User**](User.md)

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

# **users_read_user_me**
> User users_read_user_me()

Read User Me

Get current user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user import User
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)

    try:
        # Read User Me
        api_response = await api_instance.users_read_user_me()
        print("The response of UsersApi->users_read_user_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_read_user_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **users_read_users**
> List[User] users_read_users(skip=skip, limit=limit)

Read Users

Retrieve users.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user import User
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Read Users
        api_response = await api_instance.users_read_users(skip=skip, limit=limit)
        print("The response of UsersApi->users_read_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_read_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[User]**](User.md)

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

# **users_update_user**
> User users_update_user(user_id, user_update)

Update User

Update a user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.user import User
from pastel_gateway_sdk.models.user_update import UserUpdate
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    user_id = 56 # int | 
    user_update = pastel_gateway_sdk.UserUpdate() # UserUpdate | 

    try:
        # Update User
        api_response = await api_instance.users_update_user(user_id, user_update)
        print("The response of UsersApi->users_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**User**](User.md)

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

# **users_update_user_me**
> User users_update_user_me(body_users_update_user_me=body_users_update_user_me)

Update User Me

Update own user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import pastel_gateway_sdk
from pastel_gateway_sdk.models.body_users_update_user_me import BodyUsersUpdateUserMe
from pastel_gateway_sdk.models.user import User
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
    api_instance = pastel_gateway_sdk.UsersApi(api_client)
    body_users_update_user_me = pastel_gateway_sdk.BodyUsersUpdateUserMe() # BodyUsersUpdateUserMe |  (optional)

    try:
        # Update User Me
        api_response = await api_instance.users_update_user_me(body_users_update_user_me=body_users_update_user_me)
        print("The response of UsersApi->users_update_user_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_user_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_users_update_user_me** | [**BodyUsersUpdateUserMe**](BodyUsersUpdateUserMe.md)|  | [optional] 

### Return type

[**User**](User.md)

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

