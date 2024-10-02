# FulltextFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**MatchFilterMatch**](MatchFilterMatch.md) |  | [optional] 
**match_all** | **str** |  | [optional] 
**match_phrase** | **Dict[str, str]** |  | [optional] 
**query_string** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.fulltext_filter import FulltextFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextFilter from a JSON string
fulltext_filter_instance = FulltextFilter.from_json(json)
# print the JSON string representation of the object
print(FulltextFilter.to_json())

# convert the object into a dict
fulltext_filter_dict = fulltext_filter_instance.to_dict()
# create an instance of FulltextFilter from a dict
fulltext_filter_from_dict = FulltextFilter.from_dict(fulltext_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


