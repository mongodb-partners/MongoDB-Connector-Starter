from pymongo.results import InsertOneResult, InsertManyResult, DeleteResult, UpdateResult
from typing import Dict, List
from pymongo.collection import Collection


class DBOperations:
    def __init__(self, collection: Collection) -> None:
        self.collection = collection 

    def insert_document(self, document: Dict[any, any]) -> InsertOneResult:
        """Insert a single document into MongoDB, the document is a python dictionary
        Args:
            document (Dict[any, any]): Dictionary document to add to MongoDB
            collection (Collection): Target mongoDB collection for the document
        Returns:
            InsertOneResult: Insert response code for debugging
        """
        return self.collection.insert_one(document)

    def insert_documents(self, documents: List[Dict[any, any]]) -> InsertManyResult:
        """Insert multiple documents into MongoDB, documents are a list of python dictionaries
            ex: documents = [{"a":1, "b":2}, {"a":3, "b":4}]
        Args:
            documents (List[Dict[any, any]]): Documents to add to MongoDB collection
            collection (Collection): MongoDB collection object
        Returns:
            InsertManyResult: Insert many response code for debugging
        """
        return self.collection.insert_many(documents)

    def update_document(self, query: Dict[any, any], set_values: Dict[any, any]) -> UpdateResult:
        """Update a document in mongoDB, the query identifies the documents to be updated.
        Then, set values specifies which fields to update within the document. 
        Args:
            query (Dict[any,any]): MongoDB query to filter a document within a collection.
            set_values (Dict[any, any]): Specify how to update the identified document
            collection (Collection): MongoDB collection
        Returns:
            UpdateResult: update one response code, for debugging
        """
        return self.collection.update_one(query, set_values)

    def update_documents(self, query: Dict[any, any], set_values: Dict[any, any]) -> UpdateResult:
        """Update documents in mongoDB, the query identifies the documents to be updated.
        Then, set values specifies which fields to update within the document. 
        Args:
            query (Dict[any,any]): MongoDB query to filter documents within a collection.
            set_values (Dict[any, any]): Specify how to update the identified documents
            collection (Collection): MongoDB collection
        Returns:
            UpdateResult: update many response code, for debugging
        """
        return self.collection.update_many(query, set_values)

    def delete_document(self, query: Dict[any, any]) -> DeleteResult:
        """Delete a single document in a mongoDB collection
        Args:
            query (Dict[any,any]): Query to filter collection documents for deletion
            collection (Collection): MongoDB collection
        Returns:
            DeleteResult: delete document response code
        """
        return self.collection.delete_one(query)

    def delete_documents(self, query: Dict[any, any]) -> DeleteResult:
        """Delete many documents for the mongoDB collection
        Args:
            query (Dict[any,any]): Query to filter collection documents for deletion
            collection (Collection): MongoDB collection
        Returns:
            DeleteResult: delete many documents response code
        """
        return self.collection.delete_many(query)
