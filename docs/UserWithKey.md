# UserWithKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_superuser** | **bool** |  | [optional] [default to False]
**full_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**funding_address** | **str** |  | [optional] 
**balance** | **float** |  | [optional] 
**wallet_id** | **str** |  | 
**key_salt** | **str** |  | 
**wallet_key_index** | **int** |  | 

## Example

```python
from pastel_gateway_sdk.models.user_with_key import UserWithKey

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithKey from a JSON string
user_with_key_instance = UserWithKey.from_json(json)
# print the JSON string representation of the object
print(UserWithKey.to_json())

# convert the object into a dict
user_with_key_dict = user_with_key_instance.to_dict()
# create an instance of UserWithKey from a dict
user_with_key_form_dict = user_with_key.from_dict(user_with_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


