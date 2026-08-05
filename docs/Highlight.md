# Highlight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fragment_size** | **int** | Maximum size of the text fragments in highlighted snippets per field | [optional] 
**limit** | **int** | Maximum size of snippets per field | [optional] 
**limit_snippets** | **int** | Maximum number of snippets per field | [optional] 
**limit_words** | **int** | Maximum number of words per field | [optional] 
**number_of_fragments** | **int** | Total number of highlighted fragments per field | [optional] 
**after_match** | **str** | Text inserted after the matched term, typically used for HTML formatting | [optional] [default to '</strong>']
**allow_empty** | **bool** | Permits an empty string to be returned as the highlighting result. Otherwise, the beginning of the original text would be returned | [optional] 
**around** | **int** | Number of words around the match to include in the highlight | [optional] 
**before_match** | **str** | Text inserted before the match, typically used for HTML formatting | [optional] [default to '<strong>']
**emit_zones** | **bool** | Emits an HTML tag with the enclosing zone name before each highlighted snippet | [optional] 
**encoder** | **str** | If set to &#39;html&#39;, retains HTML markup when highlighting | [optional] 
**fields** | [**HighlightFields**](HighlightFields.md) |  | [optional] 
**force_all_words** | **bool** | Ignores the length limit until the result includes all keywords | [optional] 
**force_snippets** | **bool** | Forces snippet generation even if limits allow highlighting the entire text | [optional] 
**highlight_query** | [**QueryFilter**](QueryFilter.md) |  | [optional] 
**html_strip_mode** | **str** | Defines the mode for handling HTML markup in the highlight | [optional] 
**limits_per_field** | **bool** | Determines whether the &#39;limit&#39;, &#39;limit_words&#39;, and &#39;limit_snippets&#39; options operate as individual limits in each field of the document | [optional] 
**no_match_size** | **int** | If set to 1, allows an empty string to be returned as a highlighting result | [optional] 
**order** | **str** | Sets the sorting order of highlighted snippets | [optional] 
**pre_tags** | **str** | Text inserted before each highlighted snippet | [optional] [default to '<strong>']
**post_tags** | **str** | Text inserted after each highlighted snippet | [optional] [default to '</strong>']
**start_snippet_id** | **int** | Sets the starting value of the %SNIPPET_ID% macro | [optional] 
**use_boundaries** | **bool** | Defines whether to additionally break snippets by phrase boundary characters | [optional] 

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


