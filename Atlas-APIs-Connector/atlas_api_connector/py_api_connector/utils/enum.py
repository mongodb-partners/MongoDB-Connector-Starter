from enum import Enum
import py_api_connector.utils.commands as commands


class CRUD(Enum):
    FIND_ONE = ("/findOne", commands.FindOneCommand)
    FIND = ("/find", commands.FindCommand)
    INSERT_ONE = ("/insertOne", commands.InsertOne)
    INSERT_MANY = ("/insertMany", commands.InsertMany)
    UPDATE_ONE = ("/updateOne", commands.UpdateOne)
    DELETE_ONE = ("/deleteOne", commands.UpdateMany)
    UPDATE_MANY = ("/updateMany", commands.ReplaceOne)
    REPLACE_ONE = ("/replaceMany", commands.DeleteOne)
    DELETE_MANY = ("/deleteMany", commands.DeleteMany)
    AGGREGATE = ("/aggregate", commands.Aggregation)