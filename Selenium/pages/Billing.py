import allure
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Billing:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a 10-second timeout

    def test_bill(self):
        self.logger.info("Starting the billing process.")
        with allure.step("Select the country"):
            self.logger.info("Selecting 'India' from the country dropdown.")

            # Explicit wait for the dropdown to be visible and enabled
            dropdown_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//select)[1]")))
            dropdown = Select(dropdown_element)
            dropdown.select_by_value("India")
            self.logger.info("Country 'India' selected.")

        with allure.step("Select the checkbox"):
            self.logger.info("Clicking the terms and conditions checkbox.")

            # Explicit wait for the checkbox to be clickable
            checkbox_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
            checkbox_element.click()
            self.logger.info("Terms and conditions checkbox clicked.")

        with allure.step("Click on proceed"):
            self.logger.info("Clicking the 'Proceed' button.")

            # Explicit wait for the 'Proceed' button to be clickable
            proceed_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Proceed']")))
            proceed_button.click()
            self.logger.info("Successfully clicked 'Proceed'.")