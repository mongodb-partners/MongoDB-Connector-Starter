from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class DataAPICommand(ABC):
    @abstractmethod
    def get_payload(self):
        pass

class FindOne(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None) 
        payload['projection'] = kwargs.get('projection', None) 
        self.payload = payload

    def get_payload(self):
        return self.payload

class FindMany(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get("filter", None)
        payload['projection'] = kwargs.get("projection", None)
        payload['sort'] = kwargs.get("sort", None)
        payload['limit'] = kwargs.get("limit", None)
        payload['skip'] = kwargs.get("skip", None)
        self.payload = payload
    
    def get_payload(self):
        return self.payload

class InsertOne(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['document'] = kwargs.get('document', None)
        self.payload = payload
        if not isinstance(self.payload['document'], dict):
            logger.warn("Inserting document is not in correct format. Please insert document as JSON.")
    
    def get_payload(self):
        return self.payload

class InsertMany(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['documents'] = kwargs.get('documents', None)
        self.payload = payload

        if not isinstance(self.payload['documents'], list):
            logger.warn("Inserting documents are not in correct format. Please insert document as Array of JSONs.")
    
    def get_payload(self):
        return self.payload

class UpdateOne(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None)
        payload['update'] = kwargs.get('update', None)
        payload['upsert'] = kwargs.get('upsert', False)
        self.payload = payload
    
    def get_payload(self):
        return self.payload

class UpdateMany(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None)
        payload['update'] = kwargs.get('update', None)
        payload['upsert'] = kwargs.get('upsert', False)
        self.payload = payload
    
    def get_payload(self):
        return self.payload

class ReplaceOne(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None)
        payload['replacement'] = kwargs.get('replacement', None)
        payload['upsert'] = kwargs.get('upsert', False)
        self.payload = payload
    
    def get_payload(self):
        return self.payload
    
class DeleteOne(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None)
        self.payload = payload

    def get_payload(self):
        return self.payload


class DeleteMany(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['filter'] = kwargs.get('filter', None)
        self.payload = payload
    
    def get_payload(self):
        return self.payload
    
class Aggregation(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['pipeline'] = kwargs.get('pipeline', [])
        # Warning for pipelines 


        self.payload = payload
    
    def get_payload(self):
        return self.payload