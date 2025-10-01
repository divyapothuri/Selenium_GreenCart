import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PhoneCheckout:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_phone_checkout(self):
        self.logger.info("Click on checkout for billing")
        with allure.step("Click on checkout for billing"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Checkout']"))).click()
            self.logger.info("Clicked on checkout for billing")
