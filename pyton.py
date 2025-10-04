import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# список ссылок
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)  # базовое ожидание
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_stepik_feedback(browser, link):
    browser.get(link)

    # === авторизация (логин + пароль) ===
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_button.click()

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    email_input.send_keys("Leokazakoff@yandex.ru")

    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys("Pandapanda17082003")

    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    # === обработка всплывающих окон (решить снова, подтверждение) ===
    if browser.find_elements(By.CLASS_NAME, "again-btn.white"):
        browser.find_element(By.CLASS_NAME, "again-btn.white").click()

    if browser.find_elements(By.CLASS_NAME, "modal-popup__container"):
        browser.find_element(By.XPATH, "//button[text()='OK']").click()

    # === ждём, пока поле для ответа появится ===
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )

    # очищаем и вводим новый ответ
    textarea.clear()
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    # === нажимаем кнопку "Отправить" ===
    submit_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    submit_btn.click()

    # === ждём появления фидбека ===
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    # === проверка текста ===
    feedback_text = feedback.text
    assert feedback_text == "Correct!", f"Ожидалось 'Correct!', но получено '{feedback_text}'"
