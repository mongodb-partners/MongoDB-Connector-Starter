import os

import pymongo
from pymongo.collection import Collection

def get_connection_string(project_name:str='<project_name>')->str:
    """Get collection string for project
    DB_USER and DB_PWD are stored in the users bash profile
    (add the following to ~/.bashrc):
    export DB_USER = <username>
    export DB_PWD = <password>
    Args:
        project_name (str, optional): MongoDB project name. Defaults to '<project_name>'.
    Returns:
        str: Connection string for a MongoDB project
    """
    username = os.environ.get("DB_USER")
    password = os.environ.get("DB_PWD")
    return (
        f"mongodb+srv://{username}:{password}"
        f"@{project_name}.mongodb.net/?retryWrites=true&w=majority"
    )

def get_collection(project_name:str, database_name:str, collection_name:str)->Collection:
    """Get MongoDB collection based on the project, database, and collection name
    Args:
        project_name (str): MongoDB Project name
        database_name (str): MongoDB database name
        collection_name (str): MongoDB collection name
    Returns:
        Collection: MongoDB Collection
    """
    client = pymongo.MongoClient(get_connection_string(project_name))
    return client[database_name][collection_name]
