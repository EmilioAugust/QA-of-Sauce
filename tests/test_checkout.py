def test_fill_info(logged_in_with_item_to_checkout, checkout_page, user_info):
    checkout_page.fill_info(user_info["first_name"], user_info["last_name"], user_info["postal_code"])
    assert checkout_page.is_fill_info_visible() == False

def test_fill_info_without_data(logged_in_with_item_to_checkout, checkout_page):
    checkout_page.fill_info_without_data()
    assert checkout_page.is_error_displayed() == True

def test_fill_only_first_name(logged_in_with_item_to_checkout, checkout_page, user_info):
    checkout_page.fill_only_first_name(user_info["first_name"])
    assert checkout_page.is_error_displayed() == True
    assert checkout_page.error_displayed_text("Last Name is required")

def test_fill_first_and_last_name(logged_in_with_item_to_checkout, checkout_page, user_info):
    checkout_page.fill_first_and_last_name(user_info["first_name"], user_info["last_name"])
    assert checkout_page.is_error_displayed() == True
    assert checkout_page.error_displayed_text("Postal Code is required")

def test_complete_order(logged_in_with_item_to_checkout_and_finish, checkout_page):
    checkout_page.click_finish()
    assert checkout_page.is_checkout_complete_visible() == True
    assert checkout_page.is_back_home_btn_visible() == True