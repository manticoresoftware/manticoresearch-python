# AggregationCompositeSourcesInnerValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms** | [**AggregationCompositeSourcesInnerValueTerms**](AggregationCompositeSourcesInnerValueTerms.md) |  | [optional] 

## Example

```python
from manticoresearch.models.aggregation_composite_sources_inner_value import AggregationCompositeSourcesInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationCompositeSourcesInnerValue from a JSON string
aggregation_composite_sources_inner_value_instance = AggregationCompositeSourcesInnerValue.from_json(json)
# print the JSON string representation of the object
print(AggregationCompositeSourcesInnerValue.to_json())

# convert the object into a dict
aggregation_composite_sources_inner_value_dict = aggregation_composite_sources_inner_value_instance.to_dict()
# create an instance of AggregationCompositeSourcesInnerValue from a dict
aggregation_composite_sources_inner_value_from_dict = AggregationCompositeSourcesInnerValue.from_dict(aggregation_composite_sources_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


