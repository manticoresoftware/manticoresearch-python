# SuccessResponse

Response object indicating the success of an operation, such as inserting or updating a document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | Name of the document table | [optional] 
**id** | **int** | ID of the document affected by the request operation | [optional] 
**created** | **bool** | Indicates whether the document was created as a result of the operation | [optional] 
**result** | **str** | Result of the operation, typically &#39;created&#39;, &#39;updated&#39;, or &#39;deleted&#39; | [optional] 
**found** | **bool** | Indicates whether the document was found in the table | [optional] 
**status** | **int** | HTTP status code representing the result of the operation | [optional] 

## Example

```python
from manticoresearch.models.success_response import SuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponse from a JSON string
success_response_instance = SuccessResponse.from_json(json)
# print the JSON string representation of the object
print(SuccessResponse.to_json())

# convert the object into a dict
success_response_dict = success_response_instance.to_dict()
# create an instance of SuccessResponse from a dict
success_response_from_dict = SuccessResponse.from_dict(success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


