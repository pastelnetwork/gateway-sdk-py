# BodyLoginResetPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from pastel_gateway_sdk.models.body_login_reset_password import BodyLoginResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of BodyLoginResetPassword from a JSON string
body_login_reset_password_instance = BodyLoginResetPassword.from_json(json)
# print the JSON string representation of the object
print(BodyLoginResetPassword.to_json())

# convert the object into a dict
body_login_reset_password_dict = body_login_reset_password_instance.to_dict()
# create an instance of BodyLoginResetPassword from a dict
body_login_reset_password_form_dict = body_login_reset_password.from_dict(body_login_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


