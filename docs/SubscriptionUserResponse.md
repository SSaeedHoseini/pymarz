# SubscriptionUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxies** | **object** |  | 
**expire** | **int** |  | [optional] 
**data_limit** | **int** | data_limit can be 0 or greater | [optional] 
**data_limit_reset_strategy** | [**UserDataLimitResetStrategy**](UserDataLimitResetStrategy.md) |  | [optional] 
**inbounds** | **Dict[str, List[str]]** |  | [optional] 
**note** | **str** |  | [optional] 
**sub_updated_at** | **datetime** |  | [optional] 
**sub_last_user_agent** | **str** |  | [optional] 
**online_at** | **datetime** |  | [optional] 
**on_hold_expire_duration** | **int** |  | [optional] 
**on_hold_timeout** | **datetime** |  | [optional] 
**auto_delete_in_days** | **int** |  | [optional] 
**username** | **str** |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**used_traffic** | **int** |  | 
**lifetime_used_traffic** | **int** |  | [optional] [default to 0]
**created_at** | **datetime** |  | 
**links** | **List[str]** |  | [optional] [default to []]
**subscription_url** | **str** |  | [optional] [default to '']
**excluded_inbounds** | **Dict[str, List[str]]** |  | [optional] 
**admin** | [**Admin**](Admin.md) |  | [optional] 

## Example

```python
from marzapi.models.subscription_user_response import SubscriptionUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUserResponse from a JSON string
subscription_user_response_instance = SubscriptionUserResponse.from_json(json)
# print the JSON string representation of the object
print SubscriptionUserResponse.to_json()

# convert the object into a dict
subscription_user_response_dict = subscription_user_response_instance.to_dict()
# create an instance of SubscriptionUserResponse from a dict
subscription_user_response_from_dict = SubscriptionUserResponse.from_dict(subscription_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


