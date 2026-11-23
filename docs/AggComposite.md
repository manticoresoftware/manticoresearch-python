# AggComposite

Object to perform composite aggregation, i.e., grouping search results by multiple fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Maximum number of composite buckets in the result | [optional] 
**sources** | **List[Dict[str, AggCompositeSource]]** |  | [optional] 

## Example

```python
from manticoresearch.models.agg_composite import AggComposite

# TODO update the JSON string below
json = "{}"
# create an instance of AggComposite from a JSON string
agg_composite_instance = AggComposite.from_json(json)
# print the JSON string representation of the object
print(AggComposite.to_json())

# convert the object into a dict
agg_composite_dict = agg_composite_instance.to_dict()
# create an instance of AggComposite from a dict
agg_composite_from_dict = AggComposite.from_dict(agg_composite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


