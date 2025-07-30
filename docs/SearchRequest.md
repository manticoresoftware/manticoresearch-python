# SearchRequest

Request object for search operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | The table to perform the search on | 
**query** | [**SearchQuery**](SearchQuery.md) |  | [optional] 
**join** | [**List[Join]**](Join.md) | Join clause to combine search data from multiple tables | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**limit** | **int** | Maximum number of results to return | [optional] 
**knn** | [**KnnQuery**](KnnQuery.md) |  | [optional] 
**aggs** | [**Dict[str, Aggregation]**](Aggregation.md) | Defines aggregation settings for grouping results | [optional] 
**expressions** | **Dict[str, str]** | Expressions to calculate additional values for the result | [optional] 
**max_matches** | **int** | Maximum number of matches allowed in the result | [optional] 
**offset** | **int** | Starting point for pagination of the result | [optional] 
**options** | **object** | Additional search options | [optional] 
**profile** | **bool** | Enable or disable profiling of the search request | [optional] 
**sort** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**track_scores** | **bool** | Enable or disable result weight calculation used for sorting | [optional] 

## Example

```python
from manticoresearch.models.search_request import SearchRequest

# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


