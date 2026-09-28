import unittest
from src.validator import validate_main


class TestValidatePhone(unittest.TestCase):
    def test_invalid_phone_format_returns_false(self):
        is_valid, message = validate_main(
            "+1-23-456-7890", "Пароль1!", "Пароль1!"
        )
        self.assertFalse(is_valid)
        self.assertEqual(message, "телефон должен быть в формате +x-xxx-xxx-xxxx")
    def test_invalid_phone_with_letters_returns_false(self):
        is_valid, message = validate_main(
            "+1-abc-def-ghij", "Пароль1!", "Пароль1!"
        )
        self.assertFalse(is_valid)
        self.assertEqual(message, "телефон должен быть в формате +x-xxx-xxx-xxxx")
if __name__ == "__main__":
    unittest.main()
