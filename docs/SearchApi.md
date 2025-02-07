# manticoresearch.SearchApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**percolate**](SearchApi.md#percolate) | **POST** /pq/{table}/search | Perform reverse search on a percolate table
[**search**](SearchApi.md#search) | **POST** /search | Performs a search on a table


# **percolate**
> SearchResponse percolate(table, percolate_request)

Perform reverse search on a percolate table

Performs a percolate search. <br><br> This method must be used only on percolate tables. <br> Expects two parameters: the table name and an object with array of documents to be tested. <br> <br> An example of the documents object: <br>   { <br>   &nbsp;&nbsp;\"query\" {<br>   &nbsp;&nbsp;&nbsp;&nbsp;\"percolate\": {<br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"document\": { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"content\":\"sample content\" <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} <br>   &nbsp;&nbsp;&nbsp;&nbsp;} <br>   &nbsp;&nbsp;} <br>   } <br> <br> Responds with an object with matched stored queries:  <br>   { <br>   &nbsp;&nbsp;'timed_out':false, <br>   &nbsp;&nbsp;'hits': { <br>   &nbsp;&nbsp;&nbsp;&nbsp;'total':2, <br>   &nbsp;&nbsp;&nbsp;&nbsp;'max_score':1, <br>   &nbsp;&nbsp;&nbsp;&nbsp;'hits': [ <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'table':'idx_pq_1', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_type':'doc', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_id':'2', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_score':'1', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_source': { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'query': { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'match':{'title':'some'} <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }, <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'table':'idx_pq_1', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_type':'doc', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_id':'5', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_score':'1', <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '_source': { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'query': { <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'ql':'some | none' <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>   &nbsp;&nbsp;&nbsp;&nbsp; ] <br>   &nbsp;&nbsp; } <br>   } <br> 

### Example


```python
import manticoresearch
from manticoresearch.models.percolate_request import PercolateRequest
from manticoresearch.models.search_response import SearchResponse
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
    api_instance = manticoresearch.SearchApi(api_client)
    table = 'table_example' # str | Name of the percolate table
    percolate_request = {"query":{"percolate":{"document":{"title":"some text to match"}}}} # PercolateRequest | 

    try:
        # Perform reverse search on a percolate table
        api_response = api_instance.percolate(table, percolate_request)
        print("The response of SearchApi->percolate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->percolate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| Name of the percolate table | 
 **percolate_request** | [**PercolateRequest**](PercolateRequest.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | items found |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(search_request)

Performs a search on a table

 The method expects an object with the following mandatory properties: * the name of the table to search * the match query object For details, see the documentation on [**SearchRequest**](SearchRequest.md) The method returns an object with the following properties: - took: the time taken to execute the search query. - timed_out: a boolean indicating whether the query timed out. - hits: an object with the following properties:    - total: the total number of hits found.    - hits: an array of hit objects, where each hit object represents a matched document. Each hit object has the following properties:      - _id: the ID of the matched document.      - _score: the score of the matched document.      - _source: the source data of the matched document.  In addition, if profiling is enabled, the response will include an additional array with profiling information attached. Also, if pagination is enabled, the response will include an additional 'scroll' property with a scroll token to use for pagination Here is an example search response:    ```   {     'took':10,     'timed_out':false,     'hits':     {       'total':2,       'hits':       [         {'_id':'1','_score':1,'_source':{'gid':11}},         {'_id':'2','_score':1,'_source':{'gid':12}}       ]     }   }   ```  For more information about the match query syntax and additional parameters that can be added to request and response, please see the documentation [here](https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP-JSON). 

### Example


```python
import manticoresearch
from manticoresearch.models.search_request import SearchRequest
from manticoresearch.models.search_response import SearchResponse
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
    api_instance = manticoresearch.SearchApi(api_client)
    search_request = ["'request=SearchRequest(table=\"test\",query=Query(query_string=\"abc\"))'"] # SearchRequest | 

    try:
        # Performs a search on a table
        api_response = api_instance.search(search_request)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

