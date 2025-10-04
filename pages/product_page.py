from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            print("No second alert presented")
            return None
    
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
    
    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, f"Product name in message doesn't match. Expected: {product_name}, got: {message_product_name}"
    
    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "Basket total message is not presented"
    
    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Basket total doesn't match product price. Expected: {product_price}, got: {basket_total}"