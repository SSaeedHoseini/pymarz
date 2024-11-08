# pymarz.UserTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_template**](UserTemplateApi.md#add_user_template) | **POST** /api/user_template | Add User Template
[**get_user_template_endpoint**](UserTemplateApi.md#get_user_template_endpoint) | **GET** /api/user_template/{id} | Get User Template Endpoint
[**get_user_templates**](UserTemplateApi.md#get_user_templates) | **GET** /api/user_template | Get User Templates
[**modify_user_template**](UserTemplateApi.md#modify_user_template) | **PUT** /api/user_template/{id} | Modify User Template
[**remove_user_template**](UserTemplateApi.md#remove_user_template) | **DELETE** /api/user_template/{id} | Remove User Template


# **add_user_template**
> UserTemplateResponse add_user_template(user_template_create)

Add User Template

Add a new user template  - **name** can be up to 64 characters - **data_limit** must be in bytes and larger or equal to 0 - **expire_duration** must be in seconds and larger or equat to 0 - **inbounds** dictionary of protocol:inbound_tags, empty means all inbounds

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_template_create import UserTemplateCreate
from pymarz.models.user_template_response import UserTemplateResponse
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
    api_instance = pymarz.UserTemplateApi(api_client)
    user_template_create = pymarz.UserTemplateCreate() # UserTemplateCreate | 

    try:
        # Add User Template
        api_response = api_instance.add_user_template(user_template_create)
        print("The response of UserTemplateApi->add_user_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->add_user_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_template_create** | [**UserTemplateCreate**](UserTemplateCreate.md)|  | 

### Return type

[**UserTemplateResponse**](UserTemplateResponse.md)

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
**409** | Template by this name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_template_endpoint**
> UserTemplateResponse get_user_template_endpoint(template_id)

Get User Template Endpoint

Get User Template information with id

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_template_response import UserTemplateResponse
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
    api_instance = pymarz.UserTemplateApi(api_client)
    template_id = 56 # int | 

    try:
        # Get User Template Endpoint
        api_response = api_instance.get_user_template_endpoint(template_id)
        print("The response of UserTemplateApi->get_user_template_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->get_user_template_endpoint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 

### Return type

[**UserTemplateResponse**](UserTemplateResponse.md)

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

# **get_user_templates**
> List[UserTemplateResponse] get_user_templates(offset=offset, limit=limit)

Get User Templates

Get a list of User Templates with optional pagination

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_template_response import UserTemplateResponse
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
    api_instance = pymarz.UserTemplateApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # Get User Templates
        api_response = api_instance.get_user_templates(offset=offset, limit=limit)
        print("The response of UserTemplateApi->get_user_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->get_user_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**List[UserTemplateResponse]**](UserTemplateResponse.md)

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

# **modify_user_template**
> UserTemplateResponse modify_user_template(template_id, user_template_modify)

Modify User Template

Modify User Template  - **name** can be up to 64 characters - **data_limit** must be in bytes and larger or equal to 0 - **expire_duration** must be in seconds and larger or equat to 0 - **inbounds** dictionary of protocol:inbound_tags, empty means all inbounds

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import pymarz
from pymarz.models.user_template_modify import UserTemplateModify
from pymarz.models.user_template_response import UserTemplateResponse
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
    api_instance = pymarz.UserTemplateApi(api_client)
    template_id = 56 # int | 
    user_template_modify = pymarz.UserTemplateModify() # UserTemplateModify | 

    try:
        # Modify User Template
        api_response = api_instance.modify_user_template(template_id, user_template_modify)
        print("The response of UserTemplateApi->modify_user_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->modify_user_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 
 **user_template_modify** | [**UserTemplateModify**](UserTemplateModify.md)|  | 

### Return type

[**UserTemplateResponse**](UserTemplateResponse.md)

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
**409** | Template by this name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_template**
> object remove_user_template(template_id)

Remove User Template

Remove a User Template by its ID

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
    api_instance = pymarz.UserTemplateApi(api_client)
    template_id = 56 # int | 

    try:
        # Remove User Template
        api_response = api_instance.remove_user_template(template_id)
        print("The response of UserTemplateApi->remove_user_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->remove_user_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 

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

