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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from manticoresearch.models.aggregation import Aggregation
from manticoresearch.models.highlight import Highlight
from manticoresearch.models.join import Join
from manticoresearch.models.knn_query import KnnQuery
from manticoresearch.models.search_query import SearchQuery
from typing import Optional, Set
from typing_extensions import Self

class SearchRequest(BaseModel):
    """
    Request object for search operation
    """ # noqa: E501
    table: StrictStr = Field(description="The table to perform the search on")
    query: Optional[SearchQuery] = None
    join: Optional[List[Join]] = Field(default=None, description="Join clause to combine search data from multiple tables")
    highlight: Optional[Highlight] = None
    limit: Optional[StrictInt] = Field(default=None, description="Maximum number of results to return")
    knn: Optional[KnnQuery] = None
    aggs: Optional[Dict[str, Aggregation]] = Field(default=None, description="Defines aggregation settings for grouping results")
    expressions: Optional[Dict[str, StrictStr]] = Field(default=None, description="Expressions to calculate additional values for the result")
    max_matches: Optional[StrictInt] = Field(default=None, description="Maximum number of matches allowed in the result")
    offset: Optional[StrictInt] = Field(default=None, description="Starting point for pagination of the result")
    options: Optional[Dict[str, Any]] = Field(default=None, description="Additional search options")
    profile: Optional[StrictBool] = Field(default=None, description="Enable or disable profiling of the search request")
    sort: Optional[Any] = None
    source: Optional[Any] = Field(default=None, alias="_source")
    track_scores: Optional[StrictBool] = Field(default=None, description="Enable or disable result weight calculation used for sorting")
    __properties: ClassVar[List[str]] = ["table", "query", "join", "highlight", "limit", "knn", "aggs", "expressions", "max_matches", "offset", "options", "profile", "sort", "_source", "track_scores"]

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
        """Create an instance of SearchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in join (list)
        _items = []
        if self.join:
            for _item_join in self.join:
                if _item_join:
                    _items.append(_item_join.to_dict())
            _dict['join'] = _items
        # override the default output from pydantic by calling `to_dict()` of highlight
        if self.highlight:
            _dict['highlight'] = self.highlight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of knn
        if self.knn:
            _dict['knn'] = self.knn.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in aggs (dict)
        _field_dict = {}
        if self.aggs:
            for _key_aggs in self.aggs:
                if self.aggs[_key_aggs]:
                    _field_dict[_key_aggs] = self.aggs[_key_aggs].to_dict()
            _dict['aggs'] = _field_dict
        # set to None if sort (nullable) is None
        # and model_fields_set contains the field
        if self.sort is None and "sort" in self.model_fields_set:
            _dict['sort'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['_source'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "table": obj.get("table"),
            "query": SearchQuery.from_dict(obj["query"]) if obj.get("query") is not None else None,
            "join": [Join.from_dict(_item) for _item in obj["join"]] if obj.get("join") is not None else None,
            "highlight": Highlight.from_dict(obj["highlight"]) if obj.get("highlight") is not None else None,
            "limit": obj.get("limit"),
            "knn": KnnQuery.from_dict(obj["knn"]) if obj.get("knn") is not None else None,
            "aggs": dict(
                (_k, Aggregation.from_dict(_v))
                for _k, _v in obj["aggs"].items()
            )
            if obj.get("aggs") is not None
            else None,
            "expressions": obj.get("expressions"),
            "max_matches": obj.get("max_matches"),
            "offset": obj.get("offset"),
            "options": obj.get("options"),
            "profile": obj.get("profile"),
            "sort": obj.get("sort"),
            "_source": obj.get("_source"),
            "track_scores": obj.get("track_scores")
        })
        return _obj


