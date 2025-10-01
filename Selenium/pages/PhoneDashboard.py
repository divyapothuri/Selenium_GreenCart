import allure
import logging

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PhoneDashboard:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)

    def test_add_phones(self):
        self.logger.info("Adding mobile products to cart")
        with allure.step("Adding mobile products to cart"):
            # Corrected line: removed the extra parentheses
            prods = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")


            for product_card in prods:
                product_name_element = product_card.find_element(By.CSS_SELECTOR, "h4.card-title a")
                product_name = product_name_element.text
                print(f"Checking product: {product_name}")  # Added for debugging
                if product_name == "Nokia Edge":
                    product_card.find_element(By.CSS_SELECTOR, ".btn").click()
                    self.logger.info("Nokia Edge added to cart.")
                    break

    def test_click_checkout(self):
        with allure.step("Click on checkout button"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-primary"))).click()


