import allure
from pages.settings_page import DeleteAccount
import pytest
import pytest_order


@allure.title('Test delete account')
@allure.description('Удаление собственного аккаунта с вебсайта')
@allure.tag('Account', 'Settings')
@allure.epic('Account')
@allure.feature('Settings')
@allure.story('Account Deletion')
@pytest.mark.skip
@pytest.mark.order(31)
def test_delete_account(browser):
    delete_account = DeleteAccount(browser)

    delete_account.open2()
    delete_account.open_prof_menu()
    delete_account.open_settings()

    delete_account.click_delete_account_button()
    delete_account.click_checkbox1()
    delete_account.click_checkbox2()
    delete_account.click_checkbox3()

    delete_account.enter_password()
    #delete_account.confirm_delete_account()
    browser.quit()
