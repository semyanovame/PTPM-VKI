from src.Database import Database
import unittest
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
    def tearDown(self):
        self.db.close()
    def test_add_and_get_data(self):
        self.db.add_data("test_user", "password123", "password123", "Success", None)
        data = self.db.get_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], "test_user")
        self.assertEqual(data[0][2], "password123")
        self.assertEqual(data[0][3], "password123")
        self.assertEqual(data[0][4], "Success")
        self.assertIsNone(data[0][5])
    def test_delete_data(self):
        self.db.add_data("test_user", "password123", "password123", "Success", None)
        data_before_delete = self.db.get_data()
        self.assertEqual(len(data_before_delete), 1)
        user_id = data_before_delete[0][0]
        self.db.delete_data(user_id)
        data_after_delete = self.db.get_data()
        self.assertEqual(len(data_after_delete), 0)
    def test_does_user_exist(self):
        self.db.add_data("test_user", "password123", "password123", "Success", None)
        self.assertTrue(self.db.does_user_exist("test_user"))
        self.assertFalse(self.db.does_user_exist("nonexistent_user"))