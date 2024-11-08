# NodeUsageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** |  | [optional] 
**node_name** | **str** |  | 
**uplink** | **int** |  | 
**downlink** | **int** |  | 

## Example

```python
from pymarz.models.node_usage_response import NodeUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeUsageResponse from a JSON string
node_usage_response_instance = NodeUsageResponse.from_json(json)
# print the JSON string representation of the object
print NodeUsageResponse.to_json()

# convert the object into a dict
node_usage_response_dict = node_usage_response_instance.to_dict()
# create an instance of NodeUsageResponse from a dict
node_usage_response_from_dict = NodeUsageResponse.from_dict(node_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


