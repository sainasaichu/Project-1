from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (this example uses Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Allow the page to load
    time.sleep(2)

    # Locate the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Enter incorrect login credentials
    username_field.send_keys("Admin")
    password_field.send_keys("Admin12345")

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Allow time for login to process
    time.sleep(3)

    # Check for error message
    try:
        # Adjust the XPath according to the actual structure of the error message on the page
        error_message = driver.find_element(By.XPATH, "//p[contains(text(), 'Invalid credentials')]")
        print("Login failed with incorrect credentials: ", error_message.text)
    except:
        print("Error message not found. There might be an issue with the login process or the XPath used to locate the error message.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
