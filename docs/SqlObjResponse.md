# SqlObjResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | **object** |  | 
**took** | **float** |  | [optional] 
**timed_out** | **bool** |  | [optional] 

## Example

```python
from manticoresearch.models.sql_obj_response import SqlObjResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SqlObjResponse from a JSON string
sql_obj_response_instance = SqlObjResponse.from_json(json)
# print the JSON string representation of the object
print(SqlObjResponse.to_json())

# convert the object into a dict
sql_obj_response_dict = sql_obj_response_instance.to_dict()
# create an instance of SqlObjResponse from a dict
sql_obj_response_from_dict = SqlObjResponse.from_dict(sql_obj_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


