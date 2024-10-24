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


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from marzapi.models.node_status import NodeStatus

class NodeModify(BaseModel):
    """
    NodeModify
    """
    name: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    api_port: Optional[StrictInt] = None
    usage_coefficient: Optional[Union[StrictFloat, StrictInt]] = None
    status: Optional[NodeStatus] = None
    __properties = ["name", "address", "port", "api_port", "usage_coefficient", "status"]

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
    def from_json(cls, json_str: str) -> NodeModify:
        """Create an instance of NodeModify from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        # set to None if port (nullable) is None
        # and __fields_set__ contains the field
        if self.port is None and "port" in self.__fields_set__:
            _dict['port'] = None

        # set to None if api_port (nullable) is None
        # and __fields_set__ contains the field
        if self.api_port is None and "api_port" in self.__fields_set__:
            _dict['api_port'] = None

        # set to None if usage_coefficient (nullable) is None
        # and __fields_set__ contains the field
        if self.usage_coefficient is None and "usage_coefficient" in self.__fields_set__:
            _dict['usage_coefficient'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NodeModify:
        """Create an instance of NodeModify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NodeModify.parse_obj(obj)

        _obj = NodeModify.parse_obj({
            "name": obj.get("name"),
            "address": obj.get("address"),
            "port": obj.get("port"),
            "api_port": obj.get("api_port"),
            "usage_coefficient": obj.get("usage_coefficient"),
            "status": obj.get("status")
        })
        return _obj

