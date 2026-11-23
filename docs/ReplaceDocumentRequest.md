# ReplaceDocumentRequest

Object containing the document data for replacing an existing document in a table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc** | **object** | Object containing the new document data to replace the existing one. | 

## Example

```python
from manticoresearch.models.replace_document_request import ReplaceDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceDocumentRequest from a JSON string
replace_document_request_instance = ReplaceDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceDocumentRequest.to_json())

# convert the object into a dict
replace_document_request_dict = replace_document_request_instance.to_dict()
# create an instance of ReplaceDocumentRequest from a dict
replace_document_request_from_dict = ReplaceDocumentRequest.from_dict(replace_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


