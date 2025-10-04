from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration_form():
    # правильная страница
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # используем уникальные селекторы для обязательных полей
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")

    # кнопка
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждём и проверяем текст
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

    browser.quit()
