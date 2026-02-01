from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    assert "Epic sadface: Username and password do not match" in login_page.get_error_message()


def test_wrong_username(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("wrong_user", "secret_sauce")
    assert "Epic sadface: Username and password do not match" in login_page.get_error_message()
