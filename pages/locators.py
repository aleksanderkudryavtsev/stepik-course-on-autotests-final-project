from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
#     LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
#     LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
#     PASSWORD_RESET = (By.CSS_SELECTOR, "#login_form > p > a")
#     LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
#     
#     REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
#     REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
#     REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
#     REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
    