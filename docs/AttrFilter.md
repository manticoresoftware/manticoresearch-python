# AttrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equals** | [**EqualsFilterEquals**](EqualsFilterEquals.md) |  | [optional] 
**var_in** | **Dict[str, List[EqualsFilterEquals]]** |  | [optional] 
**range** | [**Dict[str, RangeFilterRangeValue]**](RangeFilterRangeValue.md) |  | [optional] 
**geo_distance** | [**GeoFilterGeoDistance**](GeoFilterGeoDistance.md) |  | [optional] 

## Example

```python
from manticoresearch.models.attr_filter import AttrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AttrFilter from a JSON string
attr_filter_instance = AttrFilter.from_json(json)
# print the JSON string representation of the object
print(AttrFilter.to_json())

# convert the object into a dict
attr_filter_dict = attr_filter_instance.to_dict()
# create an instance of AttrFilter from a dict
attr_filter_from_dict = AttrFilter.from_dict(attr_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


