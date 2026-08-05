# SqlResponse

List of responses from executed SQL queries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | **object** |  | 
**took** | **float** |  | [optional] 
**timed_out** | **bool** |  | [optional] 

## Example

```python
from manticoresearch.models.sql_response import SqlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SqlResponse from a JSON string
sql_response_instance = SqlResponse.from_json(json)
# print the JSON string representation of the object
print(SqlResponse.to_json())

# convert the object into a dict
sql_response_dict = sql_response_instance.to_dict()
# create an instance of SqlResponse from a dict
sql_response_from_dict = SqlResponse.from_dict(sql_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


