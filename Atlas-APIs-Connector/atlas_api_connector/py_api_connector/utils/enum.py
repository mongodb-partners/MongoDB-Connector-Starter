from enum import Enum
import py_api_connector.utils.commands as commands


class CRUD(Enum):
    FIND_ONE = ("/findOne", commands.FindOne)
    FIND_MANY = ("/find", commands.FindMany)
    INSERT_ONE = ("/insertOne", commands.InsertOne)
    INSERT_MANY = ("/insertMany", commands.InsertMany)
    UPDATE_ONE = ("/updateOne", commands.UpdateOne)
    UPDATE_MANY = ("/updateMany", commands.UpdateMany)
    DELETE_ONE = ("/deleteOne", commands.DeleteOne)
    DELETE_MANY = ("/deleteMany", commands.DeleteMany)
    REPLACE_ONE = ("/replaceOne", commands.ReplaceOne)
    AGGREGATE = ("/aggregate", commands.Aggregation)


class RESPONSE_CODE(Enum):
    SUCCESS = 200
    BAD_REQUEST = 400
    UNAUTHOURISED = 401
    NOT_FOUND = 404
    SERVER_ERROR = 500