# SearchRequest

Payload for search operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | 
**query** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**sort** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**aggs** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**expressions** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**highlight** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**source** | **[str]** |  | [optional] 
**profile** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


