# AggMetric

Metric aggregation over a numeric field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Numeric field to aggregate | 

## Example

```python
from manticoresearch.models.agg_metric import AggMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AggMetric from a JSON string
agg_metric_instance = AggMetric.from_json(json)
# print the JSON string representation of the object
print(AggMetric.to_json())

# convert the object into a dict
agg_metric_dict = agg_metric_instance.to_dict()
# create an instance of AggMetric from a dict
agg_metric_from_dict = AggMetric.from_dict(agg_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


