from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Находим элементы и получаем их текстовые значения
    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")
    
    # Преобразуем текст в числа и складываем
    a = int(a_element.text)
    b = int(b_element.text)
    c = a + b
    
    # Выбираем значение из выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c))  # Преобразуем число в строку
    
    # Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()