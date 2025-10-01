import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AngularLogin:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_page(self):
        self.logger.info("Starting the page")
        with allure.step("Launch angular practice shop page"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Shop']"))).click()
            self.logger.info("page title")
            print(self.driver.title)
            self.logger.info("url")
            print(self.driver.get_url)
    def test_creds(self, name, email, password):
        with allure.step("Enter user name"):
            self.logger.info("Enter user name")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(// input[@ name='name'])[1]"))).send_keys(name)
        with allure.step("Enter email"):
            self.logger.info("Enter email")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).send_keys(email)
        with allure.step("Enter password"):
            self.logger.info("Enter password")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#exampleInputPassword1"))).send_keys(password)

        with allure.step("Click checkbox"):
            self.logger.info("Check check box")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#exampleCheck1"))).click()
        with allure.step("Select Gender"):
            self.logger.info("Select Gender")
            gender_dropdown = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//select[@id='exampleFormControlSelect1']")))  # Ensure you're targeting a <select> element
            select_element = Select(gender_dropdown)  # Use Select to interact with <select> element
            select_element.select_by_index(1)  # Selecting the gender option by value

        with allure.step("Select Employee"):
            self.logger.info("Select Employee")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#inlineRadio2"))).click()

        with allure.step("Click on Submit"):
            self.logger.info("Click on Submit")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit']"))).click()

        with allure.step("Check success message"):
            self.logger.info("Check sucess message after submit")
            msg = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".alert"))).text
            print(msg)
            assert "Success" in msg


