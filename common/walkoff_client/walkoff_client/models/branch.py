# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Branch(object):
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
        'walkoff_type': 'str',
        'destination_id': 'str',
        'errors': 'list[str]',
        'id_': 'str',
        'source_id': 'str'
    }

    attribute_map = {
        'walkoff_type': '_walkoff_type',
        'destination_id': 'destination_id',
        'errors': 'errors',
        'id_': 'id_',
        'source_id': 'source_id'
    }

    def __init__(self, walkoff_type=None, destination_id=None, errors=None, id_=None, source_id=None):  # noqa: E501
        """Branch - a model defined in OpenAPI"""  # noqa: E501

        self._walkoff_type = None
        self._destination_id = None
        self._errors = None
        self._id_ = None
        self._source_id = None
        self.discriminator = None

        if walkoff_type is not None:
            self.walkoff_type = walkoff_type
        self.destination_id = destination_id
        if errors is not None:
            self.errors = errors
        if id_ is not None:
            self.id_ = id_
        self.source_id = source_id

    @property
    def walkoff_type(self):
        """Gets the walkoff_type of this Branch.  # noqa: E501

        Workflow type for json decoder  # noqa: E501

        :return: The walkoff_type of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._walkoff_type

    @walkoff_type.setter
    def walkoff_type(self, walkoff_type):
        """Sets the walkoff_type of this Branch.

        Workflow type for json decoder  # noqa: E501

        :param walkoff_type: The walkoff_type of this Branch.  # noqa: E501
        :type: str
        """

        self._walkoff_type = walkoff_type

    @property
    def destination_id(self):
        """Gets the destination_id of this Branch.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The destination_id of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this Branch.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param destination_id: The destination_id of this Branch.  # noqa: E501
        :type: str
        """
        if destination_id is None:
            raise ValueError("Invalid value for `destination_id`, must not be `None`")  # noqa: E501

        self._destination_id = destination_id

    @property
    def errors(self):
        """Gets the errors of this Branch.  # noqa: E501

        Errors attached to this ExecutionElement  # noqa: E501

        :return: The errors of this Branch.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Branch.

        Errors attached to this ExecutionElement  # noqa: E501

        :param errors: The errors of this Branch.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def id_(self):
        """Gets the id_ of this Branch.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The id_ of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._id_

    @id_.setter
    def id_(self, id_):
        """Sets the id_ of this Branch.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param id_: The id_ of this Branch.  # noqa: E501
        :type: str
        """

        self._id_ = id_

    @property
    def source_id(self):
        """Gets the source_id of this Branch.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The source_id of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this Branch.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param source_id: The source_id of this Branch.  # noqa: E501
        :type: str
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

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
        if not isinstance(other, Branch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
