# import allure
# import logging
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class CartDashboard:
#     def __init__(self, driver, logger):
#         self.driver = driver
#         self.logger = logger
#         self.wait = WebDriverWait(self.driver, 30)  # Initialize WebDriverWait with a 10-second timeout
#
#     def test_cart(self):
#         self.logger.info("Starting the cart dashboard test.")
#
#         with allure.step("Search for items"):
#             self.logger.info("Searching for item 'ber'.")
#             search_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='search']")))
#             search_input.send_keys("ber")
#             self.logger.info("Search term 'ber' entered.")
#             # It's often good practice to wait for search results to appear
#             # For example, wait for at least one product div to be present after searching
#             self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product']")))
#
#         with allure.step("Click on add to cart"):
#             self.logger.info("Adding all displayed items to the cart.")
#             # Wait for all product elements to be present
#             product_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product']")))
#
#             for product in product_elements:
#                 # Use the 'product' element as the scope for finding the button
#                 # This is crucial to avoid always clicking the first 'ADD TO CART' button found on the page
#                 add_to_cart_button = self.wait.until(EC.element_to_be_clickable((product, By.XPATH, ".//button[text()='ADD TO CART']")))
#                 add_to_cart_button.click()
#                 self.logger.debug(f"Added product to cart.")
#             self.logger.info(f"All {len(product_elements)} items added to cart.")
#
#         with allure.step("Click on cart"):
#             self.logger.info("Clicking on the cart icon.")
#             cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cart']")))
#             cart_icon.click()
#             self.logger.info("Cart icon clicked.")
#             # Optionally, wait for the cart summary/modal to be visible
#             self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))) # Example: wait for checkout button in cart view
#
#         with allure.step("Click on proceed to checkout"):
#             self.logger.info("Clicking 'PROCEED TO CHECKOUT'.")
#             proceed_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
#             proceed_button.click()
#             self.logger.info("Successfully clicked 'PROCEED TO CHECKOUT'.")


import time
import allure
import logging
from selenium.webdriver.common.by import By


class CartDashboard:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def test_cart(self):
        self.logger.info("Starting the cart dashboard test.")

        with allure.step("Search for items"):
            self.logger.info("Searching for item 'ber'.")
            self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
            time.sleep(5)

        with allure.step("Click on add to cart"):
            self.logger.info("Adding all displayed items to the cart.")
            lst = self.driver.find_elements(By.XPATH, "//div[@class='product']")
            for product in lst:
                product.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
                self.logger.debug(f"Added product to cart.")

        with allure.step("Click on cart"):
            self.logger.info("Clicking on the cart icon.")
            self.driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
            time.sleep(5)

        with allure.step("Click on proceed to checkout"):
            self.logger.info("Clicking 'PROCEED TO CHECKOUT'.")
            self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
            time.sleep(5)
            self.logger.info("Successfully proceeded to checkout.")