import pytest
from pages.registration_page import RegistrationPage
from time import sleep
import pytest_order
import allure


@pytest.mark.skip('Fails due newly added captcha')
@allure.title('Test registration')
@allure.description('Успешное прохождение регистрации')
@allure.tag('Registration')
@allure.epic('Registration')
@allure.feature('Registration')
@allure.story('Register an account')
@pytest.mark.order(1)
def test_register(browser):
    register_page = RegistrationPage(browser)
    register_page.open_page()
    register_page.register()

    register_page.register_fullname()
    register_page.register_password()
    register_page.register_email()
    register_page.register_button()

    browser.quit()
