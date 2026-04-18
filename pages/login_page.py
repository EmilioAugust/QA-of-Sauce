from pages.base_page import BasePage
from locators.login_locator import LoginLocator

class LoginPage(BasePage):
    def open(self):
        super().open()
    
    def login(self, username, password):
        self.fill(LoginLocator.USERNAME, username)
        self.fill(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BTN)
    
    def is_error_displayed(self):
        return self.is_visible(LoginLocator.ERROR)
    
    def error_displayed_text(self, text):
        return self.is_has_text(LoginLocator.ERROR, text)
    
    def is_opened(self):
        return self.is_visible(LoginLocator.LOGIN_BTN)