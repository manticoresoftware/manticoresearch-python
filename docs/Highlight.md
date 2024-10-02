# Highlight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fragment_size** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**limit_snippets** | **int** |  | [optional] 
**limit_words** | **int** |  | [optional] 
**number_of_fragments** | **int** |  | [optional] 
**after_match** | **str** |  | [optional] [default to '</strong>']
**allow_empty** | **bool** |  | [optional] 
**around** | **int** |  | [optional] 
**before_match** | **str** |  | [optional] [default to '<strong>']
**emit_zones** | **bool** |  | [optional] 
**encoder** | **str** |  | [optional] 
**fields** | [**HighlightAllOfFields**](HighlightAllOfFields.md) |  | [optional] 
**force_all_words** | **bool** |  | [optional] 
**force_snippets** | **bool** |  | [optional] 
**highlight_query** | [**QueryFilter**](QueryFilter.md) |  | [optional] 
**html_strip_mode** | **str** |  | [optional] 
**limits_per_field** | **bool** |  | [optional] 
**no_match_size** | **int** |  | [optional] 
**order** | **str** |  | [optional] 
**pre_tags** | **str** |  | [optional] [default to '<strong>']
**post_tags** | **str** |  | [optional] [default to '</strong>']
**start_snippet_id** | **int** |  | [optional] 
**use_boundaries** | **bool** |  | [optional] 

## Example

```python
from manticoresearch.models.highlight import Highlight

# TODO update the JSON string below
json = "{}"
# create an instance of Highlight from a JSON string
highlight_instance = Highlight.from_json(json)
# print the JSON string representation of the object
print(Highlight.to_json())

# convert the object into a dict
highlight_dict = highlight_instance.to_dict()
# create an instance of Highlight from a dict
highlight_from_dict = Highlight.from_dict(highlight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


