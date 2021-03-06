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


class ExecuteWorkflow(object):
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
        'execution_id': 'str',
        'parameters': 'list[Parameter]',
        'start': 'str',
        'workflow_id': 'str',
        'workflow_variables': 'list[WorkflowVariable]'
    }

    attribute_map = {
        'execution_id': 'execution_id',
        'parameters': 'parameters',
        'start': 'start',
        'workflow_id': 'workflow_id',
        'workflow_variables': 'workflow_variables'
    }

    def __init__(self, execution_id=None, parameters=None, start=None, workflow_id=None, workflow_variables=None):  # noqa: E501
        """ExecuteWorkflow - a model defined in OpenAPI"""  # noqa: E501

        self._execution_id = None
        self._parameters = None
        self._start = None
        self._workflow_id = None
        self._workflow_variables = None
        self.discriminator = None

        if execution_id is not None:
            self.execution_id = execution_id
        if parameters is not None:
            self.parameters = parameters
        if start is not None:
            self.start = start
        self.workflow_id = workflow_id
        if workflow_variables is not None:
            self.workflow_variables = workflow_variables

    @property
    def execution_id(self):
        """Gets the execution_id of this ExecuteWorkflow.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The execution_id of this ExecuteWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ExecuteWorkflow.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param execution_id: The execution_id of this ExecuteWorkflow.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def parameters(self):
        """Gets the parameters of this ExecuteWorkflow.  # noqa: E501


        :return: The parameters of this ExecuteWorkflow.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ExecuteWorkflow.


        :param parameters: The parameters of this ExecuteWorkflow.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def start(self):
        """Gets the start of this ExecuteWorkflow.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The start of this ExecuteWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ExecuteWorkflow.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param start: The start of this ExecuteWorkflow.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ExecuteWorkflow.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The workflow_id of this ExecuteWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ExecuteWorkflow.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param workflow_id: The workflow_id of this ExecuteWorkflow.  # noqa: E501
        :type: str
        """
        if workflow_id is None:
            raise ValueError("Invalid value for `workflow_id`, must not be `None`")  # noqa: E501

        self._workflow_id = workflow_id

    @property
    def workflow_variables(self):
        """Gets the workflow_variables of this ExecuteWorkflow.  # noqa: E501


        :return: The workflow_variables of this ExecuteWorkflow.  # noqa: E501
        :rtype: list[WorkflowVariable]
        """
        return self._workflow_variables

    @workflow_variables.setter
    def workflow_variables(self, workflow_variables):
        """Sets the workflow_variables of this ExecuteWorkflow.


        :param workflow_variables: The workflow_variables of this ExecuteWorkflow.  # noqa: E501
        :type: list[WorkflowVariable]
        """

        self._workflow_variables = workflow_variables

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
        if not isinstance(other, ExecuteWorkflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
