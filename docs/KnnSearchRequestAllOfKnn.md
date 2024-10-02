# KnnSearchRequestAllOfKnn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **int** |  | 
**var_field** | **str** |  | 
**k** | **int** |  | [optional] 
**ef** | **int** |  | [optional] 
**query_vector** | **List[float]** |  | 

## Example

```python
from manticoresearch.models.knn_search_request_all_of_knn import KnnSearchRequestAllOfKnn

# TODO update the JSON string below
json = "{}"
# create an instance of KnnSearchRequestAllOfKnn from a JSON string
knn_search_request_all_of_knn_instance = KnnSearchRequestAllOfKnn.from_json(json)
# print the JSON string representation of the object
print(KnnSearchRequestAllOfKnn.to_json())

# convert the object into a dict
knn_search_request_all_of_knn_dict = knn_search_request_all_of_knn_instance.to_dict()
# create an instance of KnnSearchRequestAllOfKnn from a dict
knn_search_request_all_of_knn_from_dict = KnnSearchRequestAllOfKnn.from_dict(knn_search_request_all_of_knn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


