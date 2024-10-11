# GeoDistance

Object to perform geo-distance based filtering on queries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_anchor** | [**GeoDistanceLocationAnchor**](GeoDistanceLocationAnchor.md) |  | [optional] 
**location_source** | **object** | Field name in the document that contains location data | [optional] 
**distance_type** | **object** | Algorithm used to calculate the distance | [optional] 
**distance** | **object** | The distance from the anchor point to filter results by | [optional] 

## Example

```python
from manticoresearch.models.geo_distance import GeoDistance

# create an instance of GeoDistance from a JSON string
geo_distance_instance = GeoDistance.from_json(json)
# print the JSON string representation of the object
print(GeoDistance.to_json())

# convert the object into a dict
geo_distance_dict = geo_distance_instance.to_dict()
# create an instance of GeoDistance from a dict
geo_distance_from_dict = GeoDistance.from_dict(geo_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


