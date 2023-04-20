# manticoresearch.SearchApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**percolate**](SearchApi.md#percolate) | **POST** /json/pq/{index}/search | Perform reverse search on a percolate index
[**search**](SearchApi.md#search) | **POST** /json/search | Performs a search


## **search**
> SearchResponse search(search_request)

Performs a search


Expects an object with mandatory properties:
* the index name
* the match query object
Example :

  ```
  {
    'index':'movies',
    'query':
    {
      'bool':
      {
        'must':
        [
          {'query_string':' movie'}
        ]
      }
    },
    'script_fields':
    {
      'myexpr':
      {
        'script':
        {
          'inline':'IF(rating>8,1,0)'
        }
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
        {
          '_id':'1',
          '_score':1,
          '_source':{'gid':11}
        },
        {
          '_id':'2',
          '_score':1,
          '_source':{'gid':12}
        }
      ]
    }
  }
  ```

Alternatively, you can use auxiliary query objects to build your search queries as it's shown in the example below.
For more information about the match query syntax and additional parameters that can be added to  request and response, please check: https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP.


### Example

#### SearchRequest
```python
import manticoresearch
from manticoresearch.api import search_api
from manticoresearch.model.search_request import SearchRequest
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.search_response import SearchResponse
from pprint import pprint

#### Defining the host is optional and defaults to http://127.0.0.1:9308
#### See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


#### Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    search_request = SearchRequest(
        index="test",
        query={},
        fulltext_filter={},
        attr_filter={},
        limit=1,
        offset=1,
        max_matches=1,
        sort=[],
        sort_old=[{"test":"asc"},"id"],
        aggs=[
            Aggregation(
                name="agg1",
                field="field1",
                size=10,
            ),
        ],
        expressions=[
            {},
        ],
        highlight=Highlight(
            fieldnames=["title","content"],
            fields=[
                HighlightField(
                    name="name_example",
                    limit=256,
                    limit_words=0,
                    limit_snippets=0,
                ),
            ],
            encoder="default",
            highlight_query={},
            pre_tags="<strong>",
            post_tags="</strong>",
            no_match_size=0,
            fragment_size=256,
            number_of_fragments=0,
            limit=256,
            limit_words=0,
            limit_snippets=0,
            limits_per_field=False,
            use_boundaries=False,
            force_all_words=False,
            allow_empty=False,
            emit_zones=False,
            force_snippets=False,
            around=5,
            start_snippet_id=1,
            html_strip_mode="none",
            snippet_boundary="sentence",
        ),
        source={},
        options={},
        profile=True,
        track_scores=True,
    ) # SearchRequest  

    # example passing only required values which don't have defaults set
    try:
        # Performs a search
        api_response = api_instance.search(search_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)


```
#### Building a search request with auxiliary objects

[[Docs on search options in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Options#Search-options)
```python
    #Setting a search index:
    search_req = manticoresearch.model.SearchRequest()
    search_req.index = 'test'
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
    
    #Setting extra search settings:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.offset = 0
    search_req.limit = 10
    search_req.profile = True
    search_req.options = {'ranker': 'bm25'}
    search_req.options['retry_count'] = 2
    
    api_response = api_instance.search(search_req)
    pprint(api_response)

    #Setting the `_source` property with a single field:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.source = 'field1'
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
    
    #Setting the `_source` property with multiple fields:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.source = ['field1', 'field2*']
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

##### SourceByRules

[[SourceByRules - input parameters]](SourceByRules.md)

[[Docs on the `source` property ]](https://manual.manticoresearch.com/Searching/Search_results#Source-selection)
```python
    #Setting the `_source` property with an auxillary SourceByRules object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.source = manticoresearch.model.SourceByRules()
    search_req.source.includes = ['field1', 'field2*']
    search_req.source.excludes = ['field3']
    
    api_response = api_instance.search(search_req)
    pprint(api_response)

##### Sort
```python
    #Setting the `sort` property:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.sort = ['body']
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

##### SortOrder
##### SortMVA

[[SortOrder - input parameters]](SortOrder.md)
[[SortMVA - input parameters]](SortMVA.md)

[[Docs on sorting in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Sorting_and_ranking#HTTP)
```python
    #Setting the `sort` property with auxiliary objects
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.sort = ['body']
    sort2 = manticoresearch.model.SortOrder('price', 'desc')
    sort3 = manticoresearch.model.SortMVA('codes', 'desc', 'max')
    search_req.sort += [sort2,sort3]
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

##### Expressions

[[Docs on expressions in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Expressions#Expressions-in-HTTP-JSON)
```python    
    #Setting the `expressions` property:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    expr = {'expr': 'min(price,15)'}
    search_req.expressions = [expr]
    search_req.expressions += [ {'expr2': 'max(price,15)'} ]
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

##### Aggregation

[[Aggregation - input parameters]](Aggregation.md)

[[Docs on aggregations in Manticore Search Manual](https://manual.manticoresearch.com/Searching/Faceted_search#Aggregations)
```python    
    #Setting the `aggs` property with an auxiliary object:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    agg1 = manticoresearch.model.Aggregation('agg1', 'body', 10)
    search_req.aggs = [agg1] + [ manticoresearch.model.Aggregation('agg2', 'price') ]
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

##### Highlight

[[Highlight - input parameters]](Highlight.md)

[[Docs on highlighting in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Highlighting#Highlighting)
```python
    #Settting the `highlight` property with an auxiliary object:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    highlight = manticoresearch.model.Highlight()
    highlight.fieldnames = ['body']
    highlight.post_tags = '</post_tag>'
    highlight.encoder = 'default'
    highlight.snippet_boundary = 'sentence'
    search_req.highlight = highlight
    
    api_response = api_instance.search(search_req)
    pprint(api_response) 
```

###### HighlightField

[[HighlightField - input parameters]](HighlightField.md)

[[Docs on highlight fields in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Highlighting#Highlighting)
```python
    #Settting the `highlight.fields` property with an auxiliary HighlightField object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    highlightField = manticoresearch.model.HighlightField('body')
    highlightField2 = manticoresearch.model.HighlightField('price', 5, 10)
    highlight.fields = [highlightField, highlightField2]
    search_req.highlight = highlight
    
    api_response = api_instance.search(search_req)
    pprint(api_response) 
```

##### FulltextFilter

[[Docs on fulltext filters in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP)
```python
    #Setting the `fulltext_filter` property using different fulltext filter objects:
    
    search_req = manticoresearch.model.SearchRequest(index='test')
```

###### QueryFilter

[[QueryFilter - input parameters]](QueryFilter.md)
```python    
	#Using a QueryFilter object
    search_req.fulltext_filter = manticoresearch.model.QueryFilter('test')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### MatchFilter

[[MatchFilter - input parameters]](MatchFilter.md)
```python    
    #Using a MatchFilter object
    search_req = manticoresearch.model.SearchRequestindex='test'()
    
    search_req.fulltext_filter = manticoresearch.model.MatchFilter('test', 'title')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### MatchPhraseFilter

[[MatchPhraseFilter - input parameters]](MatchPhraseFilter.md)
```python    
    #Using a MatchPhraseFilter object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.fulltext_filter = manticoresearch.model.MatchPhraseFilter('test phrase', 'title')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### MatchOpFilter

[[MatchOpFilter - input parameters]](MatchOpFilter.md)
```python    
	#Using a MatchOpFilter object
    search_req.fulltext_filter = manticoresearch.model.MatchOpFilter('test1 test2', 'title', 'and')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

##### AttrFilter
###### EqualsFilter

[[EqualsFilter - input parameters]](EqualsFilter.md)

[[Docs on equality filters in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Filters#Equality-filters)
```python
    #Setting the `attr_filter` property using different attribute filter objects:
    
    #Using an EqualsFilter object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.attr_filter = manticoresearch.model.EqualsFilter('price', 20)
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### InFilter

[[InFilter - input parameters]](InFilter.md)

[[Docs on set filters in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Filters#Set-filters)
```python
    #Using an InFilter object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    inFilter = manticoresearch.model.InFilter('price', [1,2])
    inFilter.values += [10,11]
    search_req.attr_filter = inFilter
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### RangeFilter

[[RangeFilter - input parameters]](RangeFilter.md)

[[Docs on range filters in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Filters#Range-filters)
```python
    #Using a RangeFilter object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    rangeFilter = manticoresearch.model.RangeFilter('price', lte = 20)
    rangeFilter.gte = 5
    rangeFilter.gt = 100
    rangeFilter.lt = 200
    search_req.attr_filter = rangeFilter
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### GeoDistanceFilter

[[GeoDistanceFilter - input parameters]](GeoDistanceFilter.md)

[[Docs on geo distance filters in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Filters#Geo-distance-filters)
```python
    #Using a GeoFilter object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    geoFilter = manticoresearch.model.GeoDistanceFilter(location_anchor={'lat':10,'lon':20}, location_source='field1,field2')
    geoFilter.location_source='field3,field4'
    geoFilter.distance_type='adaptive'
    geoFilter.distance='100 km'
    search_req.attr_filter = geoFilter
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

###### BoolFilter

[[BoolFilter - input parameters]](BoolFilter.md)

[[Docs on bool queries in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Filters#bool-query)
```python
    #Setting the `attr_filter` property using bool filter object:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    boolFilter = manticoresearch.model.BoolFilter()
    boolFilter.must = [ manticoresearch.model.EqualsFilter('body', 'test') ]
    search_req.attr_filter = boolFilter
    api_response = api_instance.search(search_req)
    pprint(api_response)
    
    boolFilter = manticoresearch.model.BoolFilter()
    boolFilter.must_not = [ manticoresearch.model.EqualsFilter('body', 'test') ]
    search_req.attr_filter = boolFilter
    api_response = api_instance.search(search_req)
    pprint(api_response)
    
    #Using nested bool filters
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    fulltext_filter = manticoresearch.model.MatchFilter('test', 'title')
    nestedBoolFilter = manticoresearch.model.BoolFilter()
    nestedBoolFilter.should = [manticoresearch.model.EqualsFilter('code', 'a'), fulltext_filter]
    
    boolFilter.must = [nestedBoolFilter]
    boolFilter.must += [ manticoresearch.model.EqualsFilter('price', 10) ]
    search_req.attr_filter = boolFilter
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

#### Example of how to build search requests using the alternative way with a single dictionary object 
```python
    search_req = '{"index":"hn_small","query":{"query_string":"@comment_text \"find joe fast \"/2"}, "_source": ["story_author","comment_author"], "limit":1}'

    api_response = api_instance.search(search_req)
    pprint(api_response)
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

#### Defining the host is optional and defaults to http://127.0.0.1:9308
#### See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


#### Enter a context with an instance of the API client
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
