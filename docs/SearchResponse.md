# SearchResponse

Response object containing the results of a search request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**took** | **int** | Time taken to execute the search | [optional] 
**timed_out** | **bool** | Indicates whether the search operation timed out | [optional] 
**aggregations** | **object** | Aggregated search results grouped by the specified criteria | [optional] 
**hits** | [**SearchResponseHits**](SearchResponseHits.md) |  | [optional] 
**profile** | **object** | Profile information about the search execution, if profiling is enabled | [optional] 
**scroll** | **str** | Scroll token to be used fo pagination | [optional] 
**warning** | **object** | Warnings encountered during the search operation | [optional] 

## Example

```python
from manticoresearch.models.search_response import SearchResponse

# create an instance of SearchResponse from a JSON string
search_response_instance = SearchResponse.from_json(json)
# print the JSON string representation of the object
print(SearchResponse.to_json())

# convert the object into a dict
search_response_dict = search_response_instance.to_dict()
# create an instance of SearchResponse from a dict
search_response_from_dict = SearchResponse.from_dict(search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


