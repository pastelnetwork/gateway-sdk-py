# gateway_client.LoginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_access_token**](LoginApi.md#login_access_token) | **POST** /api/v1/login/access-token | Login Access Token
[**login_password_recovery**](LoginApi.md#login_password_recovery) | **POST** /api/v1/password-recovery/{email} | Recover Password
[**login_reset_password**](LoginApi.md#login_reset_password) | **POST** /api/v1/reset-password/ | Reset Password
[**login_test_token**](LoginApi.md#login_test_token) | **POST** /api/v1/login/test-token | Test Token


# **login_access_token**
> Token login_access_token(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login Access Token

OAuth2 compatible token login, get an access token for future requests

### Example


```python
import time
import os
import gateway_client
from gateway_client.models.token import Token
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
    api_instance = gateway_client.LoginApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login Access Token
        api_response = await api_instance.login_access_token(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of LoginApi->login_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_password_recovery**
> Msg login_password_recovery(email)

Recover Password

Password Recovery

### Example


```python
import time
import os
import gateway_client
from gateway_client.models.msg import Msg
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
    api_instance = gateway_client.LoginApi(api_client)
    email = 'email_example' # str | 

    try:
        # Recover Password
        api_response = await api_instance.login_password_recovery(email)
        print("The response of LoginApi->login_password_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_password_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**Msg**](Msg.md)

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

# **login_reset_password**
> Msg login_reset_password(body_login_reset_password)

Reset Password

Reset password

### Example


```python
import time
import os
import gateway_client
from gateway_client.models.body_login_reset_password import BodyLoginResetPassword
from gateway_client.models.msg import Msg
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
    api_instance = gateway_client.LoginApi(api_client)
    body_login_reset_password = gateway_client.BodyLoginResetPassword() # BodyLoginResetPassword | 

    try:
        # Reset Password
        api_response = await api_instance.login_reset_password(body_login_reset_password)
        print("The response of LoginApi->login_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_login_reset_password** | [**BodyLoginResetPassword**](BodyLoginResetPassword.md)|  | 

### Return type

[**Msg**](Msg.md)

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

# **login_test_token**
> User login_test_token()

Test Token

Test access token

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import os
import gateway_client
from gateway_client.models.user import User
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
    api_instance = gateway_client.LoginApi(api_client)

    try:
        # Test Token
        api_response = await api_instance.login_test_token()
        print("The response of LoginApi->login_test_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_test_token: %s\n" % e)
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

