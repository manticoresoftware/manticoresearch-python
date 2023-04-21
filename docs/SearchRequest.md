# SearchRequest

Request object for search operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [default to ""]
**query** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**fulltext_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**attr_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**sort** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**sort_old** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**aggs** | [**[Aggregation]**](Aggregation.md) |  | [optional] 
**expressions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**profile** | **bool** |  | [optional] 
**track_scores** | **bool** |  | [optional] 

## Building a search request

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

### SourceByRules

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
```

### Sort
```python
    #Setting the `sort` property:
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.sort = ['body']
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

### SortOrder

[[SortOrder - input parameters]](SortOrder.md)

### SortMVA

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

### Expressions

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

### Aggregation

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

### Highlight

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

#### HighlightField

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

### FulltextFilter

[[Docs on fulltext filters in Manticore Search Manual]](https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP-JSON)
```python
    #Setting the `fulltext_filter` property using different fulltext filter objects:
    
    search_req = manticoresearch.model.SearchRequest(index='test')
```

#### QueryFilter

[[QueryFilter - input parameters]](QueryFilter.md)
```python    
    #Using a QueryFilter object
    search_req.fulltext_filter = manticoresearch.model.QueryFilter('test')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

#### MatchFilter

[[MatchFilter - input parameters]](MatchFilter.md)
```python    
    #Using a MatchFilter object
    search_req = manticoresearch.model.SearchRequestindex='test'()
    
    search_req.fulltext_filter = manticoresearch.model.MatchFilter('test', 'title')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

#### MatchPhraseFilter

[[MatchPhraseFilter - input parameters]](MatchPhraseFilter.md)
```python    
    #Using a MatchPhraseFilter object
    search_req = manticoresearch.model.SearchRequest(index='test')
    
    search_req.fulltext_filter = manticoresearch.model.MatchPhraseFilter('test phrase', 'title')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

#### MatchOpFilter

[[MatchOpFilter - input parameters]](MatchOpFilter.md)
```python    
    #Using a MatchOpFilter object
    search_req.fulltext_filter = manticoresearch.model.MatchOpFilter('test1 test2', 'title', 'and')
    
    api_response = api_instance.search(search_req)
    pprint(api_response)
```

### AttrFilter
#### EqualsFilter

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

#### InFilter

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

#### RangeFilter

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

#### GeoDistanceFilter

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

#### BoolFilter

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

## Creating a search request in an alternative way with a single dictionary object 
```python
    search_req = '{"index":"test","query":{"query_string":"find smth"}, "_source": ["field1","field2"], "limit":5}'

    api_response = api_instance.search(search_req)
    pprint(api_response)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


