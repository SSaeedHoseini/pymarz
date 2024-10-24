# ProxyHost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remark** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | [optional] 
**sni** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**security** | [**ProxyHostSecurity**](ProxyHostSecurity.md) |  | [optional] 
**alpn** | [**ProxyHostALPN**](ProxyHostALPN.md) |  | [optional] 
**fingerprint** | [**ProxyHostFingerprint**](ProxyHostFingerprint.md) |  | [optional] 
**allowinsecure** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**mux_enable** | **bool** |  | [optional] 
**fragment_setting** | **str** |  | [optional] 
**noise_setting** | **str** |  | [optional] 
**random_user_agent** | **bool** |  | [optional] 

## Example

```python
from marzapi.models.proxy_host import ProxyHost

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyHost from a JSON string
proxy_host_instance = ProxyHost.from_json(json)
# print the JSON string representation of the object
print ProxyHost.to_json()

# convert the object into a dict
proxy_host_dict = proxy_host_instance.to_dict()
# create an instance of ProxyHost from a dict
proxy_host_from_dict = ProxyHost.from_dict(proxy_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


