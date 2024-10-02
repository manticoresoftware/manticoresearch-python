# GeoFilterGeoDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_anchor** | [**GeoFilterGeoDistanceLocationAnchor**](GeoFilterGeoDistanceLocationAnchor.md) |  | [optional] 
**location_source** | **str** |  | [optional] 
**distance_type** | **str** |  | [optional] 
**distance** | **str** |  | [optional] 

## Example

```python
from manticoresearch.models.geo_filter_geo_distance import GeoFilterGeoDistance

# TODO update the JSON string below
json = "{}"
# create an instance of GeoFilterGeoDistance from a JSON string
geo_filter_geo_distance_instance = GeoFilterGeoDistance.from_json(json)
# print the JSON string representation of the object
print(GeoFilterGeoDistance.to_json())

# convert the object into a dict
geo_filter_geo_distance_dict = geo_filter_geo_distance_instance.to_dict()
# create an instance of GeoFilterGeoDistance from a dict
geo_filter_geo_distance_from_dict = GeoFilterGeoDistance.from_dict(geo_filter_geo_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


