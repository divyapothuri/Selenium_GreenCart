import allure
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a 10-second timeout

    def test_login(self, name, email):
        self.logger.info("Starting the login process.")

        with allure.step("Enter user name"):
            self.logger.info(f"Entering username: {name}.")
            # Explicit wait for the username input field to be clickable
            username_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']")))
            username_input.send_keys(name)
            self.logger.info("Username entered.")

        with allure.step("Enter email"):
            self.logger.info(f"Entering email address: {email}.")
            # Explicit wait for the email input field to be clickable
            email_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
            email_input.send_keys(email)
            self.logger.info("Email address entered.")

        with allure.step("Check terms"):
            self.logger.info("Clicking the terms agreement checkbox.")
            # Explicit wait for the terms agreement checkbox to be clickable
            agree_terms_checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, "agreeTerms")))
            agree_terms_checkbox.click()
            self.logger.info("Terms agreement checkbox clicked.")

        with allure.step("Click on submit"):
            self.logger.info("Clicking the submit button.")
            # Explicit wait for the submit button to be clickable
            submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-submit")))
            submit_button.click()
            self.logger.info("Submit button clicked.")

        # After submission, it's often good to wait for the next page to load
        # or for an element on the next page to become visible.
        # Example: if it navigates to a dashboard, wait for a dashboard element.
        # For demonstration, let's assume a success message or a new page element
        # self.wait.until(EC.url_changes(self.driver.current_url)) # Waits for URL to change
        # OR
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Welcome to Dashboard']")))

        self.logger.info("Login process completed.")