# AggMedianAbsoluteDeviation

Object to use median absolute deviation in aggregation. For more information see [Grouping](https://manual.manticoresearch.com/Searching/Grouping#PERCENTILES(),-PERCENTILE_RANKS(),-MEDIAN_ABSOLUTE_DEVIATION()) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Numeric field to calculate MAD for | 
**tdigest** | [**AggTDigest**](AggTDigest.md) |  | [optional] 

## Example

```python
from manticoresearch.models.agg_median_absolute_deviation import AggMedianAbsoluteDeviation

# TODO update the JSON string below
json = "{}"
# create an instance of AggMedianAbsoluteDeviation from a JSON string
agg_median_absolute_deviation_instance = AggMedianAbsoluteDeviation.from_json(json)
# print the JSON string representation of the object
print(AggMedianAbsoluteDeviation.to_json())

# convert the object into a dict
agg_median_absolute_deviation_dict = agg_median_absolute_deviation_instance.to_dict()
# create an instance of AggMedianAbsoluteDeviation from a dict
agg_median_absolute_deviation_from_dict = AggMedianAbsoluteDeviation.from_dict(agg_median_absolute_deviation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


