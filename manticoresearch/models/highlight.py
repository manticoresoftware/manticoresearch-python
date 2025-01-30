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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from manticoresearch.models.query_filter import QueryFilter
from typing import Optional, Set
from typing_extensions import Self

class Highlight(BaseModel):
    """
    Highlight
    """ # noqa: E501
    fragment_size: Optional[Any] = Field(default=None, description="Maximum size of the text fragments in highlighted snippets per field")
    limit: Optional[Any] = Field(default=None, description="Maximum size of snippets per field")
    limit_snippets: Optional[Any] = Field(default=None, description="Maximum number of snippets per field")
    limit_words: Optional[Any] = Field(default=None, description="Maximum number of words per field")
    number_of_fragments: Optional[Any] = Field(default=None, description="Total number of highlighted fragments per field")
    after_match: Optional[StrictStr] = Field(default='</strong>', description="Text inserted after the matched term, typically used for HTML formatting")
    allow_empty: Optional[StrictBool] = Field(default=None, description="Permits an empty string to be returned as the highlighting result. Otherwise, the beginning of the original text would be returned")
    around: Optional[StrictInt] = Field(default=None, description="Number of words around the match to include in the highlight")
    before_match: Optional[StrictStr] = Field(default='<strong>', description="Text inserted before the match, typically used for HTML formatting")
    emit_zones: Optional[StrictBool] = Field(default=None, description="Emits an HTML tag with the enclosing zone name before each highlighted snippet")
    encoder: Optional[StrictStr] = Field(default=None, description="If set to 'html', retains HTML markup when highlighting")
    fields: Optional[Dict[str, Any]] = None
    force_all_words: Optional[StrictBool] = Field(default=None, description="Ignores the length limit until the result includes all keywords")
    force_snippets: Optional[StrictBool] = Field(default=None, description="Forces snippet generation even if limits allow highlighting the entire text")
    highlight_query: Optional[QueryFilter] = None
    html_strip_mode: Optional[StrictStr] = Field(default=None, description="Defines the mode for handling HTML markup in the highlight")
    limits_per_field: Optional[StrictBool] = Field(default=None, description="Determines whether the 'limit', 'limit_words', and 'limit_snippets' options operate as individual limits in each field of the document")
    no_match_size: Optional[StrictInt] = Field(default=None, description="If set to 1, allows an empty string to be returned as a highlighting result")
    order: Optional[StrictStr] = Field(default=None, description="Sets the sorting order of highlighted snippets")
    pre_tags: Optional[StrictStr] = Field(default='<strong>', description="Text inserted before each highlighted snippet")
    post_tags: Optional[StrictStr] = Field(default='</strong>', description="Text inserted after each highlighted snippet")
    start_snippet_id: Optional[StrictInt] = Field(default=None, description="Sets the starting value of the %SNIPPET_ID% macro")
    use_boundaries: Optional[StrictBool] = Field(default=None, description="Defines whether to additionally break snippets by phrase boundary characters")
    __properties: ClassVar[List[str]] = ["fragment_size", "limit", "limit_snippets", "limit_words", "number_of_fragments", "after_match", "allow_empty", "around", "before_match", "emit_zones", "encoder", "fields", "force_all_words", "force_snippets", "highlight_query", "html_strip_mode", "limits_per_field", "no_match_size", "order", "pre_tags", "post_tags", "start_snippet_id", "use_boundaries"]

    @field_validator('encoder')
    def encoder_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'html']):
            raise ValueError("must be one of enum values ('default', 'html')")
        return value

    @field_validator('html_strip_mode')
    def html_strip_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'strip', 'index', 'retain']):
            raise ValueError("must be one of enum values ('none', 'strip', 'index', 'retain')")
        return value

    @field_validator('no_match_size')
    def no_match_size_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('order')
    def order_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['asc', 'desc', 'score']):
            raise ValueError("must be one of enum values ('asc', 'desc', 'score')")
        return value

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
        """Create an instance of Highlight from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of highlight_query
        if self.highlight_query:
            _dict['highlight_query'] = self.highlight_query.to_dict()
        # set to None if fragment_size (nullable) is None
        # and model_fields_set contains the field
        if self.fragment_size is None and "fragment_size" in self.model_fields_set:
            _dict['fragment_size'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if limit_snippets (nullable) is None
        # and model_fields_set contains the field
        if self.limit_snippets is None and "limit_snippets" in self.model_fields_set:
            _dict['limit_snippets'] = None

        # set to None if limit_words (nullable) is None
        # and model_fields_set contains the field
        if self.limit_words is None and "limit_words" in self.model_fields_set:
            _dict['limit_words'] = None

        # set to None if number_of_fragments (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_fragments is None and "number_of_fragments" in self.model_fields_set:
            _dict['number_of_fragments'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        # set to None if highlight_query (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_query is None and "highlight_query" in self.model_fields_set:
            _dict['highlight_query'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Highlight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fragment_size": obj.get("fragment_size"),
            "limit": obj.get("limit"),
            "limit_snippets": obj.get("limit_snippets"),
            "limit_words": obj.get("limit_words"),
            "number_of_fragments": obj.get("number_of_fragments"),
            "after_match": obj.get("after_match") if obj.get("after_match") is not None else '</strong>',
            "allow_empty": obj.get("allow_empty"),
            "around": obj.get("around"),
            "before_match": obj.get("before_match") if obj.get("before_match") is not None else '<strong>',
            "emit_zones": obj.get("emit_zones"),
            "encoder": obj.get("encoder"),
            "fields": obj.get("fields"),
            "force_all_words": obj.get("force_all_words"),
            "force_snippets": obj.get("force_snippets"),
            "highlight_query": QueryFilter.from_dict(obj["highlight_query"]) if obj.get("highlight_query") is not None else None,
            "html_strip_mode": obj.get("html_strip_mode"),
            "limits_per_field": obj.get("limits_per_field"),
            "no_match_size": obj.get("no_match_size"),
            "order": obj.get("order"),
            "pre_tags": obj.get("pre_tags") if obj.get("pre_tags") is not None else '<strong>',
            "post_tags": obj.get("post_tags") if obj.get("post_tags") is not None else '</strong>',
            "start_snippet_id": obj.get("start_snippet_id"),
            "use_boundaries": obj.get("use_boundaries")
        })
        return _obj


