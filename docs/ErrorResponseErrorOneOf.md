# ErrorResponseErrorOneOf

Detailed error information from error response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**reason** | **str** |  | [optional] 
**index** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.error_response_error_one_of import ErrorResponseErrorOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseErrorOneOf from a JSON string
error_response_error_one_of_instance = ErrorResponseErrorOneOf.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseErrorOneOf.to_json())

# convert the object into a dict
error_response_error_one_of_dict = error_response_error_one_of_instance.to_dict()
# create an instance of ErrorResponseErrorOneOf from a dict
error_response_error_one_of_from_dict = ErrorResponseErrorOneOf.from_dict(error_response_error_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


