from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Скроллим страницу вниз до текстового поля
    answer_input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    
    # Вводим ответ в текстовое поле
    answer_input.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()
    
    # Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()