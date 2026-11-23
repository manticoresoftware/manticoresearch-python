# MatchAll

Filter helper object defining the 'match all'' condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **str** |  | 

## Example

```python
from manticoresearch.models.match_all import MatchAll

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAll from a JSON string
match_all_instance = MatchAll.from_json(json)
# print the JSON string representation of the object
print(MatchAll.to_json())

# convert the object into a dict
match_all_dict = match_all_instance.to_dict()
# create an instance of MatchAll from a dict
match_all_from_dict = MatchAll.from_dict(match_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


