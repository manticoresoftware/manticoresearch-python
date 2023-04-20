# manticoresearch.IndexApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](IndexApi.md#bulk) | **POST** /json/bulk | Bulk index operations
[**delete**](IndexApi.md#delete) | **POST** /json/delete | Delete a document in an index
[**insert**](IndexApi.md#insert) | **POST** /json/insert | Create a new document in an index
[**replace**](IndexApi.md#replace) | **POST** /json/replace | Replace new document in an index
[**update**](IndexApi.md#update) | **POST** /json/update | Update a document in an index


# **bulk**
> BulkResponse bulk(body)

Bulk index operations

Sends multiple operatons like inserts, updates, replaces or deletes. 
For each operation it's object must have same format as in their dedicated method. 
The method expects a raw string as the batch in NDJSON.
 Each operation object needs to be serialized to 
 JSON and separated by endline (\n). 
 
  An example of raw input:
  
  ```
  {"insert": {"index": "movies", "doc": {"plot": "A secret team goes to North Pole", "rating": 9.5, "language": [2, 3], "title": "This is an older movie", "lon": 51.99, "meta": {"keywords":["travel","ice"],"genre":["adventure"]}, "year": 1950, "lat": 60.4, "advise": "PG-13"}}}
  \n
  {"delete": {"index": "movies","id":700}}
  ```
  
  Responds with an object telling whenever any errors occured and an array with status for each operation:
  
  ```
  {
    'items':
    [
      {
        'update':{'_index':'products','_id':1,'result':'updated'}
      },
      {
        'update':{'_index':'products','_id':2,'result':'updated'}
      }
    ],
    'errors':false
  }
  ```
 


### Example

```python
import manticoresearch
from manticoresearch.api import index_api
from manticoresearch.model.bulk_response import BulkResponse
from manticoresearch.model.error_response import ErrorResponse
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)

    body = "["'{\"insert\": {\"index\": \"test\", \"id\": 1, \"doc\": {\"title\": \"Title 1\"}}},\\n{\"insert\": {\"index\": \"test\", \"id\": 2, \"doc\": {\"title\": \"Title 2\"}}}'"]" # str  

    # example passing only required values which don't have defaults set
    try:
        # Bulk index operations
        api_response = api_instance.bulk(body)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling IndexApi->bulk: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-ndjson
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item updated |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteResponse delete(delete_document_request)

Delete a document in an index

Delete one or several documents.
The method has 2 ways of deleting: either by id, in case only one document is deleted or by using a  match query, in which case multiple documents can be delete .
Example of input to delete by id:

  ```
  {'index':'movies','id':100}
  ```

Example of input to delete using a query:

  ```
  {
    'index':'movies',
    'query':
    {
      'bool':
      {
        'must':
        [
          {'query_string':'new movie'}
        ]
      }
    }
  }
  ```

The match query has same syntax as in for searching.
Responds with an object telling how many documents got deleted: 

  ```
  {'_index':'products','updated':1}
  ```


### Example

```python
import manticoresearch
from manticoresearch.api import index_api
from manticoresearch.model.delete_response import DeleteResponse
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.delete_document_request import DeleteDocumentRequest
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)

    delete_document_request = DeleteDocumentRequest(
        index="index_example",
        cluster="cluster_example",
        id=1,
        query={},
    ) # DeleteDocumentRequest  

    # example passing only required values which don't have defaults set
    try:
        # Delete a document in an index
        api_response = api_instance.delete(delete_document_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling IndexApi->delete: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_document_request** | [**DeleteDocumentRequest**](DeleteDocumentRequest.md)|  | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item updated |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert**
> SuccessResponse insert(insert_document_request)

Create a new document in an index

Insert a document. 
Expects an object like:
 
  ```
  {
    'index':'movies',
    'id':701,
    'doc':
    {
      'title':'This is an old movie',
      'plot':'A secret team goes to North Pole',
      'year':1950,
      'rating':9.5,
      'lat':60.4,
      'lon':51.99,
      'advise':'PG-13',
      'meta':'{"keywords":{"travel","ice"},"genre":{"adventure"}}',
      'language':[2,3]
    }
  }
  ```
 
The document id can also be missing, in which case an autogenerated one will be used:
         
  ```
  {
    'index':'movies',
    'doc':
    {
      'title':'This is a new movie',
      'plot':'A secret team goes to North Pole',
      'year':2020,
      'rating':9.5,
      'lat':60.4,
      'lon':51.99,
      'advise':'PG-13',
      'meta':'{"keywords":{"travel","ice"},"genre":{"adventure"}}',
      'language':[2,3]
    }
  }
  ```
 
It responds with an object in format:
  
  ```
  {'_index':'products','_id':701,'created':true,'result':'created','status':201}
  ```


### Example

```python
import manticoresearch
from manticoresearch.api import index_api
from manticoresearch.model.insert_document_request import InsertDocumentRequest
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.success_response import SuccessResponse
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)

    insert_document_request = InsertDocumentRequest(
        index="index_example",
        cluster="cluster_example",
        id=1,
        doc={},
    ) # InsertDocumentRequest  

    # example passing only required values which don't have defaults set
    try:
        # Create a new document in an index
        api_response = api_instance.insert(insert_document_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling IndexApi->insert: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_document_request** | [**InsertDocumentRequest**](InsertDocumentRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> SuccessResponse replace(insert_document_request)

Replace new document in an index

Replace an existing document. Input has same format as `insert` operation. <br/>
Responds with an object in format: <br/>

  ```
  {'_index':'products','_id':1,'created':false,'result':'updated','status':200}
  ```


### Example

```python
import manticoresearch
from manticoresearch.api import index_api
from manticoresearch.model.insert_document_request import InsertDocumentRequest
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.success_response import SuccessResponse
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)

    insert_document_request = InsertDocumentRequest(
        index="index_example",
        cluster="cluster_example",
        id=1,
        doc={},
    ) # InsertDocumentRequest  

    # example passing only required values which don't have defaults set
    try:
        # Replace new document in an index
        api_response = api_instance.replace(insert_document_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling IndexApi->replace: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_document_request** | [**InsertDocumentRequest**](InsertDocumentRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> UpdateResponse update(update_document_request)

Update a document in an index

Update one or several documents.
The update can be made by passing the id or by using a match query in case multiple documents can be updated.  For example update a document using document id:

  ```
  {'index':'movies','doc':{'rating':9.49},'id':100}
  ```

And update by using a match query:

  ```
  {
    'index':'movies',
    'doc':{'rating':9.49},
    'query':
    {
      'bool':
      {
        'must':
        [
          {'query_string':'new movie'}
        ]
      }
    }
  }
  ``` 

The match query has same syntax as for searching.
Responds with an object that tells how many documents where updated in format: 

  ```
  {'_index':'products','updated':1}
  ```


### Example

```python
import manticoresearch
from manticoresearch.api import index_api
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.update_response import UpdateResponse
from manticoresearch.model.update_document_request import UpdateDocumentRequest
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)

    update_document_request = UpdateDocumentRequest(
        index="index_example",
        doc={},
        id=1,
        query={},
    ) # UpdateDocumentRequest  

    # example passing only required values which don't have defaults set
    try:
        # Update a document in an index
        api_response = api_instance.update(update_document_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling IndexApi->update: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_document_request** | [**UpdateDocumentRequest**](UpdateDocumentRequest.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item updated |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

