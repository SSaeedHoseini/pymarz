# marzapi.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hosts**](SystemApi.md#get_hosts) | **GET** /api/hosts | Get Hosts
[**get_inbounds**](SystemApi.md#get_inbounds) | **GET** /api/inbounds | Get Inbounds
[**get_system_stats**](SystemApi.md#get_system_stats) | **GET** /api/system | Get System Stats
[**modify_hosts**](SystemApi.md#modify_hosts) | **PUT** /api/hosts | Modify Hosts


# **get_hosts**
> Dict[str, List[ProxyHost]] get_hosts()

Get Hosts

Get a list of proxy hosts grouped by inbound tag.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.proxy_host import ProxyHost
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
    api_instance = marzapi.SystemApi(api_client)

    try:
        # Get Hosts
        api_response = api_instance.get_hosts()
        print("The response of SystemApi->get_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_hosts: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, List[ProxyHost]]**

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

# **get_inbounds**
> Dict[str, List[ProxyInbound]] get_inbounds()

Get Inbounds

Retrieve inbound configurations grouped by protocol.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.proxy_inbound import ProxyInbound
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
    api_instance = marzapi.SystemApi(api_client)

    try:
        # Get Inbounds
        api_response = api_instance.get_inbounds()
        print("The response of SystemApi->get_inbounds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_inbounds: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, List[ProxyInbound]]**

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

# **get_system_stats**
> SystemStats get_system_stats()

Get System Stats

Fetch system stats including memory, CPU, and user metrics.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.system_stats import SystemStats
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
    api_instance = marzapi.SystemApi(api_client)

    try:
        # Get System Stats
        api_response = api_instance.get_system_stats()
        print("The response of SystemApi->get_system_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_system_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemStats**](SystemStats.md)

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

# **modify_hosts**
> Dict[str, List[ProxyHost]] modify_hosts(request_body)

Modify Hosts

Modify proxy hosts and update the configuration.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.proxy_host import ProxyHost
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
    api_instance = marzapi.SystemApi(api_client)
    request_body = None # Dict[str, List[ProxyHost]] | 

    try:
        # Modify Hosts
        api_response = api_instance.modify_hosts(request_body)
        print("The response of SystemApi->modify_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->modify_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, List[ProxyHost]]**](List.md)|  | 

### Return type

**Dict[str, List[ProxyHost]]**

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

