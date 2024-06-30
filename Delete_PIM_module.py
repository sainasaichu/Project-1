#Test case for PIM Module to enter personal details of Employees


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
search_box.send_keys("Linda Anderson")  # Replace with the desired employee name
search_box.send_keys(Keys.RETURN)

# Wait for search results
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']/div")))

# Select the employee from the list
employee_checkbox = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[1]/div/label/span/input")
employee_checkbox.click()

# Click on the delete button
delete_button = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger']")
delete_button.click()

# Confirm the deletion
confirm_delete_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Yes, Delete']")))
confirm_delete_button.click()

# Wait for the deletion to complete
wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[1]/div/label/span/input")))

# Close the browser
driver.quit()
