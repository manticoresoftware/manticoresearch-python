# coding: utf-8

# Manticore Search Client
# Copyright (c) 2020-2021, Manticore Software LTD (https://manticoresearch.com)
# 
# All rights reserved
#



import pprint
import re  # noqa: F401

import six

from manticoresearch.configuration import Configuration

class RangeFilter(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'field': 'str',
        'lte': 'RangeFilterLte',
        'gte': 'RangeFilterLte',
        'lt': 'RangeFilterLte',
        'gt': 'RangeFilterLte'
    }

    attribute_map = {
        'field': 'field',
        'lte': 'lte',
        'gte': 'gte',
        'lt': 'lt',
        'gt': 'gt'
    }

    def __init__(self, field=None, lte=None, gte=None, lt=None, gt=None, local_vars_configuration=None):  # noqa: E501
        """RangeFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._lte = None
        self._gte = None
        self._lt = None
        self._gt = None
        self.discriminator = None

        self.field = field
        self.lte = lte
        self.gte = gte
        self.lt = lt
        self.gt = gt

    @property
    def field(self):
        """Gets the field of this RangeFilter.  # noqa: E501


        :return: The field of this RangeFilter.  # noqa: E501
        :rtype: str
        """
        return self._field
    @field.setter
    def field(self, field):
        """Sets the field of this RangeFilter.


        :param field: The field of this RangeFilter.  # noqa: E501
        :type field: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field
        

    @property
    def lte(self):
        """Gets the lte of this RangeFilter.  # noqa: E501


        :return: The lte of this RangeFilter.  # noqa: E501
        :rtype: RangeFilterLte
        """
        return self._lte
    @lte.setter
    def lte(self, lte):
        """Sets the lte of this RangeFilter.


        :param lte: The lte of this RangeFilter.  # noqa: E501
        :type lte: RangeFilterLte
        """

        self._lte = lte
        

    @property
    def gte(self):
        """Gets the gte of this RangeFilter.  # noqa: E501


        :return: The gte of this RangeFilter.  # noqa: E501
        :rtype: RangeFilterLte
        """
        return self._gte
    @gte.setter
    def gte(self, gte):
        """Sets the gte of this RangeFilter.


        :param gte: The gte of this RangeFilter.  # noqa: E501
        :type gte: RangeFilterLte
        """

        self._gte = gte
        

    @property
    def lt(self):
        """Gets the lt of this RangeFilter.  # noqa: E501


        :return: The lt of this RangeFilter.  # noqa: E501
        :rtype: RangeFilterLte
        """
        return self._lt
    @lt.setter
    def lt(self, lt):
        """Sets the lt of this RangeFilter.


        :param lt: The lt of this RangeFilter.  # noqa: E501
        :type lt: RangeFilterLte
        """

        self._lt = lt
        

    @property
    def gt(self):
        """Gets the gt of this RangeFilter.  # noqa: E501


        :return: The gt of this RangeFilter.  # noqa: E501
        :rtype: RangeFilterLte
        """
        return self._gt
    @gt.setter
    def gt(self, gt):
        """Sets the gt of this RangeFilter.


        :param gt: The gt of this RangeFilter.  # noqa: E501
        :type gt: RangeFilterLte
        """

        self._gt = gt
        


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = { 'range': {self._field: { 'gte': self._gte, 'lte': self._lte, 'gt': self._gt, 'lt': self._lt } } }
        result['range'][self._field] = {k:v for k,v in result['range'][self._field].items() if v is not None}




        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RangeFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RangeFilter):
            return True

        return self.to_dict() != other.to_dict()
