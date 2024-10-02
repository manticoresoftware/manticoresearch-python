# AggregationTerms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of attribute to aggregate by | [optional] 
**size** | **int** | Maximum number of buckets in the result | [optional] 

## Example

```python
from manticoresearch.models.aggregation_terms import AggregationTerms

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationTerms from a JSON string
aggregation_terms_instance = AggregationTerms.from_json(json)
# print the JSON string representation of the object
print(AggregationTerms.to_json())

# convert the object into a dict
aggregation_terms_dict = aggregation_terms_instance.to_dict()
# create an instance of AggregationTerms from a dict
aggregation_terms_from_dict = AggregationTerms.from_dict(aggregation_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


