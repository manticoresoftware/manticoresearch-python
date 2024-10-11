# BoolFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**must** | [**List[QueryFilter]**](QueryFilter.md) | Query clauses that must match for the document to be included | [optional] 
**must_not** | [**List[QueryFilter]**](QueryFilter.md) | Query clauses that must not match for the document to be included | [optional] 
**should** | [**List[QueryFilter]**](QueryFilter.md) | Query clauses that should be matched, but are not required | [optional] 

## Example

```python
from manticoresearch.models.bool_filter import BoolFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BoolFilter from a JSON string
bool_filter_instance = BoolFilter.from_json(json)
# print the JSON string representation of the object
print(BoolFilter.to_json())

# convert the object into a dict
bool_filter_dict = bool_filter_instance.to_dict()
# create an instance of BoolFilter from a dict
bool_filter_from_dict = BoolFilter.from_dict(bool_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


