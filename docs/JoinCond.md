# JoinCond

Object representing the conditions used to perform the join operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to join on | 
**table** | **str** | Joined table | 
**query** | [**FulltextFilter**](FulltextFilter.md) |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from manticoresearch.models.join_cond import JoinCond

# TODO update the JSON string below
json = "{}"
# create an instance of JoinCond from a JSON string
join_cond_instance = JoinCond.from_json(json)
# print the JSON string representation of the object
print(JoinCond.to_json())

# convert the object into a dict
join_cond_dict = join_cond_instance.to_dict()
# create an instance of JoinCond from a dict
join_cond_from_dict = JoinCond.from_dict(join_cond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


