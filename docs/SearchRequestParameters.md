# SearchRequestParameters


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

## Example

```python
from manticoresearch.models.search_request_parameters import SearchRequestParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestParameters from a JSON string
search_request_parameters_instance = SearchRequestParameters.from_json(json)
# print the JSON string representation of the object
print(SearchRequestParameters.to_json())

# convert the object into a dict
search_request_parameters_dict = search_request_parameters_instance.to_dict()
# create an instance of SearchRequestParameters from a dict
search_request_parameters_from_dict = SearchRequestParameters.from_dict(search_request_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


