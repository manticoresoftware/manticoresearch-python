# HighlightFields

List of fields available for highlighting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from manticoresearch.models.highlight_fields import HighlightFields

# TODO update the JSON string below
json = "{}"
# create an instance of HighlightFields from a JSON string
highlight_fields_instance = HighlightFields.from_json(json)
# print the JSON string representation of the object
print(HighlightFields.to_json())

# convert the object into a dict
highlight_fields_dict = highlight_fields_instance.to_dict()
# create an instance of HighlightFields from a dict
highlight_fields_from_dict = HighlightFields.from_dict(highlight_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


