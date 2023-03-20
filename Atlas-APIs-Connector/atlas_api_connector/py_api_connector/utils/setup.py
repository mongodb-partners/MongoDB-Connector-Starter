import json
from py_api_connector.utils.enum import CRUD

class ConnectorSetUp:
    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.data_source = kwargs.get('data_source')
        self.database = kwargs.get('database')
        self.collection = kwargs.get('collection')
        self.api_key = kwargs.get('api_key') if 'api_key' in kwargs else None 
        
        
    # def set_operation(self, operation):
    #     query_params = {
    #         'url': f"{self.base_url}/{operation}",
    #         'headers': {
    #             'Content-Type': 'application/json',
    #             'Access-Control-Request-Headers': '*',
    #             'api-key': self.api_key
    #         },
    #         'payload' : json.dumps({
    #             "collection": self.collection,
    #             "database": self.database,
    #             "dataSource": self.data_source,
    #         })
    #     }

    #     return query_params
    
    # def set_payload():
    #     pass

    