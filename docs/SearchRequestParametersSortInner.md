# SearchRequestParametersSortInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.search_request_parameters_sort_inner import SearchRequestParametersSortInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestParametersSortInner from a JSON string
search_request_parameters_sort_inner_instance = SearchRequestParametersSortInner.from_json(json)
# print the JSON string representation of the object
print(SearchRequestParametersSortInner.to_json())

# convert the object into a dict
search_request_parameters_sort_inner_dict = search_request_parameters_sort_inner_instance.to_dict()
# create an instance of SearchRequestParametersSortInner from a dict
search_request_parameters_sort_inner_from_dict = SearchRequestParametersSortInner.from_dict(search_request_parameters_sort_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


