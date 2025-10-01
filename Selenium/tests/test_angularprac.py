import configparser
import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.AngularLogin import AngularLogin
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


@allure.parent_suite("Angular Practice")
@allure.suite("Login details")
@allure.label("User details")
@allure.epic("Enter user details")
@allure.title("Practice Login")
def test_credlogin(driver, logger):

    logger.info("Starting the Login form practice automation script.")
    logger.info("Launch angular practice page")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    print(driver.current_url)
    with allure.step("Verify page"):
        logger.info("Navigating to the home page.")
        login = AngularLogin(driver, logger)
        # login.test_page()

        name = config['user']['user_name']
        email = config['user']['user_email']
        password = config['user']['user_password']
    with allure.step("Enter user details"):
        login.test_creds(name,email,password)