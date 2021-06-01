# Home: добавление комментария (94)
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

# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

# Нажмите на название книги "Selenium Ruby"
Selenium_Ruby = driver.find_element_by_xpath("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]/h3")
Selenium_Ruby.click()
time.sleep(1)

# Нажмите на вкладку "REVIEWS"
Reviews_btn = driver.find_element_by_css_selector("[href='#tab-reviews']")
Reviews_btn.click()
time.sleep(1)

# Поставьте 5 звёзд
star5_btn = driver.find_element_by_class_name("star-5")
star5_btn.click()
time.sleep(1)

# Заполните поле "Review" сообщением: "Nice book!"
Comment_field = driver.find_element_by_id("comment")
Comment_field.send_keys("Nice book!")
time.sleep(1)

# Заполните поле "Name"
Name_field = driver.find_element_by_id("author")
Name_field.send_keys("Ecoist")
time.sleep(1)

# Заполните "Email"
Email_field = driver.find_element_by_id("email")
Email_field.send_keys("eco@mail.ru")
time.sleep(1)

# Нажмите на кнопку "SUBMIT"
Submit_btn = driver.find_element_by_id("submit")
Submit_btn.click()
time.sleep(1)

driver.quit()