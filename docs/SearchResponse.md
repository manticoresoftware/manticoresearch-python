# SearchResponse

Response object containing search results. For conversational search requests that include a `chat` object, the optional chat fields below are also populated. For conversational search response fields see [Conversational search](https://manual.manticoresearch.com/Searching/Conversational_search#Response) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**took** | **int** | Time taken to execute the search | [optional] 
**timed_out** | **bool** | Indicates whether the search operation timed out | [optional] 
**aggregations** | [**Dict[str, AggBucketsResult]**](AggBucketsResult.md) | Aggregated search results grouped by the specified criteria. Each named aggregation typically contains a &#x60;buckets&#x60; array (or keyed map) of bucket objects with &#x60;key&#x60;, &#x60;doc_count&#x60;, and optional &#x60;status&#x60;.  | [optional] 
**hits** | [**SearchResponseHits**](SearchResponseHits.md) |  | [optional] 
**profile** | **object** | Profile information about the search execution, if profiling is enabled | [optional] 
**scroll** | **str** | Scroll token to be used fo pagination | [optional] 
**warning** | **object** | Warnings encountered during the search operation | [optional] 
**conversation_uuid** | **str** | Existing or generated conversation id (conversational search) | [optional] 
**user_query** | **str** | Original user query (conversational search) | [optional] 
**search_query** | **str** | Standalone search query used for KNN retrieval (conversational search) | [optional] 
**response** | **str** | LLM answer as generated (conversational search) | [optional] 
**sources** | **str** | JSON string containing retrieved source rows used as LLM context (conversational search).  | [optional] 

## Example

```python
from manticoresearch.models.search_response import SearchResponse

# TODO update the JSON string below
json = "{}"
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


