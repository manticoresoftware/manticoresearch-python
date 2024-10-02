# MatchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**MatchFilterMatch**](MatchFilterMatch.md) |  | [optional] 

## Example

```python
from manticoresearch.models.match_filter import MatchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFilter from a JSON string
match_filter_instance = MatchFilter.from_json(json)
# print the JSON string representation of the object
print(MatchFilter.to_json())

# convert the object into a dict
match_filter_dict = match_filter_instance.to_dict()
# create an instance of MatchFilter from a dict
match_filter_from_dict = MatchFilter.from_dict(match_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


