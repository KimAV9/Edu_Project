import allure
from pages.settings_page import PasswordChange
import pytest
import pytest_order


@allure.title('Test change password')
@allure.description('Изменить пароль и проверить')
@allure.tag('Account', 'Settings')
@allure.epic('Account')
@allure.feature('Settings')
@allure.story('Password')
@pytest.mark.skip
@pytest.mark.order(30)
def test_password(browser):
    password_change = PasswordChange(browser)

    password_change.open2()
    password_change.open_prof_menu()
    password_change.open_settings()

    password_change.write_current_password()
    password_change.write_new_password()
    password_change.retype_new_password()
    password_change.click_change_password()

    password_change.check_password()
    browser.quit()
