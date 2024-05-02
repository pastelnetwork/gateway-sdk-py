# BodyUsersUpdateUserMe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from pastel_gateway_sdk.models.body_users_update_user_me import BodyUsersUpdateUserMe

# TODO update the JSON string below
json = "{}"
# create an instance of BodyUsersUpdateUserMe from a JSON string
body_users_update_user_me_instance = BodyUsersUpdateUserMe.from_json(json)
# print the JSON string representation of the object
print(BodyUsersUpdateUserMe.to_json())

# convert the object into a dict
body_users_update_user_me_dict = body_users_update_user_me_instance.to_dict()
# create an instance of BodyUsersUpdateUserMe from a dict
body_users_update_user_me_form_dict = body_users_update_user_me.from_dict(body_users_update_user_me_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


