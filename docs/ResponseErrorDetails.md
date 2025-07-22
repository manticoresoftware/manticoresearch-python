# ResponseErrorDetails

Detailed error information returned in case of an error response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type or category of the error | 
**reason** | **str** | Detailed explanation of why the error occurred | [optional] 
**table** | **str** | The table related to the error, if applicable | [optional] 

## Example

```python
from manticoresearch.models.response_error_details import ResponseErrorDetails

# create an instance of ResponseErrorDetails from a JSON string
response_error_details_instance = ResponseErrorDetails.from_json(json)
# print the JSON string representation of the object
print(ResponseErrorDetails.to_json())

# convert the object into a dict
response_error_details_dict = response_error_details_instance.to_dict()
# create an instance of ResponseErrorDetails from a dict
response_error_details_from_dict = ResponseErrorDetails.from_dict(response_error_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


