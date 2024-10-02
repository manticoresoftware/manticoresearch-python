# BulkResponse

Success bulk response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** |  | [optional] 
**errors** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.bulk_response import BulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResponse from a JSON string
bulk_response_instance = BulkResponse.from_json(json)
# print the JSON string representation of the object
print(BulkResponse.to_json())

# convert the object into a dict
bulk_response_dict = bulk_response_instance.to_dict()
# create an instance of BulkResponse from a dict
bulk_response_from_dict = BulkResponse.from_dict(bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


