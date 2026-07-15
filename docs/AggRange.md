# AggRange

Group documents into custom numeric or date ranges. Use with the `range` or `date_range` aggregation type. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute to group by | 
**ranges** | [**List[Range]**](Range.md) | Ordered list of ranges | 
**keyed** | **bool** | Return buckets as an object keyed by range label when true, or as an array when false. Default is false.  | [optional] 

## Example

```python
from manticoresearch.models.agg_range import AggRange

# TODO update the JSON string below
json = "{}"
# create an instance of AggRange from a JSON string
agg_range_instance = AggRange.from_json(json)
# print the JSON string representation of the object
print(AggRange.to_json())

# convert the object into a dict
agg_range_dict = agg_range_instance.to_dict()
# create an instance of AggRange from a dict
agg_range_from_dict = AggRange.from_dict(agg_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


