# SourceRules

Defines which fields to include or exclude in the response for a search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includes** | **object** | List of fields to include in the response | [optional] 
**excludes** | **object** | List of fields to exclude from the response | [optional] 

## Example

```python
from manticoresearch.models.source_rules import SourceRules

# create an instance of SourceRules from a JSON string
source_rules_instance = SourceRules.from_json(json)
# print the JSON string representation of the object
print(SourceRules.to_json())

# convert the object into a dict
source_rules_dict = source_rules_instance.to_dict()
# create an instance of SourceRules from a dict
source_rules_from_dict = SourceRules.from_dict(source_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


