# InFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **Dict[str, List[EqualsFilterEquals]]** |  | [optional] 

## Example

```python
from manticoresearch.models.in_filter import InFilter

# TODO update the JSON string below
json = "{}"
# create an instance of InFilter from a JSON string
in_filter_instance = InFilter.from_json(json)
# print the JSON string representation of the object
print(InFilter.to_json())

# convert the object into a dict
in_filter_dict = in_filter_instance.to_dict()
# create an instance of InFilter from a dict
in_filter_from_dict = InFilter.from_dict(in_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


