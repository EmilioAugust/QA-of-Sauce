import pytest
import json
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Pages
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)

# JSON file with users
@pytest.fixture
def valid_user():
    with open("data/users.json") as f:
        return json.load(f)["valid_user"]
    
@pytest.fixture
def invalid_user():
    with open("data/users.json") as f:
        return json.load(f)["invalid_user"]
    
@pytest.fixture
def locked_out_user():
    with open("data/users.json") as f:
        return json.load(f)["locked_user"]
    
@pytest.fixture
def user_info():
    with open("data/users.json") as f:
        return json.load(f)["user_info"]
    
# Logged in user
@pytest.fixture
def logged_in(login_page, valid_user):
    login_page.open()
    login_page.login(valid_user["username"], valid_user["password"])

# Logged in user with item in cart
@pytest.fixture
def logged_in_with_item(login_page, inventory_page, valid_user):
    login_page.open()
    login_page.login(valid_user["username"], valid_user["password"])
    inventory_page.add_to_cart()

# Logged in user with item in cart to checkout
@pytest.fixture
def logged_in_with_item_to_checkout(login_page, inventory_page, cart_page, valid_user):
    login_page.open()
    login_page.login(valid_user["username"], valid_user["password"])
    inventory_page.add_to_cart()
    cart_page.open_checkout()

# Logged in user with item in cart to checkout and finish
@pytest.fixture
def logged_in_with_item_to_checkout_and_finish(login_page, inventory_page, cart_page, checkout_page, valid_user, user_info):
    login_page.open()
    login_page.login(valid_user["username"], valid_user["password"])
    inventory_page.add_to_cart()
    cart_page.open_checkout()
    checkout_page.fill_info(user_info["first_name"], user_info["last_name"], user_info["postal_code"])