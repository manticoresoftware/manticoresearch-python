# KnnSearchParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**k** | **int** |  | [optional] 
**ef** | **int** |  | [optional] 

## Example

```python
from manticoresearch.models.knn_search_parameters import KnnSearchParameters

# TODO update the JSON string below
json = "{}"
# create an instance of KnnSearchParameters from a JSON string
knn_search_parameters_instance = KnnSearchParameters.from_json(json)
# print the JSON string representation of the object
print(KnnSearchParameters.to_json())

# convert the object into a dict
knn_search_parameters_dict = knn_search_parameters_instance.to_dict()
# create an instance of KnnSearchParameters from a dict
knn_search_parameters_from_dict = KnnSearchParameters.from_dict(knn_search_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


