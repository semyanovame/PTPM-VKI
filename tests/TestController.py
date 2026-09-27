import unittest
from unittest.mock import MagicMock
from src.Controller import Controller
class TestController(unittest.TestCase):
    def test_successful_validation(self):
        validator = MagicMock()
        database = MagicMock()
        pushing_service = MagicMock()
        user_interface = MagicMock()
        controller = Controller(validator, pushing_service, database, user_interface)

        user_interface.get_input.return_value = ("valid_login", "ValidPass1!", "ValidPass1!")
        database.does_user_exist.return_value = False
        validator.validate_main.return_value = (True, "")
        validator.hash_password.return_value = "hashed_password"


        success, result = controller.process_registration()

        self.assertTrue(success)
        self.assertEqual(result, "Регистрация успешна для пользователя: valid_login")
        database.add_data.assert_called_once_with("valid_login", "hashed_password", "hashed_password", "Success", None)
        pushing_service.push_data.assert_called_once_with("Регистрация успешна для пользователя: valid_login")
    def test_failed_validation(self):
        validator = MagicMock()
        database = MagicMock()
        pushing_service = MagicMock()
        user_interface = MagicMock()
        controller = Controller(validator, pushing_service, database, user_interface)

        user_interface.get_input.return_value = ("invalid_login", "short", "short")
        database.does_user_exist.return_value = False
        validator.validate_main.return_value = (False, "Пароль слишком короткий")
        success, result = controller.process_registration()

        self.assertFalse(success)
        self.assertEqual(result, "Пароль слишком короткий")
        database.add_data.assert_not_called()
        pushing_service.push_data.assert_not_called()