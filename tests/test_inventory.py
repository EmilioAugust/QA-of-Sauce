def test_is_products_visible(logged_in, inventory_page):
    inventory_page.open()
    assert inventory_page.is_opened() == True
    assert inventory_page.is_products_visible() == True

def test_add_to_cart(logged_in, inventory_page):
    inventory_page.add_to_cart()
    assert inventory_page.is_cart_badge_visible() == True
    assert inventory_page.is_remove_btn_visible() == True

def test_add_all_products_to_cart(logged_in, inventory_page):
    inventory_page.add_all_products_to_cart()
    assert inventory_page.is_all_remove_btn_visible() == True

def test_click_on_cart_list(logged_in, inventory_page):
    inventory_page.click_on_cart()
    assert inventory_page.is_cart_list_visible() == True