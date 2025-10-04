from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


class TestRegistration:
    
    def test_registration1(self):
        """Тест для первой страницы регистрации"""
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        
        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("test@mail.ru")
        
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        assert welcome_text == "Поздравляем! Вы успешно зарегистировались!", \
            f"Текст приветствия не совпадает. Ожидалось: 'Поздравляем! Вы успешно зарегистировались!', Получено: '{welcome_text}'"
        
        browser.quit()

    def test_registration2(self):
        """Тест для второй страницы регистрации (должен падать с NoSuchElementException)"""
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        
        # Заполняем обязательные поля (здесь будет исключение для второго поля)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")  # Это вызовет исключение
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("test@mail.ru")
        
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        assert welcome_text == "Поздравляем! Вы успешно зарегистировались!", \
            f"Текст приветствия не совпадает. Ожидалось: 'Поздравляем! Вы успешно зарегистировались!', Получено: '{welcome_text}'"
        
        browser.quit()