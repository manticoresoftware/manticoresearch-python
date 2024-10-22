# AggTerms

Object containing term fields to aggregate on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of attribute to aggregate by | 
**size** | **int** | Maximum number of buckets in the result | [optional] 

## Example

```python
from manticoresearch.models.agg_terms import AggTerms

# create an instance of AggTerms from a JSON string
agg_terms_instance = AggTerms.from_json(json)
# print the JSON string representation of the object
print(AggTerms.to_json())

# convert the object into a dict
agg_terms_dict = agg_terms_instance.to_dict()
# create an instance of AggTerms from a dict
agg_terms_from_dict = AggTerms.from_dict(agg_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


