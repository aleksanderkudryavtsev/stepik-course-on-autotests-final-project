from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        
    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Add to basket message is not presented"
        
    def should_be_basket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), "Basket cost message is not presented"
        
    def should_be_correct_cost_in_basket_cost_message(self):
        self.should_be_basket_cost_message()
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        cost_in_basket_cost_message = self.browser.find_element(*ProductPageLocators.COST_IN_BASKET_COST_MESSAGE).text
        assert cost_in_basket_cost_message == product_cost, "Cost in the basket cost message is incorrect"        
                
    def should_be_correct_product_in_add_to_basket_message(self):
        self.should_be_add_to_basket_message()
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_in_add_to_basket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ADD_TO_BASKET_MESSAGE).text
        assert product_in_add_to_basket_message == product_title, "Product title in the add to basket message is incorrect"

    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message hasn't disappeared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is presented, but should not be"