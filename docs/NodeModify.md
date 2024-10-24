# NodeModify


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**api_port** | **int** |  | [optional] 
**usage_coefficient** | **float** |  | [optional] 
**status** | [**NodeStatus**](NodeStatus.md) |  | [optional] 

## Example

```python
from marzapi.models.node_modify import NodeModify

# TODO update the JSON string below
json = "{}"
# create an instance of NodeModify from a JSON string
node_modify_instance = NodeModify.from_json(json)
# print the JSON string representation of the object
print NodeModify.to_json()

# convert the object into a dict
node_modify_dict = node_modify_instance.to_dict()
# create an instance of NodeModify from a dict
node_modify_from_dict = NodeModify.from_dict(node_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


