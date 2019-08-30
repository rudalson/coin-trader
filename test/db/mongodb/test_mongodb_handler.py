"""
Test mongo handler
"""
import unittest, inspect
from autotrading.db.mongodb.mongodb_handler import MongoDbHandler


class MongoDbHandlerTestCase(unittest.TestCase):
    """
    MongodbHanlderTestCase
    """

    def setUp(self):
        print('setUp()')
        self.mongodb = MongoDbHandler("local", "stocker_test", "stocks")

    def test_set_db(self):
        """
        test set_db
        """
        print(inspect.stack()[0][3])
        self.mongodb.set_db("stocker_test")
        self.assertEqual(self.mongodb.get_current_db_name(), "stocker_test")

    def test_set_connection(self):
        """
        test set_connections
        """
        print(inspect.stack()[0][3])
        self.mongodb.set_collection("stocks")
        self.assertEqual(self.mongodb.get_current_collection_name(), "stocks")

    def test_get_db_name(self):
        print(inspect.stack()[0][3])
        dbname = self.mongodb.get_current_db_name()
        assert dbname
        print(dbname)

    def test_get_collection_name(self):
        print(inspect.stack()[0][3])
        collection_name = self.mongodb.get_current_collection_name()
        assert collection_name
        print(collection_name)

    def test_insert_item(self):
        """
        test insert_item
        """
        print(inspect.stack()[0][3])
        id = self.mongodb.insert_item({"code": "0003", "name": "TEST3"})
        print(id)

    def test_find_item(self):
        """
        test find_item
        """
        print(inspect.stack()[0][3])
        item = self.mongodb.find_item({"code": "0003"})
        if item is not None:
            pass
            # self.assertEqual(item["name"], "TEST3")
        print(item)

    def test_insert_items(self):
        """
        test insert_items
        """
        print(inspect.stack()[0][3])
        items = [{"code": "0004", "name": "Test4"},
                 {"code": "0005", "name": "Test5"}]
        ids = self.mongodb.insert_items(items)
        print(ids)

    def test_delete_items(self):
        print(inspect.stack()[0][3])
        items = [{"delete_code": "0004", "name": "Test4"},
                 {"delete_code": "0005", "name": "Test5"}]
        ids = self.mongodb.insert_items(items)
        print(ids)
        self.mongodb.delete_item({})

    def test_move_document(self):
        print(inspect.stack()[0][3])
        items = [{"delete_code": "0006", "name": "Test6"},
                 {"delete_code": "0007", "name": "Test7"}]
        ids = self.mongodb.insert_items(items)
        item_list = self.mongodb.find_item({})
        for item in item_list:
            self.mongodb.set_collection("stocks_test")
            self.mongodb.insert_item(item)
            self.mongodb.set_collection("stocks")
            self.mongodb.delete_item({"_id": item["_id"]})

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
