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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class SystemStats(BaseModel):
    """
    SystemStats
    """
    version: StrictStr = Field(...)
    mem_total: StrictInt = Field(...)
    mem_used: StrictInt = Field(...)
    cpu_cores: StrictInt = Field(...)
    cpu_usage: Union[StrictFloat, StrictInt] = Field(...)
    total_user: StrictInt = Field(...)
    users_active: StrictInt = Field(...)
    incoming_bandwidth: StrictInt = Field(...)
    outgoing_bandwidth: StrictInt = Field(...)
    incoming_bandwidth_speed: StrictInt = Field(...)
    outgoing_bandwidth_speed: StrictInt = Field(...)
    __properties = ["version", "mem_total", "mem_used", "cpu_cores", "cpu_usage", "total_user", "users_active", "incoming_bandwidth", "outgoing_bandwidth", "incoming_bandwidth_speed", "outgoing_bandwidth_speed"]

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
    def from_json(cls, json_str: str) -> SystemStats:
        """Create an instance of SystemStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemStats:
        """Create an instance of SystemStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SystemStats.parse_obj(obj)

        _obj = SystemStats.parse_obj({
            "version": obj.get("version"),
            "mem_total": obj.get("mem_total"),
            "mem_used": obj.get("mem_used"),
            "cpu_cores": obj.get("cpu_cores"),
            "cpu_usage": obj.get("cpu_usage"),
            "total_user": obj.get("total_user"),
            "users_active": obj.get("users_active"),
            "incoming_bandwidth": obj.get("incoming_bandwidth"),
            "outgoing_bandwidth": obj.get("outgoing_bandwidth"),
            "incoming_bandwidth_speed": obj.get("incoming_bandwidth_speed"),
            "outgoing_bandwidth_speed": obj.get("outgoing_bandwidth_speed")
        })
        return _obj


