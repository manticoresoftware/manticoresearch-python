# BasicSearchRequest

Request object for search operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggs** | [**Aggregation**](Aggregation.md) |  | [optional] 
**expressions** | **Dict[str, str]** |  | [optional] 
**join** | [**List[JoinInner]**](JoinInner.md) |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**index** | **str** |  | 
**limit** | **int** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**options** | **object** |  | [optional] 
**profile** | **bool** |  | [optional] 
**sort** | [**List[SearchRequestParametersSortInner]**](SearchRequestParametersSortInner.md) |  | [optional] 
**source** | [**SearchRequestParametersSource**](SearchRequestParametersSource.md) |  | [optional] 
**track_scores** | **bool** |  | [optional] 
**query** | [**QueryFilter**](QueryFilter.md) |  | 

## Example

```python
from manticoresearch.models.basic_search_request import BasicSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BasicSearchRequest from a JSON string
basic_search_request_instance = BasicSearchRequest.from_json(json)
# print the JSON string representation of the object
print(BasicSearchRequest.to_json())

# convert the object into a dict
basic_search_request_dict = basic_search_request_instance.to_dict()
# create an instance of BasicSearchRequest from a dict
basic_search_request_from_dict = BasicSearchRequest.from_dict(basic_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


