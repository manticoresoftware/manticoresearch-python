# HighlightFieldOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fragment_size** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**limit_snippets** | **int** |  | [optional] 
**limit_words** | **int** |  | [optional] 
**number_of_fragments** | **int** |  | [optional] 

## Example

```python
from manticoresearch.models.highlight_field_option import HighlightFieldOption

# TODO update the JSON string below
json = "{}"
# create an instance of HighlightFieldOption from a JSON string
highlight_field_option_instance = HighlightFieldOption.from_json(json)
# print the JSON string representation of the object
print(HighlightFieldOption.to_json())

# convert the object into a dict
highlight_field_option_dict = highlight_field_option_instance.to_dict()
# create an instance of HighlightFieldOption from a dict
highlight_field_option_from_dict = HighlightFieldOption.from_dict(highlight_field_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


