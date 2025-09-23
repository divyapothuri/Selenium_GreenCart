import logging
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import pytest

@pytest.fixture(scope="session")
def logger():
    """
    Configures and returns a logger instance for the entire test session.
    """
    # Create a logger
    test_logger = logging.getLogger("pytest_logger")
    test_logger.setLevel(logging.INFO)

    # Create a directory for logs if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, "test.log")

    # Create file handler which logs all messages
    file_handler = logging.FileHandler(log_file_path, mode='w')
    file_handler.setLevel(logging.DEBUG)

    # Create console handler to output logs to the terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    test_logger.addHandler(file_handler)
    test_logger.addHandler(console_handler)

    return test_logger

@pytest.fixture(scope="session")
def driver():
    # options = Options()
    # # Add any options here, e.g., options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com")

    print(driver.title)
    print(driver.current_url)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(5)
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the Pytest report hook to add a screenshot on test failure.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # Get the driver instance from the test class
        try:
            driver = item.funcargs['driver']
            # Take a screenshot
            screenshot_path = f"screenshots/{item.name}_failure.png"
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")



# # Example of a recording fixture
# @pytest.fixture(scope="session")
# def video_recorder(request):
#     video_file = f"videos/{request.node.name}_recording.mp4"
#     command = [
#         "ffmpeg",
#         "-f", "gdigrab",  # Use gdigrab for Windows, x11grab for Linux
#         "-i", "desktop",
#         "-framerate", "15",
#         "-pix_fmt", "yuv420p",
#         video_file
#     ]
#     # Start the recording process
#     recorder = subprocess.Popen(command)
#     yield
#     # Stop the recording process when the test session ends
#     recorder.terminate()
#     print(f"\nVideo saved to: {video_file}")