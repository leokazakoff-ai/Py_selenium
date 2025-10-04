import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

links = [
    "https://stepik.org/lesson/236895/step/1",
    # остальные ссылки
]

@pytest.fixture(scope="function")
def browser():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_stepik_feedback(browser, link):
    browser.get(link)

    # Логин
    try:
        login_link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        login_link.click()
    except TimeoutException:
        print("Не удалось найти ссылку для входа")

    # Ввод логина и пароля
    try:
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_login_email"))
        )
        password_input = browser.find_element(By.ID, "id_login_password")
        email_input.send_keys("YOUR_LOGIN")
        password_input.send_keys("YOUR_PASSWORD")
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
    except TimeoutException:
        print("Не удалось найти поля для ввода логина/пароля")

    # Ожидание и ввод ответа
    try:
        textarea = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
        )
        textarea.clear()
        answer = math.log(int(time.time()))
        textarea.send_keys(str(answer))

        # Отправка ответа
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()

        # Ожидание фидбека
        feedback = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        )
        assert feedback.text == "Correct!", f"Текст в фидбеке: '{feedback.text}'"
    except TimeoutException:
        print("Не удалось найти текстовое поле или фидбек")
