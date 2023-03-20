from enum import Enum

class CRUD(Enum):
    FIND_ONE = "action/findOne"
    FIND = "action/find"
    INSERT_ONE = "action/insertOne"
    UPDATE_ONE = "action/updateOne"
    DELETE_ONE = "action/deleteOne"