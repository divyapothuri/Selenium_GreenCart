import time

import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Flight:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_book(self):

        with allure.step("Enter country name"):
            self.logger.info("Enter country name")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#autosuggest"))).send_keys("ind")
            lst = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".ui-menu-item")))
            for l in lst:
                if l.text == "India":
                    l.click()
                    break
        with allure.step("Enter from city"):
            self.logger.info("Enter from city")
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ctl00_mainContent_ddl_originStation1_CTXT"))).click()
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[value='BLR']"))).click()

        with allure.step("Enter to city"):
            self.logger.info("Enter to city")
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ctl00_mainContent_ddl_destinationStation1_CTXT"))).click()
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "(//a[@value='HYD'][normalize-space()='Hyderabad (HYD)'])[2]"))).click()

        with allure.step("Enter to date"):
            self.logger.info("Enter to date")
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ctl00_mainContent_view_date1"))).click()
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-state-default.ui-state-active.ui-state-hover"))).click()
            self.driver.find_element(By.CSS_SELECTOR,"#ctl00_mainContent_view_date2").sele
