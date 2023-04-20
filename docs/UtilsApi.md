# manticoresearch.UtilsApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sql**](UtilsApi.md#sql) | **POST** /sql | Perform SQL requests


# **sql**
> SqlResponse sql(body,raw_response=True)

Perform SQL requests

Run a query in SQL format.
Expects a query string passed through `body` parameter and optional `raw_response` parameter that defines a format of response.
`raw_response` can be set to `False` for Select queries only, e.g., `SELECT * FROM myindex`
The query string must stay as it is, no URL encoding is needed.
The response object depends on the query executed. In select mode the response has same format as `/search` operation.


### Example

```python
import manticoresearch
from manticoresearch.api import utils_api
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.sql_response import SqlResponse
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = utils_api.UtilsApi(api_client)

    body = "SHOW TABLES" # str  |( A query parameter string.   
    raw_response = True # bool  | Optional parameter, defines a format of response. Can be set to `False` for Select only queries and set to `True` or omitted for any type of queries:  (optional) if omitted the server will use the default value of True 

    # example passing only required values which don't have defaults set
    try:
        # Perform SQL requests
        api_response = api_instance.sql(body)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling UtilsApi->sql: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Perform SQL requests
        api_response = api_instance.sql(body, raw_response=raw_response)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling UtilsApi->sql: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| A query parameter string.  | 
 **raw_response** | **bool**| Optional parameter, defines a format of response. Can be set to &#x60;False&#x60; for Select only queries and set to &#x60;True&#x60; or omitted for any type of queries:  | [optional] [default to True]

### Return type

[**SqlResponse**](SqlResponse.md)

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

