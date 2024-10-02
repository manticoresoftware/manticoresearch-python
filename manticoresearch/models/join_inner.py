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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from manticoresearch.models.fulltext_filter import FulltextFilter
from manticoresearch.models.join_inner_on_inner import JoinInnerOnInner
from typing import Optional, Set
from typing_extensions import Self

class JoinInner(BaseModel):
    """
    JoinInner
    """ # noqa: E501
    on: List[JoinInnerOnInner]
    query: Optional[FulltextFilter] = None
    table: StrictStr
    type: StrictStr
    __properties: ClassVar[List[str]] = ["on", "query", "table", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['inner', 'left']):
            raise ValueError("must be one of enum values ('inner', 'left')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of JoinInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in on (list)
        _items = []
        if self.on:
            for _item_on in self.on:
                if _item_on:
                    _items.append(_item_on.to_dict())
            _dict['on'] = _items
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JoinInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "on": [JoinInnerOnInner.from_dict(_item) for _item in obj["on"]] if obj.get("on") is not None else None,
            "query": FulltextFilter.from_dict(obj["query"]) if obj.get("query") is not None else None,
            "table": obj.get("table"),
            "type": obj.get("type")
        })
        return _obj


