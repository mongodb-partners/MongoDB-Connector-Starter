import json

import py_api_connector.api_client.commands as commands
import py_api_connector.utils.setup as setup
from py_api_connector.utils.enum import CRUD
import requests

class DataAPIClient:
    def __init__(self, **kwargs):
        self.conn_setup = setup.ConnectorSetUp(**kwargs)
        self.url = None
        self.headers = None
        self.payload = None
        self.operation = None

    def api_authenticate(self):
        '''
        Helper method for authenticating the API Key and returning if it is valid or not.
        '''
        try:
            self.set_operation(CRUD.FIND_ONE)
            self.set_payload()
            response = self.execute()
            if response.status_code == 200:
                return True
            else:
                return False

        except Exception as e:
            print("Err : ", e)
            return False

    def set_operation(self, operation):
        '''
        Helper method for setting up the url with specified operation and required headers
        '''
        self.operation = operation
        self.url = f"{self.conn_setup.base_url}/{self.operation.value}"
        self.headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': self.conn_setup.api_key
        }

    def set_payload(self, **kwargs):
        '''
        Helper method for setting up the payload, this includes the collection, database, datasource and others based on type of operation.
        '''
        payload = {
            "collection": self.conn_setup.collection,
            "database": self.conn_setup.database,
            "dataSource": self.conn_setup.data_source,
        }

        if self.operation == CRUD.FIND_ONE:
            payload = commands.FindOneCommand(payload, **kwargs).get_payload()

        elif self.operation == CRUD.FIND:
            payload = commands.FindCommand(payload, **kwargs).get_payload()

        self.payload = json.dumps(payload)

    def execute(self):
        '''
        For executing the request and returning the response.
        '''
        try:
            print("Execution values :: \n\b", self.url,
                  "\n", self.headers, "\n", self.payload)

            return requests.request(
                "POST",
                self.url,
                headers=self.headers,
                data=self.payload
            )
        except Exception as e:
            print(f"exception in execution : {e}")
            return None
