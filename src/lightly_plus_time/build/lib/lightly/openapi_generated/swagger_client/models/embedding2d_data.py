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


class Embedding2dData(object):
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
        'dataset_id': 'MongoObjectID',
        'embedding_id': 'MongoObjectID',
        'name': 'str',
        'created_at': 'Timestamp',
        'dimensionality_reduction_method': 'DimensionalityReductionMethod',
        'coordinates_dimension1': 'Embedding2dCoordinates',
        'coordinates_dimension2': 'Embedding2dCoordinates'
    }

    attribute_map = {
        'id': 'id',
        'dataset_id': 'datasetId',
        'embedding_id': 'embeddingId',
        'name': 'name',
        'created_at': 'createdAt',
        'dimensionality_reduction_method': 'dimensionalityReductionMethod',
        'coordinates_dimension1': 'coordinatesDimension1',
        'coordinates_dimension2': 'coordinatesDimension2'
    }

    def __init__(self, id=None, dataset_id=None, embedding_id=None, name=None, created_at=None, dimensionality_reduction_method=None, coordinates_dimension1=None, coordinates_dimension2=None, _configuration=None):  # noqa: E501
        """Embedding2dData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._dataset_id = None
        self._embedding_id = None
        self._name = None
        self._created_at = None
        self._dimensionality_reduction_method = None
        self._coordinates_dimension1 = None
        self._coordinates_dimension2 = None
        self.discriminator = None

        self.id = id
        self.dataset_id = dataset_id
        self.embedding_id = embedding_id
        self.name = name
        self.created_at = created_at
        self.dimensionality_reduction_method = dimensionality_reduction_method
        if coordinates_dimension1 is not None:
            self.coordinates_dimension1 = coordinates_dimension1
        if coordinates_dimension2 is not None:
            self.coordinates_dimension2 = coordinates_dimension2

    @property
    def id(self):
        """Gets the id of this Embedding2dData.  # noqa: E501


        :return: The id of this Embedding2dData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Embedding2dData.


        :param id: The id of this Embedding2dData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this Embedding2dData.  # noqa: E501


        :return: The dataset_id of this Embedding2dData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this Embedding2dData.


        :param dataset_id: The dataset_id of this Embedding2dData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def embedding_id(self):
        """Gets the embedding_id of this Embedding2dData.  # noqa: E501


        :return: The embedding_id of this Embedding2dData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._embedding_id

    @embedding_id.setter
    def embedding_id(self, embedding_id):
        """Sets the embedding_id of this Embedding2dData.


        :param embedding_id: The embedding_id of this Embedding2dData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and embedding_id is None:
            raise ValueError("Invalid value for `embedding_id`, must not be `None`")  # noqa: E501

        self._embedding_id = embedding_id

    @property
    def name(self):
        """Gets the name of this Embedding2dData.  # noqa: E501

        Name of the 2d embedding (default is embedding name + __2d)  # noqa: E501

        :return: The name of this Embedding2dData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Embedding2dData.

        Name of the 2d embedding (default is embedding name + __2d)  # noqa: E501

        :param name: The name of this Embedding2dData.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Embedding2dData.  # noqa: E501


        :return: The created_at of this Embedding2dData.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Embedding2dData.


        :param created_at: The created_at of this Embedding2dData.  # noqa: E501
        :type: Timestamp
        """
        if self._configuration.client_side_validation and created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def dimensionality_reduction_method(self):
        """Gets the dimensionality_reduction_method of this Embedding2dData.  # noqa: E501


        :return: The dimensionality_reduction_method of this Embedding2dData.  # noqa: E501
        :rtype: DimensionalityReductionMethod
        """
        return self._dimensionality_reduction_method

    @dimensionality_reduction_method.setter
    def dimensionality_reduction_method(self, dimensionality_reduction_method):
        """Sets the dimensionality_reduction_method of this Embedding2dData.


        :param dimensionality_reduction_method: The dimensionality_reduction_method of this Embedding2dData.  # noqa: E501
        :type: DimensionalityReductionMethod
        """
        if self._configuration.client_side_validation and dimensionality_reduction_method is None:
            raise ValueError("Invalid value for `dimensionality_reduction_method`, must not be `None`")  # noqa: E501

        self._dimensionality_reduction_method = dimensionality_reduction_method

    @property
    def coordinates_dimension1(self):
        """Gets the coordinates_dimension1 of this Embedding2dData.  # noqa: E501


        :return: The coordinates_dimension1 of this Embedding2dData.  # noqa: E501
        :rtype: Embedding2dCoordinates
        """
        return self._coordinates_dimension1

    @coordinates_dimension1.setter
    def coordinates_dimension1(self, coordinates_dimension1):
        """Sets the coordinates_dimension1 of this Embedding2dData.


        :param coordinates_dimension1: The coordinates_dimension1 of this Embedding2dData.  # noqa: E501
        :type: Embedding2dCoordinates
        """

        self._coordinates_dimension1 = coordinates_dimension1

    @property
    def coordinates_dimension2(self):
        """Gets the coordinates_dimension2 of this Embedding2dData.  # noqa: E501


        :return: The coordinates_dimension2 of this Embedding2dData.  # noqa: E501
        :rtype: Embedding2dCoordinates
        """
        return self._coordinates_dimension2

    @coordinates_dimension2.setter
    def coordinates_dimension2(self, coordinates_dimension2):
        """Sets the coordinates_dimension2 of this Embedding2dData.


        :param coordinates_dimension2: The coordinates_dimension2 of this Embedding2dData.  # noqa: E501
        :type: Embedding2dCoordinates
        """

        self._coordinates_dimension2 = coordinates_dimension2

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
        if issubclass(Embedding2dData, dict):
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
        if not isinstance(other, Embedding2dData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Embedding2dData):
            return True

        return self.to_dict() != other.to_dict()
