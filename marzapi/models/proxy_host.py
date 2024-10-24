# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from marzapi.models.proxy_host_alpn import ProxyHostALPN
from marzapi.models.proxy_host_fingerprint import ProxyHostFingerprint
from marzapi.models.proxy_host_security import ProxyHostSecurity

class ProxyHost(BaseModel):
    """
    ProxyHost
    """
    remark: StrictStr = Field(...)
    address: StrictStr = Field(...)
    port: Optional[StrictInt] = None
    sni: Optional[StrictStr] = None
    host: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    security: Optional[ProxyHostSecurity] = None
    alpn: Optional[ProxyHostALPN] = None
    fingerprint: Optional[ProxyHostFingerprint] = None
    allowinsecure: Optional[StrictBool] = None
    is_disabled: Optional[StrictBool] = None
    mux_enable: Optional[StrictBool] = None
    fragment_setting: Optional[StrictStr] = None
    noise_setting: Optional[StrictStr] = None
    random_user_agent: Optional[StrictBool] = None
    __properties = ["remark", "address", "port", "sni", "host", "path", "security", "alpn", "fingerprint", "allowinsecure", "is_disabled", "mux_enable", "fragment_setting", "noise_setting", "random_user_agent"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ProxyHost:
        """Create an instance of ProxyHost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if port (nullable) is None
        # and __fields_set__ contains the field
        if self.port is None and "port" in self.__fields_set__:
            _dict['port'] = None

        # set to None if sni (nullable) is None
        # and __fields_set__ contains the field
        if self.sni is None and "sni" in self.__fields_set__:
            _dict['sni'] = None

        # set to None if host (nullable) is None
        # and __fields_set__ contains the field
        if self.host is None and "host" in self.__fields_set__:
            _dict['host'] = None

        # set to None if path (nullable) is None
        # and __fields_set__ contains the field
        if self.path is None and "path" in self.__fields_set__:
            _dict['path'] = None

        # set to None if fragment_setting (nullable) is None
        # and __fields_set__ contains the field
        if self.fragment_setting is None and "fragment_setting" in self.__fields_set__:
            _dict['fragment_setting'] = None

        # set to None if noise_setting (nullable) is None
        # and __fields_set__ contains the field
        if self.noise_setting is None and "noise_setting" in self.__fields_set__:
            _dict['noise_setting'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProxyHost:
        """Create an instance of ProxyHost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProxyHost.parse_obj(obj)

        _obj = ProxyHost.parse_obj({
            "remark": obj.get("remark"),
            "address": obj.get("address"),
            "port": obj.get("port"),
            "sni": obj.get("sni"),
            "host": obj.get("host"),
            "path": obj.get("path"),
            "security": obj.get("security"),
            "alpn": obj.get("alpn"),
            "fingerprint": obj.get("fingerprint"),
            "allowinsecure": obj.get("allowinsecure"),
            "is_disabled": obj.get("is_disabled"),
            "mux_enable": obj.get("mux_enable"),
            "fragment_setting": obj.get("fragment_setting"),
            "noise_setting": obj.get("noise_setting"),
            "random_user_agent": obj.get("random_user_agent")
        })
        return _obj

