import json
from py_api_connector.utils.enum import CRUD

class ConnectorSetUp:
    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.data_source = kwargs.get('data_source')
        self.database = kwargs.get('database')
        self.collection = kwargs.get('collection')
        self.api_key = kwargs.get('api_key', None)