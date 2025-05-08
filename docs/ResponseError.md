# ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Type or category of the error | 
**reason** | **object** | Detailed explanation of why the error occurred | [optional] 
**table** | **object** | The table related to the error, if applicable | [optional] 

## Example

```python
from manticoresearch.models.response_error import ResponseError

# create an instance of ResponseError from a JSON string
response_error_instance = ResponseError.from_json(json)
# print the JSON string representation of the object
print(ResponseError.to_json())

# convert the object into a dict
response_error_dict = response_error_instance.to_dict()
# create an instance of ResponseError from a dict
response_error_from_dict = ResponseError.from_dict(response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


