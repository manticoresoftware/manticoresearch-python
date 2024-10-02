# MatchPhraseFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_phrase** | **Dict[str, str]** |  | [optional] 

## Example

```python
from manticoresearch.models.match_phrase_filter import MatchPhraseFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MatchPhraseFilter from a JSON string
match_phrase_filter_instance = MatchPhraseFilter.from_json(json)
# print the JSON string representation of the object
print(MatchPhraseFilter.to_json())

# convert the object into a dict
match_phrase_filter_dict = match_phrase_filter_instance.to_dict()
# create an instance of MatchPhraseFilter from a dict
match_phrase_filter_from_dict = MatchPhraseFilter.from_dict(match_phrase_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


