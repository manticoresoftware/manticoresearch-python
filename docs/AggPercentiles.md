# AggPercentiles

Object to use percentile values in aggregation. For more information see [Grouping](https://manual.manticoresearch.com/Searching/Grouping#PERCENTILES(),-PERCENTILE_RANKS(),-MEDIAN_ABSOLUTE_DEVIATION()) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Numeric field to calculate percentiles for | 
**values** | **List[float]** | Percentile points to compute (0-100). Defaults to 1, 5, 25, 50, 75, 95, and 99 when omitted.  | [optional] 
**keyed** | **bool** | Return an object keyed by percentile when true, or an array when false. Default is false.  | [optional] 
**tdigest** | [**AggTDigest**](AggTDigest.md) |  | [optional] 

## Example

```python
from manticoresearch.models.agg_percentiles import AggPercentiles

# TODO update the JSON string below
json = "{}"
# create an instance of AggPercentiles from a JSON string
agg_percentiles_instance = AggPercentiles.from_json(json)
# print the JSON string representation of the object
print(AggPercentiles.to_json())

# convert the object into a dict
agg_percentiles_dict = agg_percentiles_instance.to_dict()
# create an instance of AggPercentiles from a dict
agg_percentiles_from_dict = AggPercentiles.from_dict(agg_percentiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


