# manticoresearch.UtilsApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sql**](UtilsApi.md#sql) | **POST** /sql | Perform SQL requests


# **sql**
> List[object] sql(body, raw_response=raw_response, mode=mode)

Perform SQL requests

Run a query in SQL format. Expects a query string passed through `body` parameter and optional `raw_response` parameter that defines a format of response. `raw_response` can be set to `False` for Select queries only, e.g., `SELECT * FROM myindex` The query string must stay as it is, no URL encoding is needed. The response object depends on the query executed. In select mode the response has same format as `/search` operation. 

### Example


```python
import manticoresearch
from manticoresearch.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manticoresearch.UtilsApi(api_client)
    body = SHOW TABLES # str | A query parameter string. 
    raw_response = True # bool | Optional parameter, defines a format of response. Can be set to `False` for Select only queries and set to `True` for any type of queries. Default value is 'True'.  (optional) (default to True)
    mode = 'raw' # str | Optional parameter, defines a format of response. Can be set to empty for Select only queries and set to `raw` for any type of queries. Default value is 'raw'.  (optional) (default to 'raw')

    try:
        # Perform SQL requests
        api_response = api_instance.sql(body, raw_response=raw_response, mode=mode)
        print("The response of UtilsApi->sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->sql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| A query parameter string.  | 
 **raw_response** | **bool**| Optional parameter, defines a format of response. Can be set to &#x60;False&#x60; for Select only queries and set to &#x60;True&#x60; for any type of queries. Default value is &#39;True&#39;.  | [optional] [default to True]
 **mode** | **str**| Optional parameter, defines a format of response. Can be set to empty for Select only queries and set to &#x60;raw&#x60; for any type of queries. Default value is &#39;raw&#39;.  | [optional] [default to &#39;raw&#39;]

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | In case of SELECT-only in mode none the response schema is the same as of &#x60;search&#x60;. In case of &#x60;mode&#x3D;raw&#x60; or &#x60;raw_response&#x3D;true&#x60; the response depends on the query executed.  |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

