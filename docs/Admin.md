# Admin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**is_sudo** | **bool** |  | 
**telegram_id** | **int** |  | [optional] 
**discord_webhook** | **str** |  | [optional] 

## Example

```python
from marzapi.models.admin import Admin

# TODO update the JSON string below
json = "{}"
# create an instance of Admin from a JSON string
admin_instance = Admin.from_json(json)
# print the JSON string representation of the object
print Admin.to_json()

# convert the object into a dict
admin_dict = admin_instance.to_dict()
# create an instance of Admin from a dict
admin_from_dict = Admin.from_dict(admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


