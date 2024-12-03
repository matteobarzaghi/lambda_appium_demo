import time
from appium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Import By for locators

def test_google_search():
    # Replace these with your actual LambdaTest username and access key
    username = "username"
    access_key = "passkey"

    # Create ChromeOptions for capabilities
    options = Options()
    #options.set_capability("platform", "Android")  # Use 'platform' instead of 'platformName'
    options.set_capability("deviceName", "Google Pixel 4")  # Ensure the device name is correct
    options.set_capability("platformVersion", "10.0")  # Update the platform version as per device
    options.set_capability("browserName", "Chrome")
    options.set_capability("name", "Sample Appium Test")  # Test name on LambdaTest Dashboard
    options.set_capability("build", "Python Appium Pytest Build")  # Build name on LambdaTest Dashboard
    options.set_capability("isRealMobile", True)

    # Correct LambdaTest URL for mobile device automation
    remote_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

    # Create WebDriver instance
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("LambdaTest\n")
        time.sleep(3)  # Wait to view the search results
        assert "Google" in driver.title
    finally:
        driver.quit()