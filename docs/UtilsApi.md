# openapi_client.UtilsApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sql**](UtilsApi.md#sql) | **POST** /sql | Perform SQL requests


# **sql**
> dict(str, object) sql(body)

Perform SQL requests

Run a query in SQL format.
Expects is a query parameters string that can be in two modes:
* Select only query as `query=SELECT * FROM myindex`. The query string MUST be URL encoded
* any type of query in format `mode=raw&query=SHOW TABLES`. The string must be as is (no URL encoding) and `mode` must be first.
The response object depends on the query executed. In select mode the response has same format as `/search` operation.


### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UtilsApi(api_client)
    body = ["mode=raw&query=SHOW TABLES"] # str | Expects is a query parameters string that can be in two modes:    * Select only query as `query=SELECT * FROM myindex`. The query string MUST be URL encoded    * any type of query in format `mode=raw&query=SHOW TABLES`. The string must be as is (no URL encoding) and `mode` must be first. 

    try:
        # Perform SQL requests
        api_response = api_instance.sql(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UtilsApi->sql: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Expects is a query parameters string that can be in two modes:    * Select only query as &#x60;query&#x3D;SELECT * FROM myindex&#x60;. The query string MUST be URL encoded    * any type of query in format &#x60;mode&#x3D;raw&amp;query&#x3D;SHOW TABLES&#x60;. The string must be as is (no URL encoding) and &#x60;mode&#x60; must be first.  | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | In case of SELECT-only in mode none the response schema is the same as of &#x60;search&#x60;. In case of &#x60;mode&#x3D;raw&#x60; the response depends on the query executed.  |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

