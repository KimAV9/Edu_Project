import allure
from pages.general_page import CheckLocalization
import pytest
import pytest_order
from time import sleep


@allure.title('Test localization')
@allure.description('Проверка изменения языка')
@allure.tag('Localization')
@allure.epic('General')
@allure.feature('Localization')
@allure.story('Language change')
@allure.severity('Normal')
@pytest.mark.order(4)
def test_check_localization(browser):
    check_localization = CheckLocalization(browser)

    check_localization.open2()

    check_localization.open_lang_menu()
    check_localization.choose_lang()
    check_localization.assert_text()

    check_localization.open_lang_menu()
    check_localization.choose_eng()
    check_localization.check_lang()
    check_localization.confirm_localization()

    browser.quit()
