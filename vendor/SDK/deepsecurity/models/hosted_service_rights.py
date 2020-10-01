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

from deepsecurity.models.account_rights import AccountRights  # noqa: F401,E501
from deepsecurity.models.fix_rights import FixRights  # noqa: F401,E501
from deepsecurity.models.heap_rights import HeapRights  # noqa: F401,E501
from deepsecurity.models.license_rate_rights import LicenseRateRights  # noqa: F401,E501
from deepsecurity.models.network_security_rights import NetworkSecurityRights  # noqa: F401,E501
from deepsecurity.models.query_rights import QueryRights  # noqa: F401,E501
from deepsecurity.models.query_traceback_rights import QueryTracebackRights  # noqa: F401,E501
from deepsecurity.models.server_log_rights import ServerLogRights  # noqa: F401,E501
from deepsecurity.models.stack_trace_rights import StackTraceRights  # noqa: F401,E501


class HostedServiceRights(object):
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
        'account_rights': 'AccountRights',
        'fix_rights': 'FixRights',
        'heap_rights': 'HeapRights',
        'license_rate_rights': 'LicenseRateRights',
        'query_rights': 'QueryRights',
        'query_traceback_rights': 'QueryTracebackRights',
        'server_log_rights': 'ServerLogRights',
        'stack_trace_rights': 'StackTraceRights',
        'network_security_rights': 'NetworkSecurityRights'
    }

    attribute_map = {
        'account_rights': 'accountRights',
        'fix_rights': 'fixRights',
        'heap_rights': 'heapRights',
        'license_rate_rights': 'licenseRateRights',
        'query_rights': 'queryRights',
        'query_traceback_rights': 'queryTracebackRights',
        'server_log_rights': 'serverLogRights',
        'stack_trace_rights': 'stackTraceRights',
        'network_security_rights': 'networkSecurityRights'
    }

    def __init__(self, account_rights=None, fix_rights=None, heap_rights=None, license_rate_rights=None, query_rights=None, query_traceback_rights=None, server_log_rights=None, stack_trace_rights=None, network_security_rights=None):  # noqa: E501
        """HostedServiceRights - a model defined in Swagger"""  # noqa: E501

        self._account_rights = None
        self._fix_rights = None
        self._heap_rights = None
        self._license_rate_rights = None
        self._query_rights = None
        self._query_traceback_rights = None
        self._server_log_rights = None
        self._stack_trace_rights = None
        self._network_security_rights = None
        self.discriminator = None

        if account_rights is not None:
            self.account_rights = account_rights
        if fix_rights is not None:
            self.fix_rights = fix_rights
        if heap_rights is not None:
            self.heap_rights = heap_rights
        if license_rate_rights is not None:
            self.license_rate_rights = license_rate_rights
        if query_rights is not None:
            self.query_rights = query_rights
        if query_traceback_rights is not None:
            self.query_traceback_rights = query_traceback_rights
        if server_log_rights is not None:
            self.server_log_rights = server_log_rights
        if stack_trace_rights is not None:
            self.stack_trace_rights = stack_trace_rights
        if network_security_rights is not None:
            self.network_security_rights = network_security_rights

    @property
    def account_rights(self):
        """Gets the account_rights of this HostedServiceRights.  # noqa: E501

        Rights related to accounts.  # noqa: E501

        :return: The account_rights of this HostedServiceRights.  # noqa: E501
        :rtype: AccountRights
        """
        return self._account_rights

    @account_rights.setter
    def account_rights(self, account_rights):
        """Sets the account_rights of this HostedServiceRights.

        Rights related to accounts.  # noqa: E501

        :param account_rights: The account_rights of this HostedServiceRights.  # noqa: E501
        :type: AccountRights
        """

        self._account_rights = account_rights

    @property
    def fix_rights(self):
        """Gets the fix_rights of this HostedServiceRights.  # noqa: E501

        Rights related to fixes.  # noqa: E501

        :return: The fix_rights of this HostedServiceRights.  # noqa: E501
        :rtype: FixRights
        """
        return self._fix_rights

    @fix_rights.setter
    def fix_rights(self, fix_rights):
        """Sets the fix_rights of this HostedServiceRights.

        Rights related to fixes.  # noqa: E501

        :param fix_rights: The fix_rights of this HostedServiceRights.  # noqa: E501
        :type: FixRights
        """

        self._fix_rights = fix_rights

    @property
    def heap_rights(self):
        """Gets the heap_rights of this HostedServiceRights.  # noqa: E501

        Rights related to the heap.  # noqa: E501

        :return: The heap_rights of this HostedServiceRights.  # noqa: E501
        :rtype: HeapRights
        """
        return self._heap_rights

    @heap_rights.setter
    def heap_rights(self, heap_rights):
        """Sets the heap_rights of this HostedServiceRights.

        Rights related to the heap.  # noqa: E501

        :param heap_rights: The heap_rights of this HostedServiceRights.  # noqa: E501
        :type: HeapRights
        """

        self._heap_rights = heap_rights

    @property
    def license_rate_rights(self):
        """Gets the license_rate_rights of this HostedServiceRights.  # noqa: E501

        Rights related to license rates.  # noqa: E501

        :return: The license_rate_rights of this HostedServiceRights.  # noqa: E501
        :rtype: LicenseRateRights
        """
        return self._license_rate_rights

    @license_rate_rights.setter
    def license_rate_rights(self, license_rate_rights):
        """Sets the license_rate_rights of this HostedServiceRights.

        Rights related to license rates.  # noqa: E501

        :param license_rate_rights: The license_rate_rights of this HostedServiceRights.  # noqa: E501
        :type: LicenseRateRights
        """

        self._license_rate_rights = license_rate_rights

    @property
    def query_rights(self):
        """Gets the query_rights of this HostedServiceRights.  # noqa: E501

        Rights related to queries.  # noqa: E501

        :return: The query_rights of this HostedServiceRights.  # noqa: E501
        :rtype: QueryRights
        """
        return self._query_rights

    @query_rights.setter
    def query_rights(self, query_rights):
        """Sets the query_rights of this HostedServiceRights.

        Rights related to queries.  # noqa: E501

        :param query_rights: The query_rights of this HostedServiceRights.  # noqa: E501
        :type: QueryRights
        """

        self._query_rights = query_rights

    @property
    def query_traceback_rights(self):
        """Gets the query_traceback_rights of this HostedServiceRights.  # noqa: E501

        Rights related to query traceback.  # noqa: E501

        :return: The query_traceback_rights of this HostedServiceRights.  # noqa: E501
        :rtype: QueryTracebackRights
        """
        return self._query_traceback_rights

    @query_traceback_rights.setter
    def query_traceback_rights(self, query_traceback_rights):
        """Sets the query_traceback_rights of this HostedServiceRights.

        Rights related to query traceback.  # noqa: E501

        :param query_traceback_rights: The query_traceback_rights of this HostedServiceRights.  # noqa: E501
        :type: QueryTracebackRights
        """

        self._query_traceback_rights = query_traceback_rights

    @property
    def server_log_rights(self):
        """Gets the server_log_rights of this HostedServiceRights.  # noqa: E501

        Rights related to server logs.  # noqa: E501

        :return: The server_log_rights of this HostedServiceRights.  # noqa: E501
        :rtype: ServerLogRights
        """
        return self._server_log_rights

    @server_log_rights.setter
    def server_log_rights(self, server_log_rights):
        """Sets the server_log_rights of this HostedServiceRights.

        Rights related to server logs.  # noqa: E501

        :param server_log_rights: The server_log_rights of this HostedServiceRights.  # noqa: E501
        :type: ServerLogRights
        """

        self._server_log_rights = server_log_rights

    @property
    def stack_trace_rights(self):
        """Gets the stack_trace_rights of this HostedServiceRights.  # noqa: E501

        Rights related to stack traces.  # noqa: E501

        :return: The stack_trace_rights of this HostedServiceRights.  # noqa: E501
        :rtype: StackTraceRights
        """
        return self._stack_trace_rights

    @stack_trace_rights.setter
    def stack_trace_rights(self, stack_trace_rights):
        """Sets the stack_trace_rights of this HostedServiceRights.

        Rights related to stack traces.  # noqa: E501

        :param stack_trace_rights: The stack_trace_rights of this HostedServiceRights.  # noqa: E501
        :type: StackTraceRights
        """

        self._stack_trace_rights = stack_trace_rights

    @property
    def network_security_rights(self):
        """Gets the network_security_rights of this HostedServiceRights.  # noqa: E501

        Rights related to Network Security.  # noqa: E501

        :return: The network_security_rights of this HostedServiceRights.  # noqa: E501
        :rtype: NetworkSecurityRights
        """
        return self._network_security_rights

    @network_security_rights.setter
    def network_security_rights(self, network_security_rights):
        """Sets the network_security_rights of this HostedServiceRights.

        Rights related to Network Security.  # noqa: E501

        :param network_security_rights: The network_security_rights of this HostedServiceRights.  # noqa: E501
        :type: NetworkSecurityRights
        """

        self._network_security_rights = network_security_rights

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
        if issubclass(HostedServiceRights, dict):
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
        if not isinstance(other, HostedServiceRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

