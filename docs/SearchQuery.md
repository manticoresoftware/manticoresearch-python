# SearchQuery

Defines a query structure for performing search operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_string** | **object** | Filter object defining a query string | [optional] 
**match** | **object** | Filter object defining a match keyword passed as a string or in a Match object | [optional] 
**match_phrase** | **object** | Filter object defining a match phrase | [optional] 
**match_all** | **object** | Filter object to select all documents | [optional] 
**bool** | [**BoolFilter**](BoolFilter.md) |  | [optional] 
**equals** | **object** |  | [optional] 
**var_in** | **object** | Filter to match a given set of attribute values. | [optional] 
**range** | **object** | Filter to match a given range of attribute values passed in Range objects | [optional] 
**geo_distance** | [**GeoDistance**](GeoDistance.md) |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 

## Example

```python
from manticoresearch.models.search_query import SearchQuery

# create an instance of SearchQuery from a JSON string
search_query_instance = SearchQuery.from_json(json)
# print the JSON string representation of the object
print(SearchQuery.to_json())

# convert the object into a dict
search_query_dict = search_query_instance.to_dict()
# create an instance of SearchQuery from a dict
search_query_from_dict = SearchQuery.from_dict(search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


