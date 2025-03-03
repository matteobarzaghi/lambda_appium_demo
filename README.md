# Appium Demo Project

This is a demo project showcasing how to perform mobile web automation using Appium with Python. The test script runs a simple test on a real mobile device in the cloud using LambdaTest.

## Test Scenario
The test script performs the following steps:
1. Opens a Chrome browser on a real mobile device (Google Pixel 4, Android 10.0) via LambdaTest.
2. Navigates to [Google](https://www.google.com).
3. Searches for 'LambdaTest'.
4. Verifies that 'Google' is present in the page title.
5. Closes the browser.

## Prerequisites
- Python 3.7+
- Appium-Python-Client
- Selenium
- LambdaTest Account

## Installation
Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:
```
appium-python-client
selenium
```

## How to Run the Test
1. Replace the `username` and `access_key` variables in the test script with your LambdaTest credentials.
2. Run the test using the following command:

```bash
python test_google_search.py
```

## LambdaTest Dashboard
You can view your test execution in real-time on the [LambdaTest Automation Dashboard](https://automation.lambdatest.com).

## License
This project is licensed under the MIT License - see the LICENSE file for details.

