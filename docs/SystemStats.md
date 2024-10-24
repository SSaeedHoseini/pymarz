# SystemStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**mem_total** | **int** |  | 
**mem_used** | **int** |  | 
**cpu_cores** | **int** |  | 
**cpu_usage** | **float** |  | 
**total_user** | **int** |  | 
**users_active** | **int** |  | 
**incoming_bandwidth** | **int** |  | 
**outgoing_bandwidth** | **int** |  | 
**incoming_bandwidth_speed** | **int** |  | 
**outgoing_bandwidth_speed** | **int** |  | 

## Example

```python
from marzapi.models.system_stats import SystemStats

# TODO update the JSON string below
json = "{}"
# create an instance of SystemStats from a JSON string
system_stats_instance = SystemStats.from_json(json)
# print the JSON string representation of the object
print SystemStats.to_json()

# convert the object into a dict
system_stats_dict = system_stats_instance.to_dict()
# create an instance of SystemStats from a dict
system_stats_from_dict = SystemStats.from_dict(system_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


