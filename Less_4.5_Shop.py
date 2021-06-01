# Shop: количество товаров в категории (98)
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

# ЗАЛОГИНТЕСЬ
# Нажмите на вкладку "My Account Menu"
My_Account_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
My_Account_btn.click()
time.sleep(1)

# В разделе "Login", введите email для логина 		# данные можно взять из предыдущего теста
Login_email_field = driver.find_element_by_id("username")
Login_email_field.send_keys("eco@mail.ru")
time.sleep(1)

# В разделе "Login", введите пароль для логина 	    # данные можно взять из предыдущего теста
Login_Pass_field = driver.find_element_by_id("password")
Login_Pass_field.send_keys("!EcO!12_34#")
time.sleep(1)

# Нажмите на кнопку "Login"
Login_btn = driver.find_element_by_css_selector("[value='Login']")
Login_btn.click()
time.sleep(1)

# Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop_btn.click()
time.sleep(1)

# Откройте категорию "HTML"
HTML_cat  = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']")
HTML_cat.click()
time.sleep(1)

# Добавьте тест, что отображается три товара
# находим список всех товаров
items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")

# проверка что в списке действительно 3 товара
if len(items_count) == 3:
    print("В разделе 3 товара")
else:
    print("Ошибка. Количество товаров в разделе: " + str(len(items_count)))
time.sleep(1)

driver.quit()

