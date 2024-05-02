# BodyUsersCreateUserOpen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**email** | **str** |  | 
**full_name** | **str** |  | [optional] 
**balance_limit** | **float** | User&#39;s balance limit, 0 means no limit | [optional] [default to 0.0]

## Example

```python
from pastel_gateway_sdk.models.body_users_create_user_open import BodyUsersCreateUserOpen

# TODO update the JSON string below
json = "{}"
# create an instance of BodyUsersCreateUserOpen from a JSON string
body_users_create_user_open_instance = BodyUsersCreateUserOpen.from_json(json)
# print the JSON string representation of the object
print(BodyUsersCreateUserOpen.to_json())

# convert the object into a dict
body_users_create_user_open_dict = body_users_create_user_open_instance.to_dict()
# create an instance of BodyUsersCreateUserOpen from a dict
body_users_create_user_open_form_dict = body_users_create_user_open.from_dict(body_users_create_user_open_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


