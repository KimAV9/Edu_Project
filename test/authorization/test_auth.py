import allure
import pytest
from pages.auth_page import AuthPage
from time import sleep
import pytest_order


@allure.story('Authentication check')
@pytest.mark.skip
def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.login()
    auth_page.login_email()
    auth_page.login_password()
    auth_page.login_button()
    browser.quit()