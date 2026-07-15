# JoinOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**right** | [**JoinCond**](JoinCond.md) |  | [optional] 
**left** | [**JoinCond**](JoinCond.md) |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.join_on import JoinOn

# TODO update the JSON string below
json = "{}"
# create an instance of JoinOn from a JSON string
join_on_instance = JoinOn.from_json(json)
# print the JSON string representation of the object
print(JoinOn.to_json())

# convert the object into a dict
join_on_dict = join_on_instance.to_dict()
# create an instance of JoinOn from a dict
join_on_from_dict = JoinOn.from_dict(join_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


