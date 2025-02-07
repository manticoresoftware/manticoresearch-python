# manticoresearch.IndexApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](IndexApi.md#bulk) | **POST** /bulk | Bulk table operations
[**delete**](IndexApi.md#delete) | **POST** /delete | Delete a document in a table
[**insert**](IndexApi.md#insert) | **POST** /insert | Create a new document in a table
[**partial_replace**](IndexApi.md#partial_replace) | **POST** /{table}/_update/{id} | Partially replaces a document in a table
[**replace**](IndexApi.md#replace) | **POST** /replace | Replace new document in a table
[**update**](IndexApi.md#update) | **POST** /update | Update a document in a table


# **bulk**
> BulkResponse bulk(body)

Bulk table operations

Sends multiple operatons like inserts, updates, replaces or deletes.  For each operation it's object must have same format as in their dedicated method.  The method expects a raw string as the batch in NDJSON.  Each operation object needs to be serialized to   JSON and separated by endline (\\n).      An example of raw input:      ```   {\"insert\": {\"table\": \"movies\", \"doc\": {\"plot\": \"A secret team goes to North Pole\", \"rating\": 9.5, \"language\": [2, 3], \"title\": \"This is an older movie\", \"lon\": 51.99, \"meta\": {\"keywords\":[\"travel\",\"ice\"],\"genre\":[\"adventure\"]}, \"year\": 1950, \"lat\": 60.4, \"advise\": \"PG-13\"}}}   \\n   {\"delete\": {\"table\": \"movies\",\"id\":700}}   ```      Responds with an object telling whenever any errors occured and an array with status for each operation:      ```   {     'items':     [       {         'update':{'table':'products','_id':1,'result':'updated'}       },       {         'update':{'table':'products','_id':2,'result':'updated'}       }     ],     'errors':false   }   ``` 

### Example


```python
import manticoresearch
from manticoresearch.models.bulk_response import BulkResponse
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
    api_instance = manticoresearch.IndexApi(api_client)
    body = 'body_example' # str | 

    try:
        # Bulk table operations
        api_response = api_instance.bulk(body)
        print("The response of IndexApi->bulk:\n")
        pprint(api_response)
    except Exception as e:
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

Delete a document in a table

Delete one or several documents. The method has 2 ways of deleting: either by id, in case only one document is deleted or by using a  match query, in which case multiple documents can be delete . Example of input to delete by id:    ```   {'table':'movies','id':100}   ```  Example of input to delete using a query:    ```   {     'table':'movies',     'query':     {       'bool':       {         'must':         [           {'query_string':'new movie'}         ]       }     }   }   ```  The match query has same syntax as in for searching. Responds with an object telling how many documents got deleted:     ```   {'table':'products','updated':1}   ``` 

### Example


```python
import manticoresearch
from manticoresearch.models.delete_document_request import DeleteDocumentRequest
from manticoresearch.models.delete_response import DeleteResponse
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
    api_instance = manticoresearch.IndexApi(api_client)
    delete_document_request = {"table":"test","query":{"match":{"title":"apple"}}} # DeleteDocumentRequest | 

    try:
        # Delete a document in a table
        api_response = api_instance.delete(delete_document_request)
        print("The response of IndexApi->delete:\n")
        pprint(api_response)
    except Exception as e:
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

Create a new document in a table

Insert a document.  Expects an object like:     ```   {     'table':'movies',     'id':701,     'doc':     {       'title':'This is an old movie',       'plot':'A secret team goes to North Pole',       'year':1950,       'rating':9.5,       'lat':60.4,       'lon':51.99,       'advise':'PG-13',       'meta':'{\"keywords\":{\"travel\",\"ice\"},\"genre\":{\"adventure\"}}',       'language':[2,3]     }   }   ```   The document id can also be missing, in which case an autogenerated one will be used:             ```   {     'table':'movies',     'doc':     {       'title':'This is a new movie',       'plot':'A secret team goes to North Pole',       'year':2020,       'rating':9.5,       'lat':60.4,       'lon':51.99,       'advise':'PG-13',       'meta':'{\"keywords\":{\"travel\",\"ice\"},\"genre\":{\"adventure\"}}',       'language':[2,3]     }   }   ```   It responds with an object in format:      ```   {'table':'products','_id':701,'created':true,'result':'created','status':201}   ``` 

### Example


```python
import manticoresearch
from manticoresearch.models.insert_document_request import InsertDocumentRequest
from manticoresearch.models.success_response import SuccessResponse
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
    api_instance = manticoresearch.IndexApi(api_client)
    insert_document_request = {"table":"test","id":1,"doc":{"title":"sample title","gid":10}} # InsertDocumentRequest | 

    try:
        # Create a new document in a table
        api_response = api_instance.insert(insert_document_request)
        print("The response of IndexApi->insert:\n")
        pprint(api_response)
    except Exception as e:
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

# **partial_replace**
> UpdateResponse partial_replace(table, id, replace_document_request)

Partially replaces a document in a table

Partially replaces a document with given id in a table Responds with an object of the following format:     ```   {'table':'products','updated':1}   ``` 

### Example


```python
import manticoresearch
from manticoresearch.models.replace_document_request import ReplaceDocumentRequest
from manticoresearch.models.update_response import UpdateResponse
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
    api_instance = manticoresearch.IndexApi(api_client)
    table = 'table_example' # str | Name of the percolate table
    id = 56 # int | Id of the document to replace
    replace_document_request = {"doc":{"price":20}} # ReplaceDocumentRequest | 

    try:
        # Partially replaces a document in a table
        api_response = api_instance.partial_replace(table, id, replace_document_request)
        print("The response of IndexApi->partial_replace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->partial_replace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| Name of the percolate table | 
 **id** | **int**| Id of the document to replace | 
 **replace_document_request** | [**ReplaceDocumentRequest**](ReplaceDocumentRequest.md)|  | 

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

# **replace**
> SuccessResponse replace(insert_document_request)

Replace new document in a table

Replace an existing document. Input has same format as `insert` operation. <br/> Responds with an object in format: <br/>    ```   {'table':'products','_id':1,'created':false,'result':'updated','status':200}   ``` 

### Example


```python
import manticoresearch
from manticoresearch.models.insert_document_request import InsertDocumentRequest
from manticoresearch.models.success_response import SuccessResponse
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
    api_instance = manticoresearch.IndexApi(api_client)
    insert_document_request = {"table":"test","id":1,"doc":{"title":"updated title","gid":15}} # InsertDocumentRequest | 

    try:
        # Replace new document in a table
        api_response = api_instance.replace(insert_document_request)
        print("The response of IndexApi->replace:\n")
        pprint(api_response)
    except Exception as e:
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

Update a document in a table

Update one or several documents. The update can be made by passing the id or by using a match query in case multiple documents can be updated.  For example update a document using document id:    ```   {'table':'movies','doc':{'rating':9.49},'id':100}   ```  And update by using a match query:    ```   {     'table':'movies',     'doc':{'rating':9.49},     'query':     {       'bool':       {         'must':         [           {'query_string':'new movie'}         ]       }     }   }   ```   The match query has same syntax as for searching. Responds with an object that tells how many documents where updated in format:     ```   {'table':'products','updated':1}   ``` 

### Example


```python
import manticoresearch
from manticoresearch.models.update_document_request import UpdateDocumentRequest
from manticoresearch.models.update_response import UpdateResponse
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
    api_instance = manticoresearch.IndexApi(api_client)
    update_document_request = {"table":"test","doc":{"gid":20},"query":{"equals":{"cat_id":2}}} # UpdateDocumentRequest | 

    try:
        # Update a document in a table
        api_response = api_instance.update(update_document_request)
        print("The response of IndexApi->update:\n")
        pprint(api_response)
    except Exception as e:
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

