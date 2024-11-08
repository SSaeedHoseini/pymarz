# pymarz.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AdminApi.md#login) | **POST** /api/admin/token | Login and get token
[**get_current**](AdminApi.md#get_current) | **GET** /api/admin | Get Current Admin
[**create**](AdminApi.md#create) | **POST** /api/admin | Create Admin
[**get**](AdminApi.md#get) | **GET** /api/admins | Get Admins
[**update**](AdminApi.md#update) | **PUT** /api/admin/{username} | Modify Admin
[**delete**](AdminApi.md#delete) | **DELETE** /api/admin/{username} | Remove Admin


# **login**
> login(username, password)

Admin Login

Authenticate an admin and issue a token.

### Example

```python
from pymarz import MarzAPI

# Login with admin user
# if the token expires, it will be renewed automatically
client = pymarz(url="your-domain",username="admin",password="admin")

# If you need to login manually
# username="admin"
# password="admin"
await client.login()

# if you need to login with other user
# username="other-user"
# password="other-user-password"
await client.login(username="other-user",password="other-user-password")
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  |

### Return type
None

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

# **create_admin**
> Admin create_admin(admin_create)

Create Admin

Create a new admin if the current admin has sudo privileges.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.admin import Admin
from pymarz.models.admin_create import AdminCreate
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
    api_instance = pymarz.AdminApi(api_client)
    admin_create = pymarz.AdminCreate() # AdminCreate | 

    try:
        # Create Admin
        api_response = api_instance.create_admin(admin_create)
        print("The response of AdminApi->create_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_admin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_create** | [**AdminCreate**](AdminCreate.md)|  | 

### Return type

[**Admin**](Admin.md)

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
**409** | Admin already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admins**
> List[Admin] get_admins(offset=offset, limit=limit, username=username)

Get Admins

Fetch a list of admins with optional filters for pagination and username.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.admin import Admin
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
    api_instance = pymarz.AdminApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        # Get Admins
        api_response = api_instance.get_admins(offset=offset, limit=limit, username=username)
        print("The response of AdminApi->get_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_admins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**List[Admin]**](Admin.md)

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

# **get_current_admin**
> Admin get_current_admin()

Get Current Admin

Retrieve the current authenticated admin.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.admin import Admin
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
    api_instance = pymarz.AdminApi(api_client)

    try:
        # Get Current Admin
        api_response = api_instance.get_current_admin()
        print("The response of AdminApi->get_current_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_current_admin: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Admin**](Admin.md)

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

# **modify_admin**
> Admin modify_admin(username, admin_modify)

Modify Admin

Modify an existing admin's details.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.admin import Admin
from pymarz.models.admin_modify import AdminModify
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
    api_instance = pymarz.AdminApi(api_client)
    username = 'username_example' # str | 
    admin_modify = pymarz.AdminModify() # AdminModify | 

    try:
        # Modify Admin
        api_response = api_instance.modify_admin(username, admin_modify)
        print("The response of AdminApi->modify_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->modify_admin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **admin_modify** | [**AdminModify**](AdminModify.md)|  | 

### Return type

[**Admin**](Admin.md)

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
**403** | You&#39;re not allowed to edit another sudoer&#39;s account. Use marzban-cli instead. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_admin**
> object remove_admin(username)

Remove Admin

Remove an admin from the database.

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
    api_instance = pymarz.AdminApi(api_client)
    username = 'username_example' # str | 

    try:
        # Remove Admin
        api_response = api_instance.remove_admin(username)
        print("The response of AdminApi->remove_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_admin: %s\n" % e)
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
**403** | You&#39;re not allowed to delete sudo accounts. Use marzban-cli instead. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

