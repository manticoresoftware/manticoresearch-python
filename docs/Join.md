# Join


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**on** | [**List[JoinOn]**](JoinOn.md) |  | 
**query** | [**FulltextFilter**](FulltextFilter.md) |  | [optional] 
**table** | **str** |  | 

## Example

```python
from manticoresearch.models.join import Join

# TODO update the JSON string below
json = "{}"
# create an instance of Join from a JSON string
join_instance = Join.from_json(json)
# print the JSON string representation of the object
print(Join.to_json())

# convert the object into a dict
join_dict = join_instance.to_dict()
# create an instance of Join from a dict
join_from_dict = Join.from_dict(join_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


