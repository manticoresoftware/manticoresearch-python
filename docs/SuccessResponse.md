# SuccessResponse

Success response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**created** | **bool** |  | [optional] 
**result** | **str** |  | [optional] 
**found** | **bool** |  | [optional] 
**status** | **int** |  | [optional] 

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


