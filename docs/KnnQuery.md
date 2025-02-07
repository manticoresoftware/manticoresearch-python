# KnnQuery

Object representing a k-nearest neighbor search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Field to perform the k-nearest neighbor search on | 
**k** | **int** | The number of nearest neighbors to return | 
**query_vector** | **List[float]** | The vector used as input for the KNN search | [optional] 
**doc_id** | **int** | The docuemnt ID used as input for the KNN search | [optional] 
**ef** | **int** | Optional parameter controlling the accuracy of the search | [optional] 
**filter** | [**QueryFilter**](QueryFilter.md) |  | [optional] 

## Example

```python
from manticoresearch.models.knn_query import KnnQuery

# create an instance of KnnQuery from a JSON string
knn_query_instance = KnnQuery.from_json(json)
# print the JSON string representation of the object
print(KnnQuery.to_json())

# convert the object into a dict
knn_query_dict = knn_query_instance.to_dict()
# create an instance of KnnQuery from a dict
knn_query_from_dict = KnnQuery.from_dict(knn_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


