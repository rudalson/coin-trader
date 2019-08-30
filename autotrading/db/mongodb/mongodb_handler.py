"""
Mongodb handler
"""
import os

from pymongo import MongoClient
from pymongo.cursor import CursorType
import configparser


class MongoDbHandler:
    """
    mongodb handler
    """

    def __init__(self, mode="local", db_name=None, collection_name=None):
        """
        initializer
        """
        config = configparser.ConfigParser()
        config.read('../../../conf/config.ini')
        self.db_config = {"local_ip": config['MONGODB']['local_ip'], "port": config['MONGODB']['port'],
                          "remote_host": config['MONGODB']['remote_host'], "user": config['MONGODB']['user'],
                          "password": config['MONGODB']['password']}

        if mode == "remote":
            self._client = MongoClient(
                "mongodb://{user}:{password}@{remote_host}:{port}".format(**self.db_config))  # 'localhost', 27017)
        elif mode == "local":
            self._client = MongoClient("mongodb://localhost:{port}".format(**self.db_config))

        if db_name is not None:
            self._db = self._client[db_name]
            if collection_name is not None:
                self._collection = self._db[collection_name]
            else:
                raise Exception("Need to collection name")
        else:
            raise Exception("Need to db name")

    def set_db(self, db_name=None, collection_name=None):
        """
        mongo: use db
        """
        if db_name is None:
            raise Exception("Need to dbname name")

        self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]

    def set_collection(self, collection_name=None):
        """
        change collection
        """
        if collection_name is None:
            raise Exception("Need to dbname name")
        self._collection = self._db[collection_name]

    def get_current_db_name(self):
        return self._db.name  # current_db_name

    def get_current_collection_name(self):
        return self._collection.name  # current_collection_name

    def insert_item(self, data, db=None, collection=None):
        """
        insert item one
        """
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.insert_one(data).inserted_id

    def insert_items(self, datas, db=None, collection=None):
        """
        insert many item
        """
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.insert_many(datas).inserted_ids

    def find_item(self, condition=None, db=None, collection=None):
        """
        find_item
        """
        if condition is None:
            condition = {}
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.find(condition, no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)

    def find_one_item(self, condition=None, db=None, collection=None):
        """
        find_item
        """
        if condition is None:
            condition = {}
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.find_one(condition)

    def delete_item(self, condition=None, db=None, collection=None):
        """
        delete item
        """
        if condition is None:
            raise Exception("Need to condition")
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.delete_many(condition)

    def update_item(self, condition=None, update_value=None, db=None, collection=None):
        """
        update item
        """
        if condition is None:
            raise Exception("Need to condition")
        if update_value is None:
            raise Exception("Need to update value")
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.update_many(filter=condition, update=update_value)

    def aggregate(self, pipeline=None, db=None, collection=None):
        if pipeline is None:
            raise Exception("Need to pipeline")
        if db is not None:
            self._db = self._client[db]
        if collection is not None:
            self._collection = self._db[collection]
        return self._collection.aggregate(pipeline)
