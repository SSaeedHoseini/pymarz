# UsersUsagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usages** | [**List[UserUsageResponse]**](UserUsageResponse.md) |  | 

## Example

```python
from marzapi.models.users_usages_response import UsersUsagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUsagesResponse from a JSON string
users_usages_response_instance = UsersUsagesResponse.from_json(json)
# print the JSON string representation of the object
print UsersUsagesResponse.to_json()

# convert the object into a dict
users_usages_response_dict = users_usages_response_instance.to_dict()
# create an instance of UsersUsagesResponse from a dict
users_usages_response_from_dict = UsersUsagesResponse.from_dict(users_usages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


