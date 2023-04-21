# manticoresearch
Сlient for Manticore Search.



## Requirements.

Minimum Manticore Search version is >= 2.5.1 with HTTP protocol enabled.

| Manticore Search  | manticoresearch-python   |     Python    |
| ----------------- | ------------------------ | ------------- |
| >= 4.2.1          | 2.0.x                    | >= 3.4        |
| >= 4.0.2  < 4.2.1 | 1.0.6                    | >= 3.4        |
| >= 2.5.1  < 4.0.2 | 1.0.5                    | >= 2.7        |


## Installation & Usage
### pip install
Install the `manticoresearch` package with [pip](http://pypi.python.org)

```sh
pip install manticoresearch
```

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
from __future__ import print_function

import time
import manticoresearch
from manticoresearch import *
from manticoresearch.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)



# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the IndexApi API class
    api_instance = manticoresearch.IndexApi(api_client)
    body = "["'{\"insert\": {\"index\": \"test\", \"id\": 1, \"doc\": {\"title\": \"Title 1\"}}},\\n{\"insert\": {\"index\": \"test\", \"id\": 2, \"doc\": {\"title\": \"Title 2\"}}}'"]" # str | 

    try:
        # Bulk index operations
        api_response = api_instance.bulk(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndexApi->bulk: %s\n" % e)
    
    
    # Create an instance of the Search API class
    api_instance = manticoresearch.SearchApi(api_client)

    # Create SearchRequest
    search_request = SearchRequest()
    search_request.index='test'
    search_request.fullltext_filter=QueryFilter('Title 1') 
    
    # The example passes only required values which don't have defaults set
    try:
        # Perform a search
        api_response = api_instance.search(search_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```

# Documentation


Full documentation on the API Endpoints and Models used is available in  [docs](https://github.com/manticoresoftware/manticoresearch-python/tree/master/docs) folder as listed below.

Manticore Search server documentation: https://manual.manticoresearch.com.

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:9308*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IndexApi* | [**bulk**](docs/IndexApi.md#bulk) | **POST** /bulk | Bulk index operations
*IndexApi* | [**delete**](docs/IndexApi.md#delete) | **POST** /delete | Delete a document in an index
*IndexApi* | [**insert**](docs/IndexApi.md#insert) | **POST** /insert | Create a new document in an index
*IndexApi* | [**replace**](docs/IndexApi.md#replace) | **POST** /replace | Replace new document in an index
*IndexApi* | [**update**](docs/IndexApi.md#update) | **POST** /update | Update a document in an index
*SearchApi* | [**percolate**](docs/SearchApi.md#percolate) | **POST** /pq/{index}/search | Perform reverse search on a percolate index
*SearchApi* | [**search**](docs/SearchApi.md#search) | **POST** /search | Performs a search on an index
*UtilsApi* | [**sql**](docs/UtilsApi.md#sql) | **POST** /sql | Perform SQL requests


## Documentation For Models

 - [Aggregation](docs/Aggregation.md)
 - [AttrFilter](docs/AttrFilter.md)
 - [BoolFilter](docs/BoolFilter.md)
 - [BulkResponse](docs/BulkResponse.md)
 - [DeleteDocumentRequest](docs/DeleteDocumentRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [EqualsFilter](docs/EqualsFilter.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Facet](docs/Facet.md)
 - [FilterBoolean](docs/FilterBoolean.md)
 - [FilterNumber](docs/FilterNumber.md)
 - [FilterString](docs/FilterString.md)
 - [FulltextFilter](docs/FulltextFilter.md)
 - [GeoDistanceFilter](docs/GeoDistanceFilter.md)
 - [GeoDistanceFilterLocationAnchor](docs/GeoDistanceFilterLocationAnchor.md)
 - [Highlight](docs/Highlight.md)
 - [HighlightField](docs/HighlightField.md)
 - [InFilter](docs/InFilter.md)
 - [InsertDocumentRequest](docs/InsertDocumentRequest.md)
 - [MatchFilter](docs/MatchFilter.md)
 - [MatchOp](docs/MatchOp.md)
 - [MatchOpFilter](docs/MatchOpFilter.md)
 - [MatchPhraseFilter](docs/MatchPhraseFilter.md)
 - [NotFilterBoolean](docs/NotFilterBoolean.md)
 - [NotFilterNumber](docs/NotFilterNumber.md)
 - [NotFilterString](docs/NotFilterString.md)
 - [Option](docs/Option.md)
 - [PercolateRequest](docs/PercolateRequest.md)
 - [PercolateRequestQuery](docs/PercolateRequestQuery.md)
 - [QueryFilter](docs/QueryFilter.md)
 - [RangeFilter](docs/RangeFilter.md)
 - [SearchRequest](docs/SearchRequest.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [SearchResponseHits](docs/SearchResponseHits.md)
 - [SortMVA](docs/SortMVA.md)
 - [SortMultiple](docs/SortMultiple.md)
 - [SortOrder](docs/SortOrder.md)
 - [SourceByRules](docs/SourceByRules.md)
 - [SourceMultiple](docs/SourceMultiple.md)
 - [SqlResponse](docs/SqlResponse.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [UpdateDocumentRequest](docs/UpdateDocumentRequest.md)
 - [UpdateResponse](docs/UpdateResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

info@manticoresearch.com


