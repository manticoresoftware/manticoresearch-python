# BulkResponse

Success response for bulk search requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[object]** | List of results | [optional] 
**errors** | **bool** | Errors occurred during the bulk operation | [optional] 
**error** | **str** | Error message describing an error if such occurred | [optional] 
**current_line** | **int** | Number of the row returned in the response | [optional] 
**skipped_lines** | **int** | Number of rows skipped in the response | [optional] 

## Example

```python
from manticoresearch.models.bulk_response import BulkResponse

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


