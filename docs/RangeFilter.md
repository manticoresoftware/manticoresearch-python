# RangeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**Dict[str, RangeFilterRangeValue]**](RangeFilterRangeValue.md) |  | [optional] 

## Example

```python
from manticoresearch.models.range_filter import RangeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RangeFilter from a JSON string
range_filter_instance = RangeFilter.from_json(json)
# print the JSON string representation of the object
print(RangeFilter.to_json())

# convert the object into a dict
range_filter_dict = range_filter_instance.to_dict()
# create an instance of RangeFilter from a dict
range_filter_from_dict = RangeFilter.from_dict(range_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


