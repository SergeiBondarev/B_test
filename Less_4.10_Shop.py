# Shop: покупка товара (103)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Добавьте в корзину книги "HTML5 WebApp Development"
# Перед добавлением книги, проскролльте вниз на 400 пикселей
driver.execute_script("window.scrollBy(0, 400);")
HTML5_book = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
HTML5_book.click()
time.sleep(1)

# Перейдите в корзину
Basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
Basket.click()

# Нажмите "PROCEED TO CHECKOUT"
# Перед нажатием, добавьте явное ожидание
Proceed_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/checkout/']")))
Proceed_btn.click()

# ЗАПОЛНИТЕ ВСЕ ОБЯЗАТЕЛЬНЫЕ ПОЛЯ
# Перед заполнением first name, добавьте явное ожидание
# Заполните поле "First Name"
Name_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "billing_first_name")))
Name_field.send_keys("Serge")

# Заполните поле "Last Name"
Last_field = driver.find_element_by_id("billing_last_name")
Last_field.send_keys("Bond")
time.sleep(1)

# Заполните "Email"
Email_field = driver.find_element_by_id("billing_email")
Email_field.send_keys("eco@mail.ru")
time.sleep(1)

# Заполните "Phone"
Email_field = driver.find_element_by_id("billing_phone")
Email_field.send_keys("555-55-55")
time.sleep(1)

# # Нажмите на кнопку "SUBMIT"
# Submit_btn = driver.find_element_by_id("submit")
# Submit_btn.click()
# time.sleep(1)

# Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
Country_sel = driver.find_element_by_id('select2-chosen-1').click()
Ru_sel = driver.find_element_by_id("s2id_autogen1_search")
Ru_sel.send_keys("Russia")
Russia = driver.find_element_by_css_selector("span.select2-match").click()

# Заполните поле "Address"
Last_field = driver.find_element_by_id("billing_address_1")
Last_field.send_keys("Nevski 18")
time.sleep(1)

# Заполните "City"
Email_field = driver.find_element_by_id("billing_city")
Email_field.send_keys("Moscow")
time.sleep(1)

# Заполните "State"
Email_field = driver.find_element_by_id("billing_state")
Email_field.send_keys("Oblast")
time.sleep(1)

# Заполните "Zip"
Email_field = driver.find_element_by_id("billing_postcode")
Email_field.send_keys("193932")
time.sleep(1)

# Выберите способ оплаты "Check Payments"
# Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
Check_pay = driver.find_element_by_id('payment_method_cheque').click()

# Нажмите PLACE ORDER
Order_btn = driver.find_element_by_id("place_order")
Order_btn.click()
time.sleep(1)

# Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
Thank_text = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
Pay_meth = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-35']/div/div[1]/table/tfoot/tr[3]/td"), "Check Payments"))
time.sleep(1)

driver.quit()
