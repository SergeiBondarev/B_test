# Registration_login: регистрация аккаунта (95)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()
driver.get("https://google.com")
time.sleep(1)

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
time.sleep(1)

# Нажмите на вкладку "My Account Menu"
My_Account_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
My_Account_btn.click()
time.sleep(1)

# В разделе "Register", введите email для регистрации
Register_email_field = driver.find_element_by_id("reg_email")
Register_email_field.send_keys("eco@mail.ru")
time.sleep(1)

# В разделе "Register", введите пароль для регистрации
Register_Pass_field = driver.find_element_by_id("reg_password")
Register_Pass_field.send_keys("!EcO!12_34#")
time.sleep(1)
# почту и пароль сохраните, потребуюутся в дальнейшем

# Нажмите на кнопку "Register"
Register_btn = driver.find_element_by_css_selector("[value='Register']")
Register_btn.click()
time.sleep(1)

driver.quit()