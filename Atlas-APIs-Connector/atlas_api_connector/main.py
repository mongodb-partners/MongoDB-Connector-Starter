import py_api_connector as pyAPI
import config

import logging.config
import yaml
import logging
logger = logging.getLogger(__name__)

with open('logging_config.yaml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

# Initialize the connector with required configs
client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                             data_source=config.DATA_SOURCE,
                             database=config.DATABASE_NAME,
                             collection=config.COLLECTION_NAME,
                             api_key=config.API_KEY)


def check_auth(func):
    # Checks for authentication
    def authenticate():
        # For validating the api_key
        if client.api_authenticate():
            logging.info("authenticated using api_key")
        else:
            logging.info("authentication error")
        # Execute the funciton
        func()

    return authenticate


@check_auth
def find_one():
    # Set the operation to be performed
    client.set_operation(pyAPI.CRUD.FIND_ONE)
    # Set the payload, might include filter, projections.
    client.set_payload(
        filter={"st": "x+56200+002700"},
        projection={"_id": 1}
    )
    # Execute the client and get the response.
    response = client.execute()
    logging.info(response)


@check_auth
def insert_one():
    # Set INSERT_ONE operation
    client.set_operation(pyAPI.CRUD.INSERT_ONE)
    # Set the payload
    client.set_payload(
        document={"test_doc": True}
    )
    # Execute
    response = client.execute()
    logging.info(response)


def update_one():
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
    logging.info(response)


def delete_one():
    # Set operation
    client.set_operation(pyAPI.CRUD.DELETE_ONE)
    # Set payload
    client.set_payload(
        filter={'test_doc': True}
    )
    # Execute
    response = client.execute()
    logging.info(response)


def replace_one():
    # Set operation
    client.set_operation(pyAPI.CRUD.REPLACE_ONE)
    # Set payload
    client.set_payload(
        filter={'test_doc': True},
        replacement={'revised_doc': True},
        upsert=True  # Default value is False
    )
    response = client.execute()
    logging.info(response)


def aggregation():
    # Set operation
    client.set_operation(pyAPI.CRUD.AGGREGATE)
    # Set payload
    client.set_payload(
        # Pipeline to $match documents based on filter 
        # and supress _id field in the result using $project
        pipeline= [
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
    logging.info(response)


if __name__ == '__main__':

    # Uncomment functions to be tested and run the file. 

    # Find one document based on filter
    logging.info("---- FIND ONE ---- ")
    find_one()

    # Insert one document
    # logging.info("---- INSERT ONE ----")
    # insert_one()

    # Update one document
    # logging.info("---- UPDATE ONE ----")
    # update_one()

    # Delete one document
    # logging.info("---- DELETE ONE ----")
    # delete_one()

    # Replace one document
    # logging.info("---- REPLACE ONE ----")
    # replace_one()

    # Aggreagtion pipeline example
    # logging.info("---- AGGREGATION ----")
    # aggregation()
