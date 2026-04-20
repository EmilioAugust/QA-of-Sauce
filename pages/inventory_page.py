from pages.base_page import BasePage
from utils.config import INVENTORY_URL, CART_URL
from locators.inventory_locator import InventoryLocator

class InventoryPage(BasePage):
    def open(self):
        super().open(INVENTORY_URL)

    def add_to_cart(self):
        self.open()
        self.click(InventoryLocator.ADD_TO_CART_BTN)

    def is_cart_badge_visible(self):
        return self.is_visible(InventoryLocator.CART_BADGE)
    
    def is_remove_btn_visible(self):
        return self.is_visible(InventoryLocator.REMOVE_BTN)
    
    def add_all_products_to_cart(self):
        self.open()
        for btn in InventoryLocator.ADD_TO_CART_BUTTONS:
            self.click(btn)

    def is_all_remove_btn_visible(self):
        for btn in InventoryLocator.REMOVE_BUTTONS:
            return self.is_visible(btn)

    def is_products_visible(self):
        return self.is_visible(InventoryLocator.PRODUCT)

    def is_opened(self):
        return self.is_visible(InventoryLocator.PRODUCTS)
    
    def click_on_cart(self):
        self.click(InventoryLocator.SHOPPING_CART)

    def is_cart_list_visible(self):
        return self.is_visible(InventoryLocator.SHOPPING_CART_LIST)