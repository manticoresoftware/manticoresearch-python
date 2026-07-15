# AggBucket

Single bucket in an aggregation result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** |  | [optional] 
**doc_count** | **int** | Number of documents in the bucket | 
**status** | [**FacetBucketStatus**](FacetBucketStatus.md) |  | [optional] 

## Example

```python
from manticoresearch.models.agg_bucket import AggBucket

# TODO update the JSON string below
json = "{}"
# create an instance of AggBucket from a JSON string
agg_bucket_instance = AggBucket.from_json(json)
# print the JSON string representation of the object
print(AggBucket.to_json())

# convert the object into a dict
agg_bucket_dict = agg_bucket_instance.to_dict()
# create an instance of AggBucket from a dict
agg_bucket_from_dict = AggBucket.from_dict(agg_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


