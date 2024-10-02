# Manticore Python client

Сlient for Manticore Search.


❗ WARNING: this is a development version of the client. The latest release's readme is https://github.com/manticoresoftware/manticoresearch-python/tree/4.0.0

## Requirements.

Minimum Manticore Search version is >= 2.5.1 with HTTP protocol enabled.

| Manticore Search  | manticoresearch-python   |     Python    |
| ----------------- | ------------------------ | ------------- |
| >= 6.3.6          | >= 5.0.x                 | >= 3.4        |
| >= 6.2.0          | >= 3.3.1                 | >= 3.4        |
| >= 4.2.1          | >= 2.0.x                 | >= 3.4        |
| >= 4.0.2  < 4.2.1 | >= 1.0.6                 | >= 3.4        |
| >= 2.5.1  < 4.0.2 | >= 1.0.5                 | >= 2.7        |

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

    try:    
        # Perform insert and search operations
        indexApi.insert({"index": "products", "doc" : {"title" : "Crossbody Bag with Tassel", "price" : 19.85}})
        indexApi.insert({"index": "products", "doc" : {"title" : "Pet Hair Remover Glove", "price" : 7.99}})
        search_response = searchApi.search({"index": "products", "query": {"query_string": "@title bag"}, "highlight":{"fieldnames":["title"]}})
        print("The response of SearchApi->search:\n")
        pprint(search_response)
    except ApiException as e:
        print("Exception when calling Api method: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:9308*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IndexApi* | [**bulk**](docs/IndexApi.md#bulk) | **POST** /bulk | Bulk index operations
*IndexApi* | [**delete**](docs/IndexApi.md#delete) | **POST** /delete | Delete a document in an index
*IndexApi* | [**insert**](docs/IndexApi.md#insert) | **POST** /insert | Create a new document in an index
*IndexApi* | [**partial_replace**](docs/IndexApi.md#partial_replace) | **POST** /{index}/_update/{id} | Partially replaces a document in an index
*IndexApi* | [**replace**](docs/IndexApi.md#replace) | **POST** /replace | Replace new document in an index
*IndexApi* | [**update**](docs/IndexApi.md#update) | **POST** /update | Update a document in an index
*SearchApi* | [**percolate**](docs/SearchApi.md#percolate) | **POST** /pq/{index}/search | Perform reverse search on a percolate index
*SearchApi* | [**search**](docs/SearchApi.md#search) | **POST** /search | Performs a search on an index
*UtilsApi* | [**sql**](docs/UtilsApi.md#sql) | **POST** /sql | Perform SQL requests


## Documentation For Models

 - [Aggregation](docs/Aggregation.md)
 - [AggregationComposite](docs/AggregationComposite.md)
 - [AggregationCompositeSourcesInnerValue](docs/AggregationCompositeSourcesInnerValue.md)
 - [AggregationCompositeSourcesInnerValueTerms](docs/AggregationCompositeSourcesInnerValueTerms.md)
 - [AggregationSortInnerValue](docs/AggregationSortInnerValue.md)
 - [AggregationTerms](docs/AggregationTerms.md)
 - [AttrFilter](docs/AttrFilter.md)
 - [BasicSearchRequest](docs/BasicSearchRequest.md)
 - [BoolFilter](docs/BoolFilter.md)
 - [BoolFilterBool](docs/BoolFilterBool.md)
 - [BulkResponse](docs/BulkResponse.md)
 - [DeleteDocumentRequest](docs/DeleteDocumentRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [EqualsFilter](docs/EqualsFilter.md)
 - [EqualsFilterEquals](docs/EqualsFilterEquals.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponseError](docs/ErrorResponseError.md)
 - [ErrorResponseErrorOneOf](docs/ErrorResponseErrorOneOf.md)
 - [FulltextFilter](docs/FulltextFilter.md)
 - [GeoFilter](docs/GeoFilter.md)
 - [GeoFilterGeoDistance](docs/GeoFilterGeoDistance.md)
 - [GeoFilterGeoDistanceLocationAnchor](docs/GeoFilterGeoDistanceLocationAnchor.md)
 - [Highlight](docs/Highlight.md)
 - [HighlightAllOfFields](docs/HighlightAllOfFields.md)
 - [HighlightFieldOption](docs/HighlightFieldOption.md)
 - [InFilter](docs/InFilter.md)
 - [InsertDocumentRequest](docs/InsertDocumentRequest.md)
 - [JoinBasicCond](docs/JoinBasicCond.md)
 - [JoinInner](docs/JoinInner.md)
 - [JoinInnerOnInner](docs/JoinInnerOnInner.md)
 - [JoinInnerOnInnerLeft](docs/JoinInnerOnInnerLeft.md)
 - [KnnDocIdRequest](docs/KnnDocIdRequest.md)
 - [KnnQueryVectorRequest](docs/KnnQueryVectorRequest.md)
 - [KnnSearchParameters](docs/KnnSearchParameters.md)
 - [KnnSearchRequest](docs/KnnSearchRequest.md)
 - [KnnSearchRequestAllOfKnn](docs/KnnSearchRequestAllOfKnn.md)
 - [MatchAllFilter](docs/MatchAllFilter.md)
 - [MatchFilter](docs/MatchFilter.md)
 - [MatchFilterMatch](docs/MatchFilterMatch.md)
 - [MatchPhraseFilter](docs/MatchPhraseFilter.md)
 - [PercolateRequest](docs/PercolateRequest.md)
 - [PercolateRequestQuery](docs/PercolateRequestQuery.md)
 - [QueryFilter](docs/QueryFilter.md)
 - [QueryStringFilter](docs/QueryStringFilter.md)
 - [RangeFilter](docs/RangeFilter.md)
 - [RangeFilterRangeValue](docs/RangeFilterRangeValue.md)
 - [ReplaceDocumentRequest](docs/ReplaceDocumentRequest.md)
 - [SearchRequest](docs/SearchRequest.md)
 - [SearchRequestParameters](docs/SearchRequestParameters.md)
 - [SearchRequestParametersSortInner](docs/SearchRequestParametersSortInner.md)
 - [SearchRequestParametersSource](docs/SearchRequestParametersSource.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [SearchResponseHits](docs/SearchResponseHits.md)
 - [SortObject](docs/SortObject.md)
 - [SourceByRules](docs/SourceByRules.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [UpdateDocumentRequest](docs/UpdateDocumentRequest.md)
 - [UpdateResponse](docs/UpdateResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

info@manticoresearch.com


