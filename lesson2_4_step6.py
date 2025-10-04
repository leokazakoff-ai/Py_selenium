from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(" http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, "button")
    button.click()
    print("OK")

except NoSuchElementException:
    print("Ошибка: NoSuchElementException")

finally:
    browser.quit()