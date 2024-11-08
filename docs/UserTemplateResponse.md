# UserTemplateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_limit** | **int** | data_limit can be 0 or greater | [optional] 
**expire_duration** | **int** | expire_duration can be 0 or greater in seconds | [optional] 
**username_prefix** | **str** |  | [optional] 
**username_suffix** | **str** |  | [optional] 
**inbounds** | **Dict[str, List[str]]** |  | [optional] 
**id** | **int** |  | 

## Example

```python
from pymarz.models.user_template_response import UserTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTemplateResponse from a JSON string
user_template_response_instance = UserTemplateResponse.from_json(json)
# print the JSON string representation of the object
print UserTemplateResponse.to_json()

# convert the object into a dict
user_template_response_dict = user_template_response_instance.to_dict()
# create an instance of UserTemplateResponse from a dict
user_template_response_from_dict = UserTemplateResponse.from_dict(user_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


