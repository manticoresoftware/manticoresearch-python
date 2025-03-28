# Manticore Python client

Сlient for Manticore Search.


❗ WARNING: this is a development version of the client. The latest release's readme is https://github.com/manticoresoftware/manticoresearch-python/tree/7.0.0

## Requirements.

Minimum Manticore Search version is >= 2.5.1 with HTTP protocol enabled.

| **manticoresearch-python*   | **Manticore Search**                | **Python**     | **Compatibility**       |
| --------------------------- | ----------------------------------- | -------------- | ------------------------|
| `manticoresearch-devel`     | `dev` (latest development version)  | 3.4 or newer   | ✅ Fully Compatible     |
| 8.0.0 or newer              | 9.2.14 or newer                     | 3.4 or newer   | ✅ Fully Compatible     |
| 6.0.0 to 8.0.0              | 9.2.14 or newer                     | 3.4 or newer   | ⚠️ Partially Compatible |
| 6.0.0 to 8.0.0              | 7.0.0 to 9.2.14                     | 3.4 or newer   | ✅ Fully Compatible     |
| 6.0.0 or newer              | 6.2.1 to 7.0.0                      | 3.4 or newer   | ⚠️ Partially Compatible |
| 3.3.1 to 6.0.0              | 7.0.0 or newer                      | 3.4 or newer   | ⚠️ Partially Compatible |
| 3.3.1 to 6.0.0              | 6.2.1 to 7.0.0                      | 3.4 or newer   | ✅ Fully Compatible     |
| 2.0.0 to 3.3.1              | 6.2.0 or newer                      | 3.4 or newer   | ⚠️ Partially Compatible |
| 2.0.0 to 3.3.1              | 4.2.1 to 6.2.0                      | 3.4 or newer   | ✅ Fully Compatible     |
| 1.0.6 to 2.0.0              | 4.0.2 to 4.2.1                      | 3.4 or newer   | ✅ Fully Compatible     |
| 1.0.5 to 1.0.6              | 4.0.2 to 4.2.1                      | 2.7 or newer   | ⚠️ Partially Compatible |
| 1.0.5 to 1.0.6              | 2.5.1 to 4.0.2                      | 2.7 or newer   | ✅ Fully Compatible     |

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/manticoresoftware/manticoresearch-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/manticoresoftware/manticoresearch-python.git`)

Then import the package:
```python
import manticoresearch
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import manticoresearch
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    # Create instances of API classes
    indexApi = manticoresearch.IndexApi(api_client)
    searchApi = manticoresearch.SearchApi(api_client)
    utilsApi = manticoresearch.UtilsApi(api_client)

    try:
        # Perform insert and search operations    
        newDoc = {"title" : "Crossbody Bag with Tassel", "price": 19.85}
        insert_request = InsertDocumentRequest(index="products", doc=newDoc)
        indexApi.insert(insert_request)
        
        # Check out the structure of the autocreated 'products' table
        sql_response = utilsApi.sql('DESC products');
        print("The response of UtilsApi->sql:\n")
        pprint(sql_response) 

        newDoc = {"title" : "Pet Hair Remover Glove", "price": 7.99}
        insert_request = InsertDocumentRequest(index="products", doc=newDoc)
        indexApi.insert(insert_request)
        
        query_highlight = Highlight()
        query_highlight.fields = {"title":{}}
        search_query = SearchQuery(query_string="@title bag")
        search_request = SearchRequest(index="products", query=search_query, highlight=query_highlight)
        search_response = searchApi.search(search_request)    
        print("The response of SearchApi->search:\n")
        pprint(search_response)

        # Alternatively, you can pass all request arguments as a complex JSON object        
        indexApi.insert({"index": "products", "doc" : {"title" : "Crossbody Bag with Tassel", "price" : 19.85}})
        indexApi.insert({"index": "products", "doc" : {"title" : "Pet Hair Remover Glove", "price" : 7.99}})
        search_response = searchApi.search({"index": "products", "query": {"query_string": "@title bag"}, "highlight":{"fields":{"title":{}}}})
        print("The response of SearchApi->search:\n")
        pprint(search_response)
    except ApiException as e:
        print("Exception when calling Api method: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:9308*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IndexApi* | [**bulk**](docs/IndexApi.md#bulk) | **POST** /bulk | Bulk table operations
*IndexApi* | [**delete**](docs/IndexApi.md#delete) | **POST** /delete | Delete a document in a table
*IndexApi* | [**insert**](docs/IndexApi.md#insert) | **POST** /insert | Create a new document in a table
*IndexApi* | [**partial_replace**](docs/IndexApi.md#partial_replace) | **POST** /{table}/_update/{id} | Partially replaces a document in a table
*IndexApi* | [**replace**](docs/IndexApi.md#replace) | **POST** /replace | Replace new document in a table
*IndexApi* | [**update**](docs/IndexApi.md#update) | **POST** /update | Update a document in a table
*SearchApi* | [**autocomplete**](docs/SearchApi.md#autocomplete) | **POST** /autocomplete | Performs an autocomplete search on a table
*SearchApi* | [**percolate**](docs/SearchApi.md#percolate) | **POST** /pq/{table}/search | Perform reverse search on a percolate table
*SearchApi* | [**search**](docs/SearchApi.md#search) | **POST** /search | Performs a search on a table
*UtilsApi* | [**sql**](docs/UtilsApi.md#sql) | **POST** /sql | Perform SQL requests


## Documentation For Models

 - [AggComposite](docs/AggComposite.md)
 - [AggCompositeSource](docs/AggCompositeSource.md)
 - [AggCompositeTerm](docs/AggCompositeTerm.md)
 - [AggTerms](docs/AggTerms.md)
 - [Aggregation](docs/Aggregation.md)
 - [AutocompleteRequest](docs/AutocompleteRequest.md)
 - [BoolFilter](docs/BoolFilter.md)
 - [BulkResponse](docs/BulkResponse.md)
 - [DeleteDocumentRequest](docs/DeleteDocumentRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FulltextFilter](docs/FulltextFilter.md)
 - [GeoDistance](docs/GeoDistance.md)
 - [GeoDistanceLocationAnchor](docs/GeoDistanceLocationAnchor.md)
 - [Highlight](docs/Highlight.md)
 - [HighlightFieldOption](docs/HighlightFieldOption.md)
 - [InsertDocumentRequest](docs/InsertDocumentRequest.md)
 - [Join](docs/Join.md)
 - [JoinCond](docs/JoinCond.md)
 - [JoinOn](docs/JoinOn.md)
 - [KnnQuery](docs/KnnQuery.md)
 - [Match](docs/Match.md)
 - [MatchAll](docs/MatchAll.md)
 - [PercolateRequest](docs/PercolateRequest.md)
 - [PercolateRequestQuery](docs/PercolateRequestQuery.md)
 - [QueryFilter](docs/QueryFilter.md)
 - [Range](docs/Range.md)
 - [ReplaceDocumentRequest](docs/ReplaceDocumentRequest.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorDetails](docs/ResponseErrorDetails.md)
 - [SearchQuery](docs/SearchQuery.md)
 - [SearchRequest](docs/SearchRequest.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [SearchResponseHits](docs/SearchResponseHits.md)
 - [SourceRules](docs/SourceRules.md)
 - [SqlResponse](docs/SqlResponse.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [UpdateDocumentRequest](docs/UpdateDocumentRequest.md)
 - [UpdateResponse](docs/UpdateResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

info@manticoresearch.com


