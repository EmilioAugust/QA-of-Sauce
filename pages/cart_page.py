from pages.base_page import BasePage
from utils.config import CART_URL
from locators.cart_locator import CartLocator

class CartPage(BasePage):
    def open(self):
        super().open(CART_URL)

    def remove_from_cart(self):
        self.open()
        self.click(CartLocator.REMOVE_BTN)

    def is_item_in_cart_visible(self):
        return self.is_visible(CartLocator.PRODUCT)
    
    def open_checkout(self):
        self.open()
        self.click(CartLocator.CHECKOUT_BTN)
    
    def is_checkout_info_visible(self):
        return self.is_visible(CartLocator.CHECKOUT_INFO)