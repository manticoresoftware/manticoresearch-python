# manticoresearch.SearchApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /search | Performs a search on an index.
[**percolate**](SearchApi.md#percolate) | **POST** /pq/{index}/search | Perform a reverse search on a percolate index


## **search**
> SearchResponse search(search_request)

Performs a search on an index. 

The method expects a SearchRequest object with the following mandatory properties:
        
* the name of the index to search | string
        
For details, see the documentation on [**SearchRequest**](SearchRequest.md)

The method returns an object with the following properties:
        
- hits: an object with the following properties:
  - hits: an array of hit objects, where each hit object represents a matched document. Each hit object has the following properties:
    - _id: the ID of the matched document.
    - _score: the score of the matched document.
    - _source: the source data of the matched document.
  - total: the total number of hits found.
- timed_out: a boolean indicating whether the query timed out.
- took: the time taken to execute the search query.

In addition, if profiling is enabled, the response will include an additional array with profiling information attached.

Here is an example search response:
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

	# Create SearchRequest
    search_request = SearchRequest()
    search_request.index='test'
    search_request.fulltext_filter=QueryFilter('find smth') 
    
    # or create SearchRequest in an alternative way as in the previous versions of the client. It uses a single complex JSON object for a query field 
    search_request = SearchRequest(
        index='test',
        query={'query_string': 'find smth'},
    )
    
    # Both ways of creating SearchRequest are interchangeable and produce the same result  

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
| Status code | Description |
|-------------|-------------|
**200** | Success, query processed |
**500** | Server error |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## **percolate**
> SearchResponse percolate(index,percolate_request)

Perform a reverse search on a percolate index. [[More info on percolate indexes in Manticore Search Manual]](https://manual.manticoresearch.com/Creating_a_table/Local_tables/Percolate_table#Percolate-table)

This method must be used only on percolate indexes.

Expects two parameters: the index name and an object with a document or an array of documents to search by.
Here is an example of the object with a single document:

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

And here is an example of the object with multiple documents:

```
{
  "query":
  {
    "percolate":
    {
      "documents": [
        {
          "content":"sample content"
        },
        {
          "content":"another sample content"
        }
      ]
    }
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
from manticoresearch.model.percolate_request_query import PercolateRequestQuery
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

    index = "index_example" # str  | Name of the percolate index
    percolate_query = { 
        "query": { 
            "percolate": { 
                "document":  {  
                    "content":"sample content" 
                } 
            } 
        } 
    }
    percolate_request = PercolateRequest(
        query=PercolateRequestQuery(percolate_query),
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
| Status code | Description |
|-------------|-------------|
**200** | Success, query processed |
**500** | Server error |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

