# KnnDocIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**k** | **int** |  | [optional] 
**ef** | **int** |  | [optional] 
**doc_id** | **int** |  | 

## Example

```python
from manticoresearch.models.knn_doc_id_request import KnnDocIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnnDocIdRequest from a JSON string
knn_doc_id_request_instance = KnnDocIdRequest.from_json(json)
# print the JSON string representation of the object
print(KnnDocIdRequest.to_json())

# convert the object into a dict
knn_doc_id_request_dict = knn_doc_id_request_instance.to_dict()
# create an instance of KnnDocIdRequest from a dict
knn_doc_id_request_from_dict = KnnDocIdRequest.from_dict(knn_doc_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


