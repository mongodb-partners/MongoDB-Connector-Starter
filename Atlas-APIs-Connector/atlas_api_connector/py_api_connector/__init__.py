"""
    A wrapper module for using Atlas Data API, contains support for various different
    operations that are supported. 

    To understand in detail, follow this link : https://www.mongodb.com/docs/atlas/api/data-api/
"""
from py_api_connector.api_client.data_api import DataAPIClient
from py_api_connector.utils.setup import ConnectorSetUp
from py_api_connector.utils.enum import CRUD