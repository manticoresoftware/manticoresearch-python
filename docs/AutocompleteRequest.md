# AutocompleteRequest

Object containing the data for performing an autocomplete search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | The table to perform the search on | 
**query** | **str** | The beginning of the string to autocomplete | 
**options** | **object** | Autocomplete options   - layouts: A comma-separated string of keyboard layout codes to validate and check for spell correction. Available options - us, ru, ua, se, pt, no, it, gr, uk, fr, es, dk, de, ch, br, bg, be. By default, all are enabled.   - fuzziness: (0,1 or 2) Maximum Levenshtein distance for finding typos. Set to 0 to disable fuzzy matching. Default is 2   - prepend: true/false If true, adds an asterisk before the last word for prefix expansion (e.g., *word )   - append:  true/false If true, adds an asterisk after the last word for prefix expansion (e.g., word* )   - expansion_len: Number of characters to expand in the last word. Default is 10.  | [optional] 

## Example

```python
from manticoresearch.models.autocomplete_request import AutocompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteRequest from a JSON string
autocomplete_request_instance = AutocompleteRequest.from_json(json)
# print the JSON string representation of the object
print(AutocompleteRequest.to_json())

# convert the object into a dict
autocomplete_request_dict = autocomplete_request_instance.to_dict()
# create an instance of AutocompleteRequest from a dict
autocomplete_request_from_dict = AutocompleteRequest.from_dict(autocomplete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


