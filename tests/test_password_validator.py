import unittest
from src.password_validator import validate_password
class TestPasswordValidator(unittest.TestCase):
    #Позитивное тестирование
    def test_valid_password_latin(self):
        self.assertTrue(validate_password("SecurePass1!"))
    def test_valid_password_cyrillic(self):
        self.assertTrue(validate_password("ПарольТест9#"))
        #Анализ граничных значений длины
    def test_boundary_length_7(self):
        self.assertFalse(validate_password("Pa!ss1!"))
    def test_boundary_length_8(self):
        self.assertTrue(validate_password("Pa!sss1!"))
    def test_boundary_length_20(self):
        self.assertTrue(validate_password("SeecurePassw1!ord20!")) 
    def test_boundary_length_21(self):
        self.assertFalse(validate_password("SeecurePassw1!ord211!")) 

    #Классы эквивалентности (неполный состав символов)
    def test_without_A_Z(self):
        self.assertFalse(validate_password("securepass1!"))
    def test_without_a_z(self):
        self.assertFalse(validate_password("SECUREPASS1!"))
    def test_without_1_9(self):
        self.assertFalse(validate_password("SecurePassword!"))
    def test_without_special(self):
        self.assertFalse(validate_password("SecurePassword1"))
    def test_with_wrong_spec(self):
        self.assertFalse(validate_password("SecurePass1_"))
        #Тестирование исключительных ситуаций
    
    def test_type_error_int(self):
        with self.assertRaises(TypeError):
            validate_password(12345678)
    def test_type_error_None(self):
            with self.assertRaises(TypeError):
                validate_password(None)

    def test_value_error_space_at_start(self):
        with self.assertRaises(ValueError):
            validate_password(" Pass1234!")
    def test_value_error_space_at_centre(self):
        with self.assertRaises(ValueError):
            validate_password("Pass 1234!")

    def test_value_error_space_at_end(self):
        with self.assertRaises(ValueError):
            validate_password("Pass1234! ")