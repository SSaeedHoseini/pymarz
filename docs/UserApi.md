# pymarz.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UserApi.md#add_user) | **POST** /api/user | Add User
[**delete_expired_users**](UserApi.md#delete_expired_users) | **DELETE** /api/users/expired | Delete Expired Users
[**get_expired_users**](UserApi.md#get_expired_users) | **GET** /api/users/expired | Get Expired Users
[**get_user**](UserApi.md#get_user) | **GET** /api/user/{username} | Get User
[**get_user_usage**](UserApi.md#get_user_usage) | **GET** /api/user/{username}/usage | Get User Usage
[**get_users**](UserApi.md#get_users) | **GET** /api/users | Get Users
[**get_users_usage**](UserApi.md#get_users_usage) | **GET** /api/users/usage | Get Users Usage
[**modify_user**](UserApi.md#modify_user) | **PUT** /api/user/{username} | Modify User
[**remove_user**](UserApi.md#remove_user) | **DELETE** /api/user/{username} | Remove User
[**reset_user_data_usage**](UserApi.md#reset_user_data_usage) | **POST** /api/user/{username}/reset | Reset User Data Usage
[**reset_users_data_usage**](UserApi.md#reset_users_data_usage) | **POST** /api/users/reset | Reset Users Data Usage
[**revoke_user_subscription**](UserApi.md#revoke_user_subscription) | **POST** /api/user/{username}/revoke_sub | Revoke User Subscription
[**set_owner**](UserApi.md#set_owner) | **PUT** /api/user/{username}/set-owner | Set Owner


# **add_user**
> UserResponse add_user(user_create)

Add User

Add a new user  - **username**: 3 to 32 characters, can include a-z, 0-9, and underscores. - **status**: User's status, defaults to `active`. Special rules if `on_hold`. - **expire**: UTC timestamp for account expiration. Use `0` for unlimited. - **data_limit**: Max data usage in bytes (e.g., `1073741824` for 1GB). `0` means unlimited. - **data_limit_reset_strategy**: Defines how/if data limit resets. `no_reset` means it never resets. - **proxies**: Dictionary of protocol settings (e.g., `vmess`, `vless`). - **inbounds**: Dictionary of protocol tags to specify inbound connections. - **note**: Optional text field for additional user information or notes. - **on_hold_timeout**: UTC timestamp when `on_hold` status should start or end. - **on_hold_expire_duration**: Duration (in seconds) for how long the user should stay in `on_hold` status.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_create import UserCreate
from pymarz.models.user_response import UserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    user_create = pymarz.UserCreate() # UserCreate | 

    try:
        # Add User
        api_response = api_instance.add_user(user_create)
        print("The response of UserApi->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->add_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**409** | User already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_expired_users**
> List[str] delete_expired_users(expired_after=expired_after, expired_before=expired_before)

Delete Expired Users

Delete users who have expired within the specified date range.  - **expired_after** UTC datetime (optional) - **expired_before** UTC datetime (optional) - At least one of expired_after or expired_before must be provided

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    expired_after = '2024-01-01T00:00:00' # datetime |  (optional)
    expired_before = '2024-01-31T23:59:59' # datetime |  (optional)

    try:
        # Delete Expired Users
        api_response = api_instance.delete_expired_users(expired_after=expired_after, expired_before=expired_before)
        print("The response of UserApi->delete_expired_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_expired_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expired_after** | **datetime**|  | [optional] 
 **expired_before** | **datetime**|  | [optional] 

### Return type

**List[str]**

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
**404** | No expired users found in the specified date range |  -  |
**400** | Start date must be before end date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expired_users**
> List[str] get_expired_users(expired_after=expired_after, expired_before=expired_before)

Get Expired Users

Get users who have expired within the specified date range.  - **expired_after** UTC datetime (optional) - **expired_before** UTC datetime (optional) - At least one of expired_after or expired_before must be provided for filtering - If both are omitted, returns all expired users

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    expired_after = '2024-01-01T00:00:00' # datetime |  (optional)
    expired_before = '2024-01-31T23:59:59' # datetime |  (optional)

    try:
        # Get Expired Users
        api_response = api_instance.get_expired_users(expired_after=expired_after, expired_before=expired_before)
        print("The response of UserApi->get_expired_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_expired_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expired_after** | **datetime**|  | [optional] 
 **expired_before** | **datetime**|  | [optional] 

### Return type

**List[str]**

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
**400** | Start date must be before end date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(username)

Get User

Get user information

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_response import UserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(username)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_usage**
> UserUsagesResponse get_user_usage(username, start=start, end=end)

Get User Usage

Get users usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_usages_response import UserUsagesResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 
    start = '' # str |  (optional) (default to '')
    end = '' # str |  (optional) (default to '')

    try:
        # Get User Usage
        api_response = api_instance.get_user_usage(username, start=start, end=end)
        print("The response of UserApi->get_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **start** | **str**|  | [optional] [default to &#39;&#39;]
 **end** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UserUsagesResponse**](UserUsagesResponse.md)

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
**400** | Start date must be before end date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> UsersResponse get_users(offset=offset, limit=limit, username=username, search=search, admin=admin, status=status, sort=sort)

Get Users

Get all users

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_status import UserStatus
from pymarz.models.users_response import UsersResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    username = ['username_example'] # List[str] |  (optional)
    search = 'search_example' # str |  (optional)
    admin = ['admin_example'] # List[str] |  (optional)
    status = pymarz.UserStatus() # UserStatus |  (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # Get Users
        api_response = api_instance.get_users(offset=offset, limit=limit, username=username, search=search, admin=admin, status=status, sort=sort)
        print("The response of UserApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **username** | [**List[str]**](str.md)|  | [optional] 
 **search** | **str**|  | [optional] 
 **admin** | [**List[str]**](str.md)|  | [optional] 
 **status** | [**UserStatus**](.md)|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

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

# **get_users_usage**
> UsersUsagesResponse get_users_usage(start=start, end=end, admin=admin)

Get Users Usage

Get all users usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.users_usages_response import UsersUsagesResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    start = '' # str |  (optional) (default to '')
    end = '' # str |  (optional) (default to '')
    admin = ['admin_example'] # List[str] |  (optional)

    try:
        # Get Users Usage
        api_response = api_instance.get_users_usage(start=start, end=end, admin=admin)
        print("The response of UserApi->get_users_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] [default to &#39;&#39;]
 **end** | **str**|  | [optional] [default to &#39;&#39;]
 **admin** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**UsersUsagesResponse**](UsersUsagesResponse.md)

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
**400** | Start date must be before end date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user**
> UserResponse modify_user(username, user_modify)

Modify User

Modify an existing user  - **username**: Cannot be changed. Used to identify the user. - **status**: User's new status. Can be 'active', 'disabled', 'on_hold', 'limited', or 'expired'. - **expire**: UTC timestamp for new account expiration. Set to `0` for unlimited, `null` for no change. - **data_limit**: New max data usage in bytes (e.g., `1073741824` for 1GB). Set to `0` for unlimited, `null` for no change. - **data_limit_reset_strategy**: New strategy for data limit reset. Options include 'daily', 'weekly', 'monthly', or 'no_reset'. - **proxies**: Dictionary of new protocol settings (e.g., `vmess`, `vless`). Empty dictionary means no change. - **inbounds**: Dictionary of new protocol tags to specify inbound connections. Empty dictionary means no change. - **note**: New optional text for additional user information or notes. `null` means no change. - **on_hold_timeout**: New UTC timestamp for when `on_hold` status should start or end. Only applicable if status is changed to 'on_hold'. - **on_hold_expire_duration**: New duration (in seconds) for how long the user should stay in `on_hold` status. Only applicable if status is changed to 'on_hold'.  Note: Fields set to `null` or omitted will not be modified.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_modify import UserModify
from pymarz.models.user_response import UserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 
    user_modify = pymarz.UserModify() # UserModify | 

    try:
        # Modify User
        api_response = api_instance.modify_user(username, user_modify)
        print("The response of UserApi->modify_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->modify_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **user_modify** | [**UserModify**](UserModify.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **remove_user**
> object remove_user(username)

Remove User

Remove a user

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Remove User
        api_response = api_instance.remove_user(username)
        print("The response of UserApi->remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->remove_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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

# **reset_user_data_usage**
> UserResponse reset_user_data_usage(username)

Reset User Data Usage

Reset user data usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_response import UserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Reset User Data Usage
        api_response = api_instance.reset_user_data_usage(username)
        print("The response of UserApi->reset_user_data_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->reset_user_data_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**409** | User already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_users_data_usage**
> object reset_users_data_usage()

Reset Users Data Usage

Reset all users data usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)

    try:
        # Reset Users Data Usage
        api_response = api_instance.reset_users_data_usage()
        print("The response of UserApi->reset_users_data_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->reset_users_data_usage: %s\n" % e)
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

# **revoke_user_subscription**
> UserResponse revoke_user_subscription(username)

Revoke User Subscription

Revoke users subscription (Subscription link and proxies)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_response import UserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Revoke User Subscription
        api_response = api_instance.revoke_user_subscription(username)
        print("The response of UserApi->revoke_user_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->revoke_user_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **set_owner**
> UserResponse set_owner(username, admin_username)

Set Owner

Set a new owner (admin) for a user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_response import UserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.UserApi(api_client)
    username = 'username_example' # str | 
    admin_username = 'admin_username_example' # str | 

    try:
        # Set Owner
        api_response = api_instance.set_owner(username, admin_username)
        print("The response of UserApi->set_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->set_owner: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **admin_username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**404** | Admin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

