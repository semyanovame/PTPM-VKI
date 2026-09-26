import unittest
from src.validator import validate_main

class TestValidateMain(unittest.TestCase):
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
    def test_invalid_login_format_returns_false(self):
        is_valid, message = validate_main("invalid login", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "логин может содержать только латинские буквы, цифры и знак подчёркивания")
    def test_invalid_email_format_returns_false(self):
        is_valid, message = validate_main("invalidemail@", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "email должен быть в формате local-part@domain")
    def test_invalid_phone_format_returns_false(self):
        is_valid, message = validate_main("+1-23-456-7890", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "телефон должен быть в формате +x-xxx-xxx-xxxx")
    def test_valid_login_5_characters_returns_true(self):
        is_valid, message = validate_main("user1", "Пароль1!", "Пароль1!") 
        self.assertTrue(is_valid)
        self.assertEqual(message, "")
    def test_invalid_email_with_multiple_at_returns_false(self):
        is_valid, message = validate_main("user@@example.com", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "email должен быть в формате local-part@domain")
    def test_invalid_email_without_local_part_returns_false(self):
        is_valid, message = validate_main("@example.com", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "email должен быть в формате local-part@domain")
    def test_invalid_phone_with_letters_returns_false(self):
        is_valid, message = validate_main("+1-abc-def-ghij", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "телефон должен быть в формате +x-xxx-xxx-xxxx")
    def test_invalid_login_not_string_returns_false(self):
        is_valid, message = validate_main(12345, "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Логин должен быть строкой")
    def test_invalid_password_not_string_returns_false(self):
        is_valid, message = validate_main("validUser", 1234567, 1234567)
        self.assertFalse(is_valid)
        self.assertEqual(message, "Пароль должен быть строкой")
if __name__ == "__main__":
    unittest.main()
