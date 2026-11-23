# AggTDigest

T-Digest settings for approximate statistical aggregations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | **float** | Accuracy/memory trade-off. Default is 200. | [optional] 

## Example

```python
from manticoresearch.models.agg_t_digest import AggTDigest

# TODO update the JSON string below
json = "{}"
# create an instance of AggTDigest from a JSON string
agg_t_digest_instance = AggTDigest.from_json(json)
# print the JSON string representation of the object
print(AggTDigest.to_json())

# convert the object into a dict
agg_t_digest_dict = agg_t_digest_instance.to_dict()
# create an instance of AggTDigest from a dict
agg_t_digest_from_dict = AggTDigest.from_dict(agg_t_digest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


