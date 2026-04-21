from pages.base_page import BasePage
from utils.config import CHECKOUT_STEP_ONE_URL
from locators.checkout_locator import CheckoutLocator
from locators.login_locator import LoginLocator
from locators.locator import Locator

class CheckoutPage(BasePage):
    def open(self):
        return super().open(CHECKOUT_STEP_ONE_URL)
    
    def fill_info(self, first_name, last_name, postal_code):
        self.open()
        self.fill(CheckoutLocator.FIRST_NAME, first_name)
        self.fill(CheckoutLocator.LAST_NAME, last_name)
        self.fill(CheckoutLocator.POSTAL_CODE, postal_code)
        self.click(CheckoutLocator.CONTINUE_BTN)

    def fill_only_first_name(self, first_name):
        self.open()
        self.fill(CheckoutLocator.FIRST_NAME, first_name)
        self.click(CheckoutLocator.CONTINUE_BTN)

    def fill_first_and_last_name(self, first_name, last_name):
        self.open()
        self.fill(CheckoutLocator.FIRST_NAME, first_name)
        self.fill(CheckoutLocator.LAST_NAME, last_name)
        self.click(CheckoutLocator.CONTINUE_BTN)

    def fill_info_without_data(self):
        self.open()
        self.click(CheckoutLocator.CONTINUE_BTN)

    def click_finish(self):
        self.click(CheckoutLocator.FINISH_BTN)

    def is_total_price_visible(self):
        return self.is_visible(CheckoutLocator.TOTAL_PRICE)
    
    def is_checkout_complete_visible(self):
        return self.is_visible(CheckoutLocator.CHECKOUT_COMPLETE)
    
    def is_back_home_btn_visible(self):
        return self.is_visible(CheckoutLocator.BACK_HOME_BTN)

    def is_error_displayed(self):
        return self.is_visible(Locator.ERROR)
    
    def error_displayed_text(self, text):
        return self.is_has_text(Locator.ERROR, text)
    
    def is_fill_info_visible(self):
        return self.is_visible(CheckoutLocator.FILL_INFO_CONTAINER)