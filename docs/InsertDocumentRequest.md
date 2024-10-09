# InsertDocumentRequest

Object with document data. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** | Name of the index | 
**cluster** | **str** | cluster name | [optional] 
**id** | **int** | Document ID.  | [optional] 
**doc** | **object** | Object with document data  | 

## Example

```python
from manticoresearch.models.insert_document_request import InsertDocumentRequest

# TODO update the JSON string below
json = "{}"
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


