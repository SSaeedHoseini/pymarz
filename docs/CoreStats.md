# CoreStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**started** | **bool** |  | 
**logs_websocket** | **str** |  | 

## Example

```python
from marzapi.models.core_stats import CoreStats

# TODO update the JSON string below
json = "{}"
# create an instance of CoreStats from a JSON string
core_stats_instance = CoreStats.from_json(json)
# print the JSON string representation of the object
print CoreStats.to_json()

# convert the object into a dict
core_stats_dict = core_stats_instance.to_dict()
# create an instance of CoreStats from a dict
core_stats_from_dict = CoreStats.from_dict(core_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


