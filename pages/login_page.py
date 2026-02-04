from .base_page import BasePage
import allure
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    
    @allure.step("Выполнить вход с email: {email} и паролем: {password}")
    def login(self, email, password):
        self.input_text(LoginLocators.EMAIL_INPUT, email)
        self.input_text(LoginLocators.PASSWORD_INPUT, password)
        self.click_element(LoginLocators.LOGIN_BUTTON)