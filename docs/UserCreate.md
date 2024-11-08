# UserCreate


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
**username** | **str** |  | 
**status** | [**UserStatusCreate**](UserStatusCreate.md) |  | [optional] 

## Example

```python
from pymarz.models.user_create import UserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreate from a JSON string
user_create_instance = UserCreate.from_json(json)
# print the JSON string representation of the object
print UserCreate.to_json()

# convert the object into a dict
user_create_dict = user_create_instance.to_dict()
# create an instance of UserCreate from a dict
user_create_from_dict = UserCreate.from_dict(user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


