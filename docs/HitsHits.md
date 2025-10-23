# HitsHits

Search hit representing a matched document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the matched document | [optional] 
**score** | **int** | The score of the matched document | [optional] 
**source** | **object** | The source data of the matched document | [optional] 
**knn_dist** | **float** | The knn distance of the matched document returned for knn queries | [optional] 
**highlight** | **object** | The highlighting-related data of the matched document | [optional] 
**table** | **str** | The table name of the matched document returned for percolate queries | [optional] 
**type_** | **str** | The type of the matched document returned for percolate queries | [optional] 
**fields** | **object** | The percolate-related fields of the matched document returned for percolate queries | [optional] 

## Example

```python
from manticoresearch.models.hits_hits import HitsHits

# TODO update the JSON string below
json = "{}"
# create an instance of HitsHits from a JSON string
hits_hits_instance = HitsHits.from_json(json)
# print the JSON string representation of the object
print(HitsHits.to_json())

# convert the object into a dict
hits_hits_dict = hits_hits_instance.to_dict()
# create an instance of HitsHits from a dict
hits_hits_from_dict = HitsHits.from_dict(hits_hits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


