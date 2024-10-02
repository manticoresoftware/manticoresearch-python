# JoinInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | [**List[JoinInnerOnInner]**](JoinInnerOnInner.md) |  | 
**query** | [**FulltextFilter**](FulltextFilter.md) |  | [optional] 
**table** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from manticoresearch.models.join_inner import JoinInner

# TODO update the JSON string below
json = "{}"
# create an instance of JoinInner from a JSON string
join_inner_instance = JoinInner.from_json(json)
# print the JSON string representation of the object
print(JoinInner.to_json())

# convert the object into a dict
join_inner_dict = join_inner_instance.to_dict()
# create an instance of JoinInner from a dict
join_inner_from_dict = JoinInner.from_dict(join_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


