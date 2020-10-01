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


class SearchCriteria(object):
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
        'field_name': 'str',
        'boolean_test': 'bool',
        'numeric_test': 'str',
        'numeric_value': 'float',
        'string_test': 'str',
        'string_value': 'str',
        'string_wildcards': 'bool',
        'choice_test': 'str',
        'choice_value': 'str',
        'first_date_value': 'int',
        'first_date_inclusive': 'bool',
        'last_date_value': 'int',
        'last_date_inclusive': 'bool',
        'null_test': 'bool',
        'version_test': 'str',
        'version_value': 'str',
        'id_value': 'int',
        'id_test': 'str'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'boolean_test': 'booleanTest',
        'numeric_test': 'numericTest',
        'numeric_value': 'numericValue',
        'string_test': 'stringTest',
        'string_value': 'stringValue',
        'string_wildcards': 'stringWildcards',
        'choice_test': 'choiceTest',
        'choice_value': 'choiceValue',
        'first_date_value': 'firstDateValue',
        'first_date_inclusive': 'firstDateInclusive',
        'last_date_value': 'lastDateValue',
        'last_date_inclusive': 'lastDateInclusive',
        'null_test': 'nullTest',
        'version_test': 'versionTest',
        'version_value': 'versionValue',
        'id_value': 'idValue',
        'id_test': 'idTest'
    }

    def __init__(self, field_name=None, boolean_test=None, numeric_test=None, numeric_value=None, string_test=None, string_value=None, string_wildcards=None, choice_test=None, choice_value=None, first_date_value=None, first_date_inclusive=None, last_date_value=None, last_date_inclusive=None, null_test=None, version_test=None, version_value=None, id_value=None, id_test=None):  # noqa: E501
        """SearchCriteria - a model defined in Swagger"""  # noqa: E501

        self._field_name = None
        self._boolean_test = None
        self._numeric_test = None
        self._numeric_value = None
        self._string_test = None
        self._string_value = None
        self._string_wildcards = None
        self._choice_test = None
        self._choice_value = None
        self._first_date_value = None
        self._first_date_inclusive = None
        self._last_date_value = None
        self._last_date_inclusive = None
        self._null_test = None
        self._version_test = None
        self._version_value = None
        self._id_value = None
        self._id_test = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if boolean_test is not None:
            self.boolean_test = boolean_test
        if numeric_test is not None:
            self.numeric_test = numeric_test
        if numeric_value is not None:
            self.numeric_value = numeric_value
        if string_test is not None:
            self.string_test = string_test
        if string_value is not None:
            self.string_value = string_value
        if string_wildcards is not None:
            self.string_wildcards = string_wildcards
        if choice_test is not None:
            self.choice_test = choice_test
        if choice_value is not None:
            self.choice_value = choice_value
        if first_date_value is not None:
            self.first_date_value = first_date_value
        if first_date_inclusive is not None:
            self.first_date_inclusive = first_date_inclusive
        if last_date_value is not None:
            self.last_date_value = last_date_value
        if last_date_inclusive is not None:
            self.last_date_inclusive = last_date_inclusive
        if null_test is not None:
            self.null_test = null_test
        if version_test is not None:
            self.version_test = version_test
        if version_value is not None:
            self.version_value = version_value
        if id_value is not None:
            self.id_value = id_value
        if id_test is not None:
            self.id_test = id_test

    @property
    def field_name(self):
        """Gets the field_name of this SearchCriteria.  # noqa: E501

        Name of the field to be tested. Required for all tests except idTest.  # noqa: E501

        :return: The field_name of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this SearchCriteria.

        Name of the field to be tested. Required for all tests except idTest.  # noqa: E501

        :param field_name: The field_name of this SearchCriteria.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def boolean_test(self):
        """Gets the boolean_test of this SearchCriteria.  # noqa: E501

        Boolean test, suitable for boolean fields. Default \"true\".  # noqa: E501

        :return: The boolean_test of this SearchCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._boolean_test

    @boolean_test.setter
    def boolean_test(self, boolean_test):
        """Sets the boolean_test of this SearchCriteria.

        Boolean test, suitable for boolean fields. Default \"true\".  # noqa: E501

        :param boolean_test: The boolean_test of this SearchCriteria.  # noqa: E501
        :type: bool
        """

        self._boolean_test = boolean_test

    @property
    def numeric_test(self):
        """Gets the numeric_test of this SearchCriteria.  # noqa: E501

        Numeric test, suitable for numeric fields, used in conjuction with the numericValue. Default \"equal\".  # noqa: E501

        :return: The numeric_test of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._numeric_test

    @numeric_test.setter
    def numeric_test(self, numeric_test):
        """Sets the numeric_test of this SearchCriteria.

        Numeric test, suitable for numeric fields, used in conjuction with the numericValue. Default \"equal\".  # noqa: E501

        :param numeric_test: The numeric_test of this SearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["less-than", "less-than-or-equal", "equal", "greater-than-or-equal", "greater-than", "not-equal"]  # noqa: E501
        if numeric_test not in allowed_values:
            raise ValueError(
                "Invalid value for `numeric_test` ({0}), must be one of {1}"  # noqa: E501
                .format(numeric_test, allowed_values)
            )

        self._numeric_test = numeric_test

    @property
    def numeric_value(self):
        """Gets the numeric_value of this SearchCriteria.  # noqa: E501

        Value used by the numericTest. Required when performing a numericTest.  # noqa: E501

        :return: The numeric_value of this SearchCriteria.  # noqa: E501
        :rtype: float
        """
        return self._numeric_value

    @numeric_value.setter
    def numeric_value(self, numeric_value):
        """Sets the numeric_value of this SearchCriteria.

        Value used by the numericTest. Required when performing a numericTest.  # noqa: E501

        :param numeric_value: The numeric_value of this SearchCriteria.  # noqa: E501
        :type: float
        """

        self._numeric_value = numeric_value

    @property
    def string_test(self):
        """Gets the string_test of this SearchCriteria.  # noqa: E501

        String test, suitable for string fields, used in conjuction with the stringValue and stringWildcards. Default \"equal\".  # noqa: E501

        :return: The string_test of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._string_test

    @string_test.setter
    def string_test(self, string_test):
        """Sets the string_test of this SearchCriteria.

        String test, suitable for string fields, used in conjuction with the stringValue and stringWildcards. Default \"equal\".  # noqa: E501

        :param string_test: The string_test of this SearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["equal", "not-equal"]  # noqa: E501
        if string_test not in allowed_values:
            raise ValueError(
                "Invalid value for `string_test` ({0}), must be one of {1}"  # noqa: E501
                .format(string_test, allowed_values)
            )

        self._string_test = string_test

    @property
    def string_value(self):
        """Gets the string_value of this SearchCriteria.  # noqa: E501

        Value used by the stringTest. Required when performing a stringTest.  # noqa: E501

        :return: The string_value of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this SearchCriteria.

        Value used by the stringTest. Required when performing a stringTest.  # noqa: E501

        :param string_value: The string_value of this SearchCriteria.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def string_wildcards(self):
        """Gets the string_wildcards of this SearchCriteria.  # noqa: E501

        Controls whether or not wildcard characters (`%` and `_`) are treated as wildcards (true) or regular characters (false). Default \"true\".  # noqa: E501

        :return: The string_wildcards of this SearchCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._string_wildcards

    @string_wildcards.setter
    def string_wildcards(self, string_wildcards):
        """Sets the string_wildcards of this SearchCriteria.

        Controls whether or not wildcard characters (`%` and `_`) are treated as wildcards (true) or regular characters (false). Default \"true\".  # noqa: E501

        :param string_wildcards: The string_wildcards of this SearchCriteria.  # noqa: E501
        :type: bool
        """

        self._string_wildcards = string_wildcards

    @property
    def choice_test(self):
        """Gets the choice_test of this SearchCriteria.  # noqa: E501

        Choice test, suitable for enum fields, used in conjuction with the choiceValue. Default \"equal\".  # noqa: E501

        :return: The choice_test of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._choice_test

    @choice_test.setter
    def choice_test(self, choice_test):
        """Sets the choice_test of this SearchCriteria.

        Choice test, suitable for enum fields, used in conjuction with the choiceValue. Default \"equal\".  # noqa: E501

        :param choice_test: The choice_test of this SearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["equal", "not-equal"]  # noqa: E501
        if choice_test not in allowed_values:
            raise ValueError(
                "Invalid value for `choice_test` ({0}), must be one of {1}"  # noqa: E501
                .format(choice_test, allowed_values)
            )

        self._choice_test = choice_test

    @property
    def choice_value(self):
        """Gets the choice_value of this SearchCriteria.  # noqa: E501

        Value used by the choiceTest. Required when performing a choiceTest.  # noqa: E501

        :return: The choice_value of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._choice_value

    @choice_value.setter
    def choice_value(self, choice_value):
        """Sets the choice_value of this SearchCriteria.

        Value used by the choiceTest. Required when performing a choiceTest.  # noqa: E501

        :param choice_value: The choice_value of this SearchCriteria.  # noqa: E501
        :type: str
        """

        self._choice_value = choice_value

    @property
    def first_date_value(self):
        """Gets the first_date_value of this SearchCriteria.  # noqa: E501

        First (low) date used to find objects within a date range.  Null (the default) implies no lower limit on the date range.  # noqa: E501

        :return: The first_date_value of this SearchCriteria.  # noqa: E501
        :rtype: int
        """
        return self._first_date_value

    @first_date_value.setter
    def first_date_value(self, first_date_value):
        """Sets the first_date_value of this SearchCriteria.

        First (low) date used to find objects within a date range.  Null (the default) implies no lower limit on the date range.  # noqa: E501

        :param first_date_value: The first_date_value of this SearchCriteria.  # noqa: E501
        :type: int
        """

        self._first_date_value = first_date_value

    @property
    def first_date_inclusive(self):
        """Gets the first_date_inclusive of this SearchCriteria.  # noqa: E501

        Indicates whether the results should include (true) or exclude (false) an exact match for the firstDateValue. Default \"true\".  # noqa: E501

        :return: The first_date_inclusive of this SearchCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._first_date_inclusive

    @first_date_inclusive.setter
    def first_date_inclusive(self, first_date_inclusive):
        """Sets the first_date_inclusive of this SearchCriteria.

        Indicates whether the results should include (true) or exclude (false) an exact match for the firstDateValue. Default \"true\".  # noqa: E501

        :param first_date_inclusive: The first_date_inclusive of this SearchCriteria.  # noqa: E501
        :type: bool
        """

        self._first_date_inclusive = first_date_inclusive

    @property
    def last_date_value(self):
        """Gets the last_date_value of this SearchCriteria.  # noqa: E501

        Last (high) date used to find objects within a date range.  Null (the default) implies no upper limit on the date range.  # noqa: E501

        :return: The last_date_value of this SearchCriteria.  # noqa: E501
        :rtype: int
        """
        return self._last_date_value

    @last_date_value.setter
    def last_date_value(self, last_date_value):
        """Sets the last_date_value of this SearchCriteria.

        Last (high) date used to find objects within a date range.  Null (the default) implies no upper limit on the date range.  # noqa: E501

        :param last_date_value: The last_date_value of this SearchCriteria.  # noqa: E501
        :type: int
        """

        self._last_date_value = last_date_value

    @property
    def last_date_inclusive(self):
        """Gets the last_date_inclusive of this SearchCriteria.  # noqa: E501

        Indicates whether the results should include (true) or exclude (false) an exact match for the lastDateValue. Default \"true\".  # noqa: E501

        :return: The last_date_inclusive of this SearchCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._last_date_inclusive

    @last_date_inclusive.setter
    def last_date_inclusive(self, last_date_inclusive):
        """Sets the last_date_inclusive of this SearchCriteria.

        Indicates whether the results should include (true) or exclude (false) an exact match for the lastDateValue. Default \"true\".  # noqa: E501

        :param last_date_inclusive: The last_date_inclusive of this SearchCriteria.  # noqa: E501
        :type: bool
        """

        self._last_date_inclusive = last_date_inclusive

    @property
    def null_test(self):
        """Gets the null_test of this SearchCriteria.  # noqa: E501

        Null test, suitable for finding fields containing a null value.  # noqa: E501

        :return: The null_test of this SearchCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._null_test

    @null_test.setter
    def null_test(self, null_test):
        """Sets the null_test of this SearchCriteria.

        Null test, suitable for finding fields containing a null value.  # noqa: E501

        :param null_test: The null_test of this SearchCriteria.  # noqa: E501
        :type: bool
        """

        self._null_test = null_test

    @property
    def version_test(self):
        """Gets the version_test of this SearchCriteria.  # noqa: E501

        Version test, suitable for version fields, used in conjuction with the versionValue. Default \"equal\".  # noqa: E501

        :return: The version_test of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._version_test

    @version_test.setter
    def version_test(self, version_test):
        """Sets the version_test of this SearchCriteria.

        Version test, suitable for version fields, used in conjuction with the versionValue. Default \"equal\".  # noqa: E501

        :param version_test: The version_test of this SearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["less-than", "less-than-or-equal", "equal", "greater-than-or-equal", "greater-than", "not-equal"]  # noqa: E501
        if version_test not in allowed_values:
            raise ValueError(
                "Invalid value for `version_test` ({0}), must be one of {1}"  # noqa: E501
                .format(version_test, allowed_values)
            )

        self._version_test = version_test

    @property
    def version_value(self):
        """Gets the version_value of this SearchCriteria.  # noqa: E501

        Value used by the versionTest. Required when performing a versionTest.  # noqa: E501

        :return: The version_value of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._version_value

    @version_value.setter
    def version_value(self, version_value):
        """Sets the version_value of this SearchCriteria.

        Value used by the versionTest. Required when performing a versionTest.  # noqa: E501

        :param version_value: The version_value of this SearchCriteria.  # noqa: E501
        :type: str
        """

        self._version_value = version_value

    @property
    def id_value(self):
        """Gets the id_value of this SearchCriteria.  # noqa: E501


        :return: The id_value of this SearchCriteria.  # noqa: E501
        :rtype: int
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        """Sets the id_value of this SearchCriteria.


        :param id_value: The id_value of this SearchCriteria.  # noqa: E501
        :type: int
        """

        self._id_value = id_value

    @property
    def id_test(self):
        """Gets the id_test of this SearchCriteria.  # noqa: E501


        :return: The id_test of this SearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._id_test

    @id_test.setter
    def id_test(self, id_test):
        """Sets the id_test of this SearchCriteria.


        :param id_test: The id_test of this SearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["less-than", "less-than-or-equal", "equal", "greater-than-or-equal", "greater-than", "not-equal"]  # noqa: E501
        if id_test not in allowed_values:
            raise ValueError(
                "Invalid value for `id_test` ({0}), must be one of {1}"  # noqa: E501
                .format(id_test, allowed_values)
            )

        self._id_test = id_test

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
        if issubclass(SearchCriteria, dict):
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
        if not isinstance(other, SearchCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

