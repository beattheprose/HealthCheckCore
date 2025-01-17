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


class ComputerTasks(object):
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
        'agent_tasks': 'list[str]',
        'appliance_tasks': 'list[str]'
    }

    attribute_map = {
        'agent_tasks': 'agentTasks',
        'appliance_tasks': 'applianceTasks'
    }

    def __init__(self, agent_tasks=None, appliance_tasks=None):  # noqa: E501
        """ComputerTasks - a model defined in Swagger"""  # noqa: E501

        self._agent_tasks = None
        self._appliance_tasks = None
        self.discriminator = None

        if agent_tasks is not None:
            self.agent_tasks = agent_tasks
        if appliance_tasks is not None:
            self.appliance_tasks = appliance_tasks

    @property
    def agent_tasks(self):
        """Gets the agent_tasks of this ComputerTasks.  # noqa: E501

        Agent tasks. Searchable as String.  # noqa: E501

        :return: The agent_tasks of this ComputerTasks.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_tasks

    @agent_tasks.setter
    def agent_tasks(self, agent_tasks):
        """Sets the agent_tasks of this ComputerTasks.

        Agent tasks. Searchable as String.  # noqa: E501

        :param agent_tasks: The agent_tasks of this ComputerTasks.  # noqa: E501
        :type: list[str]
        """

        self._agent_tasks = agent_tasks

    @property
    def appliance_tasks(self):
        """Gets the appliance_tasks of this ComputerTasks.  # noqa: E501

        Appliance tasks. Searchable as String.  # noqa: E501

        :return: The appliance_tasks of this ComputerTasks.  # noqa: E501
        :rtype: list[str]
        """
        return self._appliance_tasks

    @appliance_tasks.setter
    def appliance_tasks(self, appliance_tasks):
        """Sets the appliance_tasks of this ComputerTasks.

        Appliance tasks. Searchable as String.  # noqa: E501

        :param appliance_tasks: The appliance_tasks of this ComputerTasks.  # noqa: E501
        :type: list[str]
        """

        self._appliance_tasks = appliance_tasks

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
        if issubclass(ComputerTasks, dict):
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
        if not isinstance(other, ComputerTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

