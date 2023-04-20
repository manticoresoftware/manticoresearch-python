# Highlight

Query HIGHLIGHT expression
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldnames** | **[str]** |  | [optional] 
**fields** | [**[HighlightField]**](HighlightField.md) |  | [optional] 
**encoder** | **str** |  | [optional] 
**highlight_query** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**pre_tags** | **str** |  | [optional] [default to "<strong>"]
**post_tags** | **str** |  | [optional] [default to "</strong>"]
**no_match_size** | **int** |  | [optional] 
**fragment_size** | **int** |  | [optional] [default to 256]
**number_of_fragments** | **int** |  | [optional] [default to 0]
**limit** | **int** |  | [optional] [default to 256]
**limit_words** | **int** |  | [optional] [default to 0]
**limit_snippets** | **int** |  | [optional] [default to 0]
**limits_per_field** | **bool** |  | [optional] [default to False]
**use_boundaries** | **bool** |  | [optional] [default to False]
**force_all_words** | **bool** |  | [optional] [default to False]
**allow_empty** | **bool** |  | [optional] [default to False]
**emit_zones** | **bool** |  | [optional] [default to False]
**force_snippets** | **bool** |  | [optional] [default to False]
**around** | **int** |  | [optional] [default to 5]
**start_snippet_id** | **int** |  | [optional] [default to 1]
**html_strip_mode** | **str** |  | [optional] 
**snippet_boundary** | **str** |  | [optional] 

[[Using in search requests]](SearchApi.md#Highlight)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


