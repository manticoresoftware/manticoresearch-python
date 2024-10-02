# KnnSearchRequest

Request object for knn search operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggs** | [**Aggregation**](Aggregation.md) |  | [optional] 
**expressions** | **Dict[str, str]** |  | [optional] 
**join** | [**List[JoinInner]**](JoinInner.md) |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**index** | **str** |  | 
**limit** | **int** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**options** | **object** |  | [optional] 
**profile** | **bool** |  | [optional] 
**sort** | [**List[SearchRequestParametersSortInner]**](SearchRequestParametersSortInner.md) |  | [optional] 
**source** | [**SearchRequestParametersSource**](SearchRequestParametersSource.md) |  | [optional] 
**track_scores** | **bool** |  | [optional] 
**knn** | [**KnnSearchRequestAllOfKnn**](KnnSearchRequestAllOfKnn.md) |  | 

## Example

```python
from manticoresearch.models.knn_search_request import KnnSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnnSearchRequest from a JSON string
knn_search_request_instance = KnnSearchRequest.from_json(json)
# print the JSON string representation of the object
print(KnnSearchRequest.to_json())

# convert the object into a dict
knn_search_request_dict = knn_search_request_instance.to_dict()
# create an instance of KnnSearchRequest from a dict
knn_search_request_from_dict = KnnSearchRequest.from_dict(knn_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


