# MatchAllFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_all** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.match_all_filter import MatchAllFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAllFilter from a JSON string
match_all_filter_instance = MatchAllFilter.from_json(json)
# print the JSON string representation of the object
print(MatchAllFilter.to_json())

# convert the object into a dict
match_all_filter_dict = match_all_filter_instance.to_dict()
# create an instance of MatchAllFilter from a dict
match_all_filter_from_dict = MatchAllFilter.from_dict(match_all_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


