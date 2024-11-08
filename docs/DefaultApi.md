# pymarz.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**base**](DefaultApi.md#base) | **GET** / | Base


# **base**
> str base()

Base

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
    api_instance = pymarz.DefaultApi(api_client)

    try:
        # Base
        api_response = api_instance.base()
        print("The response of DefaultApi->base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->base: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

