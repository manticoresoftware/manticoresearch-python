# coding: utf-8

"""
    Manticore Search Client

    Сlient for Manticore Search. 

    The version of the OpenAPI document: 5.0.0
    Contact: info@manticoresearch.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ResponseErrorDetails(BaseModel):
    """
    Detailed error information returned in case of an error response
    """ # noqa: E501
    type: StrictStr = Field(description="Type or category of the error")
    reason: Optional[StrictStr] = Field(default=None, description="Detailed explanation of why the error occurred")
    table: Optional[StrictStr] = Field(default=None, description="The table related to the error, if applicable")
    __properties: ClassVar[List[str]] = ["type", "reason", "table"]

    #model_config = ConfigDict(
    #    populate_by_name=True,
    #    validate_assignment=True,
    #    protected_namespaces=(),
    #)


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResponseErrorDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if table (nullable) is None
        # and model_fields_set contains the field
        if self.table is None and "table" in self.model_fields_set:
            _dict['table'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResponseErrorDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "reason": obj.get("reason"),
            "table": obj.get("table")
        })
        return _obj


