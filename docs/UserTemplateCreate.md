# UserTemplateCreate


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
from pymarz.models.user_template_create import UserTemplateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserTemplateCreate from a JSON string
user_template_create_instance = UserTemplateCreate.from_json(json)
# print the JSON string representation of the object
print UserTemplateCreate.to_json()

# convert the object into a dict
user_template_create_dict = user_template_create_instance.to_dict()
# create an instance of UserTemplateCreate from a dict
user_template_create_from_dict = UserTemplateCreate.from_dict(user_template_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


