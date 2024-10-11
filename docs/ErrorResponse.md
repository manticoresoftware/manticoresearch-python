# ErrorResponse

Error response object containing information about the error and a status code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ResponseError**](ResponseError.md) |  | 
**status** | **int** | HTTP status code of the error response | [optional] [default to 500]

## Example

```python
from manticoresearch.models.error_response import ErrorResponse

# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


