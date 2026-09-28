import unittest
from src.validator import validate_main


class TestValidateLogin(unittest.TestCase):
    def test_valid_login_and_password_returns_true(self):
        is_valid, message = validate_main("validUser", "Пароль1!", "Пароль1!")
        self.assertTrue(is_valid)
        self.assertEqual(message, "")
    def test_invalid_login_too_short_returns_false(self):
        # логин короче 5 символов должен отклониться на первом же шаге
        # до проверки пароля вообще не должно дойти
        is_valid, message = validate_main("ab", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Логин должен быть не короче 5 символов")
    def test_invalid_login_blacklisted_returns_false(self):
        is_valid, message = validate_main("admin", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "логин не может быть из черного списка")
    def test_invalid_login_format_returns_false(self):
        is_valid, message = validate_main(
            "invalid login", "Пароль1!", "Пароль1!"
        )
        self.assertFalse(is_valid)
        self.assertEqual(
            message,
            "логин может содержать только латинские буквы, цифры и знак подчёркивания",
        )
    def test_valid_login_5_characters_returns_true(self):
        is_valid, message = validate_main("user1", "Пароль1!", "Пароль1!")
        self.assertTrue(is_valid)
        self.assertEqual(message, "")
    def test_invalid_login_not_string_returns_false(self) -> None:
        is_valid, message = validate_main(12345, "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Логин должен быть строкой")
if __name__ == "__main__":
    unittest.main()
