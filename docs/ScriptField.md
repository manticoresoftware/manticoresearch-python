# ScriptField

Named expression computed at search time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | [**ScriptFieldScript**](ScriptFieldScript.md) |  | 

## Example

```python
from manticoresearch.models.script_field import ScriptField

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptField from a JSON string
script_field_instance = ScriptField.from_json(json)
# print the JSON string representation of the object
print(ScriptField.to_json())

# convert the object into a dict
script_field_dict = script_field_instance.to_dict()
# create an instance of ScriptField from a dict
script_field_from_dict = ScriptField.from_dict(script_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


