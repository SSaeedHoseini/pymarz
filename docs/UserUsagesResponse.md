# UserUsagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**usages** | [**List[UserUsageResponse]**](UserUsageResponse.md) |  | 

## Example

```python
from marzapi.models.user_usages_response import UserUsagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsagesResponse from a JSON string
user_usages_response_instance = UserUsagesResponse.from_json(json)
# print the JSON string representation of the object
print UserUsagesResponse.to_json()

# convert the object into a dict
user_usages_response_dict = user_usages_response_instance.to_dict()
# create an instance of UserUsagesResponse from a dict
user_usages_response_from_dict = UserUsagesResponse.from_dict(user_usages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


