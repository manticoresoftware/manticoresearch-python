# KnnQueryVectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**k** | **int** |  | [optional] 
**ef** | **int** |  | [optional] 
**query_vector** | **List[float]** |  | 

## Example

```python
from manticoresearch.models.knn_query_vector_request import KnnQueryVectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnnQueryVectorRequest from a JSON string
knn_query_vector_request_instance = KnnQueryVectorRequest.from_json(json)
# print the JSON string representation of the object
print(KnnQueryVectorRequest.to_json())

# convert the object into a dict
knn_query_vector_request_dict = knn_query_vector_request_instance.to_dict()
# create an instance of KnnQueryVectorRequest from a dict
knn_query_vector_request_from_dict = KnnQueryVectorRequest.from_dict(knn_query_vector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


