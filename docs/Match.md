# Match

Filter helper object defining a match keyword and match options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**operator** | **str** |  | [optional] 
**boost** | **float** |  | [optional] 

## Example

```python
from manticoresearch.models.match import Match

# TODO update the JSON string below
json = "{}"
# create an instance of Match from a JSON string
match_instance = Match.from_json(json)
# print the JSON string representation of the object
print(Match.to_json())

# convert the object into a dict
match_dict = match_instance.to_dict()
# create an instance of Match from a dict
match_from_dict = Match.from_dict(match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


