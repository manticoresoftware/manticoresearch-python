# AggDateHistogram

Object to use histograms in aggregation, i.e., grouping search results by histogram values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group by | 
**interval** | **int** | Interval of the histogram values | 
**offset** | **int** | Offset of the histogram values. Default value is 0. | [optional] 
**keyed** | **bool** | Flag that defines if a search response will be a dictionary with the bucket keys. Default value is false. | [optional] 

## Example

```python
from manticoresearch.models.agg_date_histogram import AggDateHistogram

# TODO update the JSON string below
json = "{}"
# create an instance of AggDateHistogram from a JSON string
agg_date_histogram_instance = AggDateHistogram.from_json(json)
# print the JSON string representation of the object
print(AggDateHistogram.to_json())

# convert the object into a dict
agg_date_histogram_dict = agg_date_histogram_instance.to_dict()
# create an instance of AggDateHistogram from a dict
agg_date_histogram_from_dict = AggDateHistogram.from_dict(agg_date_histogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


