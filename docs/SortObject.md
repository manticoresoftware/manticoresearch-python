# SortObject

Request object with defined properties used for sorting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.sort_object import SortObject

# TODO update the JSON string below
json = "{}"
# create an instance of SortObject from a JSON string
sort_object_instance = SortObject.from_json(json)
# print the JSON string representation of the object
print(SortObject.to_json())

# convert the object into a dict
sort_object_dict = sort_object_instance.to_dict()
# create an instance of SortObject from a dict
sort_object_from_dict = SortObject.from_dict(sort_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


