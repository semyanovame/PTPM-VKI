from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self._first_number_input = (By.CSS_SELECTOR, "input[ng-model='first'], input[ng-model='a']")
        self._second_number_input = (By.CSS_SELECTOR, "input[ng-model='second'], input[ng-model='b']")
        self._operator_select = (By.CSS_SELECTOR, "select")
        self._result_label = (By.CSS_SELECTOR, "h2, .ng-binding, [ng-bind]")

    def open(self, url: str):
        self.driver.get(url)

    def enter_first_number(self, number: str):
        element = self.wait.until(EC.presence_of_element_located(self._first_number_input))
        element.clear()
        element.send_keys(number)

    def enter_second_number(self, number: str):
        element = self.wait.until(EC.presence_of_element_located(self._second_number_input))
        element.clear()
        element.send_keys(number)

    def select_operation(self, operation: str):
        element = self.wait.until(EC.presence_of_element_located(self._operator_select))
        select = Select(element)
        select.select_by_visible_text(operation)

    def get_result(self) -> str:
        element = self.wait.until(EC.presence_of_element_located(self._result_label))
        return element.text