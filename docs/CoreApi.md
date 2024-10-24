# marzapi.CoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_core_config**](CoreApi.md#get_core_config) | **GET** /api/core/config | Get Core Config
[**get_core_stats**](CoreApi.md#get_core_stats) | **GET** /api/core | Get Core Stats
[**modify_core_config**](CoreApi.md#modify_core_config) | **PUT** /api/core/config | Modify Core Config
[**restart_core**](CoreApi.md#restart_core) | **POST** /api/core/restart | Restart Core


# **get_core_config**
> object get_core_config()

Get Core Config

Get the current core configuration.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzapi.CoreApi(api_client)

    try:
        # Get Core Config
        api_response = api_instance.get_core_config()
        print("The response of CoreApi->get_core_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_core_config: %s\n" % e)
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

# **get_core_stats**
> CoreStats get_core_stats()

Get Core Stats

Retrieve core statistics such as version and uptime.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.core_stats import CoreStats
from marzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzapi.CoreApi(api_client)

    try:
        # Get Core Stats
        api_response = api_instance.get_core_stats()
        print("The response of CoreApi->get_core_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_core_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CoreStats**](CoreStats.md)

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

# **modify_core_config**
> object modify_core_config(body)

Modify Core Config

Modify the core configuration and restart the core.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzapi.CoreApi(api_client)
    body = None # object | 

    try:
        # Modify Core Config
        api_response = api_instance.modify_core_config(body)
        print("The response of CoreApi->modify_core_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->modify_core_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

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

# **restart_core**
> object restart_core()

Restart Core

Restart the core and all connected nodes.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzapi.CoreApi(api_client)

    try:
        # Restart Core
        api_response = api_instance.restart_core()
        print("The response of CoreApi->restart_core:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->restart_core: %s\n" % e)
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

