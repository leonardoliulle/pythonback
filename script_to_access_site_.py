from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller

now = datetime.now()
print("Starting Script: ", now)

# Replace these variables with the actual details
login_url = ''  # The login URL of the website
username = ''
password = ''


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get(login_url)
    
    # # Acessar o link 
    # time.sleep(7)
    # login_button = driver.find_element(By.ID, 'details-button')  # Adjust the XPath as needed
    # login_button.click()

    # Logar
    time.sleep (3)
    username_field = driver.find_element(By.ID, 'tbxCartaoSUS')  # Change 'username' to the actual name or ID
    username_field.send_keys(username)

    login_button = driver.find_element(By.ID, 'imgBtnCartao')  # Clicar na lupa
    login_button.click()

    time.sleep(2)
    tbxSenha_field = driver.find_element(By.ID, 'tbxSenha')  # Change 'username' to the actual name or ID
    tbxSenha_field.send_keys(password)

    time.sleep(2)

    loginbutton = driver.find_element(By.ID, 'imgBtnLogin')  # Clicar na lupa
    loginbutton.click()

    time.sleep(5)
    cboxClose = driver.find_element(By.ID, 'cboxClose')  # Clicar no fechar
    cboxClose.click()

    # Give some time for the login to process (adjust if necessary)
    time.sleep(120)

    

    # Check if login was successful by checking the presence of some element after login
    # success_element = driver.find_element(By.XPATH, 'xpath_of_some_element_after_login')
    # if success_element:
    #     print("Login successful")
    # else:
    #     print("Login failed")

finally:
    # Close the WebDriver
    driver.quit()

now = datetime.now()
print("Finished Script: ", now)


