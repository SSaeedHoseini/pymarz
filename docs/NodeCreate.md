# NodeCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | [optional] [default to 62050]
**api_port** | **int** |  | [optional] [default to 62051]
**usage_coefficient** | **float** |  | [optional] [default to 1.0]
**add_as_new_host** | **bool** |  | [optional] [default to True]

## Example

```python
from pymarz.models.node_create import NodeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCreate from a JSON string
node_create_instance = NodeCreate.from_json(json)
# print the JSON string representation of the object
print NodeCreate.to_json()

# convert the object into a dict
node_create_dict = node_create_instance.to_dict()
# create an instance of NodeCreate from a dict
node_create_from_dict = NodeCreate.from_dict(node_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


