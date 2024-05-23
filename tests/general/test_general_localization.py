import allure
from pages.general_page import CheckLocalization
import pytest
import pytest_order
from time import sleep



def test_check_localization(browser):
    check_localization = CheckLocalization(browser)

    check_localization.open2()
    check_localization.open_lang_menu()
    check_localization.choose_lang()
    check_localization.confirm_lang_change1()
    check_localization.choose_eng()
    check_localization.assert_text()
    check_localization.check_lang()
    sleep(10)
    check_localization.confirm_localization()
