# import allure
# import logging
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LinkPractice:
#     def __init__(self, driver, logger):
#         self.driver = driver
#         self.logger = logger
#         self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a 10-second timeout
#
#     def _click_and_verify_link(self, link_text, expected_url_part):
#         """Helper method to handle clicking a link and verifying navigation."""
#         self.logger.info(f"Clicking on '{link_text}' link.")
#
#         # Explicit wait for the link to be clickable
#         practice_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
#         practice_link.click()
#         self.logger.info(f"'{link_text}' link clicked.")
#
#         # Explicit wait for the URL to change to the expected practice page URL
#         self.wait.until(EC.url_contains(expected_url_part))
#
#         self.logger.info(f"Current URL: {self.driver.current_url}")
#         self.logger.info(f"Current page title: {self.driver.title}")
#         self.logger.info(f"Successfully navigated to the practice website via '{link_text}'.")
#
#     def test_link(self):
#         self.logger.info("Starting the practice link test for 'Automation Practise - 1'.")
#         with allure.step("Select 'Automation Practise - 1' website"):
#             # Replace "practice1_url_part" with a unique part of the actual URL for Practice 1
#             self._click_and_verify_link("Automation Practise - 1", "AutomationPractice/index_new.html")  # Example part
#
#     def test_link_2(self):
#         self.logger.info("Starting the practice link test for 'Automation Practise - 2'.")
#         with allure.step("Select 'Automation Practise - 2' website"):
#             # Replace "practice2_url_part" with a unique part of the actual URL for Practice 2
#             self._click_and_verify_link("Automation Practise - 2", "AutomationPractice/index.html")  # Example part
#
#     def test_link_3(self):
#         self.logger.info("Starting the practice link test for 'Automation Practise - 3'.")
#         with allure.step("Select 'Automation Practise - 3' website"):
#             # Replace "practice3_url_part" with a unique part of the actual URL for Practice 3
#             self._click_and_verify_link("Automation Practise - 3", "another_practice_page_part")  # Example part
#             # Or perhaps if it opens in a new tab/window, you'd need to switch to it:
#             # self.wait.until(EC.number_of_windows_to_be(2))
#             # new_window_handle = [handle for handle in self.driver.window_handles if handle != self.driver.current_window_handle][0]
#             # self.driver.switch_to.window(new_window_handle)
#             # self.wait.until(EC.url_contains("another_practice_page_part"))
#             # self.logger.info(f"Switched to new window. Current URL: {self.driver.current_url}")
#             # ... perform actions on new window ...
#             # self.driver.close() # Close the new window
#             # self.driver.switch_to.window(self.driver.window_handles[0]) # Switch back to original


import time
import allure
import logging
from selenium.webdriver.common.by import By


class LinkPractice:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def test_link(self):
        self.logger.info("Starting the practice link test.")
        with allure.step("Select the Practice website"):
            self.logger.info("Clicking on 'Automation Practise - 1' link.")
            self.driver.find_element(By.LINK_TEXT, "Automation Practise - 1").click()
            time.sleep(5)
            self.logger.info(f"Current URL: {self.driver.current_url}")
            self.logger.info(f"Current page title: {self.driver.title}")
            self.logger.info("Successfully navigated to the practice website.")
    def test_link_2(self):
        self.logger.info("Clicking on 'Automation Practise - 2' link.")
        self.driver.find_element(By.LINK_TEXT, "Automation Practise - 2").click()
        time.sleep(5)
        self.logger.info(f"Current URL: {self.driver.current_url}")
        self.logger.info(f"Current page title: {self.driver.title}")
        self.logger.info("Successfully navigated to the practice website.")
    def test_link_3(self):
        self.logger.info("Clicking on 'Automation Practise - 3' link.")
        self.driver.find_element(By.LINK_TEXT, "Automation Practise - 3").click()
        time.sleep(5)
        self.logger.info(f"Current URL: {self.driver.current_url}")
        self.logger.info(f"Current page title: {self.driver.title}")
        self.logger.info("Successfully navigated to the practice website.")