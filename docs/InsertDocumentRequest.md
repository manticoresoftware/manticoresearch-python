# InsertDocumentRequest

Object containing data for inserting a new document into the table 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | Name of the table to insert the document into | 
**cluster** | **str** | Name of the cluster to insert the document into | [optional] 
**id** | **int** | Document ID. If not provided, an ID will be auto-generated  | [optional] 
**doc** | **object** | Object containing document data  | 

## Example

```python
from manticoresearch.models.insert_document_request import InsertDocumentRequest

# create an instance of InsertDocumentRequest from a JSON string
insert_document_request_instance = InsertDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(InsertDocumentRequest.to_json())

# convert the object into a dict
insert_document_request_dict = insert_document_request_instance.to_dict()
# create an instance of InsertDocumentRequest from a dict
insert_document_request_from_dict = InsertDocumentRequest.from_dict(insert_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


