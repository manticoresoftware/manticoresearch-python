# Hybrid

Perform hybrid search on tables with auto-embeddings. Runs full-text and vector search and fuses results with RRF.  For more information see [Hybrid search](https://manual.manticoresearch.com/Searching/Hybrid_search#Simplified-JSON-syntax:-hybrid) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search query string | 
**var_field** | **str** | Vector field name.  | [optional] 

## Example

```python
from manticoresearch.models.hybrid import Hybrid

# TODO update the JSON string below
json = "{}"
# create an instance of Hybrid from a JSON string
hybrid_instance = Hybrid.from_json(json)
# print the JSON string representation of the object
print(Hybrid.to_json())

# convert the object into a dict
hybrid_dict = hybrid_instance.to_dict()
# create an instance of Hybrid from a dict
hybrid_from_dict = Hybrid.from_dict(hybrid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


