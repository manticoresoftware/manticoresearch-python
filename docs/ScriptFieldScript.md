# ScriptFieldScript

Inline script used to compute a search expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline** | **str** | Expression to compute (same syntax as SQL expressions) | 

## Example

```python
from manticoresearch.models.script_field_script import ScriptFieldScript

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptFieldScript from a JSON string
script_field_script_instance = ScriptFieldScript.from_json(json)
# print the JSON string representation of the object
print(ScriptFieldScript.to_json())

# convert the object into a dict
script_field_script_dict = script_field_script_instance.to_dict()
# create an instance of ScriptFieldScript from a dict
script_field_script_from_dict = ScriptFieldScript.from_dict(script_field_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


