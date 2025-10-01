import time

import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Client:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_reg(self, name, email, password,phonenumber):
        self.logger.info("Click on register")
        with allure.step("Click on register"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn1"))).click()
        with allure.step("Enter user name"):
            self.logger.info("Enter user name")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#firstName"))).send_keys(name)
        with allure.step("Enter user name"):
            self.logger.info("Enter user  last name")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lastName"))).send_keys("pothuri")
        with allure.step("Enter email"):
            self.logger.info("Enter email")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userEmail"))).send_keys(email)
        with allure.step("enter user mobile number"):
            self.logger.info("Enter user mobile number")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#userMobile"))).send_keys(phonenumber)

        with allure.step("Select occupation"):
            self.logger.info("Select occupation")
            dropdown = Select(self.wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@formcontrolname='occupation']"))))
            dropdown.select_by_index(3)
        with allure.step("select Gender"):
            self.logger.info("select gender")
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Female']"))).click()
        with allure.step("Enter password"):
            self.logger.info("Enter password")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userPassword"))).send_keys(password)
        with allure.step("Enter confirm password"):
            self.logger.info("Enter confirm password")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmPassword"))).send_keys(password)

        with allure.step("Click checkbox"):
            self.logger.info("Check check box")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))).click()

        with allure.step("Click on Submit"):
            self.logger.info("Click on Submit")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login"))).click()

    def test_login(self, email, password):
        with allure.step("Enter email"):
            self.logger.info("Enter email")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userEmail"))).send_keys(email)

        with allure.step("Enter password"):
            self.logger.info("Enter password")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userPassword"))).send_keys(password)

        with allure.step("Click on login"):
            self.logger.info("Click on login")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login"))).click()
    def test_order(self):
        with allure.step("Add product to cart"):
            self.logger.info("Add product to cart")
            products = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//h5")))
            for prod in products:
                if prod.text == "ZARA COAT 3":
                    prod.find_element(By.XPATH,"//button[contains(text(),'Add To Cart')]").click()
            time.sleep(10)
        with allure.step("Click on cart"):
            self.logger.info("Click on cart")
            self.wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@routerlink='/dashboard/cart']"))).click()

        with allure.step("Click on checkout"):
            self.logger.info("Click on checkout")
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Checkout']"))).click()

        with allure.step("Enter country"):
            self.logger.info("Enter country")

            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select Country']"))).send_keys("Indi")
            countries = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//button[@type='button']")))
            for coun in countries:
                if coun.text == "India":
                    coun.click()
                    break



        with allure.step("Click on place order"):
            self.logger.info("Click on place order")
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".btnn"))).click()
        with allure.step("Verify order placed"):
            self.logger.info("Verify order placed")
            msg = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".hero-primary"))).text
            print(msg)
            assert "THANKYOU" in msg








            print(products)


