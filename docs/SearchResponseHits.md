# SearchResponseHits

Object containing the search hits, which represent the documents that matched the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_score** | **int** | Maximum score among the matched documents | [optional] 
**total** | **int** | Total number of matched documents | [optional] 
**total_relation** | **str** | Indicates whether the total number of hits is accurate or an estimate | [optional] 
**hits** | [**List[HitsHits]**](HitsHits.md) | Array of hit objects, each representing a matched document | [optional] 

## Example

```python
from manticoresearch.models.search_response_hits import SearchResponseHits

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseHits from a JSON string
search_response_hits_instance = SearchResponseHits.from_json(json)
# print the JSON string representation of the object
print(SearchResponseHits.to_json())

# convert the object into a dict
search_response_hits_dict = search_response_hits_instance.to_dict()
# create an instance of SearchResponseHits from a dict
search_response_hits_from_dict = SearchResponseHits.from_dict(search_response_hits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


