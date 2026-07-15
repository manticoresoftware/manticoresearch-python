# AggPercentileRanks

Object to use percentile ranks in aggregation. For more information see [Grouping](https://manual.manticoresearch.com/Searching/Grouping#PERCENTILE_RANKS(),-MEDIAN_ABSOLUTE_DEVIATION()) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Numeric field to calculate percentile ranks for | 
**values** | **List[float]** | Input values to rank | 
**keyed** | **bool** | Return an object keyed by input value when true, or an array when false. Default is false.  | [optional] 
**tdigest** | [**AggTDigest**](AggTDigest.md) |  | [optional] 

## Example

```python
from manticoresearch.models.agg_percentile_ranks import AggPercentileRanks

# TODO update the JSON string below
json = "{}"
# create an instance of AggPercentileRanks from a JSON string
agg_percentile_ranks_instance = AggPercentileRanks.from_json(json)
# print the JSON string representation of the object
print(AggPercentileRanks.to_json())

# convert the object into a dict
agg_percentile_ranks_dict = agg_percentile_ranks_instance.to_dict()
# create an instance of AggPercentileRanks from a dict
agg_percentile_ranks_from_dict = AggPercentileRanks.from_dict(agg_percentile_ranks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


