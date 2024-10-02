# GeoFilterGeoDistanceLocationAnchor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 

## Example

```python
from manticoresearch.models.geo_filter_geo_distance_location_anchor import GeoFilterGeoDistanceLocationAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of GeoFilterGeoDistanceLocationAnchor from a JSON string
geo_filter_geo_distance_location_anchor_instance = GeoFilterGeoDistanceLocationAnchor.from_json(json)
# print the JSON string representation of the object
print(GeoFilterGeoDistanceLocationAnchor.to_json())

# convert the object into a dict
geo_filter_geo_distance_location_anchor_dict = geo_filter_geo_distance_location_anchor_instance.to_dict()
# create an instance of GeoFilterGeoDistanceLocationAnchor from a dict
geo_filter_geo_distance_location_anchor_from_dict = GeoFilterGeoDistanceLocationAnchor.from_dict(geo_filter_geo_distance_location_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


