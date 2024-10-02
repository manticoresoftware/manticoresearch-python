# SourceByRules

Query fields to be included/excluded to/from response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includes** | **List[str]** |  | [optional] [default to []]
**excludes** | **List[str]** |  | [optional] [default to []]

## Example

```python
from manticoresearch.models.source_by_rules import SourceByRules

# TODO update the JSON string below
json = "{}"
# create an instance of SourceByRules from a JSON string
source_by_rules_instance = SourceByRules.from_json(json)
# print the JSON string representation of the object
print(SourceByRules.to_json())

# convert the object into a dict
source_by_rules_dict = source_by_rules_instance.to_dict()
# create an instance of SourceByRules from a dict
source_by_rules_from_dict = SourceByRules.from_dict(source_by_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


