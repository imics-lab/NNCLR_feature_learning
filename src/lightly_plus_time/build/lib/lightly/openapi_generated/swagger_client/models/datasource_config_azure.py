# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DatasourceConfigAzure(object):
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
        'account_name': 'str',
        'account_key': 'str'
    }

    attribute_map = {
        'account_name': 'accountName',
        'account_key': 'accountKey'
    }

    def __init__(self, account_name=None, account_key=None, _configuration=None):  # noqa: E501
        """DatasourceConfigAzure - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._account_key = None
        self.discriminator = None

        self.account_name = account_name
        self.account_key = account_key

    @property
    def account_name(self):
        """Gets the account_name of this DatasourceConfigAzure.  # noqa: E501

        name of the Azure Storage Account  # noqa: E501

        :return: The account_name of this DatasourceConfigAzure.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this DatasourceConfigAzure.

        name of the Azure Storage Account  # noqa: E501

        :param account_name: The account_name of this DatasourceConfigAzure.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_key(self):
        """Gets the account_key of this DatasourceConfigAzure.  # noqa: E501

        key of the Azure Storage Account  # noqa: E501

        :return: The account_key of this DatasourceConfigAzure.  # noqa: E501
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this DatasourceConfigAzure.

        key of the Azure Storage Account  # noqa: E501

        :param account_key: The account_key of this DatasourceConfigAzure.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_key is None:
            raise ValueError("Invalid value for `account_key`, must not be `None`")  # noqa: E501

        self._account_key = account_key

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
        if issubclass(DatasourceConfigAzure, dict):
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
        if not isinstance(other, DatasourceConfigAzure):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasourceConfigAzure):
            return True

        return self.to_dict() != other.to_dict()
