# User


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

## Example

```python
from gateway_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

