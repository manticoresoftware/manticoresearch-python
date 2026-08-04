# PercolateRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percolate** | **object** | Object representing the document to percolate | 

## Example

```python
from manticoresearch.models.percolate_request_query import PercolateRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PercolateRequestQuery from a JSON string
percolate_request_query_instance = PercolateRequestQuery.from_json(json)
# print the JSON string representation of the object
print(PercolateRequestQuery.to_json())

# convert the object into a dict
percolate_request_query_dict = percolate_request_query_instance.to_dict()
# create an instance of PercolateRequestQuery from a dict
percolate_request_query_from_dict = PercolateRequestQuery.from_dict(percolate_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


