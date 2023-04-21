# manticoresearch.SearchApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /search | Performs search
[**percolate**](SearchApi.md#percolate) | **POST** /pq/{index}/search | Perform reverse search on a percolate index


## **search**
> SearchResponse search(search_request)

Performs search


Expects an object with mandatory properties:
* the index name
* the match query object

Example:

  ```
  {
    'index':'movies',
    'query':
    {
      'bool':
      {
        'must':[{'query_string':' movie'}]
      }
    },
    'script_fields':
    {
      'myexpr':
      {
        'script':{'inline':'IF(rating>8,1,0)'
      }
    },
    'sort':
    [
      {'myexpr':'desc'},
      {'_score':'desc'}
    ],
    'profile':true
  }
  ```

Alternatively, you can use auxiliary objects to build your search query. For details, see the documentation on [**SearchRequest**](SearchRequest.md)

It responds with an object with:
- an array with hits (matched documents) found
- if the query is timed out
- time of execution
- if profiling is enabled, an additional array with profiling information attached


  ```
  {
    'took':10,
    'timed_out':false,
    'hits':
    {
      'total':2,
      'hits':
      [
        {'_id':'1','_score':1,'_source':{'gid':11}},
        {'_id':'2','_score':1,'_source':{'gid':12}}
      ]
    }
  }
  ```

For more information about the match query syntax and additional parameters that can be added to request and response, please check: https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP-JSON.


### Example

```python
import manticoresearch
from manticoresearch.api import search_api
from manticoresearch.model.search_request import SearchRequest
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.search_response import SearchResponse
from manticoresearch.model.query_filter import QueryFilter
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    search_request = SearchRequest()
    search_request.index='test'
    search_request.fullltext_filter=QueryFilter('find smth') 
    
    # or create SearchRequest in alternative way
    
    search_request = SearchRequest(
        index='test',
        query={'query_string': 'find smth'},
    )  

    # example passing only required values which don't have defaults set
    try:
        # Performs a search
        api_response = api_instance.search(search_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
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


## **percolate**
> SearchResponse percolate(index,percolate_request)

Perform reverse search on a percolate index

Performs a percolate search. 
This method must be used only on percolate indexes.

Expects two parameters: the index name and an object with array of documents to be tested.
An example of the documents object:

  ```
  {
    "query":
    {
      "percolate":
      {
        "document":
        {
          "content":"sample content"
        }
      }
    }
  }
  ```

Responds with an object with matched stored queries: 

  ```
  {
    'timed_out':false,
    'hits':
    {
      'total':2,
      'max_score':1,
      'hits':
      [
        {
          '_index':'idx_pq_1',
          '_type':'doc',
          '_id':'2',
          '_score':'1',
          '_source':
          {
            'query':
            {
              'match':{'title':'some'}
            }
          }
        },
        {
          '_index':'idx_pq_1',
          '_type':'doc',
          '_id':'5',
          '_score':'1',
          '_source':
          {
            'query':
            {
              'ql':'some | none'
            }
          }
        }
      ]
    }
  }
  ```


### Example

```python
import manticoresearch
from manticoresearch.api import search_api
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.search_response import SearchResponse
from manticoresearch.model.percolate_request import PercolateRequest
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    index = "index_example" # str  |( Name of the percolate index  
    percolate_request = PercolateRequest(
        query=PercolateRequestQuery(),
    ) # PercolateRequest  

    # example passing only required values which don't have defaults set
    try:
        # Perform reverse search on a percolate index
        api_response = api_instance.percolate(index, percolate_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling SearchApi->percolate: %s\n" % e)


```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Name of the percolate index | 
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

