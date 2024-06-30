from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (ensure the path to your WebDriver is correct)
driver = webdriver.Firefox()

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the browser window
driver.maximize_window()

# Wait for the login elements to be present
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

# Enter login credentials
username.send_keys("Admin")
password.send_keys("admin123")

# Submit the login form
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the dashboard to load
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))

# Navigate to PIM module
pim_module = driver.find_element(By.XPATH, "//span[text()='PIM']")
pim_module.click()

# Wait for the employee list to load
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Employee Name']")))

# Search for an employee by name
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Employee Name']")
search_box.send_keys("Amelia")  # Replace with the desired employee name
search_box.send_keys(Keys.RETURN)

# Wait for search results
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']/div")))

# Select the employee from the list
employee = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[1]/div[3]/div")
employee.click()

# Wait for the employee details page to load
wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Edit']")))

# Edit employee details
edit_button = driver.find_element(By.XPATH, "//button[text()='Edit']")
edit_button.click()

# Example: Change employee's middle name
middle_name = driver.find_element(By.NAME, "middleName")
middle_name.clear()
middle_name.send_keys("saina")

# Save the changes
save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
save_button.click()

# Optionally, add assertions to verify the changes
# Example: Verify that the middle name was updated
wait.until(EC.text_to_be_present_in_element((By.NAME, "middleName"), "NewMiddleName"))

# Close the browser
driver.quit()
