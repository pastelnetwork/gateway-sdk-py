# NftPropertiesExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_name** | **str** |  | [optional] 
**creator_website_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**green** | **bool** |  | [optional] 
**issued_copies** | **int** |  | [optional] 
**keywords** | **str** |  | [optional] 
**maximum_fee** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**royalty** | **float** |  | [optional] 
**series_name** | **str** |  | [optional] 
**youtube_url** | **str** |  | [optional] 

## Example

```python
from pastel_gateway_sdk.models.nft_properties_external import NftPropertiesExternal

# TODO update the JSON string below
json = "{}"
# create an instance of NftPropertiesExternal from a JSON string
nft_properties_external_instance = NftPropertiesExternal.from_json(json)
# print the JSON string representation of the object
print(NftPropertiesExternal.to_json())

# convert the object into a dict
nft_properties_external_dict = nft_properties_external_instance.to_dict()
# create an instance of NftPropertiesExternal from a dict
nft_properties_external_form_dict = nft_properties_external.from_dict(nft_properties_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


