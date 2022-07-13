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


class PredictionSingletonObjectDetection(object):
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
        'bbox': 'list[int]',
        'probabilities': 'Probabilities'
    }

    attribute_map = {
        'bbox': 'bbox',
        'probabilities': 'probabilities'
    }

    def __init__(self, bbox=None, probabilities=None, _configuration=None):  # noqa: E501
        """PredictionSingletonObjectDetection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bbox = None
        self._probabilities = None
        self.discriminator = None

        self.bbox = bbox
        if probabilities is not None:
            self.probabilities = probabilities

    @property
    def bbox(self):
        """Gets the bbox of this PredictionSingletonObjectDetection.  # noqa: E501

        The bbox of where a prediction task yielded a finding. [x, y, width, height]  # noqa: E501

        :return: The bbox of this PredictionSingletonObjectDetection.  # noqa: E501
        :rtype: list[int]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this PredictionSingletonObjectDetection.

        The bbox of where a prediction task yielded a finding. [x, y, width, height]  # noqa: E501

        :param bbox: The bbox of this PredictionSingletonObjectDetection.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and bbox is None:
            raise ValueError("Invalid value for `bbox`, must not be `None`")  # noqa: E501

        self._bbox = bbox

    @property
    def probabilities(self):
        """Gets the probabilities of this PredictionSingletonObjectDetection.  # noqa: E501


        :return: The probabilities of this PredictionSingletonObjectDetection.  # noqa: E501
        :rtype: Probabilities
        """
        return self._probabilities

    @probabilities.setter
    def probabilities(self, probabilities):
        """Sets the probabilities of this PredictionSingletonObjectDetection.


        :param probabilities: The probabilities of this PredictionSingletonObjectDetection.  # noqa: E501
        :type: Probabilities
        """

        self._probabilities = probabilities

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
        if issubclass(PredictionSingletonObjectDetection, dict):
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
        if not isinstance(other, PredictionSingletonObjectDetection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictionSingletonObjectDetection):
            return True

        return self.to_dict() != other.to_dict()
