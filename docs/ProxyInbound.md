# ProxyInbound


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | 
**protocol** | [**ProxyTypes**](ProxyTypes.md) |  | 
**network** | **str** |  | 
**tls** | **str** |  | 
**port** | [**Port**](Port.md) |  | 

## Example

```python
from marzapi.models.proxy_inbound import ProxyInbound

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyInbound from a JSON string
proxy_inbound_instance = ProxyInbound.from_json(json)
# print the JSON string representation of the object
print ProxyInbound.to_json()

# convert the object into a dict
proxy_inbound_dict = proxy_inbound_instance.to_dict()
# create an instance of ProxyInbound from a dict
proxy_inbound_from_dict = ProxyInbound.from_dict(proxy_inbound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


