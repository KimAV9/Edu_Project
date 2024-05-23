import allure
import pytest
from pages.profile_page import ProfilePageDeleteData
from time import sleep
import pytest_order

@allure.story('Change additional in profile')
@pytest.mark.order(7)
@pytest.mark.skip
def test_delete_personal_data(browser):
    profile_page = ProfilePageDeleteData(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()

    profile_page.click_edit_work_exp()
    profile_page.remove_work_exp()
    sleep(1)

    profile_page.click_edit_edu()
    profile_page.remove_edu()
    sleep(1)

    profile_page.click_edit_wk_pref()
    profile_page.remove_wk_pref()
    profile_page.save_wk_pref()

    browser.quit()