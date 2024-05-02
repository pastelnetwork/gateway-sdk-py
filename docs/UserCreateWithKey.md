# UserCreateWithKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**wallet_id** | **str** |  | 
**full_name** | **str** |  | [optional] 
**balance_limit** | **float** |  | [optional] [default to 0.0]

## Example

```python
from pastel_gateway_sdk.models.user_create_with_key import UserCreateWithKey

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateWithKey from a JSON string
user_create_with_key_instance = UserCreateWithKey.from_json(json)
# print the JSON string representation of the object
print(UserCreateWithKey.to_json())

# convert the object into a dict
user_create_with_key_dict = user_create_with_key_instance.to_dict()
# create an instance of UserCreateWithKey from a dict
user_create_with_key_form_dict = user_create_with_key.from_dict(user_create_with_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


