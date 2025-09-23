import subprocess
import os
import time


def generate_allure_report_with_timestamp(results_dir="reports"):
    """
    Generates an Allure HTML report with a timestamped directory name.

    Args:
        results_dir (str): The directory where Allure results are stored.
    """
    # Create the timestamped report directory
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = f"allure-report_{timestamp}"

    print(f"\n[Allure] Generating Allure report to: {report_dir}")

    try:
        # Check if the results directory exists
        if not os.path.isdir(results_dir):
            print(f"[Allure] Results directory '{results_dir}' not found. Skipping report generation.")
            return

        # Use subprocess to run the allure generate command
        command = ["allure", "generate", results_dir, "-o", report_dir, "--clean"]

        # Capture stdout and stderr for better debugging
        process = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"[Allure] Report generation completed successfully.")

    except FileNotFoundError:
        print(
            "[Allure Error] 'allure' command not found. Please ensure Allure Commandline is installed and added to your system's PATH.")
        print("For installation instructions, visit: https://docs.qameta.io/allure/latest/manual/install-cli.html")
    except subprocess.CalledProcessError as e:
        print(f"[Allure Error] Failed to generate report. Return code: {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
    except Exception as e:
        print(f"[Allure Error] An unexpected error occurred: {e}")
