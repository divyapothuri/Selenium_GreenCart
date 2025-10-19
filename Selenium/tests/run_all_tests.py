import subprocess
import time
import os

# Path to your test directory
test_dir = r"C:\Users\divya\PycharmProjects\Selenium\tests"
utils_dir = os.path.join(test_dir, "utils")  # if needed for PYTHONPATH

# List of test files
test_files = [
    "test_all_locators.py",
    "test_angularprac.py",
    "test_client.py",
    "test_flight.py",
    "test_greenkart.py",
    "test_locator_prac.py",
    "test_phoneshop.py"
]

# Directory to store Allure results
results_base_dir = os.path.join(test_dir, "allure-results")

# Ensure results directory exists
os.makedirs(results_base_dir, exist_ok=True)

# Run each test file
for test_file in test_files:
    test_path = os.path.join(test_dir, test_file)
    result_dir = os.path.join(results_base_dir, test_file.replace(".py", ""))

    # Ensure result subdirectory exists
    os.makedirs(result_dir, exist_ok=True)

    print(f"Running {test_file}...")

    # Run pytest with allure result path
    subprocess.run([
        "pytest",
        test_path,
        f"--alluredir={result_dir}"
    ])

    print(f"Completed {test_file}. Sleeping for 5 seconds...\n")
    time.sleep(5)

print("✅ All tests executed. You can now generate Allure reports using:")
print("    allure serve <path_to_individual_result_dir>")
