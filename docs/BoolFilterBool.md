# BoolFilterBool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**must** | [**List[QueryFilter]**](QueryFilter.md) |  | [optional] 
**must_not** | [**List[QueryFilter]**](QueryFilter.md) |  | [optional] 
**should** | [**List[QueryFilter]**](QueryFilter.md) |  | [optional] 

## Example

```python
from manticoresearch.models.bool_filter_bool import BoolFilterBool

# TODO update the JSON string below
json = "{}"
# create an instance of BoolFilterBool from a JSON string
bool_filter_bool_instance = BoolFilterBool.from_json(json)
# print the JSON string representation of the object
print(BoolFilterBool.to_json())

# convert the object into a dict
bool_filter_bool_dict = bool_filter_bool_instance.to_dict()
# create an instance of BoolFilterBool from a dict
bool_filter_bool_from_dict = BoolFilterBool.from_dict(bool_filter_bool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


