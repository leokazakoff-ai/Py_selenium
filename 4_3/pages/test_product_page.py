import pytest
from selenium import webdriver
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket():
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser = webdriver.Chrome()
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_message()
    page.should_be_correct_price_in_message()
    browser.quit()
