from abc import ABC, abstractmethod
from py_api_connector.utils.enum import CRUD

class DataAPICommand(ABC):
    @abstractmethod
    def get_payload(self):
        pass

class FindOneCommand(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None)
        payload['projection'] = kwargs.get('projection', None)
        self.payload = payload

    def get_payload(self):
        return self.payload

class FindCommand(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get("filter", None)
        payload['projection'] = kwargs.get("projection", None)
        payload['sort'] = kwargs.get("sort", None)
        payload['limit'] = kwargs.get("limit", None)
        payload['skip'] = kwargs.get("skip", None)
        self.payload = payload
    
    def get_payload(self):
        return self.payload