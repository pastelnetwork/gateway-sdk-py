# UserCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**is_active** | **bool** |  | [optional] 
**is_superuser** | **bool** |  | [optional] [default to False]
**full_name** | **str** |  | [optional] 
**password** | **str** |  | 
**balance_limit** | **float** |  | [optional] [default to 0.0]

## Example

```python
from pastel_gateway_sdk.models.user_create import UserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreate from a JSON string
user_create_instance = UserCreate.from_json(json)
# print the JSON string representation of the object
print(UserCreate.to_json())

# convert the object into a dict
user_create_dict = user_create_instance.to_dict()
# create an instance of UserCreate from a dict
user_create_form_dict = user_create.from_dict(user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


