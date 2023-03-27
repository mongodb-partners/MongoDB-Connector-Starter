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


def authenticate():
    # For validating the api_key
    if client.api_authenticate():
        logging.info("authenticated using api_key")
    else:
        logging.info("authentication error")


if __name__ == '__main__':
    # Check if the authentication is valid
    logging.info("---- AUTHENTICATING ---- ")
    authenticate()

    # Find one document based on filter
    logging.info("---- FIND ONE ---- ")

    # Set the operation to be performed
    client.set_operation(pyAPI.CRUD.FIND_ONE)
    # Set the payload, might include filter, projections.
    client.set_payload(
        filter={"st": "x+56200+002700"},
        projection={"_id": 1}
    )
    # Execute the client and get the response.
    response = client.execute()

    if response:
        # Check if response recieved.
        print("Response", response.text)
    else:
        print("No response!")