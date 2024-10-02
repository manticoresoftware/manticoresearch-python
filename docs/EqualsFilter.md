# EqualsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equals** | [**EqualsFilterEquals**](EqualsFilterEquals.md) |  | [optional] 

## Example

```python
from manticoresearch.models.equals_filter import EqualsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EqualsFilter from a JSON string
equals_filter_instance = EqualsFilter.from_json(json)
# print the JSON string representation of the object
print(EqualsFilter.to_json())

# convert the object into a dict
equals_filter_dict = equals_filter_instance.to_dict()
# create an instance of EqualsFilter from a dict
equals_filter_from_dict = EqualsFilter.from_dict(equals_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


