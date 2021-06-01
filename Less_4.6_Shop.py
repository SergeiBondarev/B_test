# Shop: количество товаров в категории (99)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()
driver.get("https://google.com")
# time.sleep(1)

# Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# time.sleep(1)

# ЗАЛОГИНТЕСЬ
# Нажмите на вкладку "My Account Menu"
My_Account_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
My_Account_btn.click()
# time.sleep(1)

# В разделе "Login", введите email для логина 		# данные можно взять из предыдущего теста
Login_email_field = driver.find_element_by_id("username")
Login_email_field.send_keys("eco@mail.ru")
# time.sleep(1)

# В разделе "Login", введите пароль для логина 	    # данные можно взять из предыдущего теста
Login_Pass_field = driver.find_element_by_id("password")
Login_Pass_field.send_keys("!EcO!12_34#")
# time.sleep(1)

# Нажмите на кнопку "Login"
Login_btn = driver.find_element_by_css_selector("[value='Login']")
Login_btn.click()
# time.sleep(1)

# Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop_btn.click()
# time.sleep(1)

# Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# Используйте проверку по value
Selector = driver.find_element_by_tag_name("select").click()
Default = driver.find_element_by_css_selector("[value='menu_order']")
Default_selected = Default.get_attribute("selected")
print("value of Selector: ", Default_selected)
if Default_selected is not None:
    print("Default sorting")
else:
    print("Not Default sorting!")

# Отсортируйте товары от большего к меньшему
driver.find_element_by_css_selector("[value='price-desc']").click()

# Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
# Используйте проверку по value
Selector = driver.find_element_by_tag_name("select").click()
Hi_low = driver.find_element_by_css_selector("[value='price-desc']")
Hi_low_selected = Hi_low.get_attribute("selected")
print("value of Selector: ", Hi_low_selected)
if Hi_low_selected is not None:
    print("High to Low sorting")
else:
    print("Not High to Low sorting!")

driver.quit()





