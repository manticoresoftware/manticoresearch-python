# coding: utf-8

"""
    Manticore Search Client

    Contact: info@manticoresearch.com
"""


import pprint
import re  # noqa: F401

import six

from manticoresearch.configuration import Configuration


class SearchResponse(object):
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
        'took': 'int',
        'timed_out': 'bool',
        'aggregations': 'dict(str, object)',
        'hits': 'SearchResponseHits',
        'profile': 'object'
    }

    attribute_map = {
        'took': 'took',
        'timed_out': 'timed_out',
        'aggregations': 'aggregations',
        'hits': 'hits',
        'profile': 'profile'
    }

    def __init__(self, took=None, timed_out=None, aggregations=None, hits=None, profile=None, local_vars_configuration=None):  # noqa: E501
        """SearchResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._took = None
        self._timed_out = None
        self._aggregations = None
        self._hits = None
        self._profile = None
        self.discriminator = None

        if took is not None:
            self.took = took
        if timed_out is not None:
            self.timed_out = timed_out
        if aggregations is not None:
            self.aggregations = aggregations
        if hits is not None:
            self.hits = hits
        if profile is not None:
            self.profile = profile

    @property
    def took(self):
        """Gets the took of this SearchResponse.  # noqa: E501


        :return: The took of this SearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this SearchResponse.


        :param took: The took of this SearchResponse.  # noqa: E501
        :type took: int
        """

        self._took = took

    @property
    def timed_out(self):
        """Gets the timed_out of this SearchResponse.  # noqa: E501


        :return: The timed_out of this SearchResponse.  # noqa: E501
        :rtype: bool
        """
        return self._timed_out

    @timed_out.setter
    def timed_out(self, timed_out):
        """Sets the timed_out of this SearchResponse.


        :param timed_out: The timed_out of this SearchResponse.  # noqa: E501
        :type timed_out: bool
        """

        self._timed_out = timed_out

    @property
    def aggregations(self):
        """Gets the aggregations of this SearchResponse.  # noqa: E501


        :return: The aggregations of this SearchResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this SearchResponse.


        :param aggregations: The aggregations of this SearchResponse.  # noqa: E501
        :type aggregations: dict(str, object)
        """

        self._aggregations = aggregations

    @property
    def hits(self):
        """Gets the hits of this SearchResponse.  # noqa: E501


        :return: The hits of this SearchResponse.  # noqa: E501
        :rtype: SearchResponseHits
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this SearchResponse.


        :param hits: The hits of this SearchResponse.  # noqa: E501
        :type hits: SearchResponseHits
        """

        self._hits = hits

    @property
    def profile(self):
        """Gets the profile of this SearchResponse.  # noqa: E501


        :return: The profile of this SearchResponse.  # noqa: E501
        :rtype: object
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SearchResponse.


        :param profile: The profile of this SearchResponse.  # noqa: E501
        :type profile: object
        """

        self._profile = profile

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
        if not isinstance(other, SearchResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchResponse):
            return True

        return self.to_dict() != other.to_dict()
