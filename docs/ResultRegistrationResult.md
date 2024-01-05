# ResultRegistrationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_status** | [**Status**](Status.md) |  | 
**file_name** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**file_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 
**status_messages** | [**List[CollectionRegistrationResultStatusMessagesInner]**](CollectionRegistrationResultStatusMessagesInner.md) |  | [optional] 
**retry_num** | **int** |  | [optional] 
**registration_ticket_txid** | **str** |  | [optional] 
**activation_ticket_txid** | **str** |  | [optional] 
**original_file_ipfs_link** | **str** |  | [optional] 
**stored_file_ipfs_link** | **str** |  | [optional] 
**stored_file_aws_link** | **str** |  | [optional] 
**stored_file_other_links** | **object** |  | [optional] 
**make_publicly_accessible** | **bool** |  | [optional] 
**offer_ticket_txid** | **str** |  | [optional] 
**offer_ticket_intended_rcpt_pastel_id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**result_id** | **str** |  | [optional] 

## Example

```python
from gateway_client.models.result_registration_result import ResultRegistrationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResultRegistrationResult from a JSON string
result_registration_result_instance = ResultRegistrationResult.from_json(json)
# print the JSON string representation of the object
print ResultRegistrationResult.to_json()

# convert the object into a dict
result_registration_result_dict = result_registration_result_instance.to_dict()
# create an instance of ResultRegistrationResult from a dict
result_registration_result_form_dict = result_registration_result.from_dict(result_registration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


