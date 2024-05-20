import allure
from pages.settings_page import AccountSettings
from pages.settings_page import PasswordChange
from pages.settings_page import CommunicationPreferences
import pytest


@allure.story('Change parameter in settings')
@allure.description('Change Fullname, Email, Timezone and language')
@pytest.mark.skip
def test_settings(browser):
    settings_page = AccountSettings(browser)

    settings_page.open2()
    #settings_page.login2()

    settings_page.open_prof_menu()
    settings_page.open_settings()

    settings_page.write_fullname_field()
    settings_page.write_email_field()

    settings_page.click_language_menu()
    settings_page.click_lang_select()

    settings_page.click_timezone_menu()
    settings_page.click_timezone_select()

    settings_page.click_save_button()
    browser.quit()

@pytest.mark.skip
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


@pytest.mark.skip
def test_comm_pref(browser):
    comm_pref = CommunicationPreferences(browser)

    comm_pref.open2()
    comm_pref.open_prof_menu()
    comm_pref.open_settings()
    comm_pref.open_comm_pref()
    comm_pref.click_opt_out()
    comm_pref.click_pers_recom()
    comm_pref.click_notif_promo()
    comm_pref.click_info_degr()
    comm_pref.click_surv()
    comm_pref.save1()
    comm_pref.click_proj_netw()
    comm_pref.save2()
    browser.quit()