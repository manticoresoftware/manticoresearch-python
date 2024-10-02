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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BoolFilterBool(BaseModel):
    """
    BoolFilterBool
    """ # noqa: E501
    must: Optional[List[QueryFilter]] = None
    must_not: Optional[List[QueryFilter]] = None
    should: Optional[List[QueryFilter]] = None
    __properties: ClassVar[List[str]] = ["must", "must_not", "should"]

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
        """Create an instance of BoolFilterBool from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in must (list)
        _items = []
        if self.must:
            for _item_must in self.must:
                if _item_must:
                    _items.append(_item_must.to_dict())
            _dict['must'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in must_not (list)
        _items = []
        if self.must_not:
            for _item_must_not in self.must_not:
                if _item_must_not:
                    _items.append(_item_must_not.to_dict())
            _dict['must_not'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in should (list)
        _items = []
        if self.should:
            for _item_should in self.should:
                if _item_should:
                    _items.append(_item_should.to_dict())
            _dict['should'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BoolFilterBool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "must": [QueryFilter.from_dict(_item) for _item in obj["must"]] if obj.get("must") is not None else None,
            "must_not": [QueryFilter.from_dict(_item) for _item in obj["must_not"]] if obj.get("must_not") is not None else None,
            "should": [QueryFilter.from_dict(_item) for _item in obj["should"]] if obj.get("should") is not None else None
        })
        return _obj

from manticoresearch.models.query_filter import QueryFilter
# TODO: Rewrite to not use raise_errors
BoolFilterBool.model_rebuild(raise_errors=False)

