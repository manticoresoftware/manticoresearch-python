# QueryFilter

Object used to apply various conditions, such as full-text matching or attribute filtering, to a search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **str** | Filter object defining a query string | [optional] 
**match** | **object** | Filter object defining a match keyword passed as a string or in a Match object | [optional] 
**match_phrase** | **object** | Filter object defining a match phrase | [optional] 
**match_all** | **object** | Filter object to select all documents | [optional] 
**bool** | [**BoolFilter**](BoolFilter.md) |  | [optional] 
**equals** | **object** |  | [optional] 
**var_in** | **object** | Filter to match a given set of attribute values. | [optional] 
**range** | **object** | Filter to match a given range of attribute values passed in Range objects | [optional] 
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


