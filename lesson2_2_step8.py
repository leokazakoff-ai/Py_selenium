from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

fake = Faker()

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys(fake.first_name())
    
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys(fake.last_name())
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys(fake.email())
    
    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)
    
    # Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()