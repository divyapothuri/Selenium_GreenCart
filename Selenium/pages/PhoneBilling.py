import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PhoneBilling:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_phone_bill(self):
        self.logger.info("billing page")
        with allure.step("Enter country"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#country"))).send_keys("ind")
            countries = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='suggestions']/ul/li/a")))
            for country in countries:
                if country.text == "India":
                    country.click()
                break



        with allure.step("Accept terma and conditions"):
             self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='checkbox2']"))).click()
        self.logger.info("Click on check box")

        with allure.step("Enter country"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Purchase']"))).click()

            self.logger.info(" Purchase button clicked successfully")
        with allure.step("Check success message"):
            self.logger.info("Check sucess message after submit")
            msg = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".alert"))).text
            print(msg)
            assert "Success" in msg
