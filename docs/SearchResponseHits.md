# SearchResponseHits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_score** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**total_relation** | **str** |  | [optional] 
**hits** | **List[object]** |  | [optional] 

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


