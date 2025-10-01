import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocatorPractice:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_page(self):
        self.logger.info("Starting the page")
        with allure.step("Click on forgot password"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Forgot your password?']"))).click()
            self.logger.info("glto forgot password page")
    def test_creds(self, name, email, phonenumber):
        with allure.step("Enter user name"):
            self.logger.info("Enter user name")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name']"))).send_keys(name)
        with allure.step("Enter email"):
            self.logger.info("Enter email")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']"))).send_keys(email)
        with allure.step("Enter phone number"):
            self.logger.info("Enter phonenumber")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Phone Number']"))).send_keys(phonenumber)

        with allure.step("Click Reset login"):
            self.logger.info("Click reset login box")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reset Login']"))).click()
        with allure.step("Fetch password from text"):
            self.logger.info("Fetch password from text")

            msg_ele = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='infoMsg']")))
            msg = msg_ele.text
            print(msg)
            msg1 = msg.split("'")
            password = msg1[1]

        with allure.step("Click Go to login"):
            self.logger.info("Click go to login")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".go-to-login-btn"))).click()


        with allure.step("Enter user name"):
            self.logger.info("Enter user name")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputUsername']"))).send_keys(name)
        with allure.step("Enter password"):
            self.logger.info("Enter password")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))).send_keys(password)

        with allure.step("Click checkbox1"):
            self.logger.info("Click checkbox1")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#chkboxOne"))).click()

        with allure.step("Click checkbox2"):
            self.logger.info("Click checkbox2")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#chkboxTwo"))).click()

        with allure.step("Click Sign in"):
            self.logger.info("Click sign in")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        with allure.step("Click logout"):
            self.logger.info("Click logout")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".logout-btn"))).click()




