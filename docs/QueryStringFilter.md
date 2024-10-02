# QueryStringFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.query_string_filter import QueryStringFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QueryStringFilter from a JSON string
query_string_filter_instance = QueryStringFilter.from_json(json)
# print the JSON string representation of the object
print(QueryStringFilter.to_json())

# convert the object into a dict
query_string_filter_dict = query_string_filter_instance.to_dict()
# create an instance of QueryStringFilter from a dict
query_string_filter_from_dict = QueryStringFilter.from_dict(query_string_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


