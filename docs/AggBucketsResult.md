# AggBucketsResult

Aggregation group returned under `aggregations`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | **object** |  | [optional] 
**after_key** | **object** | Pagination cursor returned by composite aggregations | [optional] 

## Example

```python
from manticoresearch.models.agg_buckets_result import AggBucketsResult

# TODO update the JSON string below
json = "{}"
# create an instance of AggBucketsResult from a JSON string
agg_buckets_result_instance = AggBucketsResult.from_json(json)
# print the JSON string representation of the object
print(AggBucketsResult.to_json())

# convert the object into a dict
agg_buckets_result_dict = agg_buckets_result_instance.to_dict()
# create an instance of AggBucketsResult from a dict
agg_buckets_result_from_dict = AggBucketsResult.from_dict(agg_buckets_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


