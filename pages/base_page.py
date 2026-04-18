from utils.config import BASE_URL

class BasePage:
    def __init__(self, page):
        self.page = page
    
    def open(self, url=""):
        self.page.goto(BASE_URL + url)

    def click(self, locator):
        self.page.locator(locator).click()
    
    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def is_visible(self, locator):
        return self.page.locator(locator).first.is_visible()
    
    def is_has_text(self, locator, text):
        return self.page.locator(locator, has_text=text).first.inner_text()