from pages.login_page import LoginPage

def test_intentionally_fail(page):
    login_page = LoginPage(page)
    login_page.open()
    # używamy poprawnego loginu, ale sprawdzamy zły URL
    login_page.login("standard_user", "secret_sauce")

    # oczekujemy złego URL, więc test NA PEWNO nie przejdzie
    assert page.url == "https://www.saucedemo.com/wrong_url"
