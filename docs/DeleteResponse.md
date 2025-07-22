# DeleteResponse

Response object for successful delete request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | The name of the table from which the document was deleted | [optional] 
**deleted** | **int** | Number of documents deleted | [optional] 
**id** | **int** | The ID of the deleted document. If multiple documents are deleted, the ID of the first deleted document is returned | [optional] 
**found** | **bool** | Indicates whether any documents to be deleted were found | [optional] 
**result** | **str** | Result of the delete operation, typically &#39;deleted&#39; | [optional] 

## Example

```python
from manticoresearch.models.delete_response import DeleteResponse

# create an instance of DeleteResponse from a JSON string
delete_response_instance = DeleteResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteResponse.to_json())

# convert the object into a dict
delete_response_dict = delete_response_instance.to_dict()
# create an instance of DeleteResponse from a dict
delete_response_from_dict = DeleteResponse.from_dict(delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


