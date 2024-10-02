# GeoFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_distance** | [**GeoFilterGeoDistance**](GeoFilterGeoDistance.md) |  | [optional] 

## Example

```python
from manticoresearch.models.geo_filter import GeoFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GeoFilter from a JSON string
geo_filter_instance = GeoFilter.from_json(json)
# print the JSON string representation of the object
print(GeoFilter.to_json())

# convert the object into a dict
geo_filter_dict = geo_filter_instance.to_dict()
# create an instance of GeoFilter from a dict
geo_filter_from_dict = GeoFilter.from_dict(geo_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


