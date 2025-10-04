from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

driver = webdriver.Chrome()

try:
    # Первая часть - находим и кликаем по ссылке
    driver.get('http://suninjuly.github.io/find_link_text')
    link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    
    # Вторая часть - заполняем форму на новой странице
    # Используем тот же драйвер, который уже перешел на новую страницу
    
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()