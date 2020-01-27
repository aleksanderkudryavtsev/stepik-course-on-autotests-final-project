from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_IN_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_COST = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    COST_IN_BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")
    
    
#     LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
#     LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
#     PASSWORD_RESET = (By.CSS_SELECTOR, "#login_form > p > a")
#     LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
#     
#     REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
#     REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
#     REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
#     REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
    