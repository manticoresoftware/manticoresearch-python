# Chat

Conversational search request handled by Manticore Buddy via `CALL CHAT`. When this object is set, the `/search` endpoint answers through an LLM using KNN-retrieved rows as context instead of returning regular search hits. Required fields are `query`, `table`, and `model_name`. Chat model management (`CREATE CHAT MODEL`, etc.) remains SQL-only. For more information see [Conversational search](https://manual.manticoresearch.com/Searching/Conversational_search#HTTP-JSON-syntax) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | User question to send to the chat model | 
**table** | **str** | Vectorized table to retrieve context from | 
**model_name** | **str** | Name of the chat model | 
**conversation_uuid** | **str** | Existing conversation id to continue the dialog, or an empty string to start a new conversation. If omitted, a new id is generated.  | [optional] 
**vector_field** | **str** | A specific vector field to search by. If omitted, Buddy uses the first &#x60;FLOAT_VECTOR&#x60; field from &#x60;SHOW CREATE TABLE&#x60;.  | [optional] 
**fields** | **str** | Legacy alias for &#x60;vector_field&#x60;. A request must not include both &#x60;vector_field&#x60; and &#x60;fields&#x60;.  | [optional] 

## Example

```python
from manticoresearch.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print(Chat.to_json())

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_from_dict = Chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


