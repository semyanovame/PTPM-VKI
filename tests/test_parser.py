import unittest
import os
from unittest.mock import patch, MagicMock
from src.parser import Parser
from src.database import DatabaseRepository

class TestParser(unittest.TestCase):
    def setUp(self):
        self.repository = DatabaseRepository(":memory:")  
        self.parser = Parser(self.repository)

        fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'sample.html')
        with open(fixture_path, 'r', encoding='utf-8') as f:
            self.sample_html = f.read()

    @patch('requests.get')
    def test_parse_page(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = self.sample_html
        mock_get.return_value = mock_response

        url = "http://example.com"
        result = self.parser.parse_page(url)

        expected_result = [
            {'id': 1, 'name': 'User1', 'message': 'This is a test message 1.'},
            {'id': 2, 'name': 'User2', 'message': 'This is a test message 2.'}
        ]
        self.assertEqual(result, expected_result)

    def test_save_to_db(self):
        parsed_data = [
            {'id': 1, 'name': 'User1', 'message': 'This is a test message 1.'},
            {'id': 2, 'name': 'User2', 'message': 'This is a test message 2.'}
        ]
        self.parser.save_to_db(parsed_data, self.repository)

        # Verify that the data was saved to the database
        result1 = self.repository.get_by_id(1)
        result2 = self.repository.get_by_id(2)

        self.assertEqual(result1['name'], 'User1')
        self.assertEqual(result1['message'], 'This is a test message 1.')
        self.assertEqual(result2['name'], 'User2')
        self.assertEqual(result2['message'], 'This is a test message 2.')