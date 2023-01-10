from selenium import webdriver
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os

# Rest of your code here
from termcolor import colored

with open('proxy/message.txt', 'r', encoding='utf-8') as f:
    message = f.read()
green = '\033[92m'
reset = '\033[0m'
print(green + message + reset)


with open('proxy/Powered.txt', 'r') as f:
    Powered  = f.read()

# Set the text color to red
red = '\033[91m'
reset = '\033[0m'  # Reset the text color

# Print the message in red
print(red + Powered + reset)
input_value = input("Press 1 to run the script: ")
if input_value == "1":
  # code to run the script goes here
  print("Running the script...")
else:
  print("Invalid input. Exiting.")




# Set the path to the chromedriver
chromedriver_path = "chrome/chromedriver"

# Prompt the user to enter the proxy address
proxy_address = input("Enter the proxy address: ")
# Prompt the user to enter their name and email
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your desired password: ")

# Set the options to configure the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy_address)

# Initialize the Chrome browser
driver = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)

# Test the connection to the proxy
try:
    response = urllib.request.urlopen("https://twitter.com/i/flow/signup")
    print("Connected to the proxy")
except urllib.error.URLError as e:
    print("Failed to connect to the proxy")
    driver.quit()
    exit()

# Open the website
driver.get("https://twitter.com/i/flow/signup")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the element to be present or visible
wait = WebDriverWait(driver, 10)
signup_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Sign up with phone or email')]")))

# Click on the element
signup_element.click()



# Wait for the element to be present or visible
wait = WebDriverWait(driver, 10)
signup_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Use email instead')]")))

# Click on the element
signup_element.click()

# Enter the name and email in the fields
from selenium.webdriver.common.by import By

name_field = driver.find_element(By.NAME, "name")

name_field.send_keys(name)



name_field = driver.find_element(By.NAME, "email")

name_field.send_keys(email)




import time

# Wait for 10 seconds
time.sleep(10)

from selenium.webdriver.common.by import By

next_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")

# Click on the "Next" button
next_button.click()





next_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")

# Click on the "Next" button
next_button.click()


# Wait for the user to bypass the CAPTCHA
captcha_bypassed = input("Press enter once the CAPTCHA has been bypassed: ")


import time

# Wait for 10 seconds
time.sleep(5)
# Locate the "Next" button element

next_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")

# Click on the "Next" button
next_button.click()


import time

# Wait for 10 seconds
time.sleep(5)
# Enter the password in the field
password_field = driver.find_element_by_name("password")
password_field.send_keys(password)

import time

# Wait for 10 seconds
time.sleep(3)


next_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")

# Click on the "Next" button
next_button.click()


# Open the text file in append mode
with open('credentials.txt', 'a') as f:
  # Write the email and password to the file, separated by a colon
  f.write(email + ':' + password + '\n')


import time

# Wait for 10 seconds
time.sleep(3)
# Find the "Skip for now" button element
skip_button = driver.find_element_by_xpath("//*[contains(text(), 'Skip for now')]")

# Click on the "Skip for now" button
skip_button.click()


import time

# Wait for 10 seconds
time.sleep(3)
# Find the "Skip for now" button element
skip_button = driver.find_element_by_xpath("//*[contains(text(), 'Skip for now')]")

# Click on the "Skip for now" button
skip_button.click()
import time

# Wait for 10 seconds
time.sleep(3)
# Find the "Skip for now" button element
skip_button = driver.find_element_by_xpath("//*[contains(text(), 'Skip for now')]")

# Click on the "Skip for now" button
skip_button.click()




next_button = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")

# Click on the "Next" button
next_button.click()



next_button = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")

# Click on the "Next" button
next_button.click()

# To avoid closing the browser, set an automatic execution for the next actions
input("Press Enter to close the browser")
driver.quit()
