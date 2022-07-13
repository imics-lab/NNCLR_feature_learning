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


class DatasetEmbeddingData(object):
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
        'id': 'MongoObjectID',
        'name': 'str',
        'is_processed': 'bool',
        'created_at': 'Timestamp',
        'is2d': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_processed': 'isProcessed',
        'created_at': 'createdAt',
        'is2d': 'is2d'
    }

    def __init__(self, id=None, name=None, is_processed=None, created_at=None, is2d=None, _configuration=None):  # noqa: E501
        """DatasetEmbeddingData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._is_processed = None
        self._created_at = None
        self._is2d = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.is_processed = is_processed
        self.created_at = created_at
        if is2d is not None:
            self.is2d = is2d

    @property
    def id(self):
        """Gets the id of this DatasetEmbeddingData.  # noqa: E501


        :return: The id of this DatasetEmbeddingData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetEmbeddingData.


        :param id: The id of this DatasetEmbeddingData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this DatasetEmbeddingData.  # noqa: E501

        name of the embedding chosen by the user calling writeCSVUrl  # noqa: E501

        :return: The name of this DatasetEmbeddingData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetEmbeddingData.

        name of the embedding chosen by the user calling writeCSVUrl  # noqa: E501

        :param name: The name of this DatasetEmbeddingData.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_processed(self):
        """Gets the is_processed of this DatasetEmbeddingData.  # noqa: E501

        indicator whether embeddings have already been processed by a background worker  # noqa: E501

        :return: The is_processed of this DatasetEmbeddingData.  # noqa: E501
        :rtype: bool
        """
        return self._is_processed

    @is_processed.setter
    def is_processed(self, is_processed):
        """Sets the is_processed of this DatasetEmbeddingData.

        indicator whether embeddings have already been processed by a background worker  # noqa: E501

        :param is_processed: The is_processed of this DatasetEmbeddingData.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_processed is None:
            raise ValueError("Invalid value for `is_processed`, must not be `None`")  # noqa: E501

        self._is_processed = is_processed

    @property
    def created_at(self):
        """Gets the created_at of this DatasetEmbeddingData.  # noqa: E501


        :return: The created_at of this DatasetEmbeddingData.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DatasetEmbeddingData.


        :param created_at: The created_at of this DatasetEmbeddingData.  # noqa: E501
        :type: Timestamp
        """
        if self._configuration.client_side_validation and created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def is2d(self):
        """Gets the is2d of this DatasetEmbeddingData.  # noqa: E501

        flag set by the background worker if the embedding is 2d  # noqa: E501

        :return: The is2d of this DatasetEmbeddingData.  # noqa: E501
        :rtype: bool
        """
        return self._is2d

    @is2d.setter
    def is2d(self, is2d):
        """Sets the is2d of this DatasetEmbeddingData.

        flag set by the background worker if the embedding is 2d  # noqa: E501

        :param is2d: The is2d of this DatasetEmbeddingData.  # noqa: E501
        :type: bool
        """

        self._is2d = is2d

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
        if issubclass(DatasetEmbeddingData, dict):
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
        if not isinstance(other, DatasetEmbeddingData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetEmbeddingData):
            return True

        return self.to_dict() != other.to_dict()
