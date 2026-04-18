from pages.base_page import BasePage
from locators.inventory_locator import InventoryLocator

class InventoryPage(BasePage):
    def open():
        super().open("inventory.html")

    def is_opened(self):
        return self.is_visible(InventoryLocator.PRODUCTS)