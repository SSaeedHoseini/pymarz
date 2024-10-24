# NodesUsageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usages** | [**List[NodeUsageResponse]**](NodeUsageResponse.md) |  | 

## Example

```python
from marzapi.models.nodes_usage_response import NodesUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodesUsageResponse from a JSON string
nodes_usage_response_instance = NodesUsageResponse.from_json(json)
# print the JSON string representation of the object
print NodesUsageResponse.to_json()

# convert the object into a dict
nodes_usage_response_dict = nodes_usage_response_instance.to_dict()
# create an instance of NodesUsageResponse from a dict
nodes_usage_response_from_dict = NodesUsageResponse.from_dict(nodes_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


