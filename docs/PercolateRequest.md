# PercolateRequest

Object containing the query for percolating documents against stored queries in a percolate table

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**PercolateRequestQuery**](PercolateRequestQuery.md) |  | 

## Example

```python
from manticoresearch.models.percolate_request import PercolateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PercolateRequest from a JSON string
percolate_request_instance = PercolateRequest.from_json(json)
# print the JSON string representation of the object
print(PercolateRequest.to_json())

# convert the object into a dict
percolate_request_dict = percolate_request_instance.to_dict()
# create an instance of PercolateRequest from a dict
percolate_request_from_dict = PercolateRequest.from_dict(percolate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


