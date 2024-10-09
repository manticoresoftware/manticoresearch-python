# GeoDistanceLocationAnchor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 

## Example

```python
from manticoresearch.models.geo_distance_location_anchor import GeoDistanceLocationAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of GeoDistanceLocationAnchor from a JSON string
geo_distance_location_anchor_instance = GeoDistanceLocationAnchor.from_json(json)
# print the JSON string representation of the object
print(GeoDistanceLocationAnchor.to_json())

# convert the object into a dict
geo_distance_location_anchor_dict = geo_distance_location_anchor_instance.to_dict()
# create an instance of GeoDistanceLocationAnchor from a dict
geo_distance_location_anchor_from_dict = GeoDistanceLocationAnchor.from_dict(geo_distance_location_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


