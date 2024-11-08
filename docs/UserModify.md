# UserModify


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxies** | **Dict[str, object]** |  | [optional] 
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
**status** | [**UserStatusModify**](UserStatusModify.md) |  | [optional] 

## Example

```python
from pymarz.models.user_modify import UserModify

# TODO update the JSON string below
json = "{}"
# create an instance of UserModify from a JSON string
user_modify_instance = UserModify.from_json(json)
# print the JSON string representation of the object
print UserModify.to_json()

# convert the object into a dict
user_modify_dict = user_modify_instance.to_dict()
# create an instance of UserModify from a dict
user_modify_from_dict = UserModify.from_dict(user_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


