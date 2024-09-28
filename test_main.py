from playwright.sync_api import Playwright, sync_playwright, expect
from LoginPage import LoginPage
from ProductPage import ProductPage
from CartPage import CartPage

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("standard_user", "wrong_password")


        error_message = login_page.get_error_message()
        assert error_message.is_visible()
        assert error_message.text_content() == "Epic sadface: Username and password do not match any user in this service"

        browser.close()

def test_order_succes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        product_page.add_to_cart()

        cart_page.checkout()
        cart_page.fill_form("John", "Doe", "12345")
        cart_page.finish()

        succes_message = cart_page.get_succes_message()
        assert succes_message.is_visible()
        assert succes_message.text_content() == "Thank you for your order!"

        browser.close()

def test_empty_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("", "")


        error_message = login_page.get_error_message()
        assert error_message.is_visible()
        assert error_message.text_content() == "Epic sadface: Username is required"

        browser.close()