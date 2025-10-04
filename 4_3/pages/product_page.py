from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == message_name, \
            f"Expected product name '{product_name}' but got '{message_name}' in the success message"

    def should_be_correct_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text
        assert product_price == message_price, \
            f"Expected product price '{product_price}' but got '{message_price}' in the basket message"
