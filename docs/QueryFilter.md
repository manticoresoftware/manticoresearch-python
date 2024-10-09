# QueryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **object** |  | [optional] 
**match** | **object** |  | [optional] 
**match_phrase** | **object** |  | [optional] 
**match_all** | **object** |  | [optional] 
**bool** | [**BoolFilter**](BoolFilter.md) |  | [optional] 
**equals** | **object** |  | [optional] 
**var_in** | **object** |  | [optional] 
**range** | **object** |  | [optional] 
**geo_distance** | [**GeoDistance**](GeoDistance.md) |  | [optional] 

## Example

```python
from manticoresearch.models.query_filter import QueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilter from a JSON string
query_filter_instance = QueryFilter.from_json(json)
# print the JSON string representation of the object
print(QueryFilter.to_json())

# convert the object into a dict
query_filter_dict = query_filter_instance.to_dict()
# create an instance of QueryFilter from a dict
query_filter_from_dict = QueryFilter.from_dict(query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


