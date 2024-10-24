# UserTemplateModify


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_limit** | **int** | data_limit can be 0 or greater | [optional] 
**expire_duration** | **int** | expire_duration can be 0 or greater in seconds | [optional] 
**username_prefix** | **str** |  | [optional] 
**username_suffix** | **str** |  | [optional] 
**inbounds** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from marzapi.models.user_template_modify import UserTemplateModify

# TODO update the JSON string below
json = "{}"
# create an instance of UserTemplateModify from a JSON string
user_template_modify_instance = UserTemplateModify.from_json(json)
# print the JSON string representation of the object
print UserTemplateModify.to_json()

# convert the object into a dict
user_template_modify_dict = user_template_modify_instance.to_dict()
# create an instance of UserTemplateModify from a dict
user_template_modify_from_dict = UserTemplateModify.from_dict(user_template_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


