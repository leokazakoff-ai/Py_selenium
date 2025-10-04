import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

@pytest.mark.parametrize('link', links)
def test_guest_should_see_feedback(browser, link):
    browser.get(link)

    # Ждём поле для ответа
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    textarea.clear()

    # Правильный ответ
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    # Отправляем
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    # Ждём появление фидбека
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    text = feedback.text
    assert text == "Correct!", f"Получен кусочек сообщения: {text}"
