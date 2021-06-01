# Shop: работа в корзине (102)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()
driver.get("https://google.com")

# Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

# Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop_btn.click()

# Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# Перед добавлением первой книги, проскролльте вниз на 400 пикселей
# После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 400);")
HTML5_book = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
HTML5_book.click()
time.sleep(1)

JS_Data = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']")
JS_Data.click()
time.sleep(1)

# Перейдите в корзину
Basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
Basket.click()

# Удалите первую книгу
# Перед удалением добавьте sleep
time.sleep(1)
X = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[1]/a")
X.click()


# Нажмите на Undo (отмена удаления)
Undo = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/div[1]/a")
Undo.click()
time.sleep(1)

# В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# Предварительно очистите поле с помощью локатор_поля.clear()
Field = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td[5]/div/input').clear()
time.sleep(1)
Qty_3 = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td[5]/div/input')
Qty_3.send_keys("3")
time.sleep(1)

# Нажмите на кнопку "UPDATE BASKET"
Update = driver.find_element_by_css_selector('[value="Update Basket"]')
Update.click()
time.sleep(1)

# Добавьте тест, что value элемента quantity для "HTML5 WebApp Development" равно 3
# используйте assert
HTML5 = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td[5]/div/input')
HTML5_value = HTML5.get_attribute("value")
assert HTML5_value == '3'

# Нажмите на кнопку "APPLY COUPON"
# Перед нажатимем добавьте sleep
time.sleep(1)
Apply_Coupon = driver.find_element_by_css_selector('[value="Apply Coupon"]')
Apply_Coupon.click()
time.sleep(1)

# Добавьте тест, что возникло сообщение: "Please enter a coupon code."
Message = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/ul/li")
Message_get_text = Message.text
assert "Please enter a coupon code." in Message_get_text

driver.quit()




