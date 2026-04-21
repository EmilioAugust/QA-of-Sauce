from pages.base_page import BasePage
from locators.login_locator import LoginLocator
from locators.locator import Locator

class LoginPage(BasePage):
    def open(self):
        super().open()
    
    def login(self, username, password):
        self.open()
        self.fill(LoginLocator.USERNAME, username)
        self.fill(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BTN)

    def login_without_username(self, password):
        self.open()
        self.fill(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BTN)

    def login_without_password(self, username):
        self.open()
        self.fill(LoginLocator.USERNAME, username)
        self.click(LoginLocator.LOGIN_BTN)

    def login_click(self):
        super().click(LoginLocator.LOGIN_BTN)
    
    def is_error_displayed(self):
        return self.is_visible(Locator.ERROR)
    
    def error_displayed_text(self, text):
        return self.is_has_text(Locator.ERROR, text)
    
    def is_opened(self):
        return self.is_visible(LoginLocator.LOGIN_BTN)