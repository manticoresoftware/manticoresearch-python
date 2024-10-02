# AggregationComposite

Used for grouping search results by multiple fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Maximum number of composite buckets in the result | [optional] 
**sources** | **List[Dict[str, AggregationCompositeSourcesInnerValue]]** |  | [optional] 

## Example

```python
from manticoresearch.models.aggregation_composite import AggregationComposite

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationComposite from a JSON string
aggregation_composite_instance = AggregationComposite.from_json(json)
# print the JSON string representation of the object
print(AggregationComposite.to_json())

# convert the object into a dict
aggregation_composite_dict = aggregation_composite_instance.to_dict()
# create an instance of AggregationComposite from a dict
aggregation_composite_from_dict = AggregationComposite.from_dict(aggregation_composite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


