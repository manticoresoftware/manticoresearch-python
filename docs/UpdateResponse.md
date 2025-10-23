# UpdateResponse

Success response returned after updating one or more documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | Name of the document table | [optional] 
**updated** | **int** | Number of documents updated | [optional] 
**id** | **int** | Document ID | [optional] 
**result** | **str** | Result of the update operation, typically &#39;updated&#39; | [optional] 

## Example

```python
from manticoresearch.models.update_response import UpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResponse from a JSON string
update_response_instance = UpdateResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateResponse.to_json())

# convert the object into a dict
update_response_dict = update_response_instance.to_dict()
# create an instance of UpdateResponse from a dict
update_response_from_dict = UpdateResponse.from_dict(update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


