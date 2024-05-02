import allure
from pages.settings_page import AccountSettings
import pytest


@allure.story('Change parameter in settings')
@allure.description('Change Fullname, Email, Timezone and language')
@pytest.mark.skip
def test_settings(browser):
    settings_page = AccountSettings(browser)

    settings_page.open2()
    settings_page.login2()

    settings_page.open_prof_menu()
    settings_page.open_settings()

    settings_page.write_fullname_field()
    settings_page.write_email_field()

    settings_page.click_language_menu()
    settings_page.click_lang_select()

    settings_page.click_timezone_menu()
    settings_page.click_timezone_select()

    settings_page.click_save_button()
