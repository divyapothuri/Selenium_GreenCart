import subprocess
import os
import time
import logging


def generate_allure_report_with_timestamp(logger, results_dir="reports"):
    """
    Generates an Allure HTML report with a timestamped directory name.

    Args:
        logger (logging.Logger): The logger instance to use for output.
        results_dir (str): The directory where Allure results are stored.
    """
    # Create the timestamped report directory
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = f"allure-report_{timestamp}"

    logger.info(f"Generating Allure report to: {report_dir}")

    try:
        # Check if the results directory exists
        if not os.path.isdir(results_dir):
            logger.warning(f"Results directory '{results_dir}' not found. Skipping report generation.")
            return

        # Use subprocess to run the allure generate command
        command = ["allure", "generate", results_dir, "-o", report_dir, "--clean"]

        # Capture stdout and stderr for better debugging
        process = subprocess.run(command, capture_output=True, text=True, check=True)
        logger.info("Report generation completed successfully.")

    except FileNotFoundError:
        logger.error(
            "'allure' command not found. Please ensure Allure Commandline is installed and added to your system's PATH.")
        logger.info(
            "For installation instructions, visit: https://docs.qameta.io/allure/latest/manual/install-cli.html")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to generate report. Return code: {e.returncode}")
        logger.debug(f"Stdout: {e.stdout}")
        logger.debug(f"Stderr: {e.stderr}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
