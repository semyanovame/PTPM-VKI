import unittest
from src.validator import validate_main


class TestValidateEmail(unittest.TestCase):
    def test_invalid_email_format_returns_false(self):
        is_valid, message = validate_main("invalidemail@", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "email должен быть в формате local-part@domain")
    def test_invalid_email_with_multiple_at_returns_false(self):
        is_valid, message = validate_main(
            "user@@example.com", "Пароль1!", "Пароль1!"
        )
        self.assertFalse(is_valid)
        self.assertEqual(message, "email должен быть в формате local-part@domain")
    def test_invalid_email_without_local_part_returns_false(self):
        is_valid, message = validate_main("@example.com", "Пароль1!", "Пароль1!")
        self.assertFalse(is_valid)
        self.assertEqual(message, "email должен быть в формате local-part@domain")
if __name__ == "__main__":
    unittest.main()
