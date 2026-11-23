# HighlightFieldOption

Options for controlling the behavior of highlighting on a per-field basis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fragment_size** | **int** | Maximum size of the text fragments in highlighted snippets per field | [optional] 
**limit** | **int** | Maximum size of snippets per field | [optional] 
**limit_snippets** | **int** | Maximum number of snippets per field | [optional] 
**limit_words** | **int** | Maximum number of words per field | [optional] 
**number_of_fragments** | **int** | Total number of highlighted fragments per field | [optional] 

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


