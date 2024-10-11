# AggCompositeSource

Object containing terms used for composite aggregation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms** | [**AggCompositeTerm**](AggCompositeTerm.md) |  | 

## Example

```python
from manticoresearch.models.agg_composite_source import AggCompositeSource

# TODO update the JSON string below
json = "{}"
# create an instance of AggCompositeSource from a JSON string
agg_composite_source_instance = AggCompositeSource.from_json(json)
# print the JSON string representation of the object
print(AggCompositeSource.to_json())

# convert the object into a dict
agg_composite_source_dict = agg_composite_source_instance.to_dict()
# create an instance of AggCompositeSource from a dict
agg_composite_source_from_dict = AggCompositeSource.from_dict(agg_composite_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


