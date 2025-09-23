import allure
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 20)  # Initialize WebDriverWait with a 10-second timeout

    def test_checkout(self):
        self.logger.info("Starting the checkout process.")
        with allure.step("Click on Place Order"):
            self.logger.info("Clicking the 'Place Order' button.")
            # Explicit wait for the 'Place Order' button to be clickable
            place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
            place_order_button.click()
            self.logger.info("Successfully clicked 'Place Order'.")
            # Optionally, wait for a new page or a confirmation message to appear after placing the order
            # For example, if it navigates to a billing page, you might wait for an element on that page.

    def test_promo(self):
        self.logger.info("Starting the promo code application process.")
        with allure.step("Apply Promo Code"):
            self.logger.info("Entering promo code 'rahulshettyacademy'.")
            # Explicit wait for the promo code input field to be clickable
            promo_code_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".promoCode")))
            promo_code_input.send_keys("rahulshettyacademy")
            self.logger.info("Promo code entered.")

            self.logger.info("Clicking the 'Apply' promo button.")
            # Explicit wait for the promo button to be clickable
            promo_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".promoBtn")))
            promo_button.click()
            self.logger.info("Promo button clicked.")

            self.logger.info("Waiting for promo code application status message.")
            # Explicit wait for the promo info message to be visible and have text
            promo_info_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
            promo_message = promo_info_element.text
            self.logger.info(f"Promo application message: {promo_message}")
            print(promo_message)