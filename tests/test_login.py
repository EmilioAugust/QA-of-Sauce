def test_successful_login(login_page, inventory_page, valid_user):
    login_page.open()
    login_page.login(valid_user["username"], valid_user["password"])
    assert login_page.is_opened() == False
    assert inventory_page.is_opened() == True

def test_invalid_login(login_page, invalid_user):
    login_page.open()
    login_page.login(invalid_user["username"], invalid_user["password"])
    assert login_page.is_error_displayed() == True
    assert login_page.error_displayed_text("Username and password do not match any user in this service")

def test_locked_out_user_login(login_page, locked_out_user):
    login_page.open()
    login_page.login(locked_out_user["username"], locked_out_user["password"])
    assert login_page.error_displayed_text("Sorry, this user has been locked out.")