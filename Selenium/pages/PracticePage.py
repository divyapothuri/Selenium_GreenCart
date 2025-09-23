import allure
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 20)  # Initialize WebDriverWait with a 10-second timeout

    def test_prac(self):
        self.logger.info("Starting the practice page test.")
        with allure.step("Click on practice link and verify navigation"):
            self.logger.info("Clicking the 'Practice' link.")

            # Explicit wait for the 'Practice' link to be clickable
            practice_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Practice")))
            practice_link.click()
            self.logger.info("Practice link clicked.")

            # Explicit wait for the URL to change to the expected practice page URL
            # Replace "expected_practice_page_url_part" with a unique part of your actual practice page URL
            # For example, if the URL changes from 'homepage.com' to 'homepage.com/practice', use '/practice'
            # Or if it's a completely different domain, use the full expected URL.
            # expected_url_part = "AutomationPractice"  # Common for "rahulshettyacademy" practice page
            # self.wait.until(EC.url_contains(expected_url_part))

            self.logger.info(f"Current URL: {self.driver.current_url}")
            self.logger.info(f"Current page title: {self.driver.title}")
            self.logger.info("Successfully navigated to the practice page and URL verified.")

            # Optional: Wait for a prominent element on the practice page to be visible
            # For example, if there's a heading like "Practice Page"
            # self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Practice Page']")))
            # self.logger.info("Prominent element on practice page is visible.")