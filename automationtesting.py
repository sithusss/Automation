from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize the browser
driver = webdriver.Chrome()  # Replace with your browser driver path
driver.get("https://demoqa.com/login")  # Login URL

# Create a directory to save screenshots if it doesn't exist
os.makedirs("test_results", exist_ok=True)

# Function to perform login and validate
def login_test(username, password):
    try:
        print(f"Testing with Username: {username}, Password: {password}")

        # Locate and fill the username field
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userName")))
        username_field.clear()
        for char in username:
            username_field.send_keys(char)
            time.sleep(0.1)  # Pause between keystrokes

        # Locate and fill the password field
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        for char in password:
            password_field.send_keys(char)
            time.sleep(0.1)  # Pause between keystrokes

       

        # Locate the login button and click
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='login']")))
        time.sleep(1)  # Pause before clicking the button
        login_button.click()

        time.sleep(3)  # Wait for the page to load

        # Validate the login status
        try:
            # Check if redirected to the profile page
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@id='submit']")))
            print("Login Successful")
            driver.save_screenshot("test_results/login_successful.png")
        except:
            # Check for the error message
            error_message = driver.find_element(By.ID, "name").text
            if "Invalid username or password!" in error_message:
                print("Login Failed: Invalid credentials")
            else:
                print("Login Failed: Unknown error")
            driver.save_screenshot("test_results/login_failed.png")
    finally:
        # Reset to the login page for the next test
        driver.get("https://demoqa.com/login")
        time.sleep(2)  # Allow the page to reset

# Test cases
login_test("testuser", "Test@123")  # Replace with actual valid credentials
login_test("invalidUser", "invalidPassword")  # Invalid credentials


# Close the browser
driver.quit()
