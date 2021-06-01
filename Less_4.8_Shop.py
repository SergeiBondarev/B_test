# Shop: проверка цены в корзине (101)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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

# Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop_btn.click()

# Добавьте в корзину книгу "HTML5 WebApp Development"
HTML5_book = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
HTML5_book.click()
time.sleep(2)

# Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# Используйте для проверки assert
item = driver.find_element_by_xpath("//*[@id='wpmenucartli']/a/span[1]")
item_get_text = item.text
assert item_get_text == "1 Item"

Item_price = driver.find_element_by_id("header")
Item_price_get_text = Item_price.text
assert "₹180.00" in Item_price_get_text

# Перейдите в корзину
Basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
Basket.click()

# Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
Subtotal = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹180.00"))

# Используя явное ожидание, проверьте что в Total отобразилась стоимость
Total_amount = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[3]/td"), "₹189.00"))
time.sleep(1)

driver.quit()

