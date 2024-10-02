# RangeFilterRangeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lt** | [**EqualsFilterEquals**](EqualsFilterEquals.md) |  | [optional] 
**gt** | [**EqualsFilterEquals**](EqualsFilterEquals.md) |  | [optional] 
**lte** | [**EqualsFilterEquals**](EqualsFilterEquals.md) |  | [optional] 
**gte** | [**EqualsFilterEquals**](EqualsFilterEquals.md) |  | [optional] 

## Example

```python
from manticoresearch.models.range_filter_range_value import RangeFilterRangeValue

# TODO update the JSON string below
json = "{}"
# create an instance of RangeFilterRangeValue from a JSON string
range_filter_range_value_instance = RangeFilterRangeValue.from_json(json)
# print the JSON string representation of the object
print(RangeFilterRangeValue.to_json())

# convert the object into a dict
range_filter_range_value_dict = range_filter_range_value_instance.to_dict()
# create an instance of RangeFilterRangeValue from a dict
range_filter_range_value_from_dict = RangeFilterRangeValue.from_dict(range_filter_range_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


