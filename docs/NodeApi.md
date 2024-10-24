# marzapi.NodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node**](NodeApi.md#add_node) | **POST** /api/node | Add Node
[**get_node**](NodeApi.md#get_node) | **GET** /api/node/{node_id} | Get Node
[**get_node_settings**](NodeApi.md#get_node_settings) | **GET** /api/node/settings | Get Node Settings
[**get_nodes**](NodeApi.md#get_nodes) | **GET** /api/nodes | Get Nodes
[**get_usage**](NodeApi.md#get_usage) | **GET** /api/nodes/usage | Get Usage
[**modify_node**](NodeApi.md#modify_node) | **PUT** /api/node/{node_id} | Modify Node
[**reconnect_node**](NodeApi.md#reconnect_node) | **POST** /api/node/{node_id}/reconnect | Reconnect Node
[**remove_node**](NodeApi.md#remove_node) | **DELETE** /api/node/{node_id} | Remove Node


# **add_node**
> NodeResponse add_node(node_create)

Add Node

Add a new node to the database and optionally add it as a host.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.node_create import NodeCreate
from marzapi.models.node_response import NodeResponse
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
    api_instance = marzapi.NodeApi(api_client)
    node_create = marzapi.NodeCreate() # NodeCreate | 

    try:
        # Add Node
        api_response = api_instance.add_node(node_create)
        print("The response of NodeApi->add_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->add_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_create** | [**NodeCreate**](NodeCreate.md)|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **get_node**
> NodeResponse get_node(node_id)

Get Node

Retrieve details of a specific node by its ID.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.node_response import NodeResponse
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
    api_instance = marzapi.NodeApi(api_client)
    node_id = 56 # int | 

    try:
        # Get Node
        api_response = api_instance.get_node(node_id)
        print("The response of NodeApi->get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **get_node_settings**
> NodeSettings get_node_settings()

Get Node Settings

Retrieve the current node settings, including TLS certificate.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.node_settings import NodeSettings
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
    api_instance = marzapi.NodeApi(api_client)

    try:
        # Get Node Settings
        api_response = api_instance.get_node_settings()
        print("The response of NodeApi->get_node_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_node_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSettings**](NodeSettings.md)

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

# **get_nodes**
> List[NodeResponse] get_nodes()

Get Nodes

Retrieve a list of all nodes. Accessible only to sudo admins.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.node_response import NodeResponse
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
    api_instance = marzapi.NodeApi(api_client)

    try:
        # Get Nodes
        api_response = api_instance.get_nodes()
        print("The response of NodeApi->get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_nodes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[NodeResponse]**](NodeResponse.md)

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

# **get_usage**
> NodesUsageResponse get_usage(start=start, end=end)

Get Usage

Retrieve usage statistics for nodes within a specified date range.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.nodes_usage_response import NodesUsageResponse
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
    api_instance = marzapi.NodeApi(api_client)
    start = '' # str |  (optional) (default to '')
    end = '' # str |  (optional) (default to '')

    try:
        # Get Usage
        api_response = api_instance.get_usage(start=start, end=end)
        print("The response of NodeApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] [default to &#39;&#39;]
 **end** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**NodesUsageResponse**](NodesUsageResponse.md)

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

# **modify_node**
> NodeResponse modify_node(node_id, node_modify)

Modify Node

Update a node's details. Only accessible to sudo admins.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import marzapi
from marzapi.models.node_modify import NodeModify
from marzapi.models.node_response import NodeResponse
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
    api_instance = marzapi.NodeApi(api_client)
    node_id = 56 # int | 
    node_modify = marzapi.NodeModify() # NodeModify | 

    try:
        # Modify Node
        api_response = api_instance.modify_node(node_id, node_modify)
        print("The response of NodeApi->modify_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->modify_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 
 **node_modify** | [**NodeModify**](NodeModify.md)|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **reconnect_node**
> object reconnect_node(node_id)

Reconnect Node

Trigger a reconnection for the specified node. Only accessible to sudo admins.

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
    api_instance = marzapi.NodeApi(api_client)
    node_id = 56 # int | 

    try:
        # Reconnect Node
        api_response = api_instance.reconnect_node(node_id)
        print("The response of NodeApi->reconnect_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->reconnect_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

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

# **remove_node**
> object remove_node(node_id)

Remove Node

Delete a node and remove it from xray in the background.

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
    api_instance = marzapi.NodeApi(api_client)
    node_id = 56 # int | 

    try:
        # Remove Node
        api_response = api_instance.remove_node(node_id)
        print("The response of NodeApi->remove_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->remove_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

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

