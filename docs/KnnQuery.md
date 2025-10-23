# KnnQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from manticoresearch.models.knn_query import KnnQuery

# TODO update the JSON string below
json = "{}"
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


