def test_delete_item_from_cart(logged_in_with_item, cart_page):
    cart_page.remove_from_cart()
    assert cart_page.is_item_in_cart_visible() == False

def test_checkout_page(logged_in_with_item, cart_page):
    cart_page.open_checkout()
    assert cart_page.is_checkout_info_visible() == True