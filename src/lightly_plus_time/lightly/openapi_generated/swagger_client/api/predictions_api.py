# coding: utf-8

"""
    Lightly API

    lightly_plus_time.lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly_plus_time.lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly_plus_time.lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly_plus_time.lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lightly_plus_time.lightly.openapi_generated.swagger_client.api_client import ApiClient


class PredictionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_or_update_prediction_by_sample_id(self, body, dataset_id, sample_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """create_or_update_prediction_by_sample_id  # noqa: E501

        Create/Update all the prediction singletons for a sampleId in the order/index of them being discovered   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_update_prediction_by_sample_id(body, dataset_id, sample_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[PredictionSingleton] body: (required)
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param MongoObjectID sample_id: ObjectId of the sample (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :return: CreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_or_update_prediction_by_sample_id_with_http_info(body, dataset_id, sample_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.create_or_update_prediction_by_sample_id_with_http_info(body, dataset_id, sample_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
            return data

    def create_or_update_prediction_by_sample_id_with_http_info(self, body, dataset_id, sample_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """create_or_update_prediction_by_sample_id  # noqa: E501

        Create/Update all the prediction singletons for a sampleId in the order/index of them being discovered   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_update_prediction_by_sample_id_with_http_info(body, dataset_id, sample_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[PredictionSingleton] body: (required)
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param MongoObjectID sample_id: ObjectId of the sample (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :return: CreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'dataset_id', 'sample_id', 'prediction_uuid_timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_prediction_by_sample_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_or_update_prediction_by_sample_id`")  # noqa: E501
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in params or
                                                       params['dataset_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dataset_id` when calling `create_or_update_prediction_by_sample_id`")  # noqa: E501
        # verify the required parameter 'sample_id' is set
        if self.api_client.client_side_validation and ('sample_id' not in params or
                                                       params['sample_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sample_id` when calling `create_or_update_prediction_by_sample_id`")  # noqa: E501
        # verify the required parameter 'prediction_uuid_timestamp' is set
        if self.api_client.client_side_validation and ('prediction_uuid_timestamp' not in params or
                                                       params['prediction_uuid_timestamp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `prediction_uuid_timestamp` when calling `create_or_update_prediction_by_sample_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501
        if 'sample_id' in params:
            path_params['sampleId'] = params['sample_id']  # noqa: E501

        query_params = []
        if 'prediction_uuid_timestamp' in params:
            query_params.append(('predictionUUIDTimestamp', params['prediction_uuid_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'auth0Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/datasets/{datasetId}/predictions/samples/{sampleId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_or_update_prediction_task_schema_by_dataset_id(self, body, dataset_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """create_or_update_prediction_task_schema_by_dataset_id  # noqa: E501

        Creates/updates a prediction task schema with the task name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_update_prediction_task_schema_by_dataset_id(body, dataset_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PredictionTaskSchema body: (required)
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :return: CreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_or_update_prediction_task_schema_by_dataset_id_with_http_info(body, dataset_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.create_or_update_prediction_task_schema_by_dataset_id_with_http_info(body, dataset_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
            return data

    def create_or_update_prediction_task_schema_by_dataset_id_with_http_info(self, body, dataset_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """create_or_update_prediction_task_schema_by_dataset_id  # noqa: E501

        Creates/updates a prediction task schema with the task name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_update_prediction_task_schema_by_dataset_id_with_http_info(body, dataset_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PredictionTaskSchema body: (required)
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :return: CreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'dataset_id', 'prediction_uuid_timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_prediction_task_schema_by_dataset_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_or_update_prediction_task_schema_by_dataset_id`")  # noqa: E501
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in params or
                                                       params['dataset_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dataset_id` when calling `create_or_update_prediction_task_schema_by_dataset_id`")  # noqa: E501
        # verify the required parameter 'prediction_uuid_timestamp' is set
        if self.api_client.client_side_validation and ('prediction_uuid_timestamp' not in params or
                                                       params['prediction_uuid_timestamp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `prediction_uuid_timestamp` when calling `create_or_update_prediction_task_schema_by_dataset_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501

        query_params = []
        if 'prediction_uuid_timestamp' in params:
            query_params.append(('predictionUUIDTimestamp', params['prediction_uuid_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'auth0Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/datasets/{datasetId}/predictions/tasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_prediction_by_sample_id(self, dataset_id, sample_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """get_prediction_by_sample_id  # noqa: E501

        Get all prediction singletons of a specific sample of a dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prediction_by_sample_id(dataset_id, sample_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param MongoObjectID sample_id: ObjectId of the sample (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :return: PredictionSingletons
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prediction_by_sample_id_with_http_info(dataset_id, sample_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.get_prediction_by_sample_id_with_http_info(dataset_id, sample_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
            return data

    def get_prediction_by_sample_id_with_http_info(self, dataset_id, sample_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """get_prediction_by_sample_id  # noqa: E501

        Get all prediction singletons of a specific sample of a dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prediction_by_sample_id_with_http_info(dataset_id, sample_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param MongoObjectID sample_id: ObjectId of the sample (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :return: PredictionSingletons
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_id', 'sample_id', 'prediction_uuid_timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prediction_by_sample_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in params or
                                                       params['dataset_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dataset_id` when calling `get_prediction_by_sample_id`")  # noqa: E501
        # verify the required parameter 'sample_id' is set
        if self.api_client.client_side_validation and ('sample_id' not in params or
                                                       params['sample_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sample_id` when calling `get_prediction_by_sample_id`")  # noqa: E501
        # verify the required parameter 'prediction_uuid_timestamp' is set
        if self.api_client.client_side_validation and ('prediction_uuid_timestamp' not in params or
                                                       params['prediction_uuid_timestamp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `prediction_uuid_timestamp` when calling `get_prediction_by_sample_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501
        if 'sample_id' in params:
            path_params['sampleId'] = params['sample_id']  # noqa: E501

        query_params = []
        if 'prediction_uuid_timestamp' in params:
            query_params.append(('predictionUUIDTimestamp', params['prediction_uuid_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'auth0Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/datasets/{datasetId}/predictions/samples/{sampleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PredictionSingletons',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_prediction_task_schema_by_task_name(self, dataset_id, prediction_uuid_timestamp, task_name, **kwargs):  # noqa: E501
        """get_prediction_task_schema_by_task_name  # noqa: E501

        Get a prediction task schemas named taskName for a datasetId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prediction_task_schema_by_task_name(dataset_id, prediction_uuid_timestamp, task_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :param TaskName task_name: The prediction task name for which one wants to list the predictions (required)
        :return: PredictionTaskSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prediction_task_schema_by_task_name_with_http_info(dataset_id, prediction_uuid_timestamp, task_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_prediction_task_schema_by_task_name_with_http_info(dataset_id, prediction_uuid_timestamp, task_name, **kwargs)  # noqa: E501
            return data

    def get_prediction_task_schema_by_task_name_with_http_info(self, dataset_id, prediction_uuid_timestamp, task_name, **kwargs):  # noqa: E501
        """get_prediction_task_schema_by_task_name  # noqa: E501

        Get a prediction task schemas named taskName for a datasetId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prediction_task_schema_by_task_name_with_http_info(dataset_id, prediction_uuid_timestamp, task_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :param TaskName task_name: The prediction task name for which one wants to list the predictions (required)
        :return: PredictionTaskSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_id', 'prediction_uuid_timestamp', 'task_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prediction_task_schema_by_task_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in params or
                                                       params['dataset_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dataset_id` when calling `get_prediction_task_schema_by_task_name`")  # noqa: E501
        # verify the required parameter 'prediction_uuid_timestamp' is set
        if self.api_client.client_side_validation and ('prediction_uuid_timestamp' not in params or
                                                       params['prediction_uuid_timestamp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `prediction_uuid_timestamp` when calling `get_prediction_task_schema_by_task_name`")  # noqa: E501
        # verify the required parameter 'task_name' is set
        if self.api_client.client_side_validation and ('task_name' not in params or
                                                       params['task_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `task_name` when calling `get_prediction_task_schema_by_task_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501
        if 'task_name' in params:
            path_params['taskName'] = params['task_name']  # noqa: E501

        query_params = []
        if 'prediction_uuid_timestamp' in params:
            query_params.append(('predictionUUIDTimestamp', params['prediction_uuid_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'auth0Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/datasets/{datasetId}/predictions/tasks/{taskName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PredictionTaskSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_prediction_task_schemas_by_dataset_id(self, dataset_id, **kwargs):  # noqa: E501
        """get_prediction_task_schemas_by_dataset_id  # noqa: E501

        Get list of all the prediction task schemas for a datasetId at a specific predictionUUIDTimestamp. If no predictionUUIDTimestamp is set, it defaults to the newest  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prediction_task_schemas_by_dataset_id(dataset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset. 
        :return: list[PredictionTaskSchema]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prediction_task_schemas_by_dataset_id_with_http_info(dataset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_prediction_task_schemas_by_dataset_id_with_http_info(dataset_id, **kwargs)  # noqa: E501
            return data

    def get_prediction_task_schemas_by_dataset_id_with_http_info(self, dataset_id, **kwargs):  # noqa: E501
        """get_prediction_task_schemas_by_dataset_id  # noqa: E501

        Get list of all the prediction task schemas for a datasetId at a specific predictionUUIDTimestamp. If no predictionUUIDTimestamp is set, it defaults to the newest  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prediction_task_schemas_by_dataset_id_with_http_info(dataset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset. 
        :return: list[PredictionTaskSchema]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_id', 'prediction_uuid_timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prediction_task_schemas_by_dataset_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in params or
                                                       params['dataset_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dataset_id` when calling `get_prediction_task_schemas_by_dataset_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501

        query_params = []
        if 'prediction_uuid_timestamp' in params:
            query_params.append(('predictionUUIDTimestamp', params['prediction_uuid_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'auth0Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/datasets/{datasetId}/predictions/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PredictionTaskSchema]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_predictions_by_dataset_id(self, dataset_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """get_predictions_by_dataset_id  # noqa: E501

        Get all prediction singletons of all samples of a dataset ordered by the sample mapping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_predictions_by_dataset_id(dataset_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :param TaskName task_name: If provided, only gets all prediction singletons of all samples of a dataset that were yielded by a specific prediction task name
        :return: list[PredictionSingletons]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_predictions_by_dataset_id_with_http_info(dataset_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.get_predictions_by_dataset_id_with_http_info(dataset_id, prediction_uuid_timestamp, **kwargs)  # noqa: E501
            return data

    def get_predictions_by_dataset_id_with_http_info(self, dataset_id, prediction_uuid_timestamp, **kwargs):  # noqa: E501
        """get_predictions_by_dataset_id  # noqa: E501

        Get all prediction singletons of all samples of a dataset ordered by the sample mapping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_predictions_by_dataset_id_with_http_info(dataset_id, prediction_uuid_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MongoObjectID dataset_id: ObjectId of the dataset (required)
        :param Timestamp prediction_uuid_timestamp: The timestamp of when the actual predictions were created. This is used as a peg to version predictions. E.g one could upload predictions on day 1 and then create new predictions with an improved model on day 30. One can then upload the new predictions to the same dataset.  (required)
        :param TaskName task_name: If provided, only gets all prediction singletons of all samples of a dataset that were yielded by a specific prediction task name
        :return: list[PredictionSingletons]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_id', 'prediction_uuid_timestamp', 'task_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_predictions_by_dataset_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in params or
                                                       params['dataset_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dataset_id` when calling `get_predictions_by_dataset_id`")  # noqa: E501
        # verify the required parameter 'prediction_uuid_timestamp' is set
        if self.api_client.client_side_validation and ('prediction_uuid_timestamp' not in params or
                                                       params['prediction_uuid_timestamp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `prediction_uuid_timestamp` when calling `get_predictions_by_dataset_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501

        query_params = []
        if 'prediction_uuid_timestamp' in params:
            query_params.append(('predictionUUIDTimestamp', params['prediction_uuid_timestamp']))  # noqa: E501
        if 'task_name' in params:
            query_params.append(('taskName', params['task_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'auth0Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/datasets/{datasetId}/predictions/samples', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PredictionSingletons]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
