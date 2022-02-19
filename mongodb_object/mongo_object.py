import logging

import pymongo


class MongoObject:

    logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["student_teacher"]

    def insert_method(self, collection_name, data_dict):
        """
        Insert given data to given collection.
        :param collection_name: Name of the collection to which the data is to be added.
        :param data_dict: Content(document) to add in the form of dictionary.
        :return: nothing
        """
        try:
            db_collection_name = self.db[collection_name]
            db_collection_name.insert_one(data_dict)
            print(f"Added given data to {collection_name}")
        except Exception as e:
            print(f"not added")
            logging.exception(msg=f"Error at insert {collection_name} {data_dict}, {e}")

    def delete_method(self, collection_name, data_dict):
        """
        Delete given data from given collection.
        :param collection_name: Name of the collection from which the data is to be deleted.
        :param data_dict: Content(document) to delete form dictionary.
        :return: nothing
        """
        try:
            db_collection_name = self.db[collection_name]
            db_collection_name.delete_one(data_dict)
            print(f"deleted given data from {collection_name}")
        except Exception as e:
            print(f"not deleted")
            logging.exception(msg=f"Error at delete {collection_name} {data_dict}, {e}")

    def update_method(self, collection_name, select_query, value_query):
        """
        update given data from given collection.
        :param value_query:Data to update
        :param select_query:Data select
        :param collection_name: Name of the collection from which the data is to be updated.
        :return: nothing
        """
        try:
            db_collection_name = self.db[collection_name]
            db_collection_name.update_one(select_query, value_query)
            print(f"updated given data from {collection_name}")
        except Exception as e:
            print(e)
            logging.debug(msg=f"Error at update {collection_name} {select_query}, {e}")

    def fetch_value(self, collection_name, select_query):
        """
        Get the id of given value
        :return: nothing
        """
        try:
            db_collection_name = self.db[collection_name]
            dict_obj = db_collection_name.find_one(select_query)
            return dict_obj.get("_id")

        except Exception as e:
            print(e)
            logging.debug(msg=f"Error at fetch value {collection_name} {select_query}, {e}")

    def fetch_value_by_id(self, collection_name, select_query, return_value):
        """
        Get the value of given column by id
        :return: nothing
        """
        try:
            db_collection_name = self.db[collection_name]
            dict_obj = db_collection_name.find_one(select_query)
            return dict_obj.get(return_value)

        except Exception as e:
            print(e)
            logging.debug(msg=f"Error at fetch value {collection_name} {select_query}, {e}")

    def print_all(self, collection_name):
        """
        Return's all documents from the given collection
        :param collection_name:
        :return:
        """
        db_collection_name = self.db[collection_name]
        return db_collection_name.find()

