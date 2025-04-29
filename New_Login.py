from selenium import webdriver
from selenium.webdriver.common.by import By


# The actual login page URL and credentials for saucedemo.com
LOGIN_URL = "https://www.saucedemo.com/"
CORRECT_USERNAME = "standard_user"
CORRECT_PASSWORD = "secret_sauce"
INCORRECT_USERNAME = "invalid_user"
INCORRECT_PASSWORD = "wrong_password"
# The expected part of the URL after successful login for saucedemo.com
DASHBOARD_URL_PART = "/inventory.html"

# --- Test Case 1: Successful login with correct credentials ---
print("\n--- Running Test Case: Successful Login ---")

# 1. Set up the browser
driver = webdriver.Firefox()
driver.maximize_window()

# 2. Navigate to the login page
driver.get(LOGIN_URL)
print(f"Navigated to: {LOGIN_URL}")

# 3. Find and interact with the username field (Using By.ID)
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(CORRECT_USERNAME)
print(f"Entered username: {CORRECT_USERNAME}")

# 4. Find and interact with the password field (Using By.ID)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(CORRECT_PASSWORD)
print(f"Entered password (masked): *************") # Adjusting mask length

# 5. Find and click the login button (Using By.ID)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Clicked the login button.")

# 6. Verification (Check if the page title indicates successful login)
assert "Swag Labs" in driver.title
print(f"Verification successful: Page title is '{driver.title}'")

# 7. Close the browser
driver.quit()
print("Browser closed.")
print("--- Successful Login Test Finished ---\n")


# --- Test Case 2: Failed login with incorrect credentials ---
print("\n--- Running Test Case: Failed Login ---")

# 1. Set up the browser
driver = webdriver.Firefox()
driver.maximize_window()

# 2. Navigate to the login page
driver.get(LOGIN_URL)
print(f"Navigated to: {LOGIN_URL}")

# 3. Find and interact with the username field (Using By.ID)
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(INCORRECT_USERNAME)
print(f"Entered username: {INCORRECT_USERNAME}")

# 4. Find and interact with the password field (Using By.ID)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(INCORRECT_PASSWORD)
print(f"Entered password (masked): *************")

# 5. Find and click the login button (Using By.ID)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Clicked the login button.")

# 6. Verification (Check for the specific error message for incorrect credentials)
error_message_element = driver.find_element(By.XPATH, "//*[@data-test='error']")
# Assert that the expected error text is in the element's text
assert "Epic sadface: Username and password do not match" in error_message_element.text
print(f"Verification successful: Error message displayed - '{error_message_element.text}'")

# 7. Close the browser
driver.quit()
print("Browser closed.")
print("--- Failed Login Test Finished ---\n")

# --- Test Case 3: Login attempt with empty fields ---
print("\n--- Running Test Case: Login Attempt with Empty Fields ---")

# 1. Set up the browser
driver = webdriver.Firefox()
driver.maximize_window()

# 2. Navigate to the login page
driver.get(LOGIN_URL)
print(f"Navigated to: {LOGIN_URL}")


# 4. Find and click the login button (Using By.ID)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Clicked the login button with empty fields.")

# 5. Verification (Check for the error message for empty fields)
error_message_element = driver.find_element(By.XPATH, "//*[@data-test='error']")
# Assert that the expected error text for missing username is in the element's text
assert "Epic sadface: Username is required" in error_message_element.text
print(f"Verification successful: Error message for empty fields displayed - '{error_message_element.text}'")

# 6. Close the browser
driver.quit()
print("Browser closed.")
print("--- Login Attempt with Empty Fields Test Finished ---\n")

# --- Test Case 4: Verification of error messages for invalid inputs ---
print("\n--- Running Test Case: Verification of Error Messages for Invalid Inputs ---")

# 1. Set up the browser
driver = webdriver.Firefox()
driver.maximize_window()

# 2. Navigate to the login page
driver.get(LOGIN_URL)
print(f"Navigated to: {LOGIN_URL}")

# 3. Enter invalid credentials (incorrect username/password)
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(INCORRECT_USERNAME)
print(f"Entered invalid username: {INCORRECT_USERNAME}")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(INCORRECT_PASSWORD)
print(f"Entered invalid password (masked): ********")

# 4. Click the login button (Using By.ID)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Clicked the login button with invalid inputs.")

# 5. Verification (Verify the error message for invalid inputs)
error_message_element = driver.find_element(By.XPATH, "//*[@data-test='error']")
# Assert that the expected error text for invalid credentials is in the element's text
assert "Epic sadface: Username and password do not match" in error_message_element.text
print(f"Verification successful: Error message for invalid inputs displayed - '{error_message_element.text}'")

# 6. Close the browser
driver.quit()
print("Browser closed.")
print("--- Verification of Error Messages for Invalid Inputs Test Finished ---\n")

# --- Test Case 5: Confirmation that a successful login redirects to a dashboard page ---
print("\n--- Running Test Case: Successful Login Redirect Confirmation ---")

# 1. Set up the browser
driver = webdriver.Firefox()
driver.maximize_window()

# 2. Navigate to the login page
driver.get(LOGIN_URL)
print(f"Navigated to: {LOGIN_URL}")

# 3. Find and interact with the username field (Using By.ID)
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(CORRECT_USERNAME)
print(f"Entered username: {CORRECT_USERNAME}")

# 4. Find and interact with the password field (Using By.ID)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(CORRECT_PASSWORD)
print(f"Entered password (masked): ********")

# 5. Find and click the login button (Using By.ID)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Clicked the login button.")

# 6. Verification (Check the current URL after successful login)
assert DASHBOARD_URL_PART in driver.current_url
print(f"Verification successful: Redirected to dashboard URL ")

# 7. Close the browser
driver.quit()
print("Browser closed.")
print("--- Successful Login Redirect Confirmation Test Finished ---\n")