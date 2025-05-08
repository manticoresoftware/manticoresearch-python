# AggCompositeTerm

Object representing a term to be used in composite aggregation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of field to operate with | 

## Example

```python
from manticoresearch.models.agg_composite_term import AggCompositeTerm

# create an instance of AggCompositeTerm from a JSON string
agg_composite_term_instance = AggCompositeTerm.from_json(json)
# print the JSON string representation of the object
print(AggCompositeTerm.to_json())

# convert the object into a dict
agg_composite_term_dict = agg_composite_term_instance.to_dict()
# create an instance of AggCompositeTerm from a dict
agg_composite_term_from_dict = AggCompositeTerm.from_dict(agg_composite_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


