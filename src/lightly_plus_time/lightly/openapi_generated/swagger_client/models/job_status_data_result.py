# coding: utf-8

"""
    Lightly API

    lightly_plus_time.lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly_plus_time.lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly_plus_time.lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly_plus_time.lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly_plus_time.lightly.openapi_generated.swagger_client.configuration import Configuration


class JobStatusDataResult(object):
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
        'type': 'JobResultType',
        'data': 'GeneralJobResult'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, type=None, data=None, _configuration=None):  # noqa: E501
        """JobStatusDataResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._data = None
        self.discriminator = None

        self.type = type
        if data is not None:
            self.data = data

    @property
    def type(self):
        """Gets the type of this JobStatusDataResult.  # noqa: E501


        :return: The type of this JobStatusDataResult.  # noqa: E501
        :rtype: JobResultType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobStatusDataResult.


        :param type: The type of this JobStatusDataResult.  # noqa: E501
        :type: JobResultType
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def data(self):
        """Gets the data of this JobStatusDataResult.  # noqa: E501


        :return: The data of this JobStatusDataResult.  # noqa: E501
        :rtype: GeneralJobResult
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this JobStatusDataResult.


        :param data: The data of this JobStatusDataResult.  # noqa: E501
        :type: GeneralJobResult
        """

        self._data = data

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
        if issubclass(JobStatusDataResult, dict):
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
        if not isinstance(other, JobStatusDataResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobStatusDataResult):
            return True

        return self.to_dict() != other.to_dict()
