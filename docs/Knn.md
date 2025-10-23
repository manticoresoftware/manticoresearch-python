# Knn

Object representing a k-nearest neighbor search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to perform the k-nearest neighbor search on | 
**k** | **int** | The number of nearest neighbors to return | 
**query** | [**KnnQuery**](KnnQuery.md) |  | [optional] 
**query_vector** | **List[float]** | The vector used as input for the KNN search | [optional] 
**doc_id** | **int** | The docuemnt ID used as input for the KNN search | [optional] 
**ef** | **int** | Optional parameter controlling the accuracy of the search | [optional] 
**filter** | [**QueryFilter**](QueryFilter.md) |  | [optional] 

## Example

```python
from manticoresearch.models.knn import Knn

# TODO update the JSON string below
json = "{}"
# create an instance of Knn from a JSON string
knn_instance = Knn.from_json(json)
# print the JSON string representation of the object
print(Knn.to_json())

# convert the object into a dict
knn_dict = knn_instance.to_dict()
# create an instance of Knn from a dict
knn_from_dict = Knn.from_dict(knn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


