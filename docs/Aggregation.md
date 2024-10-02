# Aggregation

Used for grouping search results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms** | [**AggregationTerms**](AggregationTerms.md) |  | [optional] 
**sort** | **List[Dict[str, AggregationSortInnerValue]]** |  | [optional] 
**composite** | [**AggregationComposite**](AggregationComposite.md) |  | [optional] 

## Example

```python
from manticoresearch.models.aggregation import Aggregation

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregation from a JSON string
aggregation_instance = Aggregation.from_json(json)
# print the JSON string representation of the object
print(Aggregation.to_json())

# convert the object into a dict
aggregation_dict = aggregation_instance.to_dict()
# create an instance of Aggregation from a dict
aggregation_from_dict = Aggregation.from_dict(aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


