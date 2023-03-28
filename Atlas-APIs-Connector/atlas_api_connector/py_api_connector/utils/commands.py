from abc import ABC, abstractmethod

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

class InsertOne(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['document'] = kwargs.get('document', None)
        self.payload = payload
    
    def get_payload(self):
        return self.payload

class InsertMany(DataAPICommand):
    def __init__(self, payload, **kwargs):
        payload['documents'] = kwargs.get('documents', None)
        self.payload = payload
    
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
        payload['pipeline'] = kwargs.get('pipeline', None)
        self.payload = payload
    
    def get_payload(self):
        return self.payload