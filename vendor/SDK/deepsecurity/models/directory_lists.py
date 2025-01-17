# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.186
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.directory_list import DirectoryList  # noqa: F401,E501


class DirectoryLists(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'directory_lists': 'list[DirectoryList]'
    }

    attribute_map = {
        'directory_lists': 'directoryLists'
    }

    def __init__(self, directory_lists=None):  # noqa: E501
        """DirectoryLists - a model defined in Swagger"""  # noqa: E501

        self._directory_lists = None
        self.discriminator = None

        if directory_lists is not None:
            self.directory_lists = directory_lists

    @property
    def directory_lists(self):
        """Gets the directory_lists of this DirectoryLists.  # noqa: E501


        :return: The directory_lists of this DirectoryLists.  # noqa: E501
        :rtype: list[DirectoryList]
        """
        return self._directory_lists

    @directory_lists.setter
    def directory_lists(self, directory_lists):
        """Sets the directory_lists of this DirectoryLists.


        :param directory_lists: The directory_lists of this DirectoryLists.  # noqa: E501
        :type: list[DirectoryList]
        """

        self._directory_lists = directory_lists

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DirectoryLists, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DirectoryLists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

