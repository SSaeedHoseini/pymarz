# pymarz.SubscriptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_usage**](SubscriptionApi.md#user_get_usage) | **GET** /sub/{token}/usage | User Get Usage
[**user_subscription**](SubscriptionApi.md#user_subscription) | **GET** /sub/{token}/ | User Subscription
[**user_subscription_info**](SubscriptionApi.md#user_subscription_info) | **GET** /sub/{token}/info | User Subscription Info
[**user_subscription_with_client_type**](SubscriptionApi.md#user_subscription_with_client_type) | **GET** /sub/{token}/{client_type} | User Subscription With Client Type


# **user_get_usage**
> object user_get_usage(token, start=start, end=end)

User Get Usage

Fetches the usage statistics for the user within a specified date range.

### Example

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


# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.SubscriptionApi(api_client)
    token = 'token_example' # str | 
    start = '' # str |  (optional) (default to '')
    end = '' # str |  (optional) (default to '')

    try:
        # User Get Usage
        api_response = api_instance.user_get_usage(token, start=start, end=end)
        print("The response of SubscriptionApi->user_get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_get_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **start** | **str**|  | [optional] [default to &#39;&#39;]
 **end** | **str**|  | [optional] [default to &#39;&#39;]

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
**400** | Start date must be before end date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_subscription**
> object user_subscription(token, user_agent=user_agent)

User Subscription

Provides a subscription link based on the user agent (Clash, V2Ray, etc.).

### Example

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


# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.SubscriptionApi(api_client)
    token = 'token_example' # str | 
    user_agent = '' # str |  (optional) (default to '')

    try:
        # User Subscription
        api_response = api_instance.user_subscription(token, user_agent=user_agent)
        print("The response of SubscriptionApi->user_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **user_agent** | **str**|  | [optional] [default to &#39;&#39;]

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

# **user_subscription_info**
> SubscriptionUserResponse user_subscription_info(token)

User Subscription Info

Retrieves detailed information about the user's subscription.

### Example

```python
import time
import os
import pymarz
from pymarz.models.subscription_user_response import SubscriptionUserResponse
from pymarz.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymarz.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.SubscriptionApi(api_client)
    token = 'token_example' # str | 

    try:
        # User Subscription Info
        api_response = api_instance.user_subscription_info(token)
        print("The response of SubscriptionApi->user_subscription_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_subscription_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**SubscriptionUserResponse**](SubscriptionUserResponse.md)

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

# **user_subscription_with_client_type**
> object user_subscription_with_client_type(client_type, token, user_agent=user_agent)

User Subscription With Client Type

Provides a subscription link based on the specified client type (e.g., Clash, V2Ray).

### Example

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


# Enter a context with an instance of the API client
with pymarz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymarz.SubscriptionApi(api_client)
    client_type = 'client_type_example' # str | 
    token = 'token_example' # str | 
    user_agent = '' # str |  (optional) (default to '')

    try:
        # User Subscription With Client Type
        api_response = api_instance.user_subscription_with_client_type(client_type, token, user_agent=user_agent)
        print("The response of SubscriptionApi->user_subscription_with_client_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_subscription_with_client_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_type** | **str**|  | 
 **token** | **str**|  | 
 **user_agent** | **str**|  | [optional] [default to &#39;&#39;]

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

