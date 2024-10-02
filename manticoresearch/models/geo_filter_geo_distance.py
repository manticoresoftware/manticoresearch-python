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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from manticoresearch.models.geo_filter_geo_distance_location_anchor import GeoFilterGeoDistanceLocationAnchor
from typing import Optional, Set
from typing_extensions import Self

class GeoFilterGeoDistance(BaseModel):
    """
    GeoFilterGeoDistance
    """ # noqa: E501
    location_anchor: Optional[GeoFilterGeoDistanceLocationAnchor] = None
    location_source: Optional[StrictStr] = None
    distance_type: Optional[StrictStr] = None
    distance: Optional[Annotated[str, Field(strict=True)]] = None
    __properties: ClassVar[List[str]] = ["location_anchor", "location_source", "distance_type", "distance"]

    @field_validator('distance_type')
    def distance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['adaptive', 'haversine']):
            raise ValueError("must be one of enum values ('adaptive', 'haversine')")
        return value

    @field_validator('distance')
    def distance_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\.+(km|m|cm|mm|mi|yd|ft|in|NM|nmi|kilometers|meters|centimeters|millimeters|miles|yards|foots|inches|nauticalmiles|)$", value):
            raise ValueError(r"must validate the regular expression /^\.+(km|m|cm|mm|mi|yd|ft|in|NM|nmi|kilometers|meters|centimeters|millimeters|miles|yards|foots|inches|nauticalmiles|)$/")
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
        """Create an instance of GeoFilterGeoDistance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location_anchor
        if self.location_anchor:
            _dict['location_anchor'] = self.location_anchor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeoFilterGeoDistance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location_anchor": GeoFilterGeoDistanceLocationAnchor.from_dict(obj["location_anchor"]) if obj.get("location_anchor") is not None else None,
            "location_source": obj.get("location_source"),
            "distance_type": obj.get("distance_type"),
            "distance": obj.get("distance")
        })
        return _obj


