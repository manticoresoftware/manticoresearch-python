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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from manticoresearch.models.search_response_hits import SearchResponseHits
from typing import Optional, Set
from typing_extensions import Self

class SearchResponse(BaseModel):
    """
    Response object containing the results of a search request
    """ # noqa: E501
    took: Optional[StrictInt] = Field(default=None, description="Time taken to execute the search")
    timed_out: Optional[StrictBool] = Field(default=None, description="Indicates whether the search operation timed out")
    aggregations: Optional[Dict[str, Any]] = Field(default=None, description="Aggregated search results grouped by the specified criteria")
    hits: Optional[SearchResponseHits] = None
    profile: Optional[Dict[str, Any]] = Field(default=None, description="Profile information about the search execution, if profiling is enabled")
    scroll: Optional[StrictStr] = Field(default=None, description="Scroll token to be used fo pagination")
    warning: Optional[Dict[str, Any]] = Field(default=None, description="Warnings encountered during the search operation")
    __properties: ClassVar[List[str]] = ["took", "timed_out", "aggregations", "hits", "profile", "scroll", "warning"]

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
        """Create an instance of SearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of hits
        if self.hits:
            _dict['hits'] = self.hits.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "took": obj.get("took"),
            "timed_out": obj.get("timed_out"),
            "aggregations": obj.get("aggregations"),
            "hits": SearchResponseHits.from_dict(obj["hits"]) if obj.get("hits") is not None else None,
            "profile": obj.get("profile"),
            "scroll": obj.get("scroll"),
            "warning": obj.get("warning")
        })
        return _obj


