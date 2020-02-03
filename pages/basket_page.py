from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "There's no message that basket is empty"    
    
    def should_not_be_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_FORM), "There are goods in the basket, but should not be"