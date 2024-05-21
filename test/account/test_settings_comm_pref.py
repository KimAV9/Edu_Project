import allure
from pages.settings_page import CommunicationPreferences
import pytest
import pytest_order


@allure.story('Change communication preferences in settings')
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
