import pytest
from pages.registration_page import RegistrationPage
from time import sleep
import pytest_order

@pytest.mark.skip
@pytest.mark.order(0)
def test_register(browser):
    register_page = RegistrationPage(browser)
    register_page.open_page()
    register_page.register()

    register_page.register_fullname()
    register_page.register_password()
    register_page.register_email()
    register_page.register_button()
    browser.quit()
