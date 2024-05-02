# RequestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**request_status** | [**Status**](Status.md) |  | 
**results** | [**List[ResultRegistrationResult]**](ResultRegistrationResult.md) |  | 

## Example

```python
from pastel_gateway_sdk.models.request_result import RequestResult

# TODO update the JSON string below
json = "{}"
# create an instance of RequestResult from a JSON string
request_result_instance = RequestResult.from_json(json)
# print the JSON string representation of the object
print(RequestResult.to_json())

# convert the object into a dict
request_result_dict = request_result_instance.to_dict()
# create an instance of RequestResult from a dict
request_result_form_dict = request_result.from_dict(request_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


