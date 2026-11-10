import unittest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = CalculatorPage(self.driver)
        self.page.open("https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/")

    def tearDown(self):
        try:
            self.driver.quit()
        except Exception:
            pass

    def test_addition(self):
        self.page.enter_first_number("5")   
        self.page.enter_second_number("3")
        self.page.select_operation("+")
        result = self.page.get_result()
        self.assertIn("8", result)

    def test_subtraction(self):
        self.page.enter_first_number("10")
        self.page.enter_second_number("4")
        self.page.select_operation("-")
        result = self.page.get_result()
        self.assertIn("6", result)

    def test_multiplication(self):
        self.page.enter_first_number("6")
        self.page.enter_second_number("7")
        self.page.select_operation("*")
        result = self.page.get_result()
        self.assertIn("42", result)

    def test_division(self):
        self.page.enter_first_number("20")
        self.page.enter_second_number("4")
        self.page.select_operation("/")
        result = self.page.get_result()
        self.assertIn("5", result)

    def test_division_by_zero(self):
        self.page.enter_first_number("10")
        self.page.enter_second_number("0")
        self.page.select_operation("/")
        result = self.page.get_result()
        self.assertIn("null", result)

    def test_boundary_negative_numbers(self):
        self.page.enter_first_number("-15")
        self.page.enter_second_number("5")
        self.page.select_operation("+")
        result = self.page.get_result()
        self.assertIn("-10", result)
    def test_boundary_empty_fields(self):
        self.page.enter_first_number("")
        self.page.enter_second_number("")
        self.page.select_operation("+")
        result = self.page.get_result()
        self.assertIn("0", result) 


if __name__ == '__main__':
    unittest.main()