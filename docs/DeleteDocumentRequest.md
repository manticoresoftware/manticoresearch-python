# DeleteDocumentRequest

Payload for delete request. Documents can be deleted either one by one by specifying the document id or by providing a query object. For more information see  [Delete API](https://manual.manticoresearch.com/Deleting_documents) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | Table name | 
**cluster** | **str** | Cluster name | [optional] 
**id** | **int** | The ID of document for deletion | [optional] 
**query** | **object** | Defines the criteria to match documents for deletion | [optional] 

## Example

```python
from manticoresearch.models.delete_document_request import DeleteDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDocumentRequest from a JSON string
delete_document_request_instance = DeleteDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDocumentRequest.to_json())

# convert the object into a dict
delete_document_request_dict = delete_document_request_instance.to_dict()
# create an instance of DeleteDocumentRequest from a dict
delete_document_request_from_dict = DeleteDocumentRequest.from_dict(delete_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


