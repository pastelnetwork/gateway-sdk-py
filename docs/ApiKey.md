# ApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_nft** | **bool** |  | [optional] 
**can_sense** | **bool** |  | [optional] 
**can_cascade** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**api_key** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**owner_id** | **int** |  | 
**pastel_id** | **str** |  | [optional] 

## Example

```python
from pastel_gateway_sdk.models.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_form_dict = api_key.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


