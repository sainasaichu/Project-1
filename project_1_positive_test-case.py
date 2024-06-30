# Positive login Test Case


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

    # Enter the login credentials
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Allow time for login to process
    time.sleep(5)

    # Verify the login by checking for the presence of an element unique to the logged-in page
    dashboard_element = driver.find_element(By.XPATH, "//span[text()='Dashboard']")
    print("Login successful!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
