# SearchRequest

Payload for search operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [default to ""]
**query** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**fulltext_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**attr_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**sort** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**sort_old** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**aggs** | [**[Aggregation]**](Aggregation.md) |  | [optional] 
**expressions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**profile** | **bool** |  | [optional] 
**track_scores** | **bool** |  | [optional] 

[[Using in search requests]](SearchApi.md#SearchRequest)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


