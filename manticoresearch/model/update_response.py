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

class UpdateResponse(object):
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
        'index': 'str',
        'updated': 'int',
        'id': 'int',
        'result': 'str'
    }

    attribute_map = {
        'index': '_index',
        'updated': 'updated',
        'id': '_id',
        'result': 'result'
    }

    def __init__(self, index=None, updated=None, id=None, result=None, local_vars_configuration=None):  # noqa: E501
        """UpdateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._updated = None
        self._id = None
        self._result = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        if result is not None:
            self.result = result

    @property
    def index(self):
        """Gets the index of this UpdateResponse.  # noqa: E501


        :return: The index of this UpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._index
    @index.setter
    def index(self, index):
        """Sets the index of this UpdateResponse.


        :param index: The index of this UpdateResponse.  # noqa: E501
        :type index: str
        """

        self._index = index
        

    @property
    def updated(self):
        """Gets the updated of this UpdateResponse.  # noqa: E501


        :return: The updated of this UpdateResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated
    @updated.setter
    def updated(self, updated):
        """Sets the updated of this UpdateResponse.


        :param updated: The updated of this UpdateResponse.  # noqa: E501
        :type updated: int
        """

        self._updated = updated
        

    @property
    def id(self):
        """Gets the id of this UpdateResponse.  # noqa: E501


        :return: The id of this UpdateResponse.  # noqa: E501
        :rtype: int
        """
        return self._id
    @id.setter
    def id(self, id):
        """Sets the id of this UpdateResponse.


        :param id: The id of this UpdateResponse.  # noqa: E501
        :type id: int
        """

        self._id = id
        

    @property
    def result(self):
        """Gets the result of this UpdateResponse.  # noqa: E501


        :return: The result of this UpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._result
    @result.setter
    def result(self, result):
        """Sets the result of this UpdateResponse.


        :param result: The result of this UpdateResponse.  # noqa: E501
        :type result: str
        """

        self._result = result
        


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
        if not isinstance(other, UpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateResponse):
            return True

        return self.to_dict() != other.to_dict()
