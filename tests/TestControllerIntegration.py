import unittest
from unittest.mock import Mock

from src.Controller import Controller
from src.Database import Database
from src.Validator import Validator
from src.UserInterface import AbstractUserInterface
from src.ExternalService import AbstractPushingService


class TestControllerIntegration(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.validator = Validator()
        self.push = Mock(spec=AbstractPushingService)
        self.ui = Mock(spec=AbstractUserInterface)
        self.controller = Controller(self.validator, self.push, self.db, self.ui)

    def tearDown(self):
        self.db.close()

    def test_successful_registration(self):
        self.ui.get_user_input.return_value = ("vasya_01", "Пароль1!", "Пароль1!")

        ok, msg = self.controller.process_registration()

        self.assertTrue(ok)
        self.assertIn("успешна", msg)
        self.assertTrue(self.db.does_user_exist("vasya_01"))
        self.push.push_data.assert_called_once()
        self.ui.display_message.assert_called_once()

    def test_login_already_exists(self):
        self.db.add_data("vasya_01", "hash", "hash", "Success", None)
        self.ui.get_user_input.return_value = ("vasya_01", "Пароль1!", "Пароль1!")

        ok, msg = self.controller.process_registration()

        self.assertFalse(ok)
        self.assertIn("уже существует", msg)
        self.assertEqual(len(self.db.get_data()), 1)
        self.push.push_data.assert_called_once()
        self.ui.display_message.assert_called_once()

    def test_validation_error(self):
        self.ui.get_user_input.return_value = ("abc", "Пароль1!", "Пароль1!")

        ok, msg = self.controller.process_registration()

        self.assertFalse(ok)
        self.assertIn("Ошибка", msg)
        self.assertEqual(len(self.db.get_data()), 0)
        self.push.push_data.assert_called_once()
        self.ui.display_message.assert_called_once()


if __name__ == "__main__":
    unittest.main()