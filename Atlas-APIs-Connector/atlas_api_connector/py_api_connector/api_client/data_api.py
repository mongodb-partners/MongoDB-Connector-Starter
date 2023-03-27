import json
import requests

import py_api_connector.utils.setup as setup
from py_api_connector.utils.enum import CRUD

class DataAPIClient:
    def __init__(self, **kwargs):
        self.conn_setup = setup.ConnectorSetUp(**kwargs)
        self.url = None
        self.headers = None
        self.payload = None
        self.operation = None

    def api_authenticate(self):
        '''
        For authenticating the API Key and returning if it is valid or not.
        '''
        self.set_operation(CRUD.FIND_ONE)
        self.set_payload()
        response = self.execute()
        return response.status_code == 200

    def set_operation(self, operation):
        '''
        For setting up the url with specified operation and required headers
        '''
        self.operation = operation
        self.url = f"{self.conn_setup.base_url}/action{self.operation.value[0]}"
        self.headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': self.conn_setup.api_key
        }

    def set_payload(self, **kwargs):
        '''
        For setting up the payload, this includes the collection, database, 
        datasource and others based on type of operation.

        '''
        payload = {
            "collection": self.conn_setup.collection,
            "database": self.conn_setup.database,
            "dataSource": self.conn_setup.data_source,
        }

        command_class = self.operation.value[1]
        payload = command_class(payload, **kwargs).get_payload()
        self.payload = json.dumps(payload)

    def execute(self):
        '''
        For executing the request and returning the response.
        '''
        try:
            print("Execution values :: \n\b", 
                  self.url,"\n", 
                  self.headers, "\n", 
                  self.payload)
            
            response = requests.request(
                "POST",
                self.url,
                # headers=self.headers,
                data=self.payload
            )
            response.raise_for_status()
            return response
            
        except requests.exceptions.HTTPError as httpError:
            # Handle any HTTP errors here
            status_code = httpError.response.status_code
            if status_code == 400:
                print("Bad Request \n\
                      The request was invalid. This might mean:\
                      \n - A request header is missing.\
                      \n - The request body is malformed or improperly encoded.\
                      \n - A field has a value with an invalid type.\
                      \n - The specified data source is disabled or does not exist.\
                      \n - The specified database or collection does not exist.")
                
            elif status_code == 401:
                print("Unauthorized \n\
                       - The request did not include an authorized and enabled Data API Key. Ensure that your Data API Key is enabled for the cluster.")

            elif status_code == 404:
                print("Not found\n\
                      - The request was sent to an endpoint that does not exist.")

            elif status_code >= 500:
                print("Server Error \n\
                      - The Data API encountered an internal error and could not complete the request.")
            
        except requests.exceptions.Timeout as e:
            # Handle any timeout errors here
            print('The request timed out:', e)
            
        except requests.exceptions.ConnectionError as e:
            # Handle any connection errors here
            print('A connection error occurred:', e)
            
        except Exception as e:
            # Handle any other exceptions here
            print('An unexpected error occurred:', e)
