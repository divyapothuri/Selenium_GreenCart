import configparser
import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Billing import Billing
from pages.CartDashboard import CartDashboard
from pages.LinkPractice import LinkPractice
from pages.LoginPage import LoginPage
from pages.PracticePage import PracticePage
from pages.Checkout import Checkout
from tests.conftest import logger
from utils import *
from utils.report import generate_allure_report_with_timestamp

# This line is for report generation and should be run as a separate command.
# Placing it here can cause issues with test execution.
generate_allure_report_with_timestamp()

config = configparser.ConfigParser()

# The script failed because the config.ini file was not found.
# This code will try to read the config file from two common locations.

# Path 1: Assuming config.ini is in the project root directory (one level up from 'tests')
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path_1 = os.path.join(project_root, 'config.ini')

# Path 2: Assuming config.ini is in the same directory as the test script ('tests')
config_path_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

# Try reading from both paths and log the attempt for debugging
if os.path.exists(config_path_1):
    config.read(config_path_1)
    #logger.info(f"Successfully loaded config from: {config_path_1}")
elif os.path.exists(config_path_2):
    config.read(config_path_2)
    #logger.info(f"Successfully loaded config from: {config_path_2}")
else:
    #logger.error(f"Could not find config.ini at either of these paths: {config_path_1} or {config_path_2}")
    # Raise an error to fail the test immediately with a clear message
    raise FileNotFoundError("config.ini file not found. Please ensure it's in the project root or the 'tests' directory.")


@allure.parent_suite("Green Cart")
@allure.suite("Order products")
@allure.label("veggies")
@allure.epic("Make order")
@allure.title("Full Checkout Process")
def test_cart(driver, logger):
    driver.get("https://rahulshettyacademy.com")
    print(driver.title)
    print(driver.current_url)
    """
    Tests the full checkout process on the Greenkart website.
    The 'driver' and 'logger' fixtures are automatically provided by conftest.py.
    """
    logger.info("Starting the Greenkart test automation script.")

    with allure.step("Landing on home page"):
        logger.info("Navigating to the home page.")
        home = PracticePage(driver, logger)
        home.test_prac()
        logger.info(f"Current URL: {driver.current_url}")

    with allure.step("Landing on Login page"):
        logger.info("Navigating to the login page.")
        login = LoginPage(driver, logger)
        name = config['user']['user_name']
        email = config['user']['user_email']
        login.test_login(name, email)
        logger.info("Login successful.")

    with allure.step("Click on practice link"):
        logger.info("Clicking on the practice link.")
        link = LinkPractice(driver, logger)
        link.test_link()
        logger.info("Practice page loaded.")

    with allure.step("Landing on Green cart page"):
        logger.info("Adding items to the cart.")
        cart = CartDashboard(driver, logger)
        cart.test_cart()
        logger.info("Items added and cart page loaded.")

    with allure.step("Proceeding for check out"):
        logger.info("Proceeding to checkout.")
        check = Checkout(driver, logger)
        check.test_promo()
        check.test_checkout()
        logger.info("Checkout page loaded.")

    with allure.step("Confirming the order"):
        logger.info("Confirming the final order.")
        bill = Billing(driver, logger)
        bill.test_bill()
        logger.info("Order confirmed and test completed successfully.")
