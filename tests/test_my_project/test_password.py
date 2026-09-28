import unittest
from src.validator import validate_main

class TestValidatePassword(unittest.TestCase):
    def test_invalid_password_too_short_returns_false(self):
        is_valid, message = validate_main("validUser", "Пар1!", "Пар1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен быть не короче 7 символов")
    def test_invalid_password_missing_uppercase_returns_false(self):
        is_valid, message = validate_main("validUser", "пароль1!", "пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен содержать хотя бы одну заглавную русскую букву")
    def test_invalid_password_missing_lowercase_returns_false(self):
        is_valid, message = validate_main("validUser", "ПАРОЛЬ1!", "ПАРОЛЬ1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен содержать хотя бы одну строчную русскую букву")    
    def test_invalid_password_missing_digit_returns_false(self):
        is_valid, message = validate_main("validUser", "Пароль!", "Пароль!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен содержать хотя бы одну цифру")
    def test_invalid_password_missing_special_char_returns_false(self):
        is_valid, message = validate_main("validUser", "Пароль1", "Пароль1")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен содержать хотя бы один специальный символ")
    def test_passwords_do_not_match_returns_false(self):
        is_valid, message = validate_main("validUser", "Пароль1!", "Пароль2!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароли не совпадают")
    def test_invalid_password_not_string_returns_false(self):
        is_valid, message = validate_main("validUser", 1234567, 1234567)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен быть строкой")
if __name__ == "__main__":
    unittest.main()
