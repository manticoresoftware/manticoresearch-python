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

class KnnQueryByVector(object):
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
        'query_vector': '[float]',
        'k': 'int',
        'filter': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}'
    }

    attribute_map = {
        'field': 'field',
        'query_vector': 'query_vector',
        'k': 'k',
        'filter': 'filter'
    }

    def __init__(self, field="", query_vector=None, k=None, filter={}, local_vars_configuration=None):  # noqa: E501
        """KnnQueryByVector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._query_vector = None
        self._k = None
        self._filter = None
        self.discriminator = None

        self.field = field
        self.query_vector = query_vector
        self.k = k
        if filter is not None:
            self.filter = filter

    @property
    def field(self):
        """Gets the field of this KnnQueryByVector.  # noqa: E501


        :return: The field of this KnnQueryByVector.  # noqa: E501
        :rtype: str
        """
        return self._field
    @field.setter
    def field(self, field):
        """Sets the field of this KnnQueryByVector.


        :param field: The field of this KnnQueryByVector.  # noqa: E501
        :type field: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field
        

    @property
    def query_vector(self):
        """Gets the query_vector of this KnnQueryByVector.  # noqa: E501


        :return: The query_vector of this KnnQueryByVector.  # noqa: E501
        :rtype: [float]
        """
        return self._query_vector
    @query_vector.setter
    def query_vector(self, query_vector):
        """Sets the query_vector of this KnnQueryByVector.


        :param query_vector: The query_vector of this KnnQueryByVector.  # noqa: E501
        :type query_vector: [float]
        """
        if self.local_vars_configuration.client_side_validation and query_vector is None:  # noqa: E501
            raise ValueError("Invalid value for `query_vector`, must not be `None`")  # noqa: E501

        self._query_vector = query_vector
        

    @property
    def k(self):
        """Gets the k of this KnnQueryByVector.  # noqa: E501


        :return: The k of this KnnQueryByVector.  # noqa: E501
        :rtype: int
        """
        return self._k
    @k.setter
    def k(self, k):
        """Sets the k of this KnnQueryByVector.


        :param k: The k of this KnnQueryByVector.  # noqa: E501
        :type k: int
        """
        if self.local_vars_configuration.client_side_validation and k is None:  # noqa: E501
            raise ValueError("Invalid value for `k`, must not be `None`")  # noqa: E501

        self._k = k
        

    @property
    def filter(self):
        """Gets the filter of this KnnQueryByVector.  # noqa: E501


        :return: The filter of this KnnQueryByVector.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._filter
    @filter.setter
    def filter(self, filter):
        """Sets the filter of this KnnQueryByVector.


        :param filter: The filter of this KnnQueryByVector.  # noqa: E501
        :type filter: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """

        self._filter = filter
        


    def to_dict(self):
        """Returns the model properties as a dict"""

        result = {}		
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value



        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KnnQueryByVector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KnnQueryByVector):
            return True

        return self.to_dict() != other.to_dict()
