import pytest
import json
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Pages
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

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
    
# Logged in user
@pytest.fixture
def logged_in(login_page, valid_user):
    login_page.open()
    login_page.login(valid_user["username"], valid_user["password"])