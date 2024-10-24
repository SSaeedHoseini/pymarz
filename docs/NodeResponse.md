# NodeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | [optional] [default to 62050]
**api_port** | **int** |  | [optional] [default to 62051]
**usage_coefficient** | **float** |  | [optional] [default to 1.0]
**id** | **int** |  | 
**xray_version** | **str** |  | [optional] 
**status** | [**NodeStatus**](NodeStatus.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from marzapi.models.node_response import NodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeResponse from a JSON string
node_response_instance = NodeResponse.from_json(json)
# print the JSON string representation of the object
print NodeResponse.to_json()

# convert the object into a dict
node_response_dict = node_response_instance.to_dict()
# create an instance of NodeResponse from a dict
node_response_from_dict = NodeResponse.from_dict(node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


