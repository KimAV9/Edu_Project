import allure
import pytest
from pages.auth_page import AuthPage
from time import sleep
import pytest_order


@pytest.mark.skip('Fails due newly added captcha')
@allure.title('Test authorization')
@allure.description('Успешное заполнение данных для персонализации и сохранение их профиле')
@allure.tag('Authorization')
@allure.epic('Authorization')
@allure.feature('Authorization')
@allure.story('Log into the account')
@pytest.mark.order(3)
def test_auth(browser):
    auth_page = AuthPage(browser)

    auth_page.open()
    auth_page.login()

    auth_page.login_email()
    auth_page.login_password()

    auth_page.login_button()
    browser.quit()