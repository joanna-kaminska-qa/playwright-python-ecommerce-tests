import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,expected_url_or_error",
    [
        ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),  # poprawny
        ("standard_user", "wrong_password", "Epic sadface: Username and password do not match"),  # złe hasło
        ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match")  # złe username
    ]
)
def test_login_combinations(page, username, password, expected_url_or_error):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    if expected_url_or_error.startswith("https://"):
        assert page.url == expected_url_or_error
    else:
        assert expected_url_or_error in login_page.get_error_message()
