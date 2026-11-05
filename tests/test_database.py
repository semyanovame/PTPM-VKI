import unittest
import sqlite3
from src.database import DatabaseRepository

class TestDatabaseRepository(unittest.TestCase):
    def setUp(self):
        # Use an in-memory database for testing
        self.db_repository = DatabaseRepository(":memory:")

    def test_add_and_success(self):
        result = self.db_repository.add(1, "Test User", "This is a test message.")
        self.assertTrue(result)

    def test_add_duplicate_id(self):
        self.db_repository.add(1, "Test User", "This is a test message.")
        with self.assertRaises(sqlite3.IntegrityError):
            self.db_repository.add(1, "Another User", "This is another message.")

    def test_get_by_id_and_success(self):
        self.db_repository.add(1, "Test User", "This is a test message.")
        result = self.db_repository.get_by_id(1)
        self.assertEqual(result['name'], "Test User")
        self.assertEqual(result['message'], "This is a test message.")

    def test_get_by_id_not_found(self):
        result = self.db_repository.get_by_id(999)
        self.assertIsNone(result)


    def test_get_by_name_and_success(self):
        self.db_repository.add(1, "Test User", "This is a test message.")
        self.db_repository.add(2, "Test User", "This is another test message.")
        result = self.db_repository.get_by_name("Test User")
        self.assertEqual(len(result), 2)
    def test_get_by_name_not_found(self):
        result = self.db_repository.get_by_name("Nonexistent User")
        self.assertEqual(result, [])

    def test_update_and_success(self):
        self.db_repository.add(1, "Test User", "This is a test message.")
        result = self.db_repository.update(1, "Updated message.")
        self.assertTrue(result)
        updated_record = self.db_repository.get_by_id(1)
        self.assertEqual(updated_record['message'], "Updated message.")
    def test_update_not_found(self):
        result = self.db_repository.update(999, "Updated message.")
        self.assertFalse(result)


    def test_delete_and_success(self):
        self.db_repository.add(1, "Test User", "This is a test message.")
        result = self.db_repository.delete(1)
        self.assertTrue(result)
        deleted_record = self.db_repository.get_by_id(1)
        self.assertIsNone(deleted_record)

    def test_delete_not_found(self):
        result = self.db_repository.delete(999)
        self.assertFalse(result)