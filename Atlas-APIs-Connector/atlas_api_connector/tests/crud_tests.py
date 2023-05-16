# Adding folder path
import config
import unittest
from py_api_connector.utils.enum import RESPONSE_CODE
import py_api_connector as pyAPI
import sys
sys.path.append("..")


class DataAPITests(unittest.TestCase):

    def test_fail_auth(self):
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key='fake_key')

        # Fails since not a valid API KEY added.
        self.assertEqual(client.api_authenticate(), True)

    def test_find_one(self):
        # Initialize the connector with required configs
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key=config.API_KEY)

        # Set the operation to be performed
        client.set_operation(pyAPI.CRUD.FIND_ONE)
        # Set the payload, might include filter, projections.
        client.set_payload(
            filter={"st": "x+56200+002700"},
            projection={"_id": 1}
        )
        # Execute the client and get the response.
        response = client.execute()
        self.assertEqual(response['status_code'], RESPONSE_CODE.SUCCESS.value)

    def test_insert_one(self):
        # Initialize the connector with required configs
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key=config.API_KEY)
        # Set INSERT_ONE operation
        client.set_operation(pyAPI.CRUD.INSERT_ONE)
        # Set the payload
        client.set_payload(
            document={"test_doc": True}
        )
        # Execute
        response = client.execute()
        self.assertEqual(response['status_code'], RESPONSE_CODE.INSERTED.value)

    def test_update_one(self):
        # Initialize the connector with required configs
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key=config.API_KEY)

        # Set operation
        client.set_operation(pyAPI.CRUD.UPDATE_ONE)
        # Set payload
        client.set_payload(
            filter={'test_doc': True},
            update={'test_doc': False},
            upsert=True  # Default value is False
        )
        # Execute
        response = client.execute()
        self.assertEqual(response['status_code'], RESPONSE_CODE.INSERTED.value)

    def test_delete_one(self):
        # Initialize the connector with required configs
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key=config.API_KEY)
        # Set operation
        client.set_operation(pyAPI.CRUD.DELETE_ONE)
        # Set payload
        client.set_payload(
            filter={'test_doc': True}
        )
        # Execute
        response = client.execute()
        self.assertEqual(response['status_code'], RESPONSE_CODE.SUCCESS.value)

    def test_replace_one(self):
        # Initialize the connector with required configs
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key=config.API_KEY)
        # Set operation
        client.set_operation(pyAPI.CRUD.REPLACE_ONE)
        # Set payload
        client.set_payload(
            filter={'test_doc': True},
            replacement={'revised_doc': True},
            upsert=True  # Default value is False
        )
        response = client.execute()
        self.assertEqual(response['status_code'], RESPONSE_CODE.SUCCESS.value)

    def test_aggregation_one(self):
        # Initialize the connector with required configs
        client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                                     data_source=config.DATA_SOURCE,
                                     database=config.DATABASE_NAME,
                                     collection=config.COLLECTION_NAME,
                                     api_key=config.API_KEY)
        # Set operation
        client.set_operation(pyAPI.CRUD.AGGREGATE)
        # Set payload
        client.set_payload(
            # Pipeline to $match documents based on filter
            # and supress _id field in the result using $project
            pipeline=[
                {
                    '$match': {
                        'test_doc': True
                    }
                }, {
                    '$project': {
                        '_id': 0
                    }
                }
            ]
        )
        # Execute
        response = client.execute()
        self.assertEqual(response['status_code'], RESPONSE_CODE.SUCCESS.value)


if __name__ == "__main__":
    unittest.main()
