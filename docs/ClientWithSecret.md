# ClientWithSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from pastel_gateway_sdk.models.client_with_secret import ClientWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ClientWithSecret from a JSON string
client_with_secret_instance = ClientWithSecret.from_json(json)
# print the JSON string representation of the object
print(ClientWithSecret.to_json())

# convert the object into a dict
client_with_secret_dict = client_with_secret_instance.to_dict()
# create an instance of ClientWithSecret from a dict
client_with_secret_form_dict = client_with_secret.from_dict(client_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


