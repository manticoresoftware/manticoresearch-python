# SearchRequest

Request object for search operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | 
**query** | [**SearchQuery**](SearchQuery.md) |  | [optional] 
**join** | [**List[Join]**](Join.md) |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**knn** | [**KnnQuery**](KnnQuery.md) |  | [optional] 
**aggs** | [**Dict[str, Aggregation]**](Aggregation.md) |  | [optional] 
**expressions** | **Dict[str, str]** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**options** | **object** |  | [optional] 
**profile** | **bool** |  | [optional] 
**sort** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**track_scores** | **bool** |  | [optional] 

## Example

```python
from manticoresearch.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
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


