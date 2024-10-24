# marzapi
Unified GUI Censorship Resistant Solution Powered by Xray

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.7.0
- Package version: 1.0.0
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import marzapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import marzapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import marzapi
from marzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzapi.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with marzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzapi.AdminApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Admin Token
        api_response = api_instance.admin_token(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AdminApi->admin_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**admin_token**](docs/AdminApi.md#admin_token) | **POST** /api/admin/token | Admin Token
*AdminApi* | [**create_admin**](docs/AdminApi.md#create_admin) | **POST** /api/admin | Create Admin
*AdminApi* | [**get_admins**](docs/AdminApi.md#get_admins) | **GET** /api/admins | Get Admins
*AdminApi* | [**get_current_admin**](docs/AdminApi.md#get_current_admin) | **GET** /api/admin | Get Current Admin
*AdminApi* | [**modify_admin**](docs/AdminApi.md#modify_admin) | **PUT** /api/admin/{username} | Modify Admin
*AdminApi* | [**remove_admin**](docs/AdminApi.md#remove_admin) | **DELETE** /api/admin/{username} | Remove Admin
*CoreApi* | [**get_core_config**](docs/CoreApi.md#get_core_config) | **GET** /api/core/config | Get Core Config
*CoreApi* | [**get_core_stats**](docs/CoreApi.md#get_core_stats) | **GET** /api/core | Get Core Stats
*CoreApi* | [**modify_core_config**](docs/CoreApi.md#modify_core_config) | **PUT** /api/core/config | Modify Core Config
*CoreApi* | [**restart_core**](docs/CoreApi.md#restart_core) | **POST** /api/core/restart | Restart Core
*NodeApi* | [**add_node**](docs/NodeApi.md#add_node) | **POST** /api/node | Add Node
*NodeApi* | [**get_node**](docs/NodeApi.md#get_node) | **GET** /api/node/{node_id} | Get Node
*NodeApi* | [**get_node_settings**](docs/NodeApi.md#get_node_settings) | **GET** /api/node/settings | Get Node Settings
*NodeApi* | [**get_nodes**](docs/NodeApi.md#get_nodes) | **GET** /api/nodes | Get Nodes
*NodeApi* | [**get_usage**](docs/NodeApi.md#get_usage) | **GET** /api/nodes/usage | Get Usage
*NodeApi* | [**modify_node**](docs/NodeApi.md#modify_node) | **PUT** /api/node/{node_id} | Modify Node
*NodeApi* | [**reconnect_node**](docs/NodeApi.md#reconnect_node) | **POST** /api/node/{node_id}/reconnect | Reconnect Node
*NodeApi* | [**remove_node**](docs/NodeApi.md#remove_node) | **DELETE** /api/node/{node_id} | Remove Node
*SubscriptionApi* | [**user_get_usage**](docs/SubscriptionApi.md#user_get_usage) | **GET** /sub/{token}/usage | User Get Usage
*SubscriptionApi* | [**user_subscription**](docs/SubscriptionApi.md#user_subscription) | **GET** /sub/{token}/ | User Subscription
*SubscriptionApi* | [**user_subscription_info**](docs/SubscriptionApi.md#user_subscription_info) | **GET** /sub/{token}/info | User Subscription Info
*SubscriptionApi* | [**user_subscription_with_client_type**](docs/SubscriptionApi.md#user_subscription_with_client_type) | **GET** /sub/{token}/{client_type} | User Subscription With Client Type
*SystemApi* | [**get_hosts**](docs/SystemApi.md#get_hosts) | **GET** /api/hosts | Get Hosts
*SystemApi* | [**get_inbounds**](docs/SystemApi.md#get_inbounds) | **GET** /api/inbounds | Get Inbounds
*SystemApi* | [**get_system_stats**](docs/SystemApi.md#get_system_stats) | **GET** /api/system | Get System Stats
*SystemApi* | [**modify_hosts**](docs/SystemApi.md#modify_hosts) | **PUT** /api/hosts | Modify Hosts
*UserApi* | [**add_user**](docs/UserApi.md#add_user) | **POST** /api/user | Add User
*UserApi* | [**delete_expired_users**](docs/UserApi.md#delete_expired_users) | **DELETE** /api/users/expired | Delete Expired Users
*UserApi* | [**get_expired_users**](docs/UserApi.md#get_expired_users) | **GET** /api/users/expired | Get Expired Users
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /api/user/{username} | Get User
*UserApi* | [**get_user_usage**](docs/UserApi.md#get_user_usage) | **GET** /api/user/{username}/usage | Get User Usage
*UserApi* | [**get_users**](docs/UserApi.md#get_users) | **GET** /api/users | Get Users
*UserApi* | [**get_users_usage**](docs/UserApi.md#get_users_usage) | **GET** /api/users/usage | Get Users Usage
*UserApi* | [**modify_user**](docs/UserApi.md#modify_user) | **PUT** /api/user/{username} | Modify User
*UserApi* | [**remove_user**](docs/UserApi.md#remove_user) | **DELETE** /api/user/{username} | Remove User
*UserApi* | [**reset_user_data_usage**](docs/UserApi.md#reset_user_data_usage) | **POST** /api/user/{username}/reset | Reset User Data Usage
*UserApi* | [**reset_users_data_usage**](docs/UserApi.md#reset_users_data_usage) | **POST** /api/users/reset | Reset Users Data Usage
*UserApi* | [**revoke_user_subscription**](docs/UserApi.md#revoke_user_subscription) | **POST** /api/user/{username}/revoke_sub | Revoke User Subscription
*UserApi* | [**set_owner**](docs/UserApi.md#set_owner) | **PUT** /api/user/{username}/set-owner | Set Owner
*UserTemplateApi* | [**add_user_template**](docs/UserTemplateApi.md#add_user_template) | **POST** /api/user_template | Add User Template
*UserTemplateApi* | [**get_user_template_endpoint**](docs/UserTemplateApi.md#get_user_template_endpoint) | **GET** /api/user_template/{id} | Get User Template Endpoint
*UserTemplateApi* | [**get_user_templates**](docs/UserTemplateApi.md#get_user_templates) | **GET** /api/user_template | Get User Templates
*UserTemplateApi* | [**modify_user_template**](docs/UserTemplateApi.md#modify_user_template) | **PUT** /api/user_template/{id} | Modify User Template
*UserTemplateApi* | [**remove_user_template**](docs/UserTemplateApi.md#remove_user_template) | **DELETE** /api/user_template/{id} | Remove User Template
*DefaultApi* | [**base**](docs/DefaultApi.md#base) | **GET** / | Base


## Documentation For Models

 - [Admin](docs/Admin.md)
 - [AdminCreate](docs/AdminCreate.md)
 - [AdminModify](docs/AdminModify.md)
 - [CoreStats](docs/CoreStats.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [NodeCreate](docs/NodeCreate.md)
 - [NodeModify](docs/NodeModify.md)
 - [NodeResponse](docs/NodeResponse.md)
 - [NodeSettings](docs/NodeSettings.md)
 - [NodeStatus](docs/NodeStatus.md)
 - [NodeUsageResponse](docs/NodeUsageResponse.md)
 - [NodesUsageResponse](docs/NodesUsageResponse.md)
 - [Port](docs/Port.md)
 - [ProxyHost](docs/ProxyHost.md)
 - [ProxyHostALPN](docs/ProxyHostALPN.md)
 - [ProxyHostFingerprint](docs/ProxyHostFingerprint.md)
 - [ProxyHostSecurity](docs/ProxyHostSecurity.md)
 - [ProxyInbound](docs/ProxyInbound.md)
 - [ProxyTypes](docs/ProxyTypes.md)
 - [SubscriptionUserResponse](docs/SubscriptionUserResponse.md)
 - [SystemStats](docs/SystemStats.md)
 - [Token](docs/Token.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserDataLimitResetStrategy](docs/UserDataLimitResetStrategy.md)
 - [UserModify](docs/UserModify.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserStatus](docs/UserStatus.md)
 - [UserStatusCreate](docs/UserStatusCreate.md)
 - [UserStatusModify](docs/UserStatusModify.md)
 - [UserTemplateCreate](docs/UserTemplateCreate.md)
 - [UserTemplateModify](docs/UserTemplateModify.md)
 - [UserTemplateResponse](docs/UserTemplateResponse.md)
 - [UserUsageResponse](docs/UserUsageResponse.md)
 - [UserUsagesResponse](docs/UserUsagesResponse.md)
 - [UsersResponse](docs/UsersResponse.md)
 - [UsersUsagesResponse](docs/UsersUsagesResponse.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="OAuth2PasswordBearer"></a>
### OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




