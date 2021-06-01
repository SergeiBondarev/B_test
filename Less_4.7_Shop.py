# Shop: отображение, скидка товара (100)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(chrome_options=options)

# driver.maximize_window()
driver.get("https://google.com")

# Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

# ЗАЛОГИНТЕСЬ
My_Account_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
My_Account_btn.click()

# В разделе "Login", введите email для логина 		# данные можно взять из предыдущего теста
Login_email_field = driver.find_element_by_id("username")
Login_email_field.send_keys("eco@mail.ru")

# В разделе "Login", введите пароль для логина 	    # данные можно взять из предыдущего теста
Login_Pass_field = driver.find_element_by_id("password")
Login_Pass_field.send_keys("!EcO!12_34#")

# Нажмите на кнопку "Login"
Login_btn = driver.find_element_by_css_selector("[value='Login']")
Login_btn.click()

# Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop_btn.click()

# Откройте книгу "Android Quick Start Guide"
Android_book = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
Android_book.click()

# Добавьте тест, что содержимое старой цены = "₹600.00"	    # используйте assert
Price_old = driver.find_element_by_css_selector("span.woocommerce-Price-amount.amount")
Price_old_get_text = Price_old.text
assert "600.00" in Price_old_get_text

# Добавьте тест, что содержимое новой цены = "₹450.00"	  	# используйте assert
Price_new = driver.find_element_by_css_selector("p.price")
Price_new_get_text = Price_new.text
assert "450.00" in Price_new_get_text

# Добавьте явное ожидание и нажмите на обложку книги
# Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
Android_book_pic = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")))
Android_book_pic.click()

# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
Android_book_pic_X = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
Android_book_pic_X.click()

driver.quit()






