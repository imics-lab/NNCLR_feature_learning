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


class DockerRunScheduledCreateRequest(object):
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
        'config_id': 'MongoObjectID',
        'priority': 'DockerRunScheduledPriority'
    }

    attribute_map = {
        'config_id': 'configId',
        'priority': 'priority'
    }

    def __init__(self, config_id=None, priority=None, _configuration=None):  # noqa: E501
        """DockerRunScheduledCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config_id = None
        self._priority = None
        self.discriminator = None

        self.config_id = config_id
        self.priority = priority

    @property
    def config_id(self):
        """Gets the config_id of this DockerRunScheduledCreateRequest.  # noqa: E501


        :return: The config_id of this DockerRunScheduledCreateRequest.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this DockerRunScheduledCreateRequest.


        :param config_id: The config_id of this DockerRunScheduledCreateRequest.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and config_id is None:
            raise ValueError("Invalid value for `config_id`, must not be `None`")  # noqa: E501

        self._config_id = config_id

    @property
    def priority(self):
        """Gets the priority of this DockerRunScheduledCreateRequest.  # noqa: E501


        :return: The priority of this DockerRunScheduledCreateRequest.  # noqa: E501
        :rtype: DockerRunScheduledPriority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DockerRunScheduledCreateRequest.


        :param priority: The priority of this DockerRunScheduledCreateRequest.  # noqa: E501
        :type: DockerRunScheduledPriority
        """
        if self._configuration.client_side_validation and priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

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
        if issubclass(DockerRunScheduledCreateRequest, dict):
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
        if not isinstance(other, DockerRunScheduledCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerRunScheduledCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
