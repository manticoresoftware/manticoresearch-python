# SearchRequestParametersSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includes** | **List[str]** |  | [optional] [default to []]
**excludes** | **List[str]** |  | [optional] [default to []]

## Example

```python
from manticoresearch.models.search_request_parameters_source import SearchRequestParametersSource

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestParametersSource from a JSON string
search_request_parameters_source_instance = SearchRequestParametersSource.from_json(json)
# print the JSON string representation of the object
print(SearchRequestParametersSource.to_json())

# convert the object into a dict
search_request_parameters_source_dict = search_request_parameters_source_instance.to_dict()
# create an instance of SearchRequestParametersSource from a dict
search_request_parameters_source_from_dict = SearchRequestParametersSource.from_dict(search_request_parameters_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


