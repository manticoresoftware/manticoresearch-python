# JoinInnerOnInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**JoinInnerOnInnerLeft**](JoinInnerOnInnerLeft.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**right** | [**JoinBasicCond**](JoinBasicCond.md) |  | [optional] 

## Example

```python
from manticoresearch.models.join_inner_on_inner import JoinInnerOnInner

# TODO update the JSON string below
json = "{}"
# create an instance of JoinInnerOnInner from a JSON string
join_inner_on_inner_instance = JoinInnerOnInner.from_json(json)
# print the JSON string representation of the object
print(JoinInnerOnInner.to_json())

# convert the object into a dict
join_inner_on_inner_dict = join_inner_on_inner_instance.to_dict()
# create an instance of JoinInnerOnInner from a dict
join_inner_on_inner_from_dict = JoinInnerOnInner.from_dict(join_inner_on_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


